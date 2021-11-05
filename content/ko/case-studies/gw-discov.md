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

The [Laser Interferometer Gravitational-Wave Observatory (LIGO)](https://www.ligo.caltech.edu) was designed to open the field of gravitational-wave astrophysics through the direct detection of gravitational waves predicted by Einstein’s General Theory of Relativity. It comprises two widely-separated interferometers within the United States — one in Hanford, Washington and the other in Livingston, Louisiana — operated in unison to detect gravitational waves. Each of them has multi-kilometer-scale gravitational wave detectors that use laser interferometry.  The LIGO Scientific Collaboration (LSC), is a group of more than 1000 scientists from universities around the United States and in 14 other countries supported by more than 90 universities and research institutes; approximately 250 students actively contributing to the collaboration. The new LIGO discovery is the first observation of gravitational waves themselves, made by measuring the tiny disturbances the waves make to space and time as they pass through the earth.  It has opened up new astrophysical frontiers that explore the warped side of the universe—objects and phenomena that are made from warped spacetime.


### 주요 목표

* Though its [mission](https://www.ligo.caltech.edu/page/what-is-ligo) is to detect gravitational waves from some of the most violent and energetic processes in the Universe, the data LIGO collects may have far-reaching effects on many areas of physics including gravitation, relativity, astrophysics, cosmology, particle physics, and nuclear physics.
* Crunch observed data via numerical relativity computations that involves complex maths in order to discern signal from noise, filter out relevant signal and statistically estimate significance of observed data
* Data visualization so that the binary / numerical results can be comprehended.



### 과제

* **계산**

    Gravitational Waves are hard to detect as they produce a very small effect and have tiny interaction with matter. Processing and analyzing all of LIGO's data requires a vast computing infrastructure.After taking care of noise, which is billions of times of the signal, there is still very complex relativity equations and huge amounts of data which present a computational challenge: [O(10^7) CPU hrs needed for binary merger analyses](https://youtu.be/7mcHknWWzNI) spread on 6 dedicated LIGO clusters

* **데이터 범람**

    As observational devices become more sensitive and reliable, the challenges posed by data deluge and finding a needle in a haystack rise multi-fold. LIGO generates terabytes of data every day! Making sense of this data requires an enormous effort for each and every detection. For example, the signals being collected by LIGO must be matched by supercomputers against hundreds of thousands of templates of possible gravitational-wave signatures.

* **시각화**

    Once the obstacles related to understanding Einstein’s equations well enough to solve them using supercomputers are taken care of, the next big challenge was making data comprehensible to the human brain. Simulation modeling as well as  signal detection requires effective visualization techniques.  Visualization also plays a role in lending more credibility to numerical relativity in the eyes of pure science aficionados, who did not give enough importance to numerical relativity until imaging and simulations made it easier to comprehend results for a larger audience. Speed of complex computations and rendering, re-rendering images and simulations using latest experimental inputs and insights can be a time consuming activity that challenges researchers in this domain.

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="중력파 변형 진폭" caption="**GW150914에서 추정된 중력파 변형 진폭**" attr="(**그래프 출처:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## 중력파 검출에서 NumPy의 역할

Gravitational waves emitted from the merger cannot be computed using any technique except brute force numerical relativity using supercomputers. The amount of data LIGO collects is as incomprehensibly large as gravitational wave signals are small.

NumPy, the standard numerical analysis package for Python,  was utilized by the software used for various tasks performed during the GW detection project at LIGO. NumPy helped in solving complex maths and data manipulation at high speed.  Here are some examples:

* [신호 처리](https://www.uv.es/virgogroup/Denoising_ROF.html): 글리치 검출,  [잡음 식별 및 데이터 결정](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
* 데이터 수집: 어떤 데이터를 분석할 수 있을지 결정하고, 모래 속 바늘과 같이 미미한 신호가 있는지 파악
* 통계적 분석: 관측 데이터의 통계적 유의성 추정, 모델을 비교하여 신호 매개변수(예: 별의 질량, 회전 속도, 거리 등)를 추정
* 데이터의 시각화
  - 시계열 데이터
  - 스펙트로그램
* 상관 분석 연산
* Key [Software](https://github.com/lscsoft) developed in GW data analysis such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for providing object based interfaces to utilities, tools, and methods for studying data from gravitational-wave detectors.

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy 종속성" caption="**GwPy 패키지가 어떻게 NumPy에 종속하는지를 나타내는 종속성 그래프**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy 종속성" caption="**PyCBC 패키지가 어떻게 NumPy에 종속하는지를 나타내는 종속성 그래프**" >}}

## 요약

중력파 검출을 통하여 연구자들은 완전히 예상치 못한 현상을 발견하게 됨으로써, 알려진 것 중 가장 난해한 천체물리학적 현상에 대하여 많은 사람들에게 새로운 통찰을 주었습니다. Number crunching and data visualization is a crucial step that helps scientists gain insights into data gathered from the scientific observations and understand the results. The computations are complex and cannot be comprehended by humans unless it is visualized using computer simulations that are fed with the real observed data and analysis.  NumPy along with other Python packages such as matplotlib, pandas, and scikit-learn is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to answer complex questions and discover new horizons in our understanding of the universe.

{{< figure src="/images/content_images/cs/numpy_gw_benefits.png" class="fig-center" alt="numpy를 통한 이익" caption="**활용된 주요 NumPy 기능**" >}}
