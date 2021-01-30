---
title: "ケーススタディ: クリケット分析、ゲームチェンジャー!"
sidebar: false
---

{{< figure src="/images/content_images/cs/ipl-stadium.png" caption="** IPLT20、インド最大のクリケットフェスティバル**" alt="Indian Premier League Cricket cup and stadium" attr="*(Image credits: IPLT20 (cup and logo) & Akash Yadav (stadium))*" attrlink="https://unsplash.com/@aksh1802" >}}

<blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/">
    <p>観客のために競技をするのではなく、国のために競技するのです。</p>
    <footer align="right">—M S Dhoni、 <cite>インディアンチームの元キャプテン、インターナショナル・クリケットプレイヤー、チェンナイ・スーパー・キングスのためにIPLでプレイ</cite></footer>
</blockquote>

## クリケットについて

インド人はクリケットが大好きだと言っても過言ではないでしょう。 この競技は、他のスポーツと異なり、インドの農村部や都市部を問わず、あらゆる場所でプレイされており、若者から年配の方まで広く人気があり、インドでは何十億人もの人々を結びつける役割を担っています。 クリケットは多くのメディアの注目を集めています。 非常に [多額のお金](https://www.statista.com/topics/4543/indian-premier-league-ipl/)と名声がかかっています。 過去数年間、テクノロジーは文字通りクリケットの試合を変えてきました。 視聴者は、ストリーミングメディアや、トーナメント、モバイルベースの手頃なアクセスによるライブクリケット視聴や、その他の方法に甘やかされています。

インドプレミアリーグ (IPL) は、2008年に設立された20チームから成るプロクリケットリーグです。 これは、2019年に [67億ドル](https://en.wikipedia.org/wiki/Indian_Premier_League) の市場規模と評価される世界で最も参加者が多いクリケットイベントの1つです。

クリケットは数のゲームです - バッツマンによってスコアされたランの数、ボウラーによって取られたウィケットの数、クリケットチームによって獲得した試合の数、バッツマンがボウリング攻撃に特定の方法で応答する回数など。 クリケットの数字を掘り下げてパフォーマンスを向上させるとともに、NumPyなどの数値計算ソフトウェアを利用した強力な分析ツールを介して、クリケットのビジネスチャンス、市場全体、経済性を研究することは、大きな意味を持ちます。 クリケット分析は、試合に関する興味深い洞察と、ゲームの結果に関する予測AIを提供します。

現在では、クリケットゲームの記録と 利用可能な統計データは豊富で、ほぼ無限の宝の山だと言えます。: [ESPN cricinfo や](https://stats.espncricinfo.com/ci/engine/stats/index.html) [cricsheet](https://cricsheet.org). これらのクリケットデータベースは、最新の機械学習と予測モデリングアルゴリズムを使用して、 [クリケット 分析](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) に使用されています。 メディアやプロスポーツ団体のエンターテインメントプラットフォームは、技術や分析を利用し、試合勝率を向上させるための主要なメトリックを下記のような要素だと考え始めています:

* バッティングの記録の移動平均
* スコア予測
* プレイヤーの体力やパフォーマンスについての知識を得ること
* チーム構成に戦略的な決定を下すための、各勝敗へのプレイヤーの貢献

{{< figure src="/images/content_images/cs/cricket-pitch.png" class="csfigcaption" caption="** フィールドのフォーカルポイントとなるクリケットピッチ**" alt="A cricket pitch with bowler and batsmen" align="middle" attr="*(Image credit: Debarghya Das)*" attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}}

### データ分析の主要な目標

* スポーツデータ分析はクリケットだけでなく、チーム全体のパフォーマンスを向上させ、勝利率を最大限に高めるために、 [ 他のスポーツ](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)でも使用されています。
* リアルタイムデータ分析は、ゲーム中の洞察を得ることができ、チームや関連ビジネスが経済的利益と成長のために戦術を変更するためも役立ちます。
* 履歴分析に加えて、予測モデルは可能性のある結果を求めることができますが、かなりの数のナンバークランチングとデータサイエンスのノウハウ、可視化ツール、および分析に新しい観測データを含める機能などが必要になります。

{{< figure src="/images/content_images/cs/player-pose-estimator.png" class="fig-center" alt="pose estimator" caption="**クリケットの姿勢推定**" attr="*(Image credit: connect.vin)*" attrlink="https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/" >}}

### 課題

* **データのクリーニングと前処理**

  IPLは、クリケットを古典的なテストマッチ形式をから、はるかに大規模に拡大させました。 毎シーズン、様々なフォーマットで行われる試合の数は増加しており、データ、アルゴリズム、最新のスポーツデータ分析技術、シミュレーションモデルも増加しています。 クリケットのデータ分析には、フィールドマッピング、プレイヤートラッキング、ボールトラッキング、プレイヤーショット分析、およびボールがどのように動くのか、その角度、スピン、速度、軌道など、他の沢山の種類のデータを必要とします。 これらの要因により、データクリーニングと前処理の複雑さが増してしまいました。

* **動的モデリング**

  クリケットも、他のスポーツのように、フィールド上の選手の様々な数字を追跡するために、関連する変数の数が多くなってしまいがちです。たとえば、ボールやその属性情報、および潜在的なアクションのいくつかの可能性などの変数です。 データ分析とモデリングの複雑さは、分析中に必要となる予測のための質問の種類に正比例しており、データ表現とモデルにも大きく依存しています。 打者が異なる角度や速度でボールを打った場合に何が起こるのかのような、動的なクリケットのプレーの予測が必要な場合、計算量やデータ比較が更に困難になります。

* **予測分析の複雑さ**

  クリケットの意思決定の多くは、"ボール運びがある特定のタイプの場合、バッツマンはどのくらいの頻度で特定の種類のショットを打つのか？"や、"バッツマンが特定の方法であるボール運びに反応した場合、ボウラーはどのように彼のラインと長さを変更するのか "などの質問に基づいています。 This kind of predictive analytics query requires highly granular dataset availability and the capability to synthesize data and create generative models that are highly accurate.

## NumPy’s Role in Cricket Analytics

Sports Analytics is a thriving field. Many researchers and companies [use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter, besides using the latest machine learning and AI techniques.  NumPy has been used for various kinds of cricket related sporting analytics such as:

* **Statistical Analysis:** NumPy's numerical capabilities help estimate the statistical significance of observational data or match events in the context of various player and game tactics, estimating the game outcome by comparison with a generative or static model. [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation) and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) are used for tactical analysis.

* **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provides useful insights into relationship between various datasets.

## Summary

Sports Analytics is a game changer when it comes to how professional games are played, especially how strategic decision making happens, which until recently was primarily done based on “gut feeling" or adherence to past traditions. NumPy forms a solid foundation for a large set of Python packages which provide higher level functions related to data analytics, machine learning, and AI algorithms. These packages are widely deployed to gain real-time insights that help in decision making for game-changing outcomes, both on field as well as to draw inferences and drive business around the game of cricket. Finding out the hidden parameters, patterns, and attributes that lead to the outcome of a cricket match helps the stakeholders to take notice of game insights that are otherwise hidden in numbers and statistics.

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png" class="fig-center" alt="Diagram showing benefits of using NumPy for cricket analytics" caption="**Key NumPy Capabilities utilized**" >}}
