---
title: 소식
sidebar: false
newsHeader: NumPy 2.2.0 released!
date: 2023-09-16
---

### NumPy 2.2.0 released

_8 Dec, 2024_ -- The NumPy 2.2.0 release is a quick release that brings us back
into sync with the usual twice yearly release cycle. There have been a number
of small cleanups, improvements to the StringDType, and better support for free
threaded Python. Highlights are:

- New functions `matvec` and `vecmat`,
- Many improved annotations,
- Improved support for the new StringDType,
- Improved support for free threaded Python,
- Fixes for f2py.

This release supports Python versions 3.10-3.13.

### NumPy 2.1.0 released

_18 Aug, 2024_ -- NumPy 2.1.0 provides support for Python 3.13 and
drops support for Python 3.9. 일반적인 버그 수정과 파이썬 지원 개정에 덧붙여 2.0 확장 개발 이후 NumPy를 평상적인 배포 싸이클로 복귀하도록 돕고자 하는 것입니다. The highlights for this
release are:

- Support for Python 3.13.
- Preliminary support for free threaded Python 3.13.
- Support for the array-api 2023.12 standard.

Python versions 3.10-3.13 are supported by this release.

### NumPy 2.0 출시일: 6월 16일

_16 Jun, 2024_ -- NumPy 2.0.0 is the first major release since 2006. It is the
result of 11 months of development since the last feature release and is the
work of 212 contributors spread over 1078 pull requests. It contains a large
number of exciting new features as well as changes to both the Python and C
APIs.  It includes breaking changes that could not happen in a regular minor
release - including an ABI break, changes to type promotion rules, and API
changes which may not have been emitting deprecation warnings in 1.26.x. Key
documents related to how to adapt to changes in NumPy 2.0 include:

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

The blog post ["NumPy 2.0: an evolutionary milestone"](https://blog.scientific-python.org/numpy/numpy2/)
tells a bit of the story about how this release came together.

### NumPy 2.0 출시일: 6월 16일

_23 May, 2024_ -- We are excited to announce that NumPy 2.0 is planned to be
released on June 16, 2024. 이 릴리즈를 제작하는 데 1년이 넘게 걸렸고, 2006년 이후 첫 번째 메인 릴리즈입니다. Importantly, in addition to many new
features and performance improvement, it contains **breaking changes** to the
ABI as well as the Python and C APIs. It is likely that downstream packages and
end user code needs to be adapted - if you can, please verify whether your code
works with NumPy `2.0.0rc2`. **Please see the following for more details:**

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

### NumPy 1.26.0 출시

_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount
on first-time PyCharm licenses. 지금부터 2023년 12월 23일까지 PyCharm 구매로 발생한 모든 수익은 NumFOCUS 프로그램으로 직접 전달됩니다.

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/
or a coupon code ISUPPORTDATASCIENCE

### NumPy 1.26.0 출시

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)
is now available. 주요 기능들은 다음과 같습니다:

- 파이썬 3.12.0 지원
- Cython 3.0.0 호환
- Meson 빌드 시스템 사용
- 업데이트된 SIMD 지원
- f2py 수정, meson 및 bind(x) 지원
- 업데이트된 Accelerate BLAS/LAPACK 라이브러리 지원

NumPy 1.26.0 릴리스는 Meson 빌드 시스템으로의 전환과 Cython 3.0.0 지원을 표시하는 1.25.x 시리즈의 연장입니다.
총 20명의 사람들이 이 릴리스에 기여하였으며 59개의 풀 리퀘스트가 병합되었습니다.

본 릴리즈에서 지원하는 Python 버전은 3.3.9-3.12입니다.

### numpy.org은 이제 일본어와 포르투갈어로도 이용 가능합니다.

_Aug 2, 2023_ -- numpy.org is now available in 2 additional languages:
Japanese and Portuguese. 이는 다음의 헌신적인 자원봉사자들의 노력 없이는 가능하지 않았을 것입니다:

_Portuguese:_

- Melissa Weber Mendonça (melissawm)
- Ricardo Prins (ricardoprins)
- Getúlio Silva (getuliosilva)
- Julio Batista Silva (jbsilva)
- Alexandre de Siqueira (alexdesiqueira)
- Alexandre B A Villares (villares)
- Vini Salazar (vinisalazar)

_Japanese:_

