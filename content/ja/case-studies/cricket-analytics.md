---
title: "ケーススタディ: クリケット分析、ゲームチェンジャー!"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/ipl-stadium.png'
title = 'IPLT20, the biggest Cricket Festival in India'
alt = 'Indian Premier League Cricket cup and stadium'
attribution = '(Image credits: IPLT20 (cup and logo) & Akash Yadav (stadium))'
attributionlink = 'https://unsplash.com/@aksh1802'
{{< /figure >}}

{{< blockquote
cite="https://www.scoopwhoop.com/sports/ms-dhoni/"
by="M S Dhoni, _International Cricket Player, ex-captain, Indian Team, plays for Chennai Super Kings in IPL_"

> }}
> You don't play for the crowd, you play for the country.
> {{< /blockquote >}}

## クリケットについて

インド人はクリケットが大好きだと言っても過言ではないでしょう。 この競技は、他のスポーツと異なり、インドの農村部や都市部を問わず、あらゆる場所でプレイされており、若者から年配の方まで広く人気があり、インドでは何十億人もの人々を結びつける役割を担っています。
クリケットは多くのメディアの注目を集めています。 There is a significant amount of
[money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and
fame at stake. 過去数年間、テクノロジーは文字通りクリケットの試合を変えてきました。 視聴者はストリーミングメディア、トーナメント、モバイルベースの手頃なアクセスによるライブクリケット視聴などを享受しています。

インドプレミアリーグ (IPL) は、2008年に設立された20チームから成るプロクリケットリーグです。 It is one of the most attended cricketing events in
the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League)
in 2019.

クリケットは数のゲームです。 バッツマンによってスコアされたランの数、ボウラーによって取られたウィケットの数、クリケットチームによって獲得した試合の数、バッツマンがボウリング攻撃に特定の方法で応答する回数。 クリケットの数字を掘り下げてパフォーマンスを向上させるとともに、NumPyなどの数値計算ソフトウェアを利用した強力な分析ツールを介して、クリケットのビジネスチャンス、市場全体、経済性を研究することは、大きな意味を持ちます。 クリケット分析は、試合に関する興味深い洞察と、ゲームの結果に関する予測AIを提供します。

Today, there are rich and almost infinite troves of cricket game records and
statistics available, e.g., ESPN
cricinfo and
[cricsheet](https://cricsheet.org). These and several such cricket databases
have been used for cricket
analysis
using the latest machine learning and predictive modelling algorithms.
メディアやプロスポーツ団体のエンターテインメントプラットフォームは、技術や分析を利用し、試合勝率を向上させるために、下記のような要素が主要なメトリックだと考え始めています。

- バッティング成績の移動平均
- スコア予測
- プレイヤーの体力や、異なる相手に対するパフォーマンスについての洞察
- チーム構成に戦略的な決定を下すための、各勝敗へのプレイヤーの貢献

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png'
title = 'Cricket Pitch, the focal point in the field'
alt = 'A cricket pitch with bowler and batsmen'
align = 'center'
attribution = '(Image credit: Debarghya Das)'
attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### データ分析の主要な目標

- Sports data analytics are used not only in cricket but many other
  sports for
  improving the overall team performance and maximizing winning chances.
- Real-time data analytics can help in gaining insights even during the game
  for changing tactics by the team and by associated businesses for economic
  benefits and growth.
- Besides historical analysis, predictive models are
  harnessed to determine the possible match outcomes that require significant
  number crunching and data science know-how, visualization tools and capability
  to include newer observations in the analysis.

{{< figure >}}
src = '/images/content_images/cs/player-pose-estimator.png'
alt = 'pose estimator'
title = 'Cricket Pose Estimator'
attribution = '(Image credit: connect.vin)'
attributionlink = 'https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/'
{{< /figure >}}

### 課題

- **Data Cleaning and preprocessing**

  IPL has expanded cricket beyond the classic test match format to a much
  larger scale. The number of matches played every season across various
  formats has increased and so has the data, the algorithms, newer sports data
  analysis technologies and simulation models. Cricket data analysis requires
  field mapping, player tracking, ball tracking, player shot analysis, and
  several other aspects involved in how the ball is delivered, its angle, spin,
  velocity, and trajectory. All these factors together have increased the
  complexity of data cleaning and preprocessing.

- **Dynamic Modeling**

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

- **Predictive Analytics Complexity**

  Much of the decision making in cricket is based on questions such as "how
  often does a batsman play a certain kind of shot if the ball delivery is of a
  particular type", or "how does a bowler change his line and length if the
  batsman responds to his delivery in a certain way".
  This kind of predictive analytics query requires highly granular dataset
  availability and the capability to synthesize data and create generative
  models that are highly accurate.

## クリケット解析におけるNumPyの役割

スポーツ分析は現在、非常に盛んな分野です。 Many researchers and companies
[use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)
and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter,
besides using the latest machine learning and AI techniques.  NumPyは以下のように、クリケット関連の様々なスポーツ分析に使用されています。

- **Statistical Analysis:** NumPy's numerical capabilities help estimate the
  statistical significance of observational data or match events in the context
  of various player and game tactics, estimating the game outcome by comparison
  with a generative or static model.
  [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation)
  and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)
  are used for tactical analysis.

- **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provide useful insights into relationship between various datasets.

## まとめ

スポーツアナリティクスは、プロの試合についてはまさにゲームチェンジャーです。 特に戦略的な意思決定については、最近まで主に「直感」や過去の伝統的な考え方に基づいて行われていたため、大きな影響があります。 NumPyは、データ分析・機械学習・人工知能のアルゴリズムに関連する高レベル関数を提供する沢山のPythonパッケージ群の、堅固な基盤となっています。
これらのパッケージは、ゲームの結果を変えるような意思決定を支援するリアルタイムのインサイトを得るため、クリケットの試合だけでなく関連する推論やビジネスの推進にも広く使用されています。 クリケットの試合結果につながる隠れたパラメータや、パターン、属性を見つけることは、ステークホルダーが数字や統計に隠されているゲームの洞察方法を見つけるのにも役に立つのです。

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png'
alt = 'Diagram showing benefits of using NumPy for cricket analytics'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
