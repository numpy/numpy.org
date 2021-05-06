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

重力波は、空間と時間の基本構造の波紋です。 2つのブラックホールの衝突や合体、2連星や超新星の合体など、大きな変動現象によって生成されます。重力波の観測は、重力を研究する上で重要なだけでなく、遠い宇宙におけるいくつかの不明瞭な現象と、その影響を理解するためにも役立ちます。

[レーザー干渉計重力波天文台(LIGO)](https://www. ligo. caltech. edu)は、アインシュタインの一般相対性理論によって予測された重力波の直接検出を通して、重力波天体物理学の分野を切り開くために設計されました。このシステムは、アメリカのワシントン州ハンフォードとルイジアナ州リビングストンにある2つの干渉計が一体となって構成され、重力波を検出します。それぞれのシステムには、レーザー干渉法を用いた数キロ規模の重力波検出器が設置されています。LIGO Scientific Collaboration（LSC）は、米国をはじめとする14カ国の大学から1000人以上の科学者が集まり、90以上の大学・研究機関によって支援されています。また、約250人の学生も参加しています。今回のLIGOの発見は、重力波が地球を通過する際に生じる空間と時間の微小な乱れの測定により、重力波そのものを初めて観測しました。これにより、新しい天体物理学のフロンティアが開かれました。これは、宇宙の歪んだ側面、つまり歪んだ時空から作られた物体とそれに現象を切り拓くものです。


### 主な目的

* LIGOの[ミッション](https://www.ligo.caltech.edu/page/what-is-ligo)は、宇宙で最も激しくエネルギーに満ちたプロセスからの重力波を検出することですが、LIGOが収集するデータは、重力、相対性理論、天体物理学、宇宙論、素粒子物理学、原子核物理学など、物理学の多くの分野に広く影響を与える可能性があります。
* 複雑な数学を含む相対性理論の数値計算によって観測データを解析し、信号とノイズを識別し、関連性のある信号をフィルタリングし、観測データの有意性を統計的に推定することで、宇宙の始まりのクランチを観測できるようになります。
* バイナリや数値の結果を理解しやすいようにデータを可視化することも必要です。



### 課題

* **計算**

    重力波は非常に小さい効果を生み、物質と微小な相互作用を持つため、検出が困難です。 LIGOのすべてのデータを処理・分析するには、膨大な計算インフラが必要です。信号の数十億倍のノイズを除去した後も、非常に複雑な相対性理論の方程式と膨大な量のデータがあり、計算上の課題となっています。例えば6つのLIGO専用クラスターに分散されたバイナリ結合解析には[10の7乗オーダーのCPU時間](https:/youtu.be7mcHknWWzNI)が必要です。

* **データの氾濫**

    観測装置の感度と信頼性が高まると、様々な場所でデータの氾濫による困難が待ち受けています。それは、干し草の中から針を探すようなものです。LIGOは毎日テラバイトのデータを生成しているのです！この大量のデータを解釈するには、各検出ごとに多大な労力が必要です。例えば、LIGOによって収集される信号は、数十万個の重力波シグネチャのテンプレートで構成されており、スーパーコンピュータでしか解析できません。

* **可視化**

    アインシュタイン方程式を元にスーパーコンピュータでデータを解析できるようになったら、次はデータを人間の脳で理解できるようにしなければなりません。 シミュレーションのモデリングや信号の検出には、わかりやすい可視化技術が必要です。  画像処理やシミュレーションによって、解析結果をより多くの人に理解してもらえる状態になる前の段階において、可視化は、純粋な理論家に対し、数値相対性が、より信頼性の高いものとして映るようにするという役割も果たしています。理論家は、可視化とシミュレーションが結果の把握を容易にするまで、数値相対性を十分に重要視していませんでした。複雑な計算と描画を行い、また最新の実験結果と洞察に基づいてシミュレーションと再描画を行う作業は時間のかかるもので、この分野の研究者にとっての課題です。

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="gravitational waves strain amplitude" caption="**GW150914から推定される重力波の歪みの振幅**" attr="(**Graph Credits:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## 重力波の検出におけるNumPyの役割

合成により放出される重力波は、スーパーコンピュータを用いて数値相対性を手あたり次第に試すような方法では計算できません。LIGOが収集するデータ量は、重力波の信号が少ないのと同じくらい不可解です。

Python用の標準的な数値解析パッケージNumPyは、LIGOの重力波検出プロジェクトで実行される様々なタスクに使用されるソフトウェアで利用されています。NumPyは、複雑な数学処理や高速なデータ操作に役立ちました。次にいくつかの例を示します。

* [信号処理](https://www.uv.es/virgogroup/Denoising_ROF.html): グリッジ検出、[ノイズ同定とデータ判定](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)。
* データ取得: どのデータが解析できるかを決定し、干し草の中の針のような信号が入っているかどうかを突き止める。
* 統計解析: 観測データの統計的有意性を推定し、モデルとの比較により信号パラメータ（星の質量、スピン速度、距離など）を推定する。
* データ可視化
  - 時系列データ
  - スペクトログラム
* 相関計算
* 重力波データ解析のために開発された[ソフトウェア群](https://github.com/lscsoft): [GwPy](https://gwpy.github.io/docs/stable/overview.html)や [PyCBC](https://pycbc.org)は、NumPyやAstroPyを用いて、重力波検出器データを研究するためのユーティリティー・ツール・関数へのオブジェクト指向インターフェースを提供しています。

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy depgraph" caption="**GwPyのNumPy依存グラフ**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy depgraph" caption="**PyCBCのNumPy依存グラフ**" >}}

## まとめ

重力波の検出により、研究者はこれまでに予期しなかった現象を発見することができました。 一方で、これまで知られてきた深遠な天体物理学の現象に、多くに新たな洞察を提供しました。数値処理とデータの可視化は、科学者が科学的な観測から収集したデータについての洞察を得て、その結果を理解するのに役立つ重要なステップです。 しかし、その計算は複雑であり、実際の観測データと分析を用いたコンピュータシミュレーションを用いて可視化されない限り、人間が理解することはできませんでした。  NumPyは、matplotlib・pandas・scikit-learnなどのPythonパッケージとともに、研究者が複雑な質問に答え、私たちの宇宙に対するの理解において、新しい地平を発見することを[可能にしています](https://www.gw-openscience.org/events/GW150914/)。

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**利用されたNumPyの主要機能**" >}}
