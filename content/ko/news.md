---
title: 소식
sidebar: false
newsHeader: "NumPy 1.26.0 출시"
date: 2023-09-16
---

### NumPy 1.26.0 출시
_2023년 12월 19_ -- NumFOCUS에서 연말 캠페인 기간 동안 PyCharm과 협력해 최초 PyCharm 이용자의 라이선스를 30% 할인된 가격에 제공했습니다. 지금부터 2023년 12월 23일까지 PyCharm 구매로 발생한 모든 수익은 NumFOCUS 프로그램으로 직접 전달됩니다.

구매를 추적할 수 있는 고유 URL을 이용하거나: https://lp.jetbrains.com/support-data-science/ 쿠폰 코드를 사용하세요: ISUPPORTDATASCIENCE 

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

NumPy 1.25.0 릴리스에서는 dtype의 처리 및 형변환을 개선하고 실행 속도를 높이는 작업, 문서를 보다 명료하게 다듬는 작업을 계속하고 있습니다. 미래의 NumPy 2.0.0을 위한 준비 작업도 있었는데, 이로 인해 수많은 기능들이 지원 종료 예정에 새로 포함되거나 완전히 만료되었습니다.

총 148명의 사람들이 이 릴리스에 기여하였으며 530개의 풀 리퀘스트가 병합되었습니다.

본 릴리즈에서 지원하는 Python 버전은 3.9-3.11입니다.

### 포용적인 문화 조성: 참여 요청

_2023년 5월 10일_ -- 포용적인 문화 조성: 참여 요청

다양성과 포용성의 측면에서 우리는 어떻게 더 나아질 수 있을까요? [여기](https://contributor-experience.org/docs/posts/dei-report/)에서 보고서를 읽고 함께 참여하는 방법을 알아보세요.

### NumPy 문서 팀 리더 변경

_2023년 1월 6일_ –- Mukulika Pahari, Ross Barnowski가 Melissa Mendonça를 대신해 새 NumPy 문서 팀 리더로 임명되었습니다. NumPy 공식 문서와 교육 자료에 기여한 Melissa와 한 걸음 더 나아간 Mukulika, Ross에게 감사를 표합니다.

### NumPy 1.24.0 출시

_2022년 12월 18일_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html)이 출시되었습니다. 주요 기능들은 다음과 같습니다:

* 스태킹 함수를 위한 새 "dtype" 및 "casting" 키워드.
* 새 F2PY 기능 및 수정.
* 수많은 지원 종료 예정 기능, 확인하세요.
* 수많은 만료된 기능,

NumPy 1.24.0 릴리스에서는 dtype의 처리 및 형변환을 개선하고 실행 속도를 높이는 작업, 문서를 보다 명료하게 다듬는 작업을 계속하고 있습니다. dtype의 형변환 및 정리를 변경하는 과정에서 수많은 기능들이 지원 종료 예정에 새로 포함되거나 완전히 만료되었습니다. 177명의 기여자가 생성한 444개의 풀 요청을 바탕으로 한 성과입니다. 지원하는 Python 버전은 3.8-3.11입니다.

### NumPy 1.23.0 출시

_2022년 6월 22일_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html)이 출시되었습니다. 주요 기능들은 다음과 같습니다:

* `loadtxt`를 C로 구현하여 성능이 크게 향상되었습니다.
* 데이터 교환을 쉽게 하기 위해 Python 수준에서 DLPack을 개방합니다.
* 구조화된 dtype의 형변환 및 비교 방법을 변경했습니다.
* f2py를 개선했습니다.

NumPy 1.23.0 릴리스에서는 dtype의 처리 및 형변환을 개선하고 실행 속도를 높이는 작업, 문서를 보다 명료하게 다듬는 작업, 오래된 지원 종료 예정 기능을 완전히 만료시키는 작업을 계속하고 있습니다. 151명의 기여자가 생성한 494개의 풀 요청을 바탕으로 한 성과입니다. 본 릴리즈에서 지원하는 Python 버전은 3.8-3.10입니다. Python 3.11은 rc 단계에 다다르면 지원할 예정입니다.

