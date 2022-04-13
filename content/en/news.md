---
title: News
sidebar: false
newsHeader: NumFOCUS DEI research study - call for participation
date:
---

### NumFOCUS DEI research study: call for participation

NumPy is working with [NumFOCUS](http://numfocus.org/) on a
[research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c)
funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to
understand the barriers to participation that contributors, particularly those
from historically underrepresented groups, face in the open-source software
community. The research team would like to talk to new contributors, project
developers and maintainers, and those who have contributed in the past about
their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe)
which contains additional information on the research goals, privacy, and
confidentiality considerations. Your participation will be valuable to the
growth and sustainability of diverse and inclusive open-source software
communities. Accepted participants will participate in a 30-minute interview
with a research team member.

### Numpy 1.22.0 release

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)
is now available. The highlights of the release are:

* Type annotations of the main namespace are essentially complete. Upstream is
  a moving target, so there will likely be further improvements, but the major
  work is done. This is probably the most user visible enhancement in this
  release.
* A preliminary version of the proposed
  [array API Standard](https://data-apis.org/array-api/latest/) is provided
  (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)).
  This is a step in creating a standard collection of functions that can be
  used across libraries such as CuPy and JAX.
* NumPy now has a DLPack backend. DLPack provides a common interchange format
  for array (tensor) data.
* New methods for ``quantile``, ``percentile``, and related functions. The new
  methods provide a complete set of the methods commonly found in the
  literature.
* The universal functions have been refactored to implement most of
  [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html).
  This also unlocks the ability to experiment with the future DType API.
* A new configurable memory allocator for use by downstream projects.

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread
over 609 pull requests. The Python versions supported by this release are
3.8-3.10.

### Advancing an inclusive culture in the scientific Python ecosystem

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has
[awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)
to support the onboarding, inclusion, and retention of people from historically
marginalized groups on scientific Python projects, and to structurally improve
the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/),
this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)
will support the creation of dedicated Contributor Experience Lead positions to
identify, document, and implement practices to foster inclusive open-source
communities. This project will be led by Melissa Mendonça (NumPy), with
additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy),
Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and
Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that
should structurally improve the community dynamics of our projects. By
establishing these new cross-project roles, we hope to introduce a new
collaboration model to the Scientific Python communities, allowing
community-building work within the ecosystem to be done more efficiently and
with greater outcomes. We also expect to develop a clearer picture of what
works and what doesn't in our projects to engage and retain new contributors,
especially from historically underrepresented groups. Finally, we plan on
producing detailed reports on the actions executed, explaining how they have
impacted our projects in terms of representation and interaction with our
communities.

The two-year project is expected to start by November 2021, and we are excited
to see the results from this work!
[You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021 NumPy survey

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236
NumPy users from 75 countries participated in our inaugural survey last year.
The survey findings gave us a very good understanding of what we should focus
on for the next 12 months.

It’s time for another survey, and we are counting on you once again. It will
take about 15 minutes of your time. Besides English, the survey questionnaire
is available in 8 additional languages: Bangla, French, Hindi, Japanese,
Mandarin, Portuguese, Russian, and Spanish.

Follow the link to get started: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### Numpy 1.21.0 release

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)
is now available. The highlights of the release are:

- continued SIMD work covering more functions and platforms,
- initial work on the new dtype infrastructure and casting,
- universal2 wheels for Python 3.8 and Python 3.9 on Mac,
- improved documentation,
- improved annotations,
- new ``PCG64DXSM`` bitgenerator for random numbers.

This NumPy release is the result of 581 merged pull requests contributed by 175
people.  The Python versions supported for this release are 3.7-3.9, support
for Python 3.10 will be added after Python 3.10 is released.


### 2020 NumPy survey results

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students
and faculty from the University of Michigan and the University of Maryland
conducted the first official NumPy community survey. Find the survey results
here: https://numpy.org/user-survey-2020/.


