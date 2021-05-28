---
title: 소식
sidebar: false
---

### Numpy 1.20.0 출시

_2021년 1월 30일_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)이 출시되었습니다. 역대 최대의 NumPy 릴리즈입니다. 180명이 넘는 기여자분들께 감사드립니다. 흥미롭고 새로운 두 기능이 나왔습니다.
- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule containing `ArrayLike` and `DtypeLike` aliases that users and downstream libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE, AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant performance improvements for many functions (examples: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPy 프로젝트 내 다양성

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).


### First official NumPy paper published in Nature!

_Sep 16, 2020_ -- We are pleased to announce the publication of [the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2) as a review article in Nature. This comes 14 years after the release of NumPy 1.0. The paper covers applications and fundamental concepts of array programming, the rich scientific Python ecosystem built on top of NumPy, and the recently added array protocols to facilitate interoperability with external array and tensor libraries like CuPy, Dask, and JAX.


### Python 3.9 is coming, when will NumPy release binary wheels?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. If you are an early adopter of Python versions, you may be dissapointed to find that NumPy (and other binary packages like SciPy) will not have binary wheels ready on the day of the release. It is a major effort to adapt the build infrastructure to a new Python version and it typically takes a few weeks for the packages to appear on PyPI and conda-forge. In preparation for this event, please make sure to
- update your `pip` to version 20.1 at least to support `manylinux2010` and `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from trying to build from source.


### Numpy 1.19.2 release

_Sep 10, 2020_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) is now available. This latest release in the 1.19 series fixes several bugs, prepares for the [upcoming Cython 3.x release](http://docs.cython.org/en/latest/src/changes.html) and pins setuptools to keep distutils working while upstream modifications are ongoing. The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

### The inaugural NumPy survey is live!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. The survey is available in 8 additional languages besides English: Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey [here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy에 새로운 로고가 생겼습니다!

_2020년 6월 24일_ -- NumPy에 새로운 로고가 생겼습니다.

<img src="/images/logos/numpy_logo.svg" alt="NumPy 로고" title="새 NumPy 로고" width=300>

이전 로고를 깔끔하고 현대적으로 다시 디자인했습니다. 새 로고를 만들어 주신 Isabela Presedo-Floyd님께 감사드립니다. 또 15년이 넘는 기간 동안 저희가 사용했던 로고를 만들어 주신 Travis Vaught님께도 감사의 말씀을 드립니다.


### NumPy 1.19.0 출시

_2020년 6월 20일_ -- NumPy 1.19.0이 출시되었습니다. Python 2의 지원을 중단한 첫 릴리즈라서 "정리 릴리즈"라고도 불립니다. 이제 지원하는 Python 최소 버전은 3.6입니다. 중요한 새 기능을 꼽자면, NumPy 1.17.0에 도입된 난수 생성 인프라를 Cython에서 접근할 수 있게 되었다는 것입니다.


### Season of Docs acceptance

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 release

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPy가 Chan Zuckerberg Initiative에서 보조금을 받음

_2019년 11월 15일_ -- NumPy의 주요 종속 패키지 중 하나인 NumPy와 OpenBLAS가 챈 저커버그 이니셔티브의 [과학 프로그램용 중요 오픈소스 소프트웨어](https://chanzuckerberg.com/eoss/) 지원을 통해 19만 5천 달러에 달하는 공동 보조금을 받았다는 소식을 전할 수 있어 기쁩니다. 이곳에서는 과학에 중요한 오픈소스 도구에 대해 유지 관리, 성장, 개발 및 커뮤니티 참여를 지원합니다.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## 릴리즈

NumPy 릴리즈의 목록입니다. 모든 버그 수정 릴리즈(`x.y.z`에서 `z`만 바뀐 경우)에는 새로운 기능이 없습니다. 마이너 릴리즈(`y`가 증가한 경우)에는 새로운 기능이 있습니다.

- NumPy 1.18.4 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020년 5월 3일_.
- NumPy 1.18.3 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.3)) -- _2020년 4월 19일_.
- NumPy 1.18.2 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _2020년 3월 17일_.
- NumPy 1.18.1 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _2020년 1월 6일_.
- NumPy 1.17.5 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _2020년 1월 1일_.
- NumPy 1.18.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _2019년 12월 22일_.
- NumPy 1.17.4 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _2019년 11월 11일_.
- NumPy 1.17.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _2019년 7월 26일_.
- NumPy 1.16.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _2019년 1월 14일_.
- NumPy 1.15.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018년 7월 23일_.
- NumPy 1.14.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018년 1월 7일_.
