---
title: "ケーススタディ: 重力波の発見"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/gw_sxs_image.png'
title = '重力波'
alt = 'binary coalesce black hole generating gravitational waves'
attribution = '(Image Credits: The Simulating eXtreme Spacetimes (SXS) Project at LIGO)'
attributionlink = 'https://youtu.be/Zt8Z_uzG71o'
{{< /figure >}}

{{< blockquote
cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
by="David Shoemaker, _LIGOサイエンティフィック・コラボレーション_" >}}
科学計算のためのPythonエコシステムはLIGOで行われている研究のための重要なインフラです。
{{< /blockquote >}}
{{< /blockquote >}}

## [重力波](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) と [LIGO](https://www.ligo.caltech.edu) について

重力波は、空間と時間の基本構造の波紋です。 2つのブラックホールの衝突や合体、2連星や超新星の合体など、大きな変動現象によって生成されます。 重力波の観測は、重力を研究する上で重要なだけでなく、遠い宇宙におけるいくつかの不明瞭な現象と、その影響を理解するためにも役立ちます。 Observing GW can not only help
in studying gravity but also in understanding some of the obscure phenomena in
the distant universe and its impact.

\[レーザー干渉計重力波天文台(LIGO)\](https://www. It comprises two widely separated interferometers within the
United States — one in Hanford, Washington and the other in Livingston,
Louisiana — operated in unison to detect gravitational waves. Each of them has
multi-kilometer-scale gravitational wave detectors that use laser
interferometry.  The LIGO Scientific Collaboration (LSC), is a group of more
than 1000 scientists from universities around the United States and in 14
other countries supported by more than 90 universities and research institutes;
approximately 250 students actively contributing to the collaboration. The new
LIGO discovery is the first observation of gravitational waves themselves,
made by measuring the tiny disturbances the waves make to space and time as
they pass through the earth.  It has opened up new astrophysical frontiers
that explore the warped side of the universe—objects and phenomena that are
made from warped spacetime.

### 主な目的

- LIGOの[ミッション](https://www.ligo.caltech.edu/page/what-is-ligo)は、宇宙で最も激しくエネルギーに満ちたプロセスからの重力波を検出することですが、LIGOが収集するデータは、重力、相対性理論、天体物理学、宇宙論、素粒子物理学、原子核物理学など、物理学の多くの分野に広く影響を与える可能性があります。
- Crunch observed data via numerical relativity computations that involves
  complex maths in order to discern signal from noise, filter out relevant
  signal and statistically estimate significance of observed data
- バイナリや数値の結果を理解しやすいようにデータを可視化することも必要です。

### 課題

- **計算**

  Gravitational Waves are hard to detect as they produce a very small effect
  and have tiny interaction with matter. Processing and analyzing all of
  LIGO's data requires a vast computing infrastructure.After taking care of
  noise, which is billions of times of the signal, there is still very
  complex relativity equations and huge amounts of data which present a
  computational challenge:
  [O(10^7) CPU hrs needed for binary merger analyses](https://youtu.be/7mcHknWWzNI)
  spread on 6 dedicated LIGO clusters

- **データの氾濫**

  As observational devices become more sensitive and reliable, the challenges
  posed by data deluge and finding a needle in a haystack rise multi-fold.
  LIGO generates terabytes of data every day! Making sense of this data
  requires an enormous effort for each and every detection. For example, the
  signals being collected by LIGO must be matched by supercomputers against
  hundreds of thousands of templates of possible gravitational-wave signatures.

- **可視化**

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
title = 'GW150914から推定される重力波の歪みの振幅'
attribution = '(Graph Credits: Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)'
attributionlink = 'https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger'
{{< /figure >}}

## 重力波の検出におけるNumPyの役割

合成により放出される重力波は、スーパーコンピュータを用いたブルートフォースの数値相対性処理以外の手法では計算できません。 重力波は非常に小さい効果を生み、物質と微小な相互作用を持つため、検出が困難です。 LIGOのすべてのデータを処理・分析するには、膨大な計算インフラが必要です。 信号の数十億倍のノイズを除去した後も、非常に複雑な相対性理論の方程式と膨大な量のデータがあり、計算上の課題となっています。
合成により放出される重力波は、スーパーコンピュータを用いて数値相対性を手あたり次第に試すような方法では計算できません。 LIGOが収集するデータ量は、重力波の信号が少ないのと同じくらい不可解です。

Python用の標準的な数値解析パッケージNumPyは、LIGOの重力波検出プロジェクトで実行される様々なタスクに使用されるソフトウェアで利用されています。 NumPyは、複雑な数学処理や高速なデータ操作に役立ちました。  次にいくつかの例を示します。 NumPy helped in solving complex maths and data manipulation at high
speed.  Here are some examples:

- [信号処理](https://www.uv.es/virgogroup/Denoising_ROF.html): グリッジ検出、[ノイズ同定とデータ判定](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)。
- データ取得: どのデータが解析できるかを決定し、干し草の中の針のような信号が入っているかどうかを突き止める。
- 統計解析: 観測データの統計的有意性を推定し、モデルとの比較により信号パラメータ（星の質量、スピン速度、距離など）を推定する。
- データ可視化
  - 時系列データ
  - スペクトログラム
- 相関計算
- 重力波データ解析のために開発された[ソフトウェア群](https://github.com/lscsoft): [GwPy](https://gwpy.github.io/docs/stable/overview.html)や [PyCBC](https://pycbc.org)は、NumPyやAstroPyを用いて、重力波検出器データを研究するためのユーティリティー・ツール・関数へのオブジェクト指向インターフェースを提供しています。

{{< figure >}}
src = '/images/content_images/cs/gwpy-numpy-dep-graph.png'
alt = 'gwpy-numpy depgraph'
title = 'GwPyのNumPy依存グラフ'
{{< /figure >}}

----

{{< figure >}}
src = '/images/content_images/cs/PyCBC-numpy-dep-graph.png'
alt = 'PyCBC-numpy depgraph'
title = 'PyCBCのNumPy依存グラフ'
{{< /figure >}}

## まとめ

GW detection has enabled researchers to discover entirely unexpected phenomena
while providing new insight into many of the most profound astrophysical
phenomena known. Number crunching and data visualization is a crucial step
that helps scientists gain insights into data gathered from the scientific
observations and understand the results. The computations are complex and
cannot be comprehended by humans unless it is visualized using computer
simulations that are fed with the real observed data and analysis.  NumPy
along with other Python packages such as matplotlib, pandas, and scikit-learn
is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to
answer complex questions and discover new horizons in our understanding of the
universe.

{{< figure >}}
src = '/images/content_images/cs/numpy_bh_benefits.png'
alt = 'numpy benefits'
title = '利用されたNumPyの主要機能'
{{< /figure >}}
