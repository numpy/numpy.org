---
title: "사례 연구: 중력파의 발견"
sidebar: false
---

{{< figure src="/images/content_images/cs/gw_sxs_image.png" class="fig-center" caption="**중력파**" alt="이항 결합하며 중력파를 생성하는 블랙홀" attr="*(사진 크레딧: LIGO의 Simulating eXtreme Spacetimes (SXS) 프로젝트)*" attrlink="https://youtu.be/Zt8Z_uzG71o" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>과학적 Python 생태계는 LIGO 연구에 있어서 중요한 인프라에 해당합니다.</p>
    <footer align="right">David Shoemaker, <cite>LIGO Scientific Collaboration</cite></footer>
</blockquote>

## [중력파](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) 그리고 [LIGO](https://www.ligo.caltech.edu)에 대해

중력파는 '시공간 천막'의 물결이라고 할 수 있으며, 두 블랙홀의 충돌이나 병합, 쌍성의 결합 혹은 초신성과 같이 우주가 대격변하는 사건으로부터 생성됩니다. 중력파를 관측하는 것은 비단 중력 연구에 도움을 줄 뿐만 아니라 먼 우주에서의 모호한 현상들과 이것이 미치는 영향에 대해서도 이해할 수 있게 해 줍니다.

[레이저 간섭계 중력파 관측소(LIGO)](https://www.ligo.caltech.edu) 아인슈타인의 일반상대성이론으로 예측한 중력파를 직접 탐지해 중력파 천체물리학의 장을 열기 위해 고안되었습니다. It comprises two widely separated interferometers within the United States — one in Hanford, Washington and the other in Livingston, Louisiana — operated in unison to detect gravitational waves. Each of them has multi-kilometer-scale gravitational wave detectors that use laser interferometry.  The LIGO Scientific Collaboration (LSC), is a group of more than 1000 scientists from universities around the United States and in 14 other countries supported by more than 90 universities and research institutes; approximately 250 students actively contributing to the collaboration. The new LIGO discovery is the first observation of gravitational waves themselves, made by measuring the tiny disturbances the waves make to space and time as they pass through the earth.  It has opened up new astrophysical frontiers that explore the warped side of the universe—objects and phenomena that are made from warped spacetime.


### 주요 목표

* [임무](https://www.ligo.caltech.edu/page/what-is-ligo)는 우주에서 가장 격렬하고 에너지가 넘치는 일부 과정에서 발생하는 중력파를 감지하는 것이지만, LIGO가 수집하는 데이터는 중력, 상대성 이론, 천체 물리학, 우주론, 입자 물리학 및 핵 물리학을 포함한 많은 물리학 영역에 광범위한 영향을 미칠 수 있습니다.
* 노이즈에서 신호를 식별하고, 관련 신호를 필터링하고, 관찰된 데이터의 유의성을 통계적으로 추정하기 위해 복잡한 수학을 포함하는 수치 상대성 계산을 통해 관측된 데이터를 고속 처리합니다.
* 이진/수치 상의 결과를 이해할 수 있도록 데이터 시각화를 진행합니다.



### 도전

* **계산**

    중력파는 매우 작은 효과를 생성하고 물질과의 상호 작용이 작기 때문에 감지하기 어렵습니다. LIGO의 모든 데이터를 처리하고 분석하려면 방대한 컴퓨팅 인프라가 필요합니다. 신호의 수십억 배에 해당하는 노이즈를 처리한 후에도 여전히 매우 복잡한 상대성 방정식과 엄청난 양의 데이터가 있어 계산상의 어려움이 있습니다. [바이너리 병합 분석에 필요한 O(10^7) CPU 시간](https://youtu.be/7mcHknWWzNI)은 6개의 전용 LIGO 클러스터에 퍼져 있습니다.

* **데이터 홍수**

    관찰 장치가 더 민감하고 신뢰할 수 있게 됨에 따라 데이터 폭증과 건초더미에서 바늘 찾기로 인해 제기되는 문제가 여러 배로 증가합니다. LIGO는 매일 테라바이트의 데이터를 생성합니다! 이 데이터를 이해하려면 탐지할 때마다 막대한 노력이 필요합니다. 예를 들어, LIGO가 수집하는 신호는 슈퍼컴퓨터에서 수십만 개의 가능한 중력파 서명 템플릿과 일치해야 합니다.

* **시각화**

    Once the obstacles related to understanding Einstein’s equations well enough to solve them using supercomputers are taken care of, the next big challenge was making data comprehensible to the human brain. Simulation modeling as well as  signal detection requires effective visualization techniques.  Visualization also plays a role in lending more credibility to numerical relativity in the eyes of pure science aficionados, who did not give enough importance to numerical relativity until imaging and simulations made it easier to comprehend results for a larger audience. Speed of complex computations and rendering, re-rendering images and simulations using latest experimental inputs and insights can be a time consuming activity that challenges researchers in this domain.

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="gravitational waves strain amplitude" caption="**Estimated gravitational-wave strain amplitude from GW150914**" attr="(**Graph Credits:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## 중력파 검출에서 NumPy의 역할

병합에서 방출되는 중력파는 슈퍼컴퓨터를 사용하는 무차별 대입 수치 상대성 이론을 제외하고는 어떤 기술로도 계산할 수 없습니다. LIGO가 수집하는 데이터의 양은 중력파 신호가 작은 만큼 이해할 수 없을 정도로 많습니다.

Python용 표준 수치 분석 패키지인 NumPy는 LIGO의 GW 탐지 프로젝트 동안 수행되는 다양한 작업에 사용되는 소프트웨어에서 활용되었습니다. NumPy는 복잡한 수학 및 데이터 조작을 고속으로 해결하는 데 도움이 되었습니다.  몇 가지 예시를 들자면:

* [신호 처리](https://www.uv.es/virgogroup/Denoising_ROF.html): 글리치 검출,  [잡음 식별 및 데이터 결정](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
* 데이터 수집: 어떤 데이터를 분석할 수 있을지 결정하고, 모래 속 바늘과 같이 미미한 신호가 있는지 파악
* 통계적 분석: 관측 데이터의 통계적 유의성 추정, 모델을 비교하여 신호 매개변수(예: 별의 질량, 회전 속도, 거리 등)를 추정
* 데이터의 시각화
  - 시계열 데이터
  - 스펙트로그램
* 상관 분석 연산
* [GwPy](https://gwpy.github.io/docs/stable/overview.html) 및 [PyCBC](https://pycbc.org)와 같은 중력파 데이터 분석에서 개발된 주요 [소프트웨어](https://github.com/lscsoft)는 후드 아래에서 NumPy 및 AstroPy를 사용하여 중력파 검출기에서 데이터를 연구하기 위한 유틸리티, 도구 및 방법에 객체 기반 인터페이스를 제공합니다.

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy 종속성" caption="**GwPy 패키지가 어떻게 NumPy에 종속하는지를 나타내는 종속성 그래프**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy 종속성" caption="**PyCBC 패키지가 어떻게 NumPy에 종속하는지를 나타내는 종속성 그래프**" >}}

## 요약

중력파 검출을 통하여 연구자들은 완전히 예상치 못한 현상을 발견하게 됨으로써, 알려진 것 중 가장 난해한 천체물리학적 현상에 대하여 많은 사람들에게 새로운 통찰을 주었습니다. 숫자 계산 및 데이터 시각화는 과학자가 과학적 관찰에서 수집한 데이터에 대한 통찰력을 얻고 결과를 이해하는 데 도움이 되는 중요한 단계입니다. 계산은 복잡하며 실제 관찰 데이터 및 분석을 제공하는 컴퓨터 시뮬레이션을 사용하여 시각화하지 않는 한 사람이 이해할 수 없습니다.  NumPy는 matplotlib, pandas 및 scikit-learn과 같은 다른 Python 패키지와 함께 [연구원](https://www.gw-openscience.org/events/GW150914/)이 복잡한 질문에 답하고 우주에 대한 이해의 새로운 지평을 발견할 수 있도록 합니다.

{{< figure src="/images/content_images/cs/numpy_gw_benefits.png" class="fig-center" alt="numpy를 통한 이익" caption="**활용된 주요 NumPy 기능**" >}}
