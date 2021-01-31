---
title: News
sidebar: false
---

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

Here is a list of NumPy releases, with links to release notes. All bugfix
releases (only the `z` changes in the `x.y.z` version number) have no new
features; minor releases (the `y` increases) do.

- NumPy 1.18.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 May 2020_.
- NumPy 1.18.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.3)) -- _19 Apr 2020_.
- NumPy 1.18.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _17 Mar 2020_.
- NumPy 1.18.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _6 Jan 2020_.
- NumPy 1.17.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 Jan 2020_.
- NumPy 1.18.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 Dec 2019_.
- NumPy 1.17.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _11 Nov 2019_.
- NumPy 1.17.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 Jul 2019_.
- NumPy 1.16.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 Jan 2019_.
- NumPy 1.15.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 Jul 2018_.
- NumPy 1.14.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 Jan 2018_.
