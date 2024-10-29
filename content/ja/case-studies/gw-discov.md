---
title: "ケーススタディ: 重力波の発見"
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

重力波は、空間と時間の基本構造の波紋です。 2つのブラックホールの衝突や合体、2連星や超新星の合体など、大きな変動現象によって生成されます。 重力波の観測は、重力を研究する上で重要なだけでなく、遠い宇宙におけるいくつかの不明瞭な現象と、その影響を理解するためにも役立ちます。

The [Laser Interferometer Gravitational-Wave Observatory (LIGO)](https://www.ligo.caltech.edu)
was designed to open the field of gravitational-wave astrophysics through the
direct detection of gravitational waves predicted by Einstein’s General Theory
of Relativity. このシステムは、アメリカのワシントン州ハンフォードとルイジアナ州リビングストンにある2つの干渉計が一体となって構成され、重力波を検出します。 それぞれのシステムには、レーザー干渉法を用いた数キロ規模の重力波検出器が設置されています。  LIGO Scientific Collaboration（LSC）は、米国をはじめとする14カ国の大学から1000人以上の科学者が集まり、90以上の大学・研究機関によって支援されています。 また、約250人の学生も参加しています。 今回のLIGOの発見は、重力波が地球を通過する際に生じる空間と時間の微小な乱れの測定により、重力波そのものを初めて観測しました。  これにより、新しい天体物理学のフロンティアが開かれました。 これは、宇宙の歪んだ側面、つまり歪んだ時空から作られた物体とそれに現象を切り拓くものです。

### 主な目的

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

### 課題

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
  LIGOは毎日テラバイトのデータを生成しているのです！ Making sense of this data
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

## 重力波の検出におけるNumPyの役割

合成により放出される重力波は、スーパーコンピュータを用いたブルートフォースの数値相対性処理以外の手法では計算できません。
重力波は非常に小さい効果を生み、物質と微小な相互作用を持つため、検出が困難です。 LIGOのすべてのデータを処理・分析するには、膨大な計算インフラが必要です。 信号の数十億倍のノイズを除去した後も、非常に複雑な相対性理論の方程式と膨大な量のデータがあり、計算上の課題となっています。

Python用の標準的な数値解析パッケージNumPyは、LIGOの重力波検出プロジェクトで実行される様々なタスクに使用されるソフトウェアで利用されています。 NumPyは、複雑な数学処理や高速なデータ操作に役立ちました。  次にいくつかの例を示します。

- [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch
  detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf)
  (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
- Data retrieval: Deciding which data can be analyzed, figuring out whether it
  contains a signal - needle in a haystack
- Statistical analysis: estimate the statistical significance of observational
  data, estimating the signal parameters (e.g. masses of stars, spin velocity,
  and distance) by comparison with a model.
- データ可視化
  - 時系列データ
  - スペクトログラム
- 相関計算
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

## まとめ

一方で、これまで知られてきた深遠な天体物理学の現象に、多くに新たな洞察を提供しました。 数値処理とデータの可視化は、科学者が科学的な観測から収集したデータについての洞察を得て、その結果を理解するのに役立つ重要なステップです。 しかし、その計算は複雑であり、実際の観測データと分析を用いたコンピュータシミュレーションを用いて可視化されない限り、人間が理解することはできませんでした。  NumPy
along with other Python packages such as matplotlib, pandas, and scikit-learn
is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to
answer complex questions and discover new horizons in our understanding of the
universe.

{{< figure >}}
src = '/images/content_images/cs/numpy_gw_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
