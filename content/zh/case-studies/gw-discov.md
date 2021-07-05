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
* 通过涉及复杂数学的数值相对论来计算和处理观测数据，以便从噪声中辨别信号、滤除相关信号并统计估计观测数据的重要性。
* 数据可视化，以便可以理解二进制/数值结果。



### 面临的挑战

* **计算**

    引力波很难被探测到，因为它们产生的影响非常小，与物质的相互作用也很小。 处理和分析 LIGO 的所有数据需要庞大的计算基础设施。在处理数十亿倍于引力波信号的噪声后，仍然需要使用非常复杂的相对论方程来处理海量数据，这带来了计算挑战： [二进制合并分析需要花费O(10^ 7) 级别的 CPU 小时数](https://youtu.be/7mcHknWWzNI)才能完成，这些计算过程由 6 个专用 LIGO 集群分摊解决。

* **数据泛滥**

    随着观测设备变得更加敏感和可靠，数据泛滥和大海捞针所带来的挑战成倍增加。 LIGO 每天生成数 TB 的数据！ 每一次检测之后要理解这些数据都要付出巨大的努力。 例如，LIGO 收集的信号必须由超级计算机与数十万个可能的引力波特征模板进行匹配。

* **可视化**

    一旦解决了理解爱因斯坦方程以及使用超级计算机求解这些方程相关的障碍，下一个重大挑战就是使人脑能够理解数据。 仿真建模以及信号检测需要有效的可视化技术。  在纯科学爱好者的眼中，可视化在为数值相对论提供更多可信度方面也发挥了作用，在成像和模拟使更多人更容易理解结果之前，他们并没有对数值相对论给予足够的重视。 Speed of complex computations and rendering, re-rendering images and simulations using latest experimental inputs and insights can be a time consuming activity that challenges researchers in this domain.

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
