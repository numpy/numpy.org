---
title: 소식
sidebar: false
---

### Advancing an inclusive culture in the scientific Python ecosystem

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has [awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) to support the onboarding, inclusion, and retention of people from historically marginalized groups on scientific Python projects, and to structurally improve the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/), this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) will support the creation of dedicated Contributor Experience Lead positions to identify, document, and implement practices to foster inclusive open-source communities. This project will be led by Melissa Mendonça (NumPy), with additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy), Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that should structurally improve the community dynamics of our projects. By establishing these new cross-project roles, we hope to introduce a new collaboration model to the Scientific Python communities, allowing community-building work within the ecosystem to be done more efficiently and with greater outcomes. We also expect to develop a clearer picture of what works and what doesn't in our projects to engage and retain new contributors, especially from historically underrepresented groups. Finally, we plan on producing detailed reports on the actions executed, explaining how they have impacted our projects in terms of representation and interaction with our communities.

2개년 프로젝트가 2021년 11월부터 시작될 예정입니다. 프로젝트의 결과를 볼 날이 기대되네요! [전체 정보는 여기서 열람하실 수 있습니다](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021년도 NumPy 설문조사

_2021년 7월 12일_ -- NumPy에서, 우리는 커뮤니티의 힘을 믿습니다. 1,236 NumPy users from 75 countries participated in our inaugural survey last year. 설문 조사 결과를 통해 다음 12개월 동안 우리가 어떤 것에 집중해야 할지 아주 잘 이해할 수 있었습니다.

이제 또다른 설문 조사를 진행할 시간이고, 여러분의 도움이 다시 한 번 필요합니다. 완료하는 데 약 15분 정도 소요될 겁니다. 설문지는 영어 외에도 8개 국어로 제공됩니다: 벵골어, 프랑스어, 힌디어, 일본어, 중국 관화, 포르투갈어, 러시아어, 스페인어.

시작하려면 아래 링크를 눌러 주세요: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### Numpy 1.21.0 출시

_2021년 6월 23일_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)이 출시되었습니다. 주요 기능들은 다음과 같습니다:

- continued SIMD work covering more functions and platforms,
- initial work on the new dtype infrastructure and casting,
- universal2 wheels for Python 3.8 and Python 3.9 on Mac,
- 문서화 향상,
- 주석 향상,
- 난수 생성에 이용되는 새 `PCG64DXSM` 비트 생성기

이번 NumPy 릴리즈는 175명이 기여해주신 581개의 풀 리퀘스트가 합쳐진 결과입니다. The Python versions supported for this release are 3.7-3.9, support for Python 3.10 will be added after Python 3.10 is released.


### 2020년도 NumPy 설문조사 결과

_2021년 6월 22일_ -- 2020년에, NumPy 조사 팀은 조사방법론 학사 과정의 학생 및 교수와 협력하여 미시간 대학과 매릴렌드 대학이 공동으로 개최한 첫 공식 NumPy 커뮤니티 조사를 실시했습니다. 여기서 조사 결과를 확인하세요: https://numpy.org/user-survey-2020/.


### Numpy 1.20.0 출시

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) is now available. This is the largest NumPy release to date, thanks to 180+ contributors. The two most exciting new features are:
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


### Numpy 1.19.2 출시

_2020년 9월 10일_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html)이 출시되었습니다. This latest release in the 1.19 series fixes several bugs, prepares for the [upcoming Cython 3.x release](http://docs.cython.org/en/latest/src/changes.html) and pins setuptools to keep distutils working while upstream modifications are ongoing. The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

### The inaugural NumPy survey is live!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. 설문지는 영어 외에도 8개 국어로 제공됩니다: 벵골어, 프랑스어, 힌디어, 일본어, 중국 관화, 포르투갈어, 러시아어, 스페인어.

NumPy를 개선할 수 있도록 도와주시고 [여기](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl)에서 설문 조사에 참여해주시면 감사드리겠습니다.


### NumPy에 새로운 로고가 생겼습니다!

_2020년 6월 24일_ -- NumPy에 새로운 로고가 생겼습니다.

<img src="/images/logos/numpy_logo.svg" alt="NumPy 로고" title="새 NumPy 로고" width=300>

이전 로고를 깔끔하고 현대적으로 다시 디자인했습니다. 새 로고를 만들어 주신 Isabela Presedo-Floyd님께 감사드립니다. 또 15년이 넘는 기간 동안 저희가 사용했던 로고를 만들어 주신 Travis Vaught님께도 감사의 말씀을 드립니다.


### NumPy 1.19.0 출시

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### Season of Docs acceptance

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 출시

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPy가 Chan Zuckerberg Initiative에서 보조금을 받음

_2019년 11월 15일_ -- NumPy의 주요 종속 패키지 중 하나인 NumPy와 OpenBLAS가 챈 저커버그 이니셔티브의 [과학 프로그램용 중요 오픈소스 소프트웨어](https://chanzuckerberg.com/eoss/) 지원을 통해 19만 5천 달러에 달하는 공동 보조금을 받았다는 소식을 전할 수 있어 기쁩니다. 이곳에서는 과학에 중요한 오픈소스 도구에 대해 유지 관리, 성장, 개발 및 커뮤니티 참여를 지원합니다.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## 릴리즈

NumPy 릴리즈의 목록을 볼 수 있으며, 릴리즈 노트로 링크도 걸려 있습니다. 버그 수정 릴리즈(`x.y.z`에서 `z`만 바뀐 경우)에는 새로운 기능이 없습니다. 마이너 릴리즈(`y`가 증가한 경우)에는 새로운 기능이 있습니다.

- NumPy 1.21.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _2021년 6월 22일_.
- NumPy 1.20.3 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _2021년 5월 10일_.
- NumPy 1.20.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _2021년 1월 30일_.
- NumPy 1.19.5 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _2021년 1월 5일_.
- NumPy 1.19.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _2020년 6월 20일_.
- NumPy 1.18.4 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020년 5월 3일_.
- NumPy 1.17.5 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _2020년 1월 1일_.
- NumPy 1.18.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _2019년 12월 22일_.
- NumPy 1.17.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _2019년 7월 26일_.
- NumPy 1.16.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _2019년 1월 14일_.
- NumPy 1.15.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018년 7월 23일_.
- NumPy 1.14.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018년 1월 7일_.
