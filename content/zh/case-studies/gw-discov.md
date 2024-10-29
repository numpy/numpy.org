---
title: 案例研究：发现引力波
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

引力波是空间和时间结构中的涟漪。由宇宙中的灾难性事件产生，例如两个黑洞的碰撞和合并或双星或超新星的合并。 观测引力波不仅有助于研究引力，而且有助于了解遥远宇宙中一些不为人知的现象及其影响。

The [Laser Interferometer Gravitational-Wave Observatory (LIGO)](https://www.ligo.caltech.edu)
was designed to open the field of gravitational-wave astrophysics through the
direct detection of gravitational waves predicted by Einstein’s General Theory
of Relativity. It comprises two widely separated interferometers within the
United States — one in Hanford, Washington and the other in Livingston,
Louisiana — operated in unison to detect gravitational waves. 每一个仪器都装载使用了激光干涉测量法的公里级引力波探测器。  LIGO科学计算团队(LSC) 是由来自美国各地大学和其他 14 个国家的 1000 多名科学家组成的团体，得到了 90 多所大学和研究机构的支持；大约 250 名学生积极参与项目合作。 LIGO 的新发现是关于对引力波本身的首次观测，通过测量引力波在穿过地球时对空间和时间造成的微小扰动而制成。  它开辟了新的天体物理学研究方向，致力于探索宇宙扭曲的一面—研究由扭曲的时空构成的物体和现象。

### 关键目标

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

### 面临的挑战

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
  LIGO 每天生成数 TB 的数据！ Making sense of this data
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

## Numpy 在引力波检测中的作用

除了使用超级计算机暴力计算数值相对论之外，目前还无法使用任何其它技术计算黑洞合并发出的引力波。
LIGO 收集的数据量之大，就像无比微弱的引力波信号一样，令人难以置信。

NumPy 是 Python 的标准数值分析包，被用于 LIGO GW 检测项目期间执行的各种任务的软件所使用。 NumPy 有助于高性能处理复杂的数学问题和数据操作。  这里有一些例子：

- [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch
  detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf)
  (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
- Data retrieval: Deciding which data can be analyzed, figuring out whether it
  contains a signal - needle in a haystack
- Statistical analysis: estimate the statistical significance of observational
  data, estimating the signal parameters (e.g. masses of stars, spin velocity,
  and distance) by comparison with a model.
- 数据可视化
  - 时间序列
  - 频谱图
- 计算相关性
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

## 总结

GW 探测使研究人员能够发现完全出乎意料的现象，同时为许多已知的最深刻的天体物理现象提供了新的见解。 数学运算和数据可视化是帮助科学家深入了解从科学观察中收集到的数据并理解结果的关键步骤。 计算是复杂的，除非使用计算机模拟进行可视化，并提供真实的观察数据和分析，否则人类无法理解。  NumPy
along with other Python packages such as matplotlib, pandas, and scikit-learn
is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to
answer complex questions and discover new horizons in our understanding of the
universe.

{{< figure >}}
src = '/images/content_images/cs/numpy_gw_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