- Atsushi Sakai (AtsushiSakai)
- KKunai
- Tom Kelly (TomKellyGenetics)
- Yuji Kanagawa (kngwyu)
- Tetsuo Koyama (tkoyama010)

번역 인프라에 대한 작업은 CZI로부터의 자금 지원을 받아 진행되었습니다.

나아가서 NumPy 웹사이트가 더 많은 언어로 번역되기를 바랍니다.
도움을 주시려면 다음 Slack 링크를 통해 NumPy Translations Team 에 연락을 주십시오: https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w.
(#translations 채널을 add 해주세요) 또한 과학적 파이썬 생태계 전반에서 문서 및 교육 콘텐츠를 지역화하는데 참여할 Translations Team을 구축하고 있습니다. 이에 흥미를 느낀다면 Scientific Python Discord에서 함께해 주세요: https://discord.gg/khWtqY6RKr. (#translation 채널을 찾아보세요)

### NumPy 1.25.0 출시

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html)
is now available. 주요 기능들은 다음과 같습니다:

- MUSL 지원, 이제 MUSL Wheel도 배포됩니다.
- Fujitsu C/C++ 컴파일러 지원
- Einsum에서 객체 배열 지원
- Support for the inplace matrix multiplication (`@=`).

NumPy 1.25.0 릴리스에서는 dtype의 처리 및 형변환을 개선하고
실행 속도를 높이는 작업, 문서를 보다 명료하게 다듬는
작업을 계속하고 있습니다. 미래의 NumPy 2.0.0을 위한 준비 작업도 있었는데,
이로 인해 수많은 기능들이 지원 종료 예정에 새로 포함되거나 완전히 만료되었습니다.

총 148명의 사람들이 이 릴리스에 기여하였으며 530개의 풀 리퀘스트가 병합되었습니다.

본 릴리즈에서 지원하는 Python 버전은 3.9-3.11입니다.

### 포용적인 문화 조성: 참여 요청

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

다양성과 포용성의 측면에서 우리는 어떻게 더 나아질 수 있을까요?
Read the report and find out how to get involved
[here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy 문서 팀 리더 변경

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy
documentation team leads replacing Melissa Mendonça. NumPy 공식 문서와 교육 자료에 기여한 Melissa와 한 걸음 더 나아간 Mukulika, Ross에게 감사를 표합니다.

### NumPy 1.24.0 출시

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html)
is now available. 주요 기능들은 다음과 같습니다:

- 스태킹 함수를 위한 새 "dtype" 및 "casting" 키워드.
- 새 F2PY 기능 및 수정.
- 수많은 지원 종료 예정 기능, 확인하세요.
- 수많은 만료된 기능,

NumPy 1.24.0 릴리스에서는 dtype의 처리 및 형변환을 개선하고 실행 속도를 높이는 작업, 문서를 보다 명료하게 다듬는 작업을 계속하고 있습니다.
dtype의 형변환 및 정리를 변경하는 과정에서 수많은 기능들이 지원 종료 예정에
새로 포함되거나 완전히 만료되었습니다. 177명의 기여자가 생성한
444개의 풀 요청을 바탕으로 한 성과입니다. 지원하는 Python 버전은 3.8-3.11입니다.

### NumPy 1.23.0 출시

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html)
is now available. 주요 기능들은 다음과 같습니다:

- Implementation of `loadtxt` in C, greatly improving its performance.
- 데이터 교환을 쉽게 하기 위해 Python 수준에서 DLPack을 개방합니다.
- 구조화된 dtype의 형변환 및 비교 방법을 변경했습니다.
- f2py를 개선했습니다.

NumPy 1.23.0 릴리스에서는 dtype의 처리 및 형변환을 개선하고 실행 속도를 높이는 작업, 문서를 보다 명료하게 다듬는 작업, 오래된 지원 종료 예정 기능을 완전히 만료시키는 작업을 계속하고 있습니다. 151명의 기여자가 생성한
494개의 풀 요청을 바탕으로 한 성과입니다. 본 릴리즈에서 지원하는 Python 버전은 3.8-3.10입니다.
Python 3.11은 rc 단계에 다다르면 지원할 예정입니다.

