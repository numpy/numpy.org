---
title: "사례 연구: 중력파의 발견"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/gw_sxs_image.png'
title = 'Gravitational Waves'
alt = 'binary coalesce black hole generating gravitational waves'
attribution = '(Image Credits: The Simulating eXtreme Spacetimes (SXS) Project at LIGO)'
attributionlink = 'https://youtu.be/Zt8Z_uzG71o'
{{< /figure >}}

{{< blockquote
cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
by="David Shoemaker, _LIGO Scientific Collaboration_" >}}
The scientific Python ecosystem is critical infrastructure for the research done at LIGO.
{{< /blockquote >}}

## About [Gravitational Waves](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) and [LIGO](https://www.ligo.caltech.edu)

중력파는 '시공간 천막'의 물결이라고 할 수 있으며, 두 블랙홀의 충돌이나 병합, 쌍성의 결합 혹은 초신성과 같이 우주가 대격변하는 사건으로부터 생성됩니다. 중력파를 관측하는 것은 비단 중력 연구에 도움을 줄 뿐만 아니라 먼 우주에서의 모호한 현상들과 이것이 미치는 영향에 대해서도 이해할 수 있게 해 줍니다.

The [Laser Interferometer Gravitational-Wave Observatory (LIGO)](https://www.ligo.caltech.edu)
was designed to open the field of gravitational-wave astrophysics through the
direct detection of gravitational waves predicted by Einstein’s General Theory
of Relativity. 그것은 중력파를 감지하기 위해 함께 작동하는 미국 내에서 두 개의 널리 분리된 간섭계로 구성됩니다. 하나는 워싱턴주 핸포드에 있고 다른 하나는 루이지애나주 리빙스턴에 있습니다. 그들 각각은 레이저 간섭계를 사용하는 수 킬로미터 규모의 중력파 탐지기를 가지고 있습니다.  LIGO Scientific Collaboration(LSC) 은 미국 전역과 90개 이상의 대학 및 연구 기관에서 지원하는 14개국의 대학에서 온 1000명 이상의 과학자 그룹입니다. 약 250명의 학생들이 협력에 적극적으로 기여하고 있습니다. LIGO의 새로운 발견은 중력파가 지구를 통과할 때 공간과 시간에 미치는 미세한 교란을 측정함으로써 중력파 자체를 처음으로 관찰한 것입니다.  그것은 우주의 뒤틀린 측면, 즉 뒤틀린 시공간에서 만들어진 물체와 현상을 탐구하는 새로운 천체물리학의 영역을 열었습니다.

### 주요 목표

- Though its [mission](https://www.ligo.caltech.edu/page/what-is-ligo) is to
  detect gravitational waves from some of the most violent and energetic
  processes in the Universe, the data LIGO collects may have far-reaching
  effects on many areas of physics including gravitation, relativity,
  astrophysics, cosmology, particle physics, and nuclear physics.
- Crunch observed data via numerical relativity computations that involves
  complex maths in order to discern signal from noise, filter out relevant
  signal and statistically estimate significance of observed data
- Data visualization so that the binary / numerical results can be
  comprehended.

### 과제

- **Computation**

  Gravitational Waves are hard to detect as they produce a very small effect
  and have tiny interaction with matter. Processing and analyzing all of
  LIGO's data requires a vast computing infrastructure.After taking care of
  noise, which is billions of times of the signal, there is still very
  complex relativity equations and huge amounts of data which present a
  computational challenge:
  [O(10^7) CPU hrs needed for binary merger analyses](https://youtu.be/7mcHknWWzNI)
  spread on 6 dedicated LIGO clusters

- **Data Deluge**

  As observational devices become more sensitive and reliable, the challenges
  posed by data deluge and finding a needle in a haystack rise multi-fold.
  LIGO는 매일 테라바이트의 데이터를 생성합니다! Making sense of this data
  requires an enormous effort for each and every detection. For example, the
  signals being collected by LIGO must be matched by supercomputers against
  hundreds of thousands of templates of possible gravitational-wave signatures.

- **Visualization**

  Once the obstacles related to understanding Einstein’s equations well
  enough to solve them using supercomputers are taken care of, the next big
  challenge was making data comprehensible to the human brain. Simulation
  modeling as well as  signal detection requires effective visualization
  techniques.  Visualization also plays a role in lending more credibility
  to numerical relativity in the eyes of pure science aficionados, who did
  not give enough importance to numerical relativity until imaging and
  simulations made it easier to comprehend results for a larger audience.
  Speed of complex computations and rendering, re-rendering images and
  simulations using latest experimental inputs and insights can be a time
  consuming activity that challenges researchers in this domain.

{{< figure >}}
src = '/images/content_images/cs/gw_strain_amplitude.png'
alt = 'gravitational waves strain amplitude'
title = 'Estimated gravitational-wave strain amplitude from GW150914'
attribution = '(Graph Credits: Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)'
attributionlink = 'https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger'
{{< /figure >}}

## 중력파 검출에서 NumPy의 역할

병합에서 방출되는 중력파는 슈퍼컴퓨터를 사용하는 무차별 대입 수치 상대성 이론을 제외하고는 어떤 기술로도 계산할 수 없습니다.
LIGO가 수집하는 데이터의 양은 중력파 신호가 작은 만큼 이해할 수 없을 정도로 많습니다.

Python용 표준 수치 분석 패키지인 NumPy는 LIGO의 GW 탐지 프로젝트 동안 수행되는 다양한 작업에 사용되는 소프트웨어에서 활용되었습니다. NumPy는 복잡한 수학 및 데이터 조작을 고속으로 해결하는 데 도움이 되었습니다.  몇 가지 예시를 들자면:

- [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch
  detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf)
  (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
- Data retrieval: Deciding which data can be analyzed, figuring out whether it
  contains a signal - needle in a haystack
- Statistical analysis: estimate the statistical significance of observational
  data, estimating the signal parameters (e.g. masses of stars, spin velocity,
  and distance) by comparison with a model.
- 데이터의 시각화
  - 시계열 데이터
  - 스펙트로그램
- 상관 분석 연산
- Key [Software](https://github.com/lscsoft) developed in GW data analysis
  such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and
  [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for
  providing object based interfaces to utilities, tools, and methods for
  studying data from gravitational-wave detectors.

{{< figure >}}
src = '/images/content_images/cs/gwpy-numpy-dep-graph.png'
alt = 'gwpy-numpy depgraph'
title = 'Dependency graph showing how GwPy package depends on NumPy'
{{< /figure >}}

----

{{< figure >}}
src = '/images/content_images/cs/PyCBC-numpy-dep-graph.png'
alt = 'PyCBC-numpy depgraph'
title = 'Dependency graph showing how PyCBC package depends on NumPy'
{{< /figure >}}

## 요약

중력파 검출을 통하여 연구자들은 완전히 예상치 못한 현상을 발견하게 됨으로써, 알려진 것 중 가장 난해한 천체물리학적 현상에 대하여 많은 사람들에게 새로운 통찰을 주었습니다. 숫자 계산 및 데이터 시각화는 과학자가 과학적 관찰에서 수집한 데이터에 대한 통찰력을 얻고 결과를 이해하는 데 도움이 되는 중요한 단계입니다. 계산은 복잡하며 실제 관찰 데이터 및 분석을 제공하는 컴퓨터 시뮬레이션을 사용하여 시각화하지 않는 한 사람이 이해할 수 없습니다.  NumPy
along with other Python packages such as matplotlib, pandas, and scikit-learn
is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to
answer complex questions and discover new horizons in our understanding of the
universe.

{{< figure >}}
src = '/images/content_images/cs/numpy_gw_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
