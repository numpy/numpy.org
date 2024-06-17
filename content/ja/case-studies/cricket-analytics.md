---
title: "ケーススタディ: クリケット分析、ゲームチェンジャー!"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/ipl-stadium.png'
title = ' IPLT20、インド最大のクリケットフェスティバル'
alt = 'Indian Premier League Cricket cup and stadium'
attribution = '(Image credits: IPLT20 (cup and logo) & Akash Yadav (stadium))'
attributionlink = 'https://unsplash.com/@aksh1802'
{{< /figure >}}

{{< blockquote
cite="https://www.scoopwhoop.com/sports/ms-dhoni/"
by="M S Dhoni、 _インディアンチームの元キャプテン、インターナショナル・クリケットプレイヤー、チェンナイ・スーパー・キングスのためにIPLでプレイ_"

> }}
> You don't play for the crowd, you play for the country.
> {{< /blockquote >}}

## クリケットについて

It would be an understatement to state that Indians love cricket. The game is
played in just about every nook and cranny of India, rural or urban, popular
with the young and the old alike, connecting billions in India unlike any other sport.
Cricket enjoys lots of media attention. There is a significant amount of
[money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and
fame at stake. Over the last several years, technology has literally been a game
changer. Audiences are spoilt for choice with streaming media, tournaments,
affordable access to mobile based live cricket watching, and more.

IPLは、クリケットを古典的なテストマッチ形式から、はるかに大規模に拡大させました。 毎シーズン、様々なフォーマットで行われる試合の数は増加しており、データ、アルゴリズム、最新のスポーツデータ分析技術、シミュレーションモデルも増加しています。 クリケットのデータ分析には、フィールドマッピング、プレイヤートラッキング、ボールトラッキング、プレイヤーショット分析、およびボールがどのように動くのか、その角度、スピン、速度、軌道など、他の沢山の種類のデータを必要とします。 これらの要因により、データクリーニングと前処理の複雑さが増してしまいました。 インドプレミアリーグ (IPL) は、2008年に設立された20チームから成るプロクリケットリーグです。 これは世界で最も参加者が多いクリケットイベントの1つで、2019年の市場規模は[67億ドル](https://en.wikipedia.org/wiki/Indian_Premier_League)だと評価されています。

Cricket is a game of numbers - the runs scored by a batsman, the wickets taken
by a bowler, the matches won by a cricket team, the number of times a batsman
responds in a certain way to a kind of bowling attack, etc. The capability to
dig into cricketing numbers for both improving performance and studying
the business opportunities, overall market, and economics of cricket via powerful
analytics tools, powered by numerical computing software such as NumPy, is a big
deal. Cricket analytics provides interesting insights into the game and
predictive intelligence regarding game outcomes.

現在では、クリケットゲームの記録と 利用可能な統計データは豊富で、ほぼ無限の宝の山だと言えます。 : [ESPN cricinfo や](https://stats.espncricinfo.com/ci/engine/stats/index.html) [cricsheet](https://cricsheet.org). These and several such cricket databases
have been used for cricket
analysis
using the latest machine learning and predictive modelling algorithms.
Media and entertainment platforms along with professional sports bodies
associated with the game use technology and analytics for determining key
metrics for improving match winning chances:

- バッティング成績の移動平均
- スコア予測
- プレイヤーの体力や、異なる相手に対するパフォーマンスについての洞察
- チーム構成に戦略的な決定を下すための、各勝敗へのプレイヤーの貢献

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png'
title = ' フィールドのフォーカルポイントとなるクリケットピッチ'
alt = 'A cricket pitch with bowler and batsmen'
align = 'center'
attribution = '(Image credit: Debarghya Das)'
attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### データ分析の主要な目標

- スポーツデータ分析はクリケットだけでなく、チーム全体のパフォーマンスを向上させ、勝利率を最大限に高めるために、 [他のスポーツ](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)でも使用されています。
- リアルタイムデータ分析は、ゲーム中の洞察を得ることができ、チームや関連ビジネスが経済的利益と成長のために戦術を変更するためも役立ちます。
- 履歴分析に加えて、予測モデルは可能性のある結果を求めることができますが、かなりの数のナンバークランチングとデータサイエンスのノウハウ、可視化ツール、および分析に新しい観測データを含める機能などが必要になります。

{{< figure >}}
src = '/images/content_images/cs/player-pose-estimator.png'
alt = 'pose estimator'
title = 'クリケットの姿勢推定'
attribution = '(Image credit: connect.vin)'
attributionlink = 'https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/'
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

Sports Analytics is a thriving field. スポーツ分析は現在、非常に盛んな分野です。 多くの研究者や企業は、最新の機械学習やAI技術以外にも、NumPyや、Scikit-learn, SciPy, Matplotlib, Jupyterなどの他のPyDataパッケージを[使っています](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)。  NumPyは以下のように、クリケット関連の様々なスポーツ分析に使用されています。  NumPy has been used
for various kinds of cricket related sporting analytics such as:

- **統計分析:** NumPyの数値計算機能は、様々なプレイヤーやゲーム戦術のコンテキストでの観測データで、試合中のイベントの統計的有意性を推定し、生成モデルや静的モデルと比較して試合結果を推定するのに役立ちます。 [因果分析](https://amplitude.com/blog/2017/01/19/causation-correlation) と [ビッグデータアプローチ](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)が戦術的分析に使用されています。
  [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation)
  and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)
  are used for tactical analysis.

- **データ可視化:** データのグラフ化・[可視化](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) は、さまざまなデータセット間の関係について、有益な洞察を与えてくれます。

## まとめ

Sports Analytics is a game changer when it comes to how professional games are
played, especially how strategic decision making happens, which until recently
was primarily done based on “gut feeling" or adherence to past traditions. NumPy
forms a solid foundation for a large set of Python packages which provide higher
level functions related to data analytics, machine learning, and AI algorithms.
These packages are widely deployed to gain real-time insights that help in
decision making for game-changing outcomes, both on field as well as to draw
inferences and drive business around the game of cricket. Finding out the
hidden parameters, patterns, and attributes that lead to the outcome of a
cricket match helps the stakeholders to take notice of game insights that are
otherwise hidden in numbers and statistics.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png'
alt = 'クリケット分析にNumPyを使用するメリットを示す図'
title = ' 利用されている主なNumPy機能 '
{{< /figure >}}
