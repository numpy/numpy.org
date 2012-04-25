Mark's initial summary
========================
Points of agreement:

1. The NA (Not Available) abstraction is a good thing, following in
the footsteps of S, R, etc. In particular, using "propagate" by
default for reduction operations is desirable.
2. The numpy community has not achieved consensus about missing
data functionality.
3. We do not want to get stuck supporting an implementation that
is "yet another bad missing data choice among many," but rather
would like a solution which gets high user adoption.
4. Including the NA masks as is, enabled by default, exposes some risk of #3.

Points of disagreement:

1. Whether NA/IGNORE and mask/bitpattern are fully independent concepts
    Mark: They are fully independent, NA/IGNORE is about computation,
        and mask/bitpattern is about whether data gets destroyed in
        certain contexts.
    Nathaniel: People naturally think about NA as bitpatterns and
        IGNORE as masks.
2. What is the best strategy for gaining knowledge, experience and input for gaining consensus about missing data in numpy.
    Mark: The lack of consensus is in large part a consequence of the
        fact that so many different missing data applications are in
        the wild, and there is no existing example of an implementation
        simultaneously supporting NA + masks + view semantics in the
        wild for comparison.
          Therefore, an easily accessible implementation for people to
        experiment with and gain practical experience is essential to
        better understand the problem and how it relates to numpy in
        particular, and the current implementation should ship with
        numpy, marked as experimental in the documentation and
        possible disabled by default with a global flag.
    Nathaniel: Consensus should be reached before releasing an NA
        implementation in mainline numpy, particularly an implementation
        which might be ignored by many people. The long term support
        burden of such a release may be huge, and there is a big risk
        that existing mask users won't like the NA-behavior, while
        the stats users won't like the overhead of a mask.
          Therefore, the NA mask should be excised from the code, and
          put in a separate module for interested users to install
          and experiment with separately.



NA overview
###########

The debate about how numpy should handle missing data, a subject with
many preexisting approaches, requirements, and conventions, has been long and
contentious, with multiple competing proposals going through
multiple revisions, plus innumerable mailing list posts. This
has made it difficult for interested parties to understand the
issues, which is a prerequisite for consensus.