### NumFOCUS DEI 연구: 참여 요청

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a
research project
funded by the Gordon & Betty Moore Foundation to
understand the barriers to participation that contributors, particularly those
from historically underrepresented groups, face in the open-source software
community. 연구팀은 새 기여자, 프로젝트 개발자 및 유지관리자, 과거에 기여한 사람들과 NumPy에 참여하고 기여한 경험에 대해 이야기하고자 합니다.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe)
which contains additional information on the research goals, privacy, and
confidentiality considerations. 당신의 참여가 다양성과 포용성을 갖춘 오픈 소스 소프트웨어 커뮤니티의 성장과 지속 가능성에 도움이 될 것입니다. 승인된 참가자는 연구팀과 30분 면담을 진행하게 됩니다.

### Numpy 1.22.0 출시

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)
is now available. 주요 기능들은 다음과 같습니다:

- 기본 네임스페이스에 대해 유형 주석의 지원을 거의 완료했습니다. Upstream is
  a moving target, so there will likely be further improvements, but the major
  work is done. This is probably the most user visible enhancement in this
  release.
- A preliminary version of the proposed
  [array API Standard](https://data-apis.org/array-api/latest/) is provided
  (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)).
  This is a step in creating a standard collection of functions that can be
  used across libraries such as CuPy and JAX.
- NumPy가 DLPack 백엔드로 구동됩니다. DLPack provides a common interchange format
  for array (tensor) data.
- New methods for `quantile`, `percentile`, and related functions. The new
  methods provide a complete set of the methods commonly found in the
  literature.
- The universal functions have been refactored to implement most of
  [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html).
  이를 통해 미래의 DType API를 실험할 수 있는 능력도 갖췄습니다.
- 새 구성 가능한 메모리 할당자를 다운스트림 프로젝트에서 사용할 수 있습니다.

NumPy 1.22.0은 153명의 기여자가 생성한 609개의 풀 요청을 바탕으로 만들어진 대형 릴리즈입니다. 본 릴리즈에서 지원하는 Python 버전은 3.8-3.10입니다.

### 과학 Python 생태계에서 포용적 문화 발전

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has
[awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)
to support the onboarding, inclusion, and retention of people from historically
marginalized groups on scientific Python projects, and to structurally improve
the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/),
this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)
will support the creation of dedicated Contributor Experience Lead positions to
identify, document, and implement practices to foster inclusive open-source
communities. 이 프로젝트는 Melissa Mendonça(NumPy) 님이 이끌고 Ralf Gommers(NumPy, SciPy), Hannah Aizenman, Thomas Caswell(Matplotlib), Matt Haberland(SciPy), Joris Van den Bossche(Pandas) 님이 추가 멘토링 및 지침을 제공합니다.

이것은 프로젝트의 커뮤니티 역학을 구조적으로 개선해야 하는 활동을 발견하고 구현하는 것을 목표로 하는 야심 찬 프로젝트입니다. 새로운 교차 프로젝트 역할을 설정함으로써 과학적 Python 커뮤니티에 새로운 협업 모델을 도입하여 생태계 내에서 커뮤니티 구축 작업을 보다 효율적으로 수행하고 더 큰 결과를 얻을 수 있을 것으로 기대됩니다. 또한 특히 역사적으로 과소대표된 집단의 새로운 기여자를 참여시키고 유지하기 위해, 프로젝트에서 효과적인 것과 그렇지 않은 것에 대한 명확한 그림을 구축할 것으로 기대합니다. 마지막으로, 시행된 조치에 대해 자세한 보고서를 작성하여 커뮤니티와의 대표 및 상호 작용 측면에서 프로젝트에 어떤 영향을 미쳤는지 설명할 계획입니다.

2개년 프로젝트가 2021년 11월부터 시작될 예정입니다. 프로젝트의 결과를 볼 날이 기대되네요!
[You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021년도 NumPy 설문조사

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 작년에 75개국에서 1,236명의 NumPy 사용자가 첫 번째 설문조사에 참여했습니다.
설문 조사 결과를 통해 다음 12개월 동안 우리가 어떤 것에 집중해야 할지 아주 잘 이해할 수 있었습니다.

이제 또다른 설문 조사를 진행할 시간이고, 여러분의 도움이 다시 한 번 필요합니다. 완료하는 데 약 15분 정도 소요될 겁니다. 설문지는 영어 외에도 8개 국어로 제공됩니다: 벵골어, 프랑스어, 힌디어, 일본어, 중국 관화, 포르투갈어, 러시아어, 스페인어.

시작하려면 아래 링크를 눌러 주세요: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.

### Numpy 1.21.0 출시

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)
is now available. 주요 기능들은 다음과 같습니다:

