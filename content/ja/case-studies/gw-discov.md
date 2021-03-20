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

[レーザー干渉計重力波天文台(LIGO)](https://www. ligo. caltech. edu)は、アインシュタインの一般相対性理論によって予測された重力波の直接検出を通して、重力波天体物理学の分野を切り開くように設計されました。 このシステムは、アメリカのワシントン州ハンフォードとルイジアナ州リビングストンにある2つの干渉計が一体となって構成され、重力波を検出します。 それぞれのシステムには、レーザー干渉法を用いた数キロ規模の重力波検出器が設置されています。  LIGO Scientific Collaboration（LSC）は、米国をはじめとする14カ国の大学から1000人以上の科学者が集まり、90以上の大学・研究機関によって支援されています。また、約250人の学生も参加しています。 今回のLIGOの重要な発見は、重力波が地球を通過する際に生じる空間と時間の微小な乱れを測定することで、重力波そのものを観測した初めての例であることです。  これにより、ゆがんだ時空から作られた 物体とそれに伴う現象を、宇宙の歪んだ側面から探索する、新しい天体物理学のフロンティア が開かれました。


### 主な目的

* LIGOの[ミッション](https://www.ligo.caltech.edu/page/what-is-ligo)は、宇宙で最も激しくエネルギーに満ちたプロセスからの重力波を検出することですが、LIGOが収集するデータは、重力、相対性理論、天体物理学、宇宙論、素粒子物理学、原子核物理学など、物理学の多くの分野に広く影響を与える可能性があります。
* 複雑な数学を含む相対性理論の数値計算によって観測データを解析し、信号とノイズを識別し、関連性のある信号をフィルタリングし、観測データの有意性を統計的に推定することで、宇宙の始まりのクランチを観測できるようになります。
* バイナリや数値の結果を理解しやすいのようにデータを可視化することも必要です。



### 課題

* **計算**

    重力波は非常に小さい効果を生み、物質と微小な相互作用を持つため、検出が困難です。 LIGOのすべてのデータを処理・分析するには、膨大な計算インフラが必要です。信号の数十億倍のノイズを除去した後も、非常に複雑な相対性理論の方程式と膨大な量のデータがあり、計算上の課題となっています。例えば6つのLIGO専用クラスターに分散されたバイナリ結合解析には[O(10^7)個のCPU時間](https:/youtu.be7mcHknWWzNI)が必要です。

* **データの氾濫**

    観測装置がより高感度で信頼性を持つようになると、データの大洪水によって、干し草の中から針を探すような問題が、多重に発生することがわかります。 LIGOは毎日テラバイトのデータを生成しているからです！ この大量のデータを解釈するには、各検出ごとに多大な労力が必要です。 例えば、LIGOによって収集される信号は、数十万個の重力波シグネチャのテンプレートで構成されており、スーパーコンピュータでしか解析できません。

* **可視化**

    アインシュタインの方程式を元にスーパーコンピュータでデータを解析できるようになったら、次はデータを人間の脳で理解できるようにしなければなりません。 シミュレーションのモデリングや信号の検出には、わかりやすい可視化技術が必要です。  画像処理やシミュレーションによって、解析結果をより多くの人に理解してもらえる状態になる前の段階において、可視化は、数値相対性を十分に重要視していなかった純粋な科学愛好家の目に、数値相対性が、より信頼性の高いものとして映るようにするという役割も果たしています。 実験データの処理や考察のために、複雑な計算をしたり、画像やシミュレーションの再レンダリングしたりすることは、この分野の研究者にとって時間のかかる作業となります。

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