So, here is our (Mark and Nathaniel's) attempt to summarize the problem
scope, proposals, and points of disagreement in a single place, so we
can all start debating from the same page.

What does "missing data" mean?
==============================

For this discussion, "missing data" means array elements
which can be indexed (e.g. A[3] in an array A with shape (5,)),
but for which there is not a value present.

Differences between various missing data approaches include:

* What values are computed when doing element-wise ufuncs.
* What values are computed when doing reductions.
* Whether the storage for an element gets overwritten when assigning NA.
* Whether computations resulting in NaN automatically turn into a
  missing value.
* Whether one interacts with missing values using a placeholder object
  (e.g. called "NA"), or through a separate boolean array.

This is distinct from sparse storage, a closely related technique
where A[3] would not have any bytes in memory allocated for the element.

What's the problem we're trying to solve?
=========================================

Here are some descriptions of existing practice that guides our
views of missing data. In an attempt to avoid any preconceptions
about what the missing data means in different cases, we will use
the placeholder MISSING for the missing data in all our examples.

Statistical Packages Like R
---------------------------

When doing various sorts of statistical analyses, it often occurs that
there is some specific, meaningful value that *should* exist, but for
some reason does not.

For example, if we have a table listing the height,
age, and income of a number of individuals, but one person did not
provide their income, then we need some way to represent this. A
natural way to do this is to define a special "missing" value::

  Person | Height | Age | Income
  ------------------------------
     1   |   63   | 25  | 15000
     2   |   58   | 32  | MISSING
     3   |   71   | 45  | 30000

One way to think about what computations this should result in
is to ask the question "Is the result consistent with later
discovering the values that were missing?"

Let's say we want to compute the mean income, how might we do
this? One way would be to just ignore the MISSING entry, and
compute the mean of the remaining entries. This gives
us (15000 + 30000)/2, or 22500.

Is this result consistent with discovering the income of person 2?
Let's say we find out that person 2's income is 50000. This means
the correct answer is (15000 + 50000 + 30000)/3, or 31666.67,
indicating clearly that it is not consistent. Therefore, the mean
income is MISSING, i.e. a specific number whose value we are unable
to compute.

This use case suggests the following semantics:
Assignment
  MISSING values are understood to represent specific
  unknown values, and thus should have value-like semantics with
  respect to assignment and other basic data manipulation
  operations. Code which does not actually look at the values involved
  should work the same regardless of whether some of them are
  missing. For example, one might write::

    income[:] = income[np.argsort(height)]
  
  to perform an in-place sort of the ``income`` array, and know that
  the shortest person's income would end up being first. It turns out
  that the shortest person's income is not known, so the array should
  end up being ``[MISSING, 15000, 30000]``, but there's nothing
  special about MISSINGness here.

Propagation
  In the example above, we concluded that an operation like *mean*
  should produce MISSING when one of its data values was MISSING.
  This can be generalized into a notion called propagation.

  If you ask me, "what is 3 plus x?", then my only possible answer
  is "I don't know, it depends on x". MISSING means "I don't know",
  so 3 + MISSING is MISSING.
  
  This is also important for safety: missing data often
  requires special handling for correctness -- the fact that you are
  missing information might mean that something you wanted to compute
  cannot actually be computed, and there are whole books written on
  how to compensate in various situations. Plus, it's easy to not
  realize that you have missing data, and write code that assumes you
  have all the data. Such code should not silently produce the wrong
  answer.
  
  Even simple code like the naive implementation of mean::

    def my_mean(x):
        x = np.asarray(x)
        return np.sum(x) / x.size

  will silently return the wrong answer if ``x`` contains MISSING
  values and ``np.sum`` skips over them. Therefore, MISSING must
  "propagate" though calculations, unless explicitly requested
  otherwise.

  There is an important exception to characterizing this as propagation,
  in the case of boolean values. Consider the calculation::

    v = np.any([False, False, MISSING, True])

  If we strictly propagate, *v* will become MISSING. However, no
  matter whether we place True or False into the third array position,
  *v* will then get the value True. The answer to the question
  "Is the result True consistent with later discovering the value
  that was missing?" is yes, so it is reasonable to not propagate here,
  and instead return the value True. This is what R does::

    > any(c(F, F, NA, T))
    [1] TRUE
    > any(c(F, F, NA, F))
    [1] NA

Currently numpy does not provide any very useful solution to users who
find themselves in this situation. Users who need this functionality
are instead using:
* NaNs (limited to floats, needs hackish special functions like
  nanmean, and doesn't quite have the right semantics -- e.g.
  ``MISSING == 20000`` should be MISSING, because they might or might
  not be equal, while ``NaN == 20000`` is False)
* hacky extensions of the NaN idea, e.g. strings and integers that can
  be NaN (see pandas)
* numpy.ma
* R

Situation 2: "ignoring" data
----------------------------

It is also often the case that users want to perform calculations on
some subset of an array, without modifying or including the rest of
the array. Of course, numpy has rich support for such operations
already, by use of various indexing operations, e.g.::

  arr1[mask] += arr2[mask]
  np.add(arr1, arr2, out=arr1, where=mask)

But there are three reasons why some users find these insufficient:
1. One often needs to perform complex operations like indexing or
iteration on *both* an array and its mask simultaneously, to keep them
'lined up' for future operations. Writing this code can be a
hassle. Similarly, it can be annoying to have to pass two arguments
(data + mask) to every function, instead of just one. (Example of this
usage: matplotlib)
2. There are functions which one would like to run on a subset of
one's data, but which accept only an array, not a mask. Some subset of
these functions could be convinced to run on a subset of data by going
through and adding a where= argument to all their ufunc calls. (Of
course, others would silently start returning the wrong results,
cf. ``my_mean``!) So it could be convenient to have a special sort of
array which automatically added a where= argument to all the ufuncs
that were called on it.
3. Many users (esp. those without as much programming experience) may
simply find it easier to think about one more complex object that
someone else put together and documented in one place (a "masked
array"), instead of two simple objects that are combined in flexible
ways on the fly using atomic operations like indexing.

The semantics for this use case are more controversial, but we can
say:
* It's critical that masking out some data point does not mutate the
  underlying array
* Most users seem to expect that reduction operations like np.sum
  should automatically skip over ignored values: ``np.sum([1,
  MISSING]) == 1``. However, see below for debate on this.
* Most users seem to expect that accessing and modifying which values
  are ignored should be convenient and straightforward.

Situation 3?
------------

One can imagine all kinds of hybrid or extended functionality somewhat
along these lines... but as far as we can tell, the two specific
situations above seem to cover everyone who's spoken up so far. And at
this point we think we've pretty much done due diligence.

So if you have such a situation, please speak up! But until that
happens, then we suggest that we shouldn't worry too much about
handling such hypothetical cases. Obviously extra flexibility is great
if it falls out of a design, but it needs to be justified by either
increased technical elegance, or its ability to make one of these two
real-life cases easier to handle.

[**Mark**, do you agree with this?]

Implementation options
======================

There are two basic strategies for implementing these features. One is
the "bit-pattern" strategy, in which we define some special values for
a given type to 'count as' the missing values, e.g. we might declare
that INT_MAX or a NaN with a special payload really *mean* that the
corresponding value is missing, and arrange for ufuncs and such to
treat them appropriately. The other is the "mask" strategy, in which
we store a separate boolean array along-side our data, and the entries
in the boolean array indicate which entries in the data are "real".

The bit-pattern approach is only possible for "missing data"
situation, not for "ignoring data". The mask approach could
potentially handle either or both situations.

Our opinion(s)
==============

"missing data"
--------------

**Nathaniel THINKS, and THINKS THAT MARK MIGHT AGREE MAYBE?, that:**
The missing data case is best served by bit-patterns. For this
specific use case, masks have a number of substantial
disadvantages. The most important is that bit-patterns avoid the extra
memory and speed overhead of storing and checking a mask (especially
for the common case of floating point data, where some tricks with
NaNs allow us to get the desired MISSING semantics more or less for
free) -- this alone appears to make a mask-based implementation
unacceptable to many "missing data" users, particularly in areas like
neuroscience (where memory is tight) or financial modeling (where
milliseconds are critical). In addition, the bit-pattern approach is
less confusing conceptually (e.g., assignment really is just
assignment, no magic going on behind the curtain), and it's possible
to have in-memory compatibility with R for inter-language calls via
rpy2.

For this use case, masks offer no comparable advantage to outweigh
these disadvantages. The strongest argument in their favor is that
they might let us get away with a single implementation that covered
both use cases, which would definitely be simpler if it worked. But at
this point, everyone seems to agree that we will need *some* kind of
bit-pattern support, which negates that advantage.

"ignoring data"
---------------

Here we disagree. Let's break this down into a sequence of simple,
concrete questions.

Should ignored values propagate?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mark** likes the way the "missing value" semantics are clear and
internally consistent - 'this data is Not Available' tells you
everything you need to know to work out how they should behave in any
particular situation, whether that be binary ufuncs, reductions,
whatever. When he says "NA semantics", this is what he's talking
about. (And this is why we've avoided using the term "NA" above -
we're trying to avoid confusion between terms like "missing" that
refer to use cases, and terms like "NA" referring to API semantics.)
Therefore, he thinks that this should be the default semantics
globally, whether the underlying implementation is bit-pattern-based
or mask-based, and "ignoring" values should always require an explicit
function argument. Critically, ignored values should still propagate
in reductions::

  >>> np.sum([10, NA, 30])
  NA

**Nathaniel** agrees that there is a real question about how to make
the "ignored" semantics self-consistent, but doubts that it is
possible to convince people with the "ignored value" use case that
they should accept NA semantics instead. He thinks that if we try then
they'll just stick with numpy.ma, which would defeat the point of this
whole exercise. Therefore, if we want to support masks at all, then
ignored values should be ignored in reductions::

  >>> a = [10, 20, 30]
  # ugly fake syntax so as to avoid committing to any particular real
  # syntax:
  >>> set_ignored(a, [False, True, False])
  >>> np.sum(a)
  40

Is there a distinction between bit-pattern MISSING and masked-out values?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **Mark's** scheme, both bit-patterns and masks always have the same
(NA, "missing-style") semantics. Therefore, he argues that it is
simplest to merge these two concepts into one in the API, so that
assigning a bit-pattern NA to an array looks identical to flipping a
mask bit::

  a1 = np.zeros(10, dtype=withNA(float))
  a1[0] = np.NA # writes a magic bit-pattern into a1[0]
  a2 = np.zeros(10, maskna=True)
  a2[0] = np.NA # does not modify data array, modifies mask instead

One consequence is that in his design, if you have an array that has
both a bit-pattern dtype and a mask, then it is possible to modify the
array by writing ordinary values, but it is impossible to write the
magic bit-pattern value -- attempts to do so will go to the mask
instead::

  a3 = np.zeros(10, dtype=withNA(float), maskna=True)
  a3[0] = 1 # modifies underlying data array
  a3[1] = np.NA # underlying data is not modified
  a4 = a3.view(ownmaskna=True)
  a4[2] = 2 # this affects both a3 and a4
  a4[3] = np.NA # this affects a4 only; a3 is unaffected
  a4[3] = np.no_really_the_NA_value # this would affect both a3 and a4
                                    # if it were allowed, but it isn't.

He believes that this is useful because he believes that the standard
thing people want to do with a masked array is to pretend that some
values are missing, without actually writing a missing value.

**Nathaniel** disagrees for several reasons. First, he doesn't think
bit-patterns and masks should have the same semantics, so merging them
doesn't make much sense. But even if it did, he thinks it would be a
bad idea, because they seem to serve different use cases. He thinks
that people use masks to mean things that are different than
missingness, and therefore they might well want to have both a mask
and bit-patterns in the same array while preserving the distinction
between them. He also thinks it's quite confusing to have two arrays
where writing some values is shared, but some values aren't (keeping
in mind that these are arrays that have a bit-pattern dtype, so np.NA
really does refer to a specific value). And since he's not sold on
this use of masking in general, he would like it to remain separate
from bit-patterns, so that he would at least have the option to use
the one and ignore the other.

How do you unmask or "peek behind" the mask?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Nathaniel** thinks that if people are working with masks, it's
specifically because they care about both the underlying array and
mask values separately, and so modifying the mask should be as
straightforward as possible. He believes that the most straightforward
way is to make it a standard boolean ndarray stored as an attribute,
like .mask or .visible, so that one can do indexing, re-assignment (to
swap masks), etc., in the standard ways. Similarly, he thinks the
underlying data array should be easily accessible in case one wants to
"peek behind the mask", perhaps as a .data attribute as in numpy.ma.

**Mark** is concerned that a misbehaving function might take advantage
of this leniency to access values that it isn't supposed to; he
believes that if a value is masked out, numpy should enforce that by
making it impossible to unmask or "peek behind" directly. Therefore,
his design does not allow one to access either the data or mask arrays
directly; one can overwrite data with new values, but not read out
masked values. Of course, it still needs to be possible to get at the
masked values somehow, or masking wouldn't really count as
non-destructive. His solution is to allow multiple views of a single
data array to (optionally) use different mask arrays, so one can mask
out access to a particular data point in one view of an array, while
still being able to access it via the original ndarray object.

**Nathaniel** agrees that this could be made to work, but is not sure
why it is so important to enforce the hiddenness of masked values
(esp. since this can be trivially circumvented at the C level), and
thinks the view-based approach adds enough complexity (as compared to
simply exposing the mask as an ndarray) to make the cure worse than
the disease.

**Mark** is also concerned that exposing the mask would force us to
commit to either True=visible or False=visible, which has been a point
of contention.

How do you mask out a value?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **Nathaniel's** scheme, we have both bit-pattern dtypes, where
there really is a "magic value" called something like np.NA, and we
also separately have masked arrays. He thinks that this distinction
might be kept clearer if we *don't* create a constant like np.IGNORED
which looks like a value, but really does something magic to the
mask. Therefore, he suggests that the way you mask out a value is by
modifying the mask directly. (Except, probably, that assigning a slice
of one masked array to a slice of another should copy the mask.)

In **Mark's** approach masking is done by assigning np.NA to an array
that has a mask.

What happens when you read out a masked value?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since **Nathaniel** is inclined to avoid having a magic constant for
masked values, he suggests that scalar access to a masked value should
be an error::

  >>> a = masked_array([1, 2, 3])
  >>> a.visible[0] = False
  >>> a[:2] # slicing a masked array, no problem
  [--, 2]
  >>> a[0] # scalar access is not allowed
  Traceback [...]: ValueError

**Mark** again thinks that returning np.NA in this case is fine.

What should we do next?
-----------------------

Here, **Mark and Nathaniel AGREE** that:
* The community shouldn't commit to supporting any particular design
  until it reaches consensus, and we have a reasonable expectation
  that users will actually adopt it in preference to
  numpy.ma/NaNs/etc.
* Bit-patterns have a relatively clear path forward
* There are many more uncertainties about what a good masking API
  would look like, and very little prior art to draw on
* Therefore, while we may be able to rule out certain approaches by
  discussion, we won't be able to commit to a masking API without
  getting some more real-world experience.

How can we get this experience?

**Mark** thinks the best way is to ship the code currently in master,
with warnings that it is experimental.

**Nathaniel** is much more dubious. First, our release manager seems
to think that even if we mark something experimental, that only covers
tweaks, not fundamental changes in its operation, and there are some
pretty fundamental disagreements listed above. (Mark and Nathaniel's
visions of masking APIs are definitely not ABI compatible.)
Furthermore, he's not sure that the code in master is the best way to
gain experience. Certainly experience with it would be *useful*, but
there is clearly a very large space of possible designs
here. (Consider that not only do Mark and Nathaniel disagree on so
many decisions up above, but numpy.ma actually disagrees with each of
them on about half of those!) So lighter-weight prototypes that can be
easily tweaked and experimented with seem like they'd give us much
more valuable data than would a monolithic C implementation that's
embedded in a library that few people understand and that has a slow
release cycle.

And finally, **Nathaniel** is actually still worried about whether
adding masking support to the core ndarray object is a good idea *at
all*. Unlike the "missing data" use case, the "ignoring data" use case
is really just about adding some convenience short-hands -- but it
comes at the cost of complexifying all ndarray code, at least to the
extent of making everyone have to think more often, every time they
write a function, about what would happen if someone were to pass in a
masked array. (Again, consider the my_mean function above.) (It is at
least a little weird, right, that we've reached the point where we're
seriously considering making it so numpy *would not support* a simple
array-of-doubles data structure, and would *only* support an
array-of-double-plus-mask structure? Even if we're going to have some
optimizations to avoid allocating the mask when unnecessary?
Especially since most people paying attention to this are the ones who
like masked arrays, not the ones who are happy with plain old arrays?)
A lot of numpy's power and clarity come from having a small number of
orthogonal concepts (strided arrays, indexing, broadcasting,
ufuncs). There's always a temptation to extend a foundational library
like this to provide pre-packaged solutions to specific problems,
because wouldn't it be convenient if instead of having to look in the
cookbook, I could just look in the library docs? So he's worried that
we might be succumbing to this temptation in a bad way, and losing
that orthogonality. Of course, we might also be succumbing in a good
way -- not ruling that out.

But there's no a priori reason why we can't arrange it so that np.ma
or a third-party library (``pip install masked_array``) can have
first-class functionality, even without being built into the numpy
core. So along with debating the best masking *API*, **Nathaniel**
thinks we should still consider seriously whether the best masking
*implementation* might consist of some minimal, generally-useful hooks
into ndarray and the ufunc machinery, plus a separate library. And in
case we find we can't easily distinguish which API is best from
discussion and playing with prototypes alone, this approach would also
allow competing masking APIs to fight it out for developer mind-share
without having to fork numpy itself.

References/history
==================

The original NEP describes Mark's NA-semantics/mask
implementation/view based mask handling API:
  https://github.com/numpy/numpy/blob/master/doc/neps/missing-data.rst

The alterNEP was Nathaniel's initial attempt at separating MISSING and
IGNORED handling into bit-patterns versus masks:
  https://gist.github.com/1056379

miniNEP 2 was a later attempt by Nathaniel to sketch out an
implementation strategy for NA dtypes:
  https://gist.github.com/1068264

A discussion overview page is here:
  https://github.com/njsmith/numpy/wiki/NA-discussion-status

Other issues
============

Thought of this, wanted to raise a flag -- it isn't clear how
generalized ufuncs interact with any of this. Traditional ufuncs put
the generic machinery in charge of the looping, so the generic
machinery can play tricks like skipping values which should be
ignored. Generalized ufuncs allow for operations like dot product,
where a loop happens inside the function-specific code. Do we need to
add a where_mask argument to the generalized ufunc signature, so that
this internal loop can do the right thing?

