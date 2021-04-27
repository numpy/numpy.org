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

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="gravitational waves strain amplitude" caption="**GW150914から推定される重力波の歪みの振幅**" attr="(**Graph Credits:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## 重力波の検出におけるNumPyの役割

合成により放出される重力波は、スーパーコンピュータを用いたブルートフォースの数値相対性処理以外の手法では計算できません。 LIGOが収集するデータ量は、重力波の信号が少ないのと同じくらい不可解です。

Python用の標準的な数値解析パッケージNumPyは、LIGOの重力波検出プロジェクトで実行される様々なタスクに使用されるソフトウェアで利用されています。 NumPyは、複雑な数学と高速なデータ操作に役立ちました。  次にいくつかの例を示します。

* [信号処理](https://www.uv.es/virgogroup/Denoising_ROF.html): グリッジ検出,  [ノイズ同定とデータ判定](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
* データ取得: どのデータが解析できるかを決定し、干し草の中の針のような信号が入っているかどうかを突き止める。
* 統計解析：観測データの統計的有意性を推定し、モデルとの比較により信号パラメータ（星の質量、スピン速度、距離など）を推定する。
* データの可視化
  - 時系列データ
  - スペクトログラム
* 相関計算
* 重力波データ解析のために開発された [ソフトウェア](https://github.com/lscsoft)である[GwPy](https://gwpy.github.io/docs/stable/overview.html)や [PyCBC](https://pycbc.org)はNumPy やAstroPyを重力波検出器からのデータを研究するためのユーティリティー、ツール、およびメソッドへのオブジェクトベースのインターフェースを提供するために利用しています。

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy depgraph" caption="**GwPyのNumPy依存グラフ**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy depgraph" caption="**PyCBCのNumPy依存グラフ**" >}}

## まとめ

重力波の検出により、研究者はこれまでに予期しなかった現象を発見することができました。 一方で、これまで知られてきた深遠な天体物理学の現象に、多くに新たな洞察を提供しました。 データ解釈とデータの可視化は、科学者が科学的な観測から収集したデータについての洞察を得て、その結果を理解するのに役立つ重要なステップです。 しかし、その計算は複雑であり、実際の観測データと分析を用いたコンピュータシミュレーションを用いて可視化されない限り、人間が理解することはできませんでした。  NumPy、matplotlib、pandasなどの、Pythonパッケージとともに、 scikit-learningは 、研究者 [が](https://www.gw-openscience.org/events/GW150914/) 複雑な質問に答え、 私たちの宇宙についての理解において、新しい地平を発見することを可能にしてきたのです。

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**利用されたNumPyの主要機能**" >}}
