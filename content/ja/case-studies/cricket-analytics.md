---
title: "ケーススタディ: クリケット分析、ゲームチェンジャー!"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="{{< blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/" by="M S Dhoni、 _インディアンチームの元キャプテン、インターナショナル・クリケットプレイヤー、チェンナイ・スーパー・キングスのためにIPLでプレイ_""
  by="\*\* IPLT20、インド最大のクリケットフェスティバル\*\*"
>}}
{{< /blockquote >}}

## クリケットについて

インド人はクリケットが大好きだと言っても過言ではないでしょう。 この競技は、他のスポーツと異なり、インドの農村部や都市部を問わず、あらゆる場所でプレイされており、若者から年配の方まで広く人気があり、インドでは何十億人もの人々を結びつける役割を担っています。
クリケットは多くのメディアの注目を集めています。 There is a significant amount of
[money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and
fame at stake. 過去数年間、テクノロジーは文字通りクリケットの試合を変えてきました。 視聴者はストリーミングメディア、トーナメント、モバイルベースの手頃なアクセスによるライブクリケット視聴などを享受しています。

インドプレミアリーグ (IPL) は、2008年に設立された20チームから成るプロクリケットリーグです。 インドプレミアリーグ (IPL) は、2008年に設立された20チームから成るプロクリケットリーグです。 これは世界で最も参加者が多いクリケットイベントの1つで、2019年の市場規模は[67億ドル](https://en.wikipedia.org/wiki/Indian_Premier_League)だと評価されています。

クリケットは数のゲームです。 バッツマンによってスコアされたランの数、ボウラーによって取られたウィケットの数、クリケットチームによって獲得した試合の数、バッツマンがボウリング攻撃に特定の方法で応答する回数。 クリケットの数字を掘り下げてパフォーマンスを向上させるとともに、NumPyなどの数値計算ソフトウェアを利用した強力な分析ツールを介して、クリケットのビジネスチャンス、市場全体、経済性を研究することは、大きな意味を持ちます。 クリケット分析は、試合に関する興味深い洞察と、ゲームの結果に関する予測AIを提供します。

現在では、クリケットゲームの記録と 利用可能な統計データは豊富で、ほぼ無限の宝の山だと言えます。 : [ESPN cricinfo や](https://stats.espncricinfo.com/ci/engine/stats/index.html) [cricsheet](https://cricsheet.org). These and several such cricket databases
have been used for cricket
analysis
using the latest machine learning and predictive modelling algorithms.
メディアやプロスポーツ団体のエンターテインメントプラットフォームは、技術や分析を利用し、試合勝率を向上させるために、下記のような要素が主要なメトリックだと考え始めています。

- バッティング成績の移動平均
- スコア予測
- プレイヤーの体力や、異なる相手に対するパフォーマンスについての洞察
- チーム構成に戦略的な決定を下すための、各勝敗へのプレイヤーの貢献

{{< figure >}}
{{< /figure >}}

### データ分析の主要な目標

- スポーツデータ分析はクリケットだけでなく、チーム全体のパフォーマンスを向上させ、勝利率を最大限に高めるために、 [他のスポーツ](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)でも使用されています。
- リアルタイムデータ分析は、ゲーム中の洞察を得ることができ、チームや関連ビジネスが経済的利益と成長のために戦術を変更するためも役立ちます。
- 履歴分析に加えて、予測モデルは可能性のある結果を求めることができますが、かなりの数のナンバークランチングとデータサイエンスのノウハウ、可視化ツール、および分析に新しい観測データを含める機能などが必要になります。

{{< figure >}}
{{< /figure >}}

### 課題

- **データのクリーニングと前処理**

  IPL has expanded cricket beyond the classic test match format to a much
  larger scale. The number of matches played every season across various
  formats has increased and so has the data, the algorithms, newer sports data
  analysis technologies and simulation models. Cricket data analysis requires
  field mapping, player tracking, ball tracking, player shot analysis, and
  several other aspects involved in how the ball is delivered, its angle, spin,
  velocity, and trajectory. All these factors together have increased the
  complexity of data cleaning and preprocessing.

- **動的モデリング**

  In cricket, just like any other sport,
  there can be a large number of variables related to tracking various numbers
  of players on the field, their attributes, the ball, and several possibilities
  of potential actions. The complexity of data analytics and modeling is
  directly proportional to the kind of predictive questions that are put forth
  during analysis and are highly dependent on data representation and the
  model. Things get even more challenging in terms of computation, data
  comparisons when dynamic cricket play predictions are sought such as what
  would have happened if the batsman had hit the ball at a different angle or
  velocity.

- **予測分析の複雑さ**

  クリケットにおいて、意思決定の多くは「ボウラーがある特定のタイプの場合、打者はどのくらいの頻度で特定の種類のショットを打つのか」「バッツマンが特定の方法であるボウラーに反応した場合、ボウラーはどのようにラインと長さを変更するのか 」などの質問に基づいています。 この種の予測分析クエリでは、精度の良いデータセットが利用できることと、データを合成して高精度な生成モデルを作成できることが必要とされます。
  This kind of predictive analytics query requires highly granular dataset
  availability and the capability to synthesize data and create generative
  models that are highly accurate.

## クリケット解析におけるNumPyの役割

スポーツ分析は現在、非常に盛んな分野です。 スポーツ分析は現在、非常に盛んな分野です。 多くの研究者や企業は、最新の機械学習やAI技術以外にも、NumPyや、Scikit-learn, SciPy, Matplotlib, Jupyterなどの他のPyDataパッケージを[使っています](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)。  NumPyは以下のように、クリケット関連の様々なスポーツ分析に使用されています。  NumPyは以下のように、クリケット関連の様々なスポーツ分析に使用されています。

- **統計分析:** NumPyの数値計算機能は、様々なプレイヤーやゲーム戦術のコンテキストでの観測データで、試合中のイベントの統計的有意性を推定し、生成モデルや静的モデルと比較して試合結果を推定するのに役立ちます。 [因果分析](https://amplitude.com/blog/2017/01/19/causation-correlation) と [ビッグデータアプローチ](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)が戦術的分析に使用されています。
  [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation)
  and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)
  are used for tactical analysis.

- **Data Visualization:** Data graphing and visualization provide useful insights into relationship between various datasets.

## まとめ

スポーツアナリティクスは、プロの試合についてはまさにゲームチェンジャーです。 特に戦略的な意思決定については、最近まで主に「直感」や過去の伝統的な考え方に基づいて行われていたため、大きな影響があります。 NumPyは、データ分析・機械学習・人工知能のアルゴリズムに関連する高レベル関数を提供する沢山のPythonパッケージ群の、堅固な基盤となっています。
これらのパッケージは、ゲームの結果を変えるような意思決定を支援するリアルタイムのインサイトを得るため、クリケットの試合だけでなく関連する推論やビジネスの推進にも広く使用されています。 クリケットの試合結果につながる隠れたパラメータや、パターン、属性を見つけることは、ステークホルダーが数字や統計に隠されているゲームの洞察方法を見つけるのにも役に立つのです。

{{< figure >}}
{{< /figure >}}