- 더 많은 기능과 플랫폼을 다루는 지속적인 SIMD 작업,
- 새로운 dtype 인프라 및 캐스팅에 대한 초기 작업,
- Mac의 Python 3.8 및 Python 3.9용 universal2 휠,
- 문서화 향상,
- 주석 향상,
- new `PCG64DXSM` bitgenerator for random numbers.

이번 NumPy 릴리즈는 175명이 기여해주신 581개의 풀 리퀘스트가 합쳐진 결과입니다.  본 릴리즈에서 지원하는 Python 버전은 3.7-3.9입니다. Python 3.10은 Python 3.10 릴리즈 이후 지원할 예정입니다.

### 2020년도 NumPy 설문조사 결과

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students
and faculty from the University of Michigan and the University of Maryland
conducted the first official NumPy community survey. 여기서 조사 결과를 확인하세요: https://numpy.org/user-survey-2020/.

### Numpy 1.20.0 출시

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)
is now available. 역대 최대의 NumPy 릴리즈입니다. 180명이 넘는 기여자분들께 감사드립니다. 다음은 이번 출시에서 가장 흥미로운 두가지 기능들 입니다.

- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule
  containing `ArrayLike` and `DtypeLike` aliases that users and downstream
  libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE,
  AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant
  performance improvements for many functions (examples:
  [sin/cos](https://github.com/numpy/numpy/pull/17587),
  [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPy 프로젝트 내 다양성

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).

### Nature에 첫 공식 NumPy 논문 발표!

_Sep 16, 2020_ -- We are pleased to announce the publication of
[the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2)
as a review article in Nature. NumPy 1.0이 나온 지 14년 만입니다.
이 백서에서는 배열 프로그래밍의 응용 프로그램 및 기본 개념, NumPy 위에 구축된 풍부한 과학적 Python 생태계, CuPy, Dask 및 JAX와 같은 외부 배열 및 텐서 라이브러리와의 상호 운용성을 촉진하기 위해 최근에 추가된 배열 프로토콜을 다룹니다.

### Python 3.9가 곧 출시하는데, NumPy는 바이너리 Wheel을 언제 출시합니까?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. 만약 Python 얼리어답터라면, NumPy (그리고 SciPy 등 다른 바이너리 패키지) 가 릴리즈 시일에 바이너리 Wheel을 준비하지 못한다는 것을 알고 실망했을 수 있습니다. 새로운 Python 버전에 빌드 환경을 맞추는 것은 많은 노력을 요하고, 패키지가 PyPI 및 conda-forge에 배포되는 데에는 일반적으로 몇 주가 걸립니다. 출시를 대비하려면 아래 요건을 충족하도록 하십시오.

- update your `pip` to version 20.1 at least to support `manylinux2010` and
  `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from
  trying to build from source.

### NumPy 1.19.2 출시

_Sep 10, 2020_ -- NumPy
1.19.2 is now available.
This latest release in the 1.19 series fixes several bugs, prepares for the
upcoming Cython 3.x
release and pins
setuptools to keep distutils working while upstream modifications are ongoing.
aarch64 휠은 다양한 Linux 배포판에서 사용되는 다양한 페이지 크기 문제를 해결하는 최신 manylinux2014 릴리스로 제작되었습니다.

### 최초의 NumPy 설문조사가 진행 중입니다!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for
decision-making about the development of NumPy as software and as a community.
설문지는 영어 외에도 8개 국어로 제공됩니다: 벵골어, 프랑스어, 힌디어, 일본어, 중국 관화, 포르투갈어, 러시아어, 스페인어.

Please help us make NumPy better and take the survey
[here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).

### NumPy에 새로운 로고가 생겼습니다!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img
src="/images/logos/numpy_logo.svg"
alt="NumPy logo"
title="The new NumPy logo"
width=300>

이전 로고를 깔끔하고 현대적으로 다시 디자인했습니다. 새 로고를 만들어 주신 Isabela Presedo-Floyd님께 감사드립니다. 또 15년이 넘는 기간 동안 저희가 사용했던 로고를 만들어 주신 Travis Vaught님께도 감사의 말씀을 드립니다.

### NumPy 1.19.0 출시

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. Python 2의 지원을 중단한 첫 릴리즈라서 "정리 릴리즈"라고도 불립니다. 이제 지원하는 Python 최소 버전은 3.6입니다. 중요한 새 기능을 꼽자면, NumPy 1.17.0에 도입된 난수 생성 인프라를 Cython에서 접근할 수 있게 되었다는 것입니다.

### Season of Docs 승인

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for
the Google Season of Docs program. 테크니컬 라이터와 협력해서 NumPy 문서를 다시 한 번 개선할 수 있는 기회를 갖게 되어 좋습니다! For more
details, please see
[the official Season of Docs site](https://developers.google.com/season-of-docs/) and our
[ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).

### NumPy 1.18.0 출시

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. 1.17.0에서의 주요 변경점을 통합하는 릴리즈입니다. 본 릴리즈는 Python 3.5를 지원하는 마지막 마이너 릴리즈입니다. Highlights of the release includes the addition of basic
infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.

### NumPy가 Chan Zuckerberg Initiative에서 보조금을 받았습니다

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

이 보조금은 NumPy 문서, 웹사이트 재설계 및 커뮤니티 개발을 개선하여 빠르게 성장하는 대규모 사용자 기반에 더 나은 서비스를 제공하고 프로젝트의 장기적인 지속 가능성을 보장하는 데 사용될 것입니다. OpenBLAS 팀은 OpenBLAS가 의존하는 ReLAPACK(Recursive LAPACK) 의 알고리즘 개선뿐만 아니라 특히 스레드 안전성, AVX-512 및 스레드 로컬 스토리지(TLS) 문제와 같은 일련의 핵심 기술 문제를 해결하는 데 집중할 것입니다.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). 2019년 12월 1일부터 작업을 시작하여 다음 12개월 동안 진행할 예정입니다.

<a name="releases"></a>

## 릴리즈

NumPy 릴리즈의 목록입니다. 릴리즈 노트로 링크도 걸려 있습니다. Bugfix
releases (only the `z` changes in the `x.y.z` version number) have no new
features; minor releases (the `y` increases) do.

- 넘파이 2.2.5 ([릴리즈 노츠](https://github.com/numpy/numpy/releases/tag/v2.2.5)) -- _19 Apr 2025_.
- NumPy 2.2.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.4)) -- _16 Mar 2025_.
- NumPy 2.2.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.3)) -- _13 Feb 2025_.
- NumPy 2.2.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.2)) -- _18 Jan 2025_.
- NumPy 2.2.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.1)) -- _21 Dec 2024_.
- NumPy 2.2.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.0)) -- _8 Dec 2024_.
- NumPy 2.1.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.3)) -- _2 Nov 2024_.
- NumPy 2.1.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.2)) -- _5 Oct 2024_.
- NumPy 2.1.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.1)) -- _3 Sep 2024_.
- NumPy 2.0.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.2)) -- _26 Aug 2024_.
- NumPy 2.1.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.0)) -- _18 Aug 2024_.
- NumPy 2.0.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.1)) -- _21 Jul 2024_.
- NumPy 2.0.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.0)) -- _16 Jun 2024_.
- NumPy 1.26.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.4)) -- _5 Feb 2024_.
- NumPy 1.26.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _2 Jan 2024_.
- NumPy 1.26.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _12 Nov 2023_.
- NumPy 1.26.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _14 Oct 2023_.
- NumPy 1.26.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _16 Sep 2023_.
- NumPy 1.25.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.2)) -- _31 Jul 2023_.
- NumPy 1.25.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _8 Jul 2023_.
- NumPy 1.24.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _26 Jun 2023_.
- NumPy 1.25.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _17 Jun 2023_.
- NumPy 1.24.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 Apr 2023_.
- NumPy 1.24.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 Feb 2023_.
- NumPy 1.24.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 Dec 2022_.
- NumPy 1.24.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.0)) -- _18 Dec 2022_.
- NumPy 1.23.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _19 Nov 2022_.
- NumPy 1.23.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _12 Oct 2022_.
- NumPy 1.23.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 Sep 2022_.
- NumPy 1.23.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 Aug 2022_.
- NumPy 1.23.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 Jul 2022_.
- NumPy 1.23.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 Jun 2022_.
- NumPy 1.22.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 May 2022_.
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