### NumFOCUS DEI 연구: 참여 요청

_2022년 4월 13일_ -- NumPy는 [NumFOCUS](http://numfocus.org/)와 협력하여 [Gordon & Betty Moore 재단](https://www.moore.org/)에서 기금을 제공하는 [연구 프로젝트](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c)를 진행합니다. 본 연구는 오픈 소스 소프트웨어 커뮤니티에 기여자, 특히 역사적으로 과소평가된 집단의 기여자가 참여할 때 직면하는 장벽을 이해하는 것을 목표로 합니다. 연구팀은 새 기여자, 프로젝트 개발자 및 유지관리자, 과거에 기여한 사람들과 NumPy에 참여하고 기여한 경험에 대해 이야기하고자 합니다.

**경험을 공유하고 싶으신가요?**

간단한 ["참여 희망" 양식](https://numfocus.typeform.com/to/WBWVJSqe)을 작성해주세요. 양식에서 연구 목표, 개인정보 보호, 기밀 유지 사항에 대한 추가 정보를 확인할 수 있습니다. 당신의 참여가 다양성과 포용성을 갖춘 오픈 소스 소프트웨어 커뮤니티의 성장과 지속 가능성에 도움이 될 것입니다. 승인된 참가자는 연구팀과 30분 면담을 진행하게 됩니다.

### Numpy 1.22.0 출시

_2021년 12월 31일_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)이 출시되었습니다. 주요 기능들은 다음과 같습니다:

* 기본 네임스페이스에 대해 유형 주석의 지원을 거의 완료했습니다. 업스트림 코드는 항상 변하므로 추가 개선이 있을 수 있지만 주요 작업은 완료되었습니다. 아마도 이 릴리스에서 가장 체감되는 개선 사항일 것입니다.
* 제안된 [배열 API 표준의 예비 버전](https://data-apis.org/array-api/latest/)이 제공됩니다([NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html) 참조). 이는 CuPy 및 JAX와 같은 라이브러리에서 사용할 수 있는 표준 함수 모음을 만드는 단계입니다.
* NumPy가 DLPack 백엔드로 구동됩니다. DLPack은 배열(텐서) 데이터에 대한 공통 교환 형식을 제공합니다.
* `quantile`, `percentile` 관련 함수를 위한 새 메서드를 추가했습니다. 새 메서드를 이용해 문헌에서 일반적으로 쓰이는 처리를 진행할 수 있습니다.
* 범용 함수가 대부분의 [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html)을 구현하도록 리팩터링되었습니다. 이를 통해 미래의 DType API를 실험할 수 있는 능력도 갖췄습니다.
* 새 구성 가능한 메모리 할당자를 다운스트림 프로젝트에서 사용할 수 있습니다.

NumPy 1.22.0은 153명의 기여자가 생성한 609개의 풀 요청을 바탕으로 만들어진 대형 릴리즈입니다. 본 릴리즈에서 지원하는 Python 버전은 3.8-3.10입니다.

### 과학 Python 생태계에서 포용적 문화 발전

_2021년 8월 31일_ -- Chan Zuckerberg Initiative가 과학적 Python 프로젝트에서 역사적으로 소외된 그룹의 사람들을 온보딩, 포함 및 유지하고 NumPy, SciPy, Matplotlib 그리고 Pandas 의 커뮤니티 역학을 구조적으로 개선하기 위한 [보조금을 수여](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)했음을 발표하게 되어 기쁩니다.

[CZI의 Essential Open Source Software for Science 프로그램](https://chanzuckerberg.com/eoss/)의 일환으로 이 [Diversity & 포함 추가 보조금](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)은 포괄적인 오픈 소스 커뮤니티를 육성하기 위한 관행을 식별, 문서화 및 구현하기 위한 전담 기여자 경험 리드 직책 생성을 지원합니다. 이 프로젝트는 Melissa Mendonça(NumPy) 님이 이끌고 Ralf Gommers(NumPy, SciPy), Hannah Aizenman, Thomas Caswell(Matplotlib), Matt Haberland(SciPy), Joris Van den Bossche(Pandas) 님이 추가 멘토링 및 지침을 제공합니다.

이것은 프로젝트의 커뮤니티 역학을 구조적으로 개선해야 하는 활동을 발견하고 구현하는 것을 목표로 하는 야심 찬 프로젝트입니다. 새로운 교차 프로젝트 역할을 설정함으로써 과학적 Python 커뮤니티에 새로운 협업 모델을 도입하여 생태계 내에서 커뮤니티 구축 작업을 보다 효율적으로 수행하고 더 큰 결과를 얻을 수 있을 것으로 기대됩니다. 또한 특히 역사적으로 과소대표된 집단의 새로운 기여자를 참여시키고 유지하기 위해, 프로젝트에서 효과적인 것과 그렇지 않은 것에 대한 명확한 그림을 구축할 것으로 기대합니다. 마지막으로, 시행된 조치에 대해 자세한 보고서를 작성하여 커뮤니티와의 대표 및 상호 작용 측면에서 프로젝트에 어떤 영향을 미쳤는지 설명할 계획입니다.

2개년 프로젝트가 2021년 11월부터 시작될 예정입니다. 프로젝트의 결과를 볼 날이 기대되네요! [여기에서 전체 제안서를 열람할 수 있습니다](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021년도 NumPy 설문조사

_2021년 7월 12일_ -- NumPy에서, 우리는 커뮤니티의 힘을 믿습니다. 작년에 75개국에서 1,236명의 NumPy 사용자가 첫 번째 설문조사에 참여했습니다. 설문 조사 결과를 통해 다음 12개월 동안 우리가 어떤 것에 집중해야 할지 아주 잘 이해할 수 있었습니다.

이제 또다른 설문 조사를 진행할 시간이고, 여러분의 도움이 다시 한 번 필요합니다. 완료하는 데 약 15분 정도 소요될 겁니다. 설문지는 영어 외에도 8개 국어로 제공됩니다: 벵골어, 프랑스어, 힌디어, 일본어, 중국 관화, 포르투갈어, 러시아어, 스페인어.

시작하려면 아래 링크를 눌러 주세요: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### Numpy 1.21.0 출시

_2021년 9월 23일_ -- [NumPy 1.1.21](https://numpy.org/doc/stable/release/1.21.0-notes.html)이 출시되었습니다. 주요 기능들은 다음과 같습니다:

- 더 많은 기능과 플랫폼을 다루는 지속적인 SIMD 작업,
- 새로운 dtype 인프라 및 캐스팅에 대한 초기 작업,
- Mac의 Python 3.8 및 Python 3.9용 universal2 휠,
- 문서화 향상,
- 주석 향상,
- 난수 생성에 이용되는 새 `PCG64DXSM` 비트 생성기.

이번 NumPy 릴리즈는 175명이 기여해주신 581개의 풀 리퀘스트가 합쳐진 결과입니다.  본 릴리즈에서 지원하는 Python 버전은 3.7-3.9입니다. Python 3.10은 Python 3.10 릴리즈 이후 지원할 예정입니다.


### 2020년도 NumPy 설문조사 결과

_2021년 6월 22일_ -- 2020년에, NumPy 조사 팀은 조사방법론 학사 과정의 학생 및 교수와 협력하여 미시간 대학과 매릴렌드 대학이 공동으로 개최한 첫 공식 NumPy 커뮤니티 조사를 실시했습니다. 여기서 조사 결과를 확인하세요: https://numpy.org/user-survey-2020/.


### Numpy 1.20.0 출시

_2021년 9월 30일_ -- [NumPy 1.1.20](https://numpy.org/doc/stable/release/1.20.0-notes.html)이 출시되었습니다. 역대 최대의 NumPy 릴리즈입니다. 180명이 넘는 기여자분들께 감사드립니다. 다음은 이번 출시에서 가장 흥미로운 두가지 기능들 입니다.
- NumPy의 많은 부분에 대한 유형 주석 및 사용자와 다운스트림 라이브러리가 추가할 때 사용할 수 있는 `ArrayLike` 및 `DtypeLike` 별칭을 포함하는 새로운 `numpy.typing` 하위 모듈 자체 코드에 주석을 입력합니다.
- x86(SSE, AVX), ARM64(Neon) 및 PowerPC(VSX) 명령을 지원하는 다중 플랫폼 SIMD 컴파일러 최적화 입니다. 이는 많은 함수들의 상당한 성능향상을 가져왔습니다 (예: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPy 프로젝트 내 다양성

_2020년 9월 20일_ -- 우리는 [NumPy 프로젝트 안에서의 다양성과 포용성에 관한 소셜 미디어의 상태 및 토론에 대한 성명서를 작성했습니다](/diversity_sep2020).


### Nature에 첫 공식 NumPy 논문 발표!

_2020년 9월 16일_ -- [NumPy에 대한 첫 번째 공식 논문](https://www.nature.com/articles/s41586-020-2649-2)이 Nature에 리뷰 기사로 게재되었음을 발표하게 되어 기쁩니다. NumPy 1.0이 나온 지 14년 만입니다. 이 백서에서는 배열 프로그래밍의 응용 프로그램 및 기본 개념, NumPy 위에 구축된 풍부한 과학적 Python 생태계, CuPy, Dask 및 JAX와 같은 외부 배열 및 텐서 라이브러리와의 상호 운용성을 촉진하기 위해 최근에 추가된 배열 프로토콜을 다룹니다.


### Python 3.9가 곧 출시하는데, NumPy는 바이너리 Wheel을 언제 출시합니까?

_2020년 9월 14일_ -- Python 3.9가 몇 주 내로 출시될 것입니다. 만약 Python 얼리어답터라면, NumPy (그리고 SciPy 등 다른 바이너리 패키지) 가 릴리즈 시일에 바이너리 Wheel을 준비하지 못한다는 것을 알고 실망했을 수 있습니다. 새로운 Python 버전에 빌드 환경을 맞추는 것은 많은 노력을 요하고, 패키지가 PyPI 및 conda-forge에 배포되는 데에는 일반적으로 몇 주가 걸립니다. 출시를 대비하려면 아래 요건을 충족하도록 하십시오.
- `pip` 버전을 최소 20.1로 업데이트하여 `manylinux2010` 및 `manylinux2014`를 지원하도록 합니다
- [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary)를 사용하거나 또는 `--only-binary=:all:`을 사용하여 `pip`가 소스에서 빌드하는 것을 막아주세요.


### NumPy 1.19.2 출시

_2020년 9월 10일_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html)이 출시되었습니다. 1.19 시리즈의 이 최신 릴리스는 몇 가지 버그를 수정하고 [다가오는 Cython 3.x 릴리스](http://docs.cython.org/en/latest/src/changes.html)를 준비하며 setuptools를 고정하여 업스트림 수정이 진행되는 동안 distutils가 계속 작동하도록 합니다. aarch64 휠은 다양한 Linux 배포판에서 사용되는 다양한 페이지 크기 문제를 해결하는 최신 manylinux2014 릴리스로 제작되었습니다.

### 최초의 NumPy 설문조사가 진행 중입니다!

_2020년 7월 2일_ -- 본 설문조사는 소프트웨어 및 커뮤니티로서의 NumPy 개발에 대하여, 의사결정의 우선 순위를 안내하고 설정하기 위해 실시됩니다. 설문지는 영어 외에도 8개 국어로 제공됩니다: 벵골어, 프랑스어, 힌디어, 일본어, 중국 관화, 포르투갈어, 러시아어, 스페인어.

NumPy를 개선하게 도와주시고 이를위해 설문조사에 참여해 주세요. [여기](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy에 새로운 로고가 생겼습니다!

_2020년 6월 24일_ -- NumPy에 새로운 로고가 생겼습니다.

<img src="/images/logos/numpy_logo.svg" alt="NumPy 로고" title="새 NumPy 로고" width=300>

이전 로고를 깔끔하고 현대적으로 다시 디자인했습니다. 새 로고를 만들어 주신 Isabela Presedo-Floyd님께 감사드립니다. 또 15년이 넘는 기간 동안 저희가 사용했던 로고를 만들어 주신 Travis Vaught님께도 감사의 말씀을 드립니다.


### NumPy 1.19.0 출시

_2020년 6월 20일_ -- NumPy 1.19.0이 출시되었습니다. Python 2의 지원을 중단한 첫 릴리즈라서 "정리 릴리즈"라고도 불립니다. 이제 지원하는 Python 최소 버전은 3.6입니다. 중요한 새 기능을 꼽자면, NumPy 1.17.0에 도입된 난수 생성 인프라를 Cython에서 접근할 수 있게 되었다는 것입니다.


### Season of Docs 승인

_2020년 5월 11일_ -- NumPy가 Google Season of Docs 프로그램의 선도 조직으로 승인되었습니다. 테크니컬 라이터와 협력해서 NumPy 문서를 다시 한 번 개선할 수 있는 기회를 갖게 되어 좋습니다! 이상 자세한 내용은 [공식 문서 시즌 사이트](https://developers.google.com/season-of-docs/) 및 [아이디어 페이지](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas) 를 참조하세요.


### NumPy 1.18.0 출시

_2019년 12월 22일_ -- NumPy 1.18.0이 출시되었습니다. 1.17.0에서의 주요 변경점을 통합하는 릴리즈입니다. 본 릴리즈는 Python 3.5를 지원하는 마지막 마이너 릴리즈입니다. 릴리즈의 주요 내용으로는, 64비트 BLAS 및 LAPACK 라이브러리와 연결하기 위한 환경 조성, `numpy.random`을 위한 새로운 C-API 등이 있습니다.

자세한 내용은 [출시 노트](https://github.com/numpy/numpy/releases/tag/v1.18.0)를 참조하세요.


### NumPy가 Chan Zuckerberg Initiative에서 보조금을 받았습니다

_2019년 11월 15일_ -- NumPy의 주요 종속 패키지 중 하나인 NumPy와 OpenBLAS가 챈 저커버그 이니셔티브의 [과학 프로그램용 중요 오픈소스 소프트웨어](https://chanzuckerberg.com/eoss/) 지원을 통해 19만 5천 달러에 달하는 공동 보조금을 받았다는 소식을 전할 수 있어 기쁩니다. 이곳에서는 과학에 중요한 오픈소스 도구에 대해 유지 관리, 성장, 개발 및 커뮤니티 참여를 지원합니다.

이 보조금은 NumPy 문서, 웹사이트 재설계 및 커뮤니티 개발을 개선하여 빠르게 성장하는 대규모 사용자 기반에 더 나은 서비스를 제공하고 프로젝트의 장기적인 지속 가능성을 보장하는 데 사용될 것입니다. OpenBLAS 팀은 OpenBLAS가 의존하는 ReLAPACK(Recursive LAPACK) 의 알고리즘 개선뿐만 아니라 특히 스레드 안전성, AVX-512 및 스레드 로컬 스토리지(TLS) 문제와 같은 일련의 핵심 기술 문제를 해결하는 데 집중할 것입니다.

제안된 계획 및 결과물에 대한 자세한 내용은 [전체 보조금 제안](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167)에서 확인할 수 있습니다. 2019년 12월 1일부터 작업을 시작하여 다음 12개월 동안 진행할 예정입니다.


<a name="releases"></a>

## 릴리즈

NumPy 릴리즈의 목록입니다. 릴리즈 노트로 링크도 걸려 있습니다. 버그 수정 릴리즈(`x.y.z`에서 `z`만 바뀐 경우)에는 새로운 기능이 없습니다. 마이너 릴리즈(`y`가 증가한 경우)에는 새로운 기능이 있습니다.

- NumPy 1.26.3 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _2024년 1월 2일_.
- NumPy 1.26.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _2 Jan 2024_.
- NumPy 1.126.2 ([릴리즈 노트](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _2023년 1월 2일_.
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