### Numpy 1.20.0 release

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)
is now available. This is the largest NumPy release to date, thanks to 180+
contributors. The two most exciting new features are:
- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule
  containing `ArrayLike` and `DtypeLike` aliases that users and downstream
  libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE,
  AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant
  performance improvements for many functions (examples:
  [sin/cos](https://github.com/numpy/numpy/pull/17587),
  [einsum](https://github.com/numpy/numpy/pull/18194)).

### Diversity in the NumPy project

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).


### First official NumPy paper published in Nature!

_Sep 16, 2020_ -- We are pleased to announce the publication of
[the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2)
as a review article in Nature. This comes 14 years after the release of NumPy 1.0.
The paper covers applications and fundamental concepts of array programming,
the rich scientific Python ecosystem built on top of NumPy, and the recently added
array protocols to facilitate interoperability with external array and tensor
libraries like CuPy, Dask, and JAX.


### Python 3.9 is coming, when will NumPy release binary wheels?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. If you are an
early adopter of Python versions, you may be dissapointed to find that NumPy
(and other binary packages like SciPy) will not have binary wheels ready on the
day of the release. It is a major effort to adapt the build infrastructure to a
new Python version and it typically takes a few weeks for the packages to appear
on PyPI and conda-forge. In preparation for this event, please make sure to
- update your `pip` to version 20.1 at least to support `manylinux2010` and
  `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from
  trying to build from source.


### Numpy 1.19.2 release

_Sep 10, 2020_ -- [NumPy
1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) is now available.
This latest release in the 1.19 series fixes several bugs, prepares for the
[upcoming Cython 3.x
release](http://docs.cython.org/en/latest/src/changes.html) and pins
setuptools to keep distutils working while upstream modifications are ongoing.
The aarch64 wheels are built with the latest manylinux2014 release that fixes
the problem of differing page sizes used by different linux distros.

### The inaugural NumPy survey is live!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for
decision-making about the development of NumPy as software and as a community.
The survey is available in 8 additional languages besides English:
Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey
[here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy has a new logo!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img
  src="/images/logos/numpy_logo.svg"
  alt="NumPy logo"
  title="The new NumPy logo"
  width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to
Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught
for the old logo that served us well for 15+ years.


### NumPy 1.19.0 release

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release
without Python 2 support, hence it was a "clean-up release". The minimum
supported Python version is now Python 3.6. An important new feature is that
the random number generation infrastructure that was introduced in NumPy 1.17.0
is now accessible from Cython.


### Season of Docs acceptance

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for
the Google Season of Docs program. We are excited about the opportunity to
work with a technical writer to improve NumPy's documentation once again! For more
details, please see
[the official Season of Docs site](https://developers.google.com/season-of-docs/) and our
[ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 release

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in
1.17.0, this is a consolidation release. It is the last minor release that will
support Python 3.5. Highlights of the release includes the addition of basic
infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for ``numpy.random``.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPy receives a grant from the Chan Zuckerberg Initiative

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## Releases

Here is a list of NumPy releases, with links to release notes. Bugfix
releases (only the `z` changes in the `x.y.z` version number) have no new
features; minor releases (the `y` increases) do.

- NumPy 1.21.6 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 Apr 2022_.
- NumPy 1.22.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.3)) -- _7 Mar 2022_.
- NumPy 1.22.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 Feb 2022_.
- NumPy 1.22.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 Jan 2022_.
- NumPy 1.22.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 Dec 2021_.
- NumPy 1.21.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 Dec 2021_.
- NumPy 1.21.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 Jun 2021_.
- NumPy 1.20.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 May 2021_.
- NumPy 1.20.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 Jan 2021_.
- NumPy 1.19.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 Jan 2021_.
- NumPy 1.19.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _20 Jun 2020_.
- NumPy 1.18.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 May 2020_.
- NumPy 1.17.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 Jan 2020_.
- NumPy 1.18.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 Dec 2019_.
- NumPy 1.17.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 Jul 2019_.
- NumPy 1.16.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 Jan 2019_.
- NumPy 1.15.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 Jul 2018_.
- NumPy 1.14.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 Jan 2018_.
