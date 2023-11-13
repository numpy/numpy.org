---
title: 소식
sidebar: false
newsHeader: "NumPy 1.26.0 출시"
date: 2023-09-16
---

### NumPy 1.26.0 출시

_2023년 12월 16일_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)이 출시되었습니다. 주요 기능들은 다음과 같습니다:

* 파이썬 3.12.0 지원
* Cython 3.0.0 호환
* Meson 빌드 시스템 사용
* 업데이트된 SIMD 지원
* f2py 수정, meson 및 bind(x) 지원
* 업데이트된 Accelerate BLAS/LAPACK 라이브러리 지원

NumPy 1.26.0 릴리스는 Meson 빌드 시스템으로의 전환과 Cython 3.0.0 지원을 표시하는 1.25.x 시리즈의 연장입니다. 총 20명의 사람들이 이 릴리스에 기여하였으며 59개의 풀 리퀘스트가 병합되었습니다.

본 릴리즈에서 지원하는 Python 버전은 3.3.9-3.12입니다.

### numpy.org은 이제 일본어와 포르투갈어로도 이용 가능합니다.

_2023년 8월 2일_ - numpy.org은 이제 추가로 일본어와 포르투갈어로 이용 가능합니다. 이는 다음의 헌신적인 자원봉사자들의 노력 없이는 가능하지 않았을 것입니다:

_포르투갈어_
* Melissa Weber Mendonça (melissawm)
* Ricardo Prins (ricardoprins)
* Getúlio Silva (getuliosilva)
* Julio Batista Silva (jbsilva)
* Alexandre de Siqueira (alexdesiqueira)
* Alexandre B A Villares (villares)
* Vini Salazar (vinisalazar)

_일본어_
* Atsushi Sakai (AtsushiSakai)
* KKunai
* Tom Kelly (TomKellyGenetics)
* Yuji Kanagawa (kngwyu)
* Tetsuo Koyama (tkoyama010)

번역 인프라에 대한 작업은 CZI로부터의 자금 지원을 받아 진행되었습니다.

나아가서 NumPy 웹사이트가 더 많은 언어로 번역되기를 바랍니다. 도움을 주시려면 다음 Slack 링크를 통해 NumPy Translations Team 에 연락을 주십시오: https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w. (#translations 채널을 add 해주세요) 또한 과학적 파이썬 생태계 전반에서 문서 및 교육 콘텐츠를 지역화하는데 참여할 Translations Team을 구축하고 있습니다. 이에 흥미를 느낀다면 Scientific Python Discord에서 함께해 주세요: https://discord.gg/khWtqY6RKr. (#translation 채널을 찾아보세요)

### NumPy 1.25.0 출시

_2023년 6월 17일_ -- 이제 [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html)을 이용할 수 있습니다. 주요 기능들은 다음과 같습니다:

* MUSL 지원, 이제 MUSL Wheel도 배포됩니다.
* Fujitsu C/C++ 컴파일러 지원
* Einsum에서 객체 배열 지원
* Inplace 행렬 곱셈 (`@=`) 지원

The NumPy 1.25.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, and clarify the documentation. There has also been preparatory work for the future NumPy 2.0.0, resulting in a large number of new and expired deprecations.

A total of 148 people contributed to this release and 530 pull requests were merged.

The Python versions supported by this release are 3.9-3.11.

### Fostering an Inclusive Culture: Call for Participation

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

How can we be better when it comes to diversity and inclusion? Read the report and find out how to get involved [here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy documentation team leadership transition

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy documentation team leads replacing Melissa Mendonça. We thank Melissa for all her contributions to the NumPy official documentation and educational materials, and Mukulika and Ross for stepping up.

### NumPy 1.24.0 출시

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) is now available. The highlights of the release are:

* New "dtype" and "casting" keywords for stacking functions.
* New F2PY features and fixes.
* Many new deprecations, check them out.
* Many expired deprecations,

The NumPy 1.24.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase execution speed, and clarify the documentation. There are a large number of new and expired deprecations due to changes in dtype promotion and cleanups. It is the work of 177 contributors spread over 444 pull requests. The supported Python versions are 3.8-3.11.

### NumPy 1.23.0 출시

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) is now available. The highlights of the release are:

* Implementation of `loadtxt` in C, greatly improving its performance.
* Exposure of DLPack at the Python level for easy data exchange.
* Changes to the promotion and comparisons of structured dtypes.
* Improvements to f2py.

The NumPy 1.23.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, clarify the documentation, and expire old deprecations. It is the work of 151 contributors spread over 494 pull requests. The Python versions supported by this release 3.8-3.10. Python 3.11 will be supported when it reaches the rc stage.

### NumFOCUS DEI research study: call for participation

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a [research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c) funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to understand the barriers to participation that contributors, particularly those from historically underrepresented groups, face in the open-source software community. The research team would like to talk to new contributors, project developers and maintainers, and those who have contributed in the past about their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe) which contains additional information on the research goals, privacy, and confidentiality considerations. Your participation will be valuable to the growth and sustainability of diverse and inclusive open-source software communities. Accepted participants will participate in a 30-minute interview with a research team member.

### Numpy 1.22.0 출시

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) is now available. The highlights of the release are:

* Type annotations of the main namespace are essentially complete. Upstream is a moving target, so there will likely be further improvements, but the major work is done. This is probably the most user visible enhancement in this release.
* A preliminary version of the proposed [array API Standard](https://data-apis.org/array-api/latest/) is provided (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)). This is a step in creating a standard collection of functions that can be used across libraries such as CuPy and JAX.
* NumPy now has a DLPack backend. DLPack provides a common interchange format for array (tensor) data.
* New methods for `quantile`, `percentile`, and related functions. The new methods provide a complete set of the methods commonly found in the literature.
* The universal functions have been refactored to implement most of [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html). This also unlocks the ability to experiment with the future DType API.
* A new configurable memory allocator for use by downstream projects.

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread over 609 pull requests. The Python versions supported by this release are 3.8-3.10.

### Advancing an inclusive culture in the scientific Python ecosystem

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has [awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) to support the onboarding, inclusion, and retention of people from historically marginalized groups on scientific Python projects, and to structurally improve the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/), this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) will support the creation of dedicated Contributor Experience Lead positions to identify, document, and implement practices to foster inclusive open-source communities. This project will be led by Melissa Mendonça (NumPy), with additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy), Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that should structurally improve the community dynamics of our projects. By establishing these new cross-project roles, we hope to introduce a new collaboration model to the Scientific Python communities, allowing community-building work within the ecosystem to be done more efficiently and with greater outcomes. We also expect to develop a clearer picture of what works and what doesn't in our projects to engage and retain new contributors, especially from historically underrepresented groups. Finally, we plan on producing detailed reports on the actions executed, explaining how they have impacted our projects in terms of representation and interaction with our communities.

The two-year project is expected to start by November 2021, and we are excited to see the results from this work! [You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021년도 NumPy 설문조사

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 NumPy users from 75 countries participated in our inaugural survey last year. The survey findings gave us a very good understanding of what we should focus on for the next 12 months.

It’s time for another survey, and we are counting on you once again. It will take about 15 minutes of your time. Besides English, the survey questionnaire is available in 8 additional languages: Bangla, French, Hindi, Japanese, Mandarin, Portuguese, Russian, and Spanish.

Follow the link to get started: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### Numpy 1.21.0 출시

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) is now available. The highlights of the release are:

- continued SIMD work covering more functions and platforms,
- initial work on the new dtype infrastructure and casting,
- universal2 wheels for Python 3.8 and Python 3.9 on Mac,
- improved documentation,
- improved annotations,
- new `PCG64DXSM` bitgenerator for random numbers.

This NumPy release is the result of 581 merged pull requests contributed by 175 people.  The Python versions supported for this release are 3.7-3.9, support for Python 3.10 will be added after Python 3.10 is released.


### 2020년도 NumPy 설문조사 결과

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students and faculty from the University of Michigan and the University of Maryland conducted the first official NumPy community survey. Find the survey results here: https://numpy.org/user-survey-2020/.


