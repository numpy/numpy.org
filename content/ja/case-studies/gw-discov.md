---
title: "ケーススタディ: 重力波の発見"
sidebar: false
---

{{< figure src="/images/content_images/cs/gw_sxs_image.png" class="fig-center" caption="**重力波**" alt="binary coalesce black hole generating gravitational waves" attr="*(Image Credits: The Simulating eXtreme Spacetimes (SXS) Project at LIGO)*" attrlink="https://youtu.be/Zt8Z_uzG71o" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>科学計算のためのPythonエコシステムはLIGOで行われている研究のための重要なインフラです。</p>
    <footer align="right">David Shoemaker, <cite>LIGOサイエンティフィック・コラボレーション</cite></footer>
</blockquote>

## [重力波](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) と [LIGO](https://www.ligo.caltech.edu) について

重力波は、空間と時間の基本構造の波紋です。 2つのブラックホールの衝突や合体、2連星や超新星の合体など、大きな変動現象によって生成されます。 重力波を観測することは、重力を研究する上で 重要なだけでなく、遠い宇宙とその影響におけるいくつかの不明瞭な現象の理解するためにも役立ちます。

[レーザー干渉計重力波天文台(LIGO)](https://www. ligo. caltech. edu)は、アインシュタインの一般相対性理論によって予測された重力波の直接検出を通して、重力波天体物理学の分野を切り開くように設計されました。 このシステムは、アメリカのワシントン州ハンフォードとルイジアナ州リビングストンにある2つの干渉計が一体となって構成され、重力波を検出します。 それぞれのシステムには、レーザー干渉法を用いた数キロ規模の重力波検出器が設置されています。  LIGO Scientific Collaboration（LSC）は、米国をはじめとする14カ国の大学から1000人以上の科学者が集まり、90以上の大学・研究機関によって支援されています。また、約250人の学生も参加しています。 今回のLIGOの重要な発見は、重力波が地球を通過する際に生じる空間と時間の微小な乱れを測定することで、重力波そのものを観測した初めての例であることです。  それは、ゆがんだ時空から作られた 物体と現象を宇宙の歪んだ側面を探索する、新しい天体物理学フロンティア を開きました。


### Key Objectives

* Though its [mission](https://www.ligo.caltech.edu/page/what-is-ligo) is to detect gravitational waves from some of the most violent and energetic processes in the Universe, the data LIGO collects may have far-reaching effects on many areas of physics including gravitation, relativity, astrophysics, cosmology, particle physics, and nuclear physics.
* Crunch observed data via numerical relativity computations that involves complex maths in order to discern signal from noise, filter out relevant signal and statistically estimate significance of observed data
* Data visualization so that the binary / numerical results can be comprehended.



### The Challenges

* **Computation**

    Gravitational Waves are hard to detect as they produce a very small effect and have tiny interaction with matter. Processing and analyzing all of LIGO's data requires a vast computing infrastructure.After taking care of noise, which is billions of times of the signal, there is still very complex relativity equations and huge amounts of data which present a computational challenge: [O(10^7) CPU hrs needed for binary merger analyses](https://youtu.be/7mcHknWWzNI) spread on 6 dedicated LIGO clusters

* **Data Deluge**

    As observational devices become more sensitive and reliable, the challenges posed by data deluge and finding a needle in a haystack rise multi-fold. LIGO generates terabytes of data every day! Making sense of this data requires an enormous effort for each and every detection. For example, the signals being collected by LIGO must be matched by supercomputers against hundreds of thousands of templates of possible gravitational-wave signatures.

* **Visualization**

    Once the obstacles related to understanding Einstein’s equations well enough to solve them using supercomputers are taken care of, the next big challenge was making data comprehensible to the human brain. Simulation modeling as well as  signal detection requires effective visualization techniques.  Visualization also plays a role in lending more credibility to numerical relativity in the eyes of pure science aficionados, who did not give enough importance to numerical relativity until imaging and simulations made it easier to comprehend results for a larger audience. Speed of complex computations and rendering, re-rendering images and simulations using latest experimental inputs and insights can be a time consuming activity that challenges researchers in this domain.

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="gravitational waves strain amplitude" caption="**Estimated gravitational-wave strain amplitude from GW150914**" attr="(**Graph Credits:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## NumPy’s Role in the Detection of Gravitational Waves

Gravitational waves emitted from the merger cannot be computed using any technique except brute force numerical relativity using supercomputers. The amount of data LIGO collects is as incomprehensibly large as gravitational wave signals are small.

NumPy, the standard numerical analysis package for Python,  was utilized by the software used for various tasks performed during the GW detection project at LIGO. NumPy helped in solving complex maths and data manipulation at high speed.  Here are some examples:

* [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
* Data retrieval: Deciding which data can be analyzed, figuring out whether it contains a signal - needle in a haystack
* Statistical analysis: estimate the statistical significance of observational data, estimating the signal parameters (e.g. masses of stars, spin velocity, and distance) by comparison with a model.
* Visualization of data
  - Time series
  - Spectrograms
* Compute Correlations
* Key [Software](https://github.com/lscsoft) developed in GW data analysis such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for providing object based interfaces to utilities, tools, and methods for studying data from gravitational-wave detectors.

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy depgraph" caption="**Dependency graph showing how GwPy package depends on NumPy**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy depgraph" caption="**Dependency graph showing how PyCBC package depends on NumPy**" >}}

## Summary

GW detection has enabled researchers to discover entirely unexpected phenomena while providing new insight into many of the most profound astrophysical phenomena known. Number crunching and data visualization is a crucial step that helps scientists gain insights into data gathered from the scientific observations and understand the results. The computations are complex and cannot be comprehended by humans unless it is visualized using computer simulations that are fed with the real observed data and analysis.  NumPy along with other Python packages such as matplotlib, pandas, and scikit-learn is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to answer complex questions and discover new horizons in our understanding of the universe.

{{< figure src="/images/content_images/cs/numpy_gw_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}
