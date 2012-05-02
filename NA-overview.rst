Missing data: an orientation
############################

The debate about how numpy should handle missing data, a subject with
many preexisting approaches, requirements, and conventions, has been long and
contentious. There has been more than one proposal for how to implement
support into numpy, and there is a testable implementation which is
merged into numpy's current master. The vast number of emails and differing
points of view has made it difficult for interested parties to understand
the issues and be comfortable with the direction numpy is going.

Here is our (Mark and Nathaniel's) attempt to summarize the
problem, proposals, and points of agreement/disagreement in a single
place, to help the community move towards consensus.

The Numpy developers' problem
=============================

For this discussion, "missing data" means array elements
which can be indexed (e.g. A[3] in an array A with shape (5,)),
but have, in some sense, no value. We will use the token MISSING
to represent such an array element during this discussion.

It does not refer to compressed or sparse storage techniques where
the value for A[3] is not actually stored in memory, but still has a
well-defined value like 0.

This is still vague, and to create an actual implementation,
it is necessary to answer such questions as:

* What values are computed when doing element-wise ufuncs.
* What values are computed when doing reductions.
* Whether the storage for an element gets overwritten when assigning MISSING.
* Whether computations resulting in NaN automatically turn into a
  missing value.
* Whether one interacts with missing values using a placeholder object
  (e.g. called "NA" or "masked"), or through a separate boolean array.
* Whether there is such a thing as an array object that cannot hold
  missing array elements.
* How the (C and Python) API is expressed, in terms of dtypes,
  masks, and other constructs.
* If we decide to answer some of these questions in multiple ways,
  then that creates the question of whether that requires multiple
  systems, and if so how they should interact.

There's clearly a very large space of missing-data APIs that *could*
be implemented. There is likely at least one user, somewhere, who
would find any possible implementation to be just the thing they
need to solve some problem. On the other hand, much of numpy's power
and clarity comes from having a small number of orthogonal concepts,
such as strided arrays, flexible indexing, broadcasting, and ufuncs.

There has been dissatisfaction among several major groups of numpy users
about the existing status quo of missing data support. In particular,
neither the numpy.ma component nor use of floating-point NaNs as a
missing data signal fully satisfy the performance requirements and
ease of use for these users. The example of R, where missing data
is treated via an NA placeholder and is deeply integrated into all
computation, is where many of these users point to indicate what
functionality they would like. Doing a deep integration of missing
data like in R must be considered carefully, it must be clear it
is not being done in a way which sacrifices existing performance
or functionality.

Our problem is, how can we choose some incremental additions to
numpy that will make a large class of users happy, be
reasonably elegant, complement the existing design, and that we're
comfortable we won't regret being stuck with in the long term.

Prior art
=========

So a major (maybe *the* major) problem is figuring out how ambitious
the project to add missing data support to numpy should be, and which
kinds of problems are in scope. Let's start with the
best understood situation where "missing data" comes into play:

"Statistical missing data"
--------------------------

In statistics, social science, etc., "missing data" is a term of art
referring to a specific (but extremely common and important)
situation: we have tried to gather some measurements according to some
scheme, but some of these measurements are missing. For example, if we
have a table listing the height, age, and income of a number of
individuals, but one person did not provide their income, then we need
some way to represent this::

  Person | Height | Age | Income
  ------------------------------
     1   |   63   | 25  | 15000
     2   |   58   | 32  | MISSING
     3   |   71   | 45  | 30000

The traditional way is to record that income as, say, "-99", and
document this in the README along with the data set. Then, you have to
remember to check for and handle such incomes specially; if you
forget, you'll get superficially reasonable but completely incorrect
results, like calculating the average income on this data set as
14967. If you're in one of these fields, then such missing-ness is
routine and inescapable, and if you use the "-99" approach then it's a
pitfall you have to remember to check for explicitly on literally
*every* calculation you ever do. This is, obviously, an unpleasant way
to live.

Let's call this situation the "statistical missing data" situation,
just to have a convenient handle for it. (As mentioned, practitioners
just call this "missing data", and what to do about it is literally an
entire sub-field of statistics; if you google "missing data" then
every reference is on how to handle it.) Numpy isn't going to do
automatic imputation or anything like that, but it could help a great
deal by providing some standard way to at least represent data which
is missing in this sense.

The main prior art for how this could be done comes from the S/S+/R
family of languages. Their strategy is, for each type they support,
to define a special value called "NA". (For ints this is INT_MAX,
for floats it's a special NaN value that's distinguishable from
other NaNs, ...) Then, they arrange that in computations, this
value has a special semantics that we will call "NA semantics".

NA Semantics
------------

The idea of NA semantics is that any computations involving NA
values should be consistent with what would have happened if we
had known the correct value.

For example, let's say we want to compute the mean income, how might
we do this? One way would be to just ignore the MISSING entry, and
compute the mean of the remaining entries. This gives us (15000 +
30000)/2, or 22500.

Is this result consistent with discovering the income of person 2?
Let's say we find out that person 2's income is 50000. This means
the correct answer is (15000 + 50000 + 30000)/3, or 31666.67,
indicating clearly that it is not consistent. Therefore, the mean
income is NA, i.e. a specific number whose value we are unable
to compute.

This motivates the following rules, which are how R implements NA:

Assignment:
  NA values are understood to represent specific
  unknown values, and thus should have value-like semantics with
  respect to assignment and other basic data manipulation
  operations. Code which does not actually look at the values involved
  should work the same regardless of whether some of them are
  missing. For example, one might write::

    income[:] = income[np.argsort(height)]
  
  to perform an in-place sort of the ``income`` array, and know that
  the shortest person's income would end up being first. It turns out
  that the shortest person's income is not known, so the array should
  end up being ``[NA, 15000, 30000]``, but there's nothing
  special about NAness here.

Propagation:
  In the example above, we concluded that an operation like ``mean``
  should produce NA when one of its data values was NA.
  If you ask me, "what is 3 plus x?", then my only possible answer is
  "I don't know what x is, so I don't know what 3 + x is either". NA
  means "I don't know", so 3 + NA is NA.
  
  This is important for safety when analyzing data: missing data often
  requires special handling for correctness -- the fact that you are
  missing information might mean that something you wanted to compute
  cannot actually be computed, and there are whole books written on
  how to compensate in various situations. Plus, it's easy to not
  realize that you have missing data, and write code that assumes you
  have all the data. Such code should not silently produce the wrong
  answer.
  
  There is an important exception to characterizing this as propagation,
  in the case of boolean values. Consider the calculation::

    v = np.any([False, False, NA, True])

  If we strictly propagate, ``v`` will become NA. However, no
  matter whether we place True or False into the third array position,
  ``v`` will then get the value True. The answer to the question
  "Is the result True consistent with later discovering the value
  that was missing?" is yes, so it is reasonable to not propagate here,
  and instead return the value True. This is what R does::

    > any(c(F, F, NA, T))
    [1] TRUE
    > any(c(F, F, NA, F))
    [1] NA

Other:
  NaN and NA are conceptually distinct. 0.0/0.0 is not a mysterious,
  unknown value -- it's defined to be NaN by IEEE floating point, Not a
  Number. NAs are numbers (or strings, or whatever), just unknown
  ones.

  In R, all reduction operations implement an alternative semantics,
  activated by passing a special argument (``na.rm=TRUE`` in R).
  ``sum(a)`` means "give me the sum of all the
  values" (which is NA if some of the values are NA);
  ``sum(a, na.rm=True)`` means "give me the sum of all the non-NA
  values".

Other prior art
---------------

Once we move beyond the "statistical missing data" case, the correct
behavior for missing data becomes less clearly defined. There are many
cases where specific elements are singled out to be treated specially
or excluded from computations, and these often fit as missing data.

In image processing, it's common to use a single image together with
one or more boolean masks to e.g. composite subsets of an image. As
Joe Harrington pointed out on the list, in the context of processing
astronomical images, it's also common to generalize to a
floating-point valued mask, or alpha channel, to indicate degrees of
"missingness". We think this is out of scope for the present design,
but it is an important use case, and ideally numpy should support
natural ways of manipulating such data.

After R, numpy.ma is probably the second-most mature source of
experience on missing-data-related APIs. It uses both different semantics
from R, like reductions skip masked values by default and
NaNs convert to masked, and a different storage strategy via a separate
mask. While it seems to be generally considered sub-optimal for
general use, it's hard to pin down whether this is because the API is
immature but basically good, or the API is fundamentally broken, or
the API is great but the code should be faster, or what. We looked at
some of those users to try and get a better idea.

Matplotlib seems to use numpy.ma primarily to allow users to tell
what data is missing when passing it to be graphed. In doing a number
of different test plots, the results of numpy.ma missing data in
matplotlib match the results of NA missing data in R's plotting.
Both matplotlib and R treat NaNs in the same fashion as NA for plotting
purposes.

Additionally, matplotlib uses numpy.ma arrays and separately computed
boolean masks to store and pass 'validity' information for each input
array in a cheap and non-destructive fashion. Mark's impression from
some shallow code review is that mostly it works directly with the
data and mask attributes of the masked arrays, not extensively using
the particular computational semantics of numpy.ma.

Paul Hobson `posted some code`__ on the list that uses numpy.ma for
storing arrays of contaminant concentration measurements. Here the
mask indicates whether the corresponding number represents an actual
measurement, or just the estimated detection limit for a concentration
which was too small to detect. Nathaniel's impression from reading
through this code is that it also mostly uses the .data and .mask
attributes in preference to performing operations on the MaskedArray
directly. Conceptually, this seems to fit the NA semantic model to
track which values aren't truly known, but simultaneously computing
best-guess results based on the available estimates corresponding to
the NAs.
  
__ http://mail.scipy.org/pipermail/numpy-discussion/2012-April/061743.html

Semantics, storage, API, oh my!
===============================

We think it's useful to draw a clear line between use cases,
semantics, and storage. Use cases are situations that users encounter,
regardless of what numpy does; they're the focus of the previous
section. When we say *semantics*, we mean the result of different
operations as viewed from the Python level without regard to the
underlying implementation.

*NA semantics* are the ones described above and used by R::

  1 + NA = NA
  sum([1, 2, NA]) = NA
  NA | False = NA
  NA | True = True

With ``na.rm=TRUE`` or ``skipNA=True``, this switches to::

  1 + NA = illegal # in R, only reductions take na.rm argument
  sum([1, 2, NA], skipNA=True) = 3

There's also been discussion of what we'll call *ignore
semantics*. These are somewhat underdefined::

  sum([1, 2, IGNORED]) = 3
  # Several options here:
  1 + IGNORED = 1
  #  or
  1 + IGNORED = <leaves output array untouched>
  #  or
  1 + IGNORED = IGNORED

For either NA or IGNORED semantics implemented with masks, there
is a choice of what should be done to the value in the storage
for an array element which gets assigned a missing value. Two
possibilities are to leave that memory untouched
(the choice made in the NEP), or to do the calculation with the
values independently of the mask (ideal for Paul Hobson's
numpy.ma use-case).

The numpy.ma semantics are::

  sum([1, 2, masked]) = 3
  1 + masked = masked # The value from the left operand is copied to
                      # the output. Generally the values behind the
                      # mask of a+b and b+a will be different.

When we talk about *storage*, we mean the debate about whether missing
values should be represented by designating a particular value of the
underlying data-type (the *bitpattern dtype* option, as used in R), or
by using a separate *mask* stored alongside the data itself.

For mask-based storage, there is also an important question about what
the API looks like for accessing the mask, modifying the mask, and
"peeking behind" the mask.

Designs that have been proposed
===============================

One option is to just copy R, by implementing a mechanism whereby
dtypes can arrange for certain bitpatterns to be given NA semantics.

One option is to copy numpy.ma closely, but with a more optimized
implementation. (Or to simply optimize the existing implementation.)

One option is that described in the NEP_, for which an implementation
of mask-based missing data exists. This system is roughly:

.. _NEP: https://github.com/numpy/numpy/blob/master/doc/neps/missing-data.rst

* There is both bitpattern and mask-based missing data, and both
  have identical default interoperable NA semantics.
* Masks are modified by assigning np.NA or values to array elements.
  The way to peek behind the mask or to unmask values is to keep a
  view of the array that shares the data pointer but not the mask pointer.
* Mark would like to add a way to access and manipulate the mask more
  directly, to be used in addition to this view-based API.
* If an array has both a bitpattern dtype and a mask, then assigning
  np.NA writes to the mask, rather than to the array itself. Writing
  a bitpattern NA to an array which supports both requires accessing
  the data by "peeking under the mask".

One option is that described in the alterNEP_, which is to implement
bitpattern dtypes with NA semantics for the "statistical missing data"
use case, and to also implement a totally independent API for masked
arrays with ignore semantics and all mask manipulation done explicitly
through a .mask attribute.

.. _alterNEP: https://gist.github.com/1056379

Another option would be to define an aligned array container that
holds multiple arrays and that can be used to pass them around
together. It would support indexing (to help with the common problem
of wanting to subset several arrays together without their becoming
unaligned), but all arithmetic etc. would be done by accessing the
underlying arrays directly via attributes. The "prior art" discussion
above suggests that something like this holding a .data and a .mask
array might actually be solve a number of people's problems without
requiring any major architectural changes to numpy. This is similar
to a structured array, but with each field in a separately stored
array instead of packed together.

Several people have suggested that there should be a single system
that has multiple missing values that each have different semantics,
e.g., a MISSING value that has NA semantics, and a separate IGNORED
value that has ignored semantics.

None of these options are necessarily exclusive.

The debate
==========

We both are dubious of using ignored semantics as a default missing
data behavior. **Nathaniel** likes NA semantics because he is most
interested in the "statistical missing data" use case, and NA semantics
are exactly right for that. **Mark** isn't as interested in that use
case in particular, but he likes the NA computational abstraction
because it is unambiguous and well-defined in all cases, and has a
lot of existing experience to draw from.

**Nathaniel**

* The "statistical missing data" use case is clear and compelling; the
  other use cases are probably important, but it's hard to say what
  they *are* exactly yet.
* The "statistical missing data" use case is best served by an R-style
  system that uses bitpattern storage to implement NA semantics. The
  main advantage of bitpattern storage for this use case is that it
  avoids the extra memory and speed overhead of storing and checking a
  mask (especially for the common case of floating point data, where
  some tricks with NaNs allow us to effectively hardware-accelerate
  most NA operations). These concerns alone appears to make a
  mask-based implementation unacceptable to many NA users,
  particularly in areas like neuroscience (where memory is tight) or
  financial modeling (where milliseconds are critical). In addition,
  the bit-pattern approach is less confusing conceptually (e.g.,
  assignment really is just assignment, no magic going on behind the
  curtain), and it's possible to have in-memory compatibility with R
  for inter-language calls via rpy2.  The main disadvantage of the
  bitpattern approach is the need to give up a value to represent NA,
  but this is not an issue for the most important data types (float,
  bool, strings, enums, objects); really, only integers are
  affected. And even for integers, giving up a value doesn't really
  matter for statistical problems. (Occupy Wall Street
  notwithstanding, no-one's income is 2**63 - 1. And if it were, we'd
  be switching to floats anyway to avoid overflow.)
* Adding new dtypes requires some cooperation with the ufunc and
  casting machinery, but doesn't require any architectural changes or
  violations of numpy's current orthogonality.
* His impression from the mailing list discussion, esp. the `"what can
  we agree on?" thread`__, is that many numpy.ma users like the
  combination of masked storage, the mask being easily accessible
  through the API, and ignored semantics. He could be wrong, though.

  __ http://thread.gmane.org/gmane.comp.python.numeric.general/46704

* R's NA support is a `headline feature`__ and its target audience
  consider it a compelling advantage over other platforms like Matlab
  or Python. Working with statistical missing data is very painful
  without platform support.

  __ http://www.sr.bham.ac.uk/~ajrs/R/why_R.html

* In comparison, we clearly have much more uncertainty about the use
  cases that require a mask-based implementation, and it doesn't seem
  like people will suffer too badly if they are forced for now to
  stick to numpy's excellent mask-based indexing, the new where=
  support, and even numpy.ma.
* Making mask and bitpattern NAs act the same is helpful if one often
  wants to treat them the same (for example, temporarily pretend that
  certain data is "statistically missing data"), and unhelpful if one
  often wants to treat them differently. He's leaning on the
  "unhelpful" side, personally, and doesn't feel at all certain that
  the people asking about masked array support, but not "statistical
  missing data", really want that. And certainly R manages just fine
  without this feature and no-one seems to have noticed its lack. So
  he would say the jury is still very much out on whether this aspect
  of the NEP design is an advantage or a disadvantage.
* If asking people to type 'pip install numpy_experimental_api' and
  try it out is really too hard, then he doesn't really have any
  objection to making experimental API's available in the the main
  numpy distribution with some hoops required to try them out. (This
  might also be a good strategy for adding some warranty-violating
  interfaces that would be generally useful for future experiments --
  e.g. some way to tell the PyArray constructors to start returning a
  different ndarray subclass by default. Terrifying for general use,
  quite useful for prototype hacks.) But, two points.

  First, it seems kind of premature to ask people to try out the code
  before we can even agree on fundamental issues like NA semantics
  versus ignore semantics, and when there are still plans to majorly
  change how masks are exposed and accessed?

  Second, given how intrusive the NEP code changes are and the
  concerns about their causing (minor) `ABI issues`__, maybe it would
  be better if they weren't present in the C API at all, and hoops
  required were something instead like, 'we have included a hacky
  pure-Python prototype accessible by typing "import
  numpy.experiment.donttrythisathome.NEP" and would welcome feedback'?

  __ http://thread.gmane.org/gmane.comp.python.numeric.general/49485>

  If so, then he should mention that he did implement a horribly
  klugy, pure Python implementation of the NEP API that works with
  numpy 1.6.1. This was mostly an experiment to see how possible such
  prototyping was and how much a proper ufunc override mechanism would
  help, but if there's interest, the module is available here:
  https://github.com/njsmith/numpyNEP

  (It passes the maskna test-suite, with some minor issues described
  in a big comment at the top.)

**Mark**

* The idea of using NA semantics by default for missing data, inspired
  by the "statistical missing data" problem, is better than all the
  other default behaviors which were considered. This applies equally
  to the bitpattern and the masked approach.
* For NA-style functionality to get proper support by all numpy
  features and eventually all third-party libraries, it needs to be
  in the core. How to correctly and efficiently handle missing data
  differs by algorithm, and if thinking about it is required to fully
  support numpy, NA support will be broader and higher quality.
* At the same time, providing two different missing data interfaces,
  one for masks and one for bitpatterns, requires numpy developers
  and third-party numpy plugin developers to separately consider the
  question of what to do in either case, and do two additional
  implementations of their code. This complicates their job,
  and could lead to inconsistent support for missing data.
* Providing the ability to work with both masks and bitpatterns through
  the same C and Python programming interface makes missing data support
  cleanly orthogonal with all other numpy features.
* There are many trade-offs of memory usage, performance, correctness, and
  flexibility between masks and bitpatterns. Providing support for both
  approaches allows users of numpy to choose the approach which is
  most compatible with their way of thinking, or has characteristics
  which best match their use-case. Providing them through the same
  interface further allows them to try both with minimal effort, and
  choose the one which performs better or uses the least memory for
  their programs.
* Memory Usage
  - With bitpatterns, less memory is used for storing a single NA-capable
    array.
  - With masks, less memory is used when a single array of data is used
    with multiple different choices of NAs.
* Performance
  - With bitpatterns, the floating point type can use native hardware
    operations, and achieve results which are correct in all but a few
    cases. With other types, code must be written which specially checks
    for the missing-data bitpattern.
  - With masks, inner loops must be implemented to support the
    masking semantics, which adds some overhead. The implementation
    that currently exists has no performance tuning for this, so
    it is not a good basis to judge the performance difference.
* Correctness
  - With bitpatterns, the choice of native floating-point operations
    results in semantics which are not strictly correct in all cases.
    An inconsistent case is NaN+NA vs NA+NaN. This performance/
    correctness tradeoff seems reasonable.
  - With masks, there is not a similar performance/correctness tradeoff.
* Generality
  - The bitpattern approach can work in a fully general way only when
    there is a specific value which can be given up from the
    data type. For IEEE floating point, a NaN is an obvious choice,
    and for booleans represented as a byte, there are plenty of choices.
    For integers, a valid value must be sacrificed to use this approach.
  - The mask approach works universally with all data types.

Recommendations for Moving Forward
==================================

**Nathaniel**

* Go ahead and implement bitpattern NAs
* *Not* implement masked arrays in the core -- or at least, not
  yet. Instead, we should focus on figuring out how to implement
  them out-of-core, so that people can try out different approaches
  without us committing to any one approach. (And anyway, we're
  going to have to figure out how to experiment with such changes
  out-of-core if numpy is to continue to evolve without forking --
  might as well do it now.)

**Mark**

* The existing code should remain as is, with a global run-time experimental
  flag added which disables NA support by default.

A more detailed rationale for this recommendation is:

* A solid preliminary NA-mask implementation is currently in numpy
  master. This went through the pull request and numpy-discussion
  process which had become the conventional numpy development process
  when it was merged. This implementation has been extensively tested
  against scipy and other third-party packages, and has been in master
  in a stable state for a significant amount of time.
* This implementation integrates deeply with the core, providing an
  interface which is usable in the same way R's NA support is. It
  provides a compelling, user-friendly answer to R's NA support.
* The missing data NEP provides a plan for adding bitpattern-based
  dtype support of NAs, which will operate through the same interface
  but allow for the same performance/correctness tradeoffs that R has made.
  There are developer resources committed to furthering this plan.

Because of its preliminary state, the existing implementation is marked
as experimental in the numpy documentation. It would be good for this
to remain marked as experimental until it is more fleshed out, for
example supporting struct and array dtypes and with a fuller set of
numpy operations.

I think the code should stay as it is, except to add a run-time global
numpy flag, perhaps numpy.experimental.maskna, which defaults to
False and can be toggled to True. In its default state, any NA feature
usage would raise an "ExperimentalError" exception, a measure which
would prevent it from being accidentally used and communicate its
experimental status very clearly.

The ABI issues seem very tricky to deal with effectively in the 1.x
series of releases, but I believe that with proper implementation-hiding
in a 2.0 release, evolving the software to support various other
ABI ideas that have been discussed is feasible. This is the approach
I like best.

References/history
==================

The original NEP describes Mark's NA-semantics/mask
implementation/view based mask handling API:
https://github.com/numpy/numpy/blob/master/doc/neps/missing-data.rst

The alterNEP was Nathaniel's initial attempt at separating MISSING and
IGNORED handling into bit-patterns versus masks, though there's a
bunch he would change about the proposal at this point:
https://gist.github.com/1056379

miniNEP 2 was a later attempt by Nathaniel to sketch out an
implementation strategy for NA dtypes:
https://gist.github.com/1068264

A discussion overview page is here:
https://github.com/njsmith/numpy/wiki/NA-discussion-status