### Numpy 1.20.0 출시

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) is now available. This is the largest NumPy release to date, thanks to 180+ contributors. The two most exciting new features are:
- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule containing `ArrayLike` and `DtypeLike` aliases that users and downstream libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE, AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant performance improvements for many functions (examples: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPy 프로젝트 내 다양성

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).


### Nature에 첫 공식 NumPy 논문 발표!

_Sep 16, 2020_ -- We are pleased to announce the publication of [the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2) as a review article in Nature. This comes 14 years after the release of NumPy 1.0. The paper covers applications and fundamental concepts of array programming, the rich scientific Python ecosystem built on top of NumPy, and the recently added array protocols to facilitate interoperability with external array and tensor libraries like CuPy, Dask, and JAX.


### Python 3.9가 곧 출시하는데, NumPy는 바이너리 Wheel을 언제 출시합니까?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. If you are an early adopter of Python versions, you may be dissapointed to find that NumPy (and other binary packages like SciPy) will not have binary wheels ready on the day of the release. It is a major effort to adapt the build infrastructure to a new Python version and it typically takes a few weeks for the packages to appear on PyPI and conda-forge. In preparation for this event, please make sure to
- update your `pip` to version 20.1 at least to support `manylinux2010` and `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from trying to build from source.


### NumPy 1.19.2 출시

_Sep 10, 2020_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) is now available. This latest release in the 1.19 series fixes several bugs, prepares for the [upcoming Cython 3.x release](http://docs.cython.org/en/latest/src/changes.html) and pins setuptools to keep distutils working while upstream modifications are ongoing. The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

### 최초의 NumPy 설문조사가 진행 중입니다!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. The survey is available in 8 additional languages besides English: Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey [here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy에 새로운 로고가 생겼습니다!

_2020년 6월 24일_ -- NumPy에 새로운 로고가 생겼습니다.

<img src="/images/logos/numpy_logo.svg" alt="NumPy 로고" title="새 NumPy 로고" width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught for the old logo that served us well for 15+ years.


### NumPy 1.19.0 출시

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### Season of Docs 승인

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 출시

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPy가 Chan Zuckerberg Initiative에서 보조금을 받았습니다

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


<a name="releases"></a>

## 릴리즈

NumPy 릴리즈의 목록입니다. 릴리즈 노트로 링크도 걸려 있습니다. 버그 수정 릴리즈(`x.y.z`에서 `z`만 바뀐 경우)에는 새로운 기능이 없습니다. 마이너 릴리즈(`y`가 증가한 경우)에는 새로운 기능이 있습니다.

- NumPy 1.26.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _12 Nov 2023_.
- NumPy 1.26.1 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _2023년 10월 14일_.
- NumPy 1.26.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _2023년 16월 9일_.
- NumPy 1.25.2 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.25.2)) -- _2023년 7월 31일_.
- NumPy 1.25.1 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _2023년 7월 8일_.
- NumPy 1.24.4 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _2023년 6월 26일_.
- NumPy 1.25.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _2023년 6월 17일_.
- NumPy 1.24.3 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _2023년 4월 22일_.
- NumPy 1.24.2 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _2023년 2월 5일_.
- NumPy 1.24.1 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _2022년 12월 26일_.
- NumPy 1.24.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.24.0)) -- _2022년 12월 18일_.
- NumPy 1.23.5 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _2022년 11월 19일_.
- NumPy 1.23.4 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _2022년 10월 12일_.
- NumPy 1.23.3 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _2022년 9월 9일_.
- NumPy 1.23.2 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _2022년 8월 14일_.
- NumPy 1.23.1 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _2022년 7월 8일_.
- NumPy 1.23.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _2022년 6월 22일_.
- NumPy 1.22.4 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _2022년 5월 20일_.
- NumPy 1.21.6 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _2022년 4월 12일_.
- NumPy 1.22.3 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.22.3)) -- _2022년 3월 7일_.
- NumPy 1.22.2 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _2022년 2월 3일_.
- NumPy 1.22.1 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _2022년 1월 14일_.
- NumPy 1.22.0 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _2021년 12월 31일_.
- NumPy 1.21.5 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _2021년 12월 19일_.
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
