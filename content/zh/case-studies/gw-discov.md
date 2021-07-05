---
title: "案例研究：发现引力波"
sidebar: false
---

{{< figsrc="/images/content_images/cs/gw_sxs_image. ng" class="fig-center" caption="**引力波**" alt="两个黑洞合并生成引力波纹" totel="*(图片来源：LIGO的极端时空模拟 (SXS) 项目)*" totlink="https://youtu. e/Zt8Z_uzG71o">}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>Python 科学生态系统是 LIGO 研究的关键基础设施。</p>
    <footer align="right">David Shoemaker, <cite>LIGO科学计算团队</cite></footer>
</blockquote>

## 关于 [引力波](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) and [LIGO](https://www.ligo.caltech.edu)

引力波是空间和时间结构中的涟漪。由宇宙中的灾难性事件产生，例如两个黑洞的碰撞和合并或双星或超新星的合并。 观测引力波不仅有助于研究引力，而且有助于了解遥远宇宙中一些不为人知的现象及其影响。

[激光干涉引力波天文台(LIGO)](https://www.ligo.caltech.edu)旨在通过直接探测爱因斯坦广义相对论预测的引力波来打开引力波天体物理学领域。 它由美国境内的两个相距甚远的干涉仪组成—一个位于华盛顿汉福德，另一个位于路易斯安那州利文斯顿—它们同时运行以探测引力波。 每一个仪器都装载使用了激光干涉测量法的公里级引力波探测器。  LIGO科学计算团队(LSC) 是由来自美国各地大学和其他 14 个国家的 1000 多名科学家组成的团体，得到了 90 多所大学和研究机构的支持；大约 250 名学生积极参与项目合作。 LIGO 的新发现是关于对引力波本身的首次观测，通过测量引力波在穿过地球时对空间和时间造成的微小扰动而制成。  它开辟了新的天体物理学研究方向，致力于探索宇宙扭曲的一面—研究由扭曲的时空构成的物体和现象。


### 关键目标

* 虽然它的 [任务](https://www.ligo.caltech.edu/page/what-is-ligo) 是探测宇宙中反应最剧烈和能量最集中的区域产生的引力波，但 LIGO 收集的数据可能会对物理学的许多领域产生深远的影响，包括引力、相对论、天体物理学、宇宙学、粒子物理学和核物理。
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
