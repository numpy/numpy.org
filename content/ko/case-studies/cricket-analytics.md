---
title: "사례 연구: 판도를 뒤집은 크리켓 통계!"
sidebar: false
---

{{< figure src="/images/content_images/cs/ipl-stadium.png" caption="**인도 최대의 크리켓 축제인 IPLT20**" alt="인도 프리미어 리그 크리켓 컵 및 경기장" attr="*(사진 출처: IPLT20 (컵 및 로고) & Akash Yadav (경기장))*" attrlink="https://unsplash.com/@aksh1802" >}}

<blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/">
    <p>군중을 위해서가 아니라, 국가를 위해 뛰는 겁니다.</p>
    <footer align="right">—M S Dhoni, <cite>국제 크리켓 선수, 전 팀장, 인도 팀, IPL의 Chennai Super Kings에서 활약</cite></footer>
</blockquote>

## 크리켓이란

인도인들이 크리켓과 사랑에 빠졌다고 해도 과언이 아닙니다. 크리켓은 인도의 거의 모든 지역 구석구석에서 시골이든 도시든 상관없이 사랑받고 있습니다. 다른 스포츠와 달리 인도의 수십억 명을 연결하는 매개체 역할을 하는 데다 남녀노소 모두에게 인기가 있습니다. Cricket enjoys lots of media attention. There is a significant amount of [money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and fame at stake. Over the last several years, technology has literally been a game changer. Audiences are spoilt for choice with streaming media, tournaments, affordable access to mobile based live cricket watching, and more.

The Indian Premier League (IPL) is a professional Twenty20 cricket league, founded in 2008. It is one of the most attended cricketing events in the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League) in 2019.

Cricket is a game of numbers - the runs scored by a batsman, the wickets taken by a bowler, the matches won by a cricket team, the number of times a batsman responds in a certain way to a kind of bowling attack, etc. The capability to dig into cricketing numbers for both improving performance and studying the business opportunities, overall market, and economics of cricket via powerful analytics tools, powered by numerical computing software such as NumPy, is a big deal. Cricket analytics provides interesting insights into the game and predictive intelligence regarding game outcomes.

Today, there are rich and almost infinite troves of cricket game records and statistics available, e.g., [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) and [cricsheet](https://cricsheet.org). These and several such cricket databases have been used for [cricket analysis](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) using the latest machine learning and predictive modelling algorithms. Media and entertainment platforms along with professional sports bodies associated with the game use technology and analytics for determining key metrics for improving match winning chances:

* batting performance moving average,
* score forecasting,
* gaining insights into fitness and performance of a player against different opposition,
* player contribution to wins and losses for making strategic decisions on team composition

{{< figure src="/images/content_images/cs/cricket-pitch.png" class="csfigcaption" caption="**Cricket Pitch, the focal point in the field**" alt="A cricket pitch with bowler and batsmen" align="middle" attr="*(Image credit: Debarghya Das)*" attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}}

### Key Data Analytics Objectives

* Sports data analytics are used not only in cricket but many [other sports](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) for improving the overall team performance and maximizing winning chances.
* Real-time data analytics can help in gaining insights even during the game for changing tactics by the team and by associated businesses for economic benefits and growth.
* Besides historical analysis, predictive models are harnessed to determine the possible match outcomes that require significant number crunching and data science know-how, visualization tools and capability to include newer observations in the analysis.

{{< figure src="/images/content_images/cs/player-pose-estimator.png" class="fig-center" alt="pose estimator" caption="**Cricket Pose Estimator**" attr="*(Image credit: connect.vin)*" attrlink="https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/" >}}

### 과제

* **Data Cleaning and preprocessing**

  IPL has expanded cricket beyond the classic test match format to a much larger scale. The number of matches played every season across various formats has increased and so has the data, the algorithms, newer sports data analysis technologies and simulation models. Cricket data analysis requires field mapping, player tracking, ball tracking, player shot analysis, and several other aspects involved in how the ball is delivered, its angle, spin, velocity, and trajectory. All these factors together have increased the complexity of data cleaning and preprocessing.

* **Dynamic Modeling**

  In cricket, just like any other sport, there can be a large number of variables related to tracking various numbers of players on the field, their attributes, the ball, and several possibilities of potential actions. The complexity of data analytics and modeling is directly proportional to the kind of predictive questions that are put forth during analysis and are highly dependent on data representation and the model. Things get even more challenging in terms of computation, data comparisons when dynamic cricket play predictions are sought such as what would have happened if the batsman had hit the ball at a different angle or velocity.

* **Predictive Analytics Complexity**

  Much of the decision making in cricket is based on questions such as "how often does a batsman play a certain kind of shot if the ball delivery is of a particular type", or "how does a bowler change his line and length if the batsman responds to his delivery in a certain way". This kind of predictive analytics query requires highly granular dataset availability and the capability to synthesize data and create generative models that are highly accurate.

## 크리켓 분석에서 NumPy의 역할

스포츠 분석은 현재 매우 활발한 분야입니다. 많은 연구자들과 기업체에서는 최신 머신러닝 및 AI 기법을 쓰는 대신 [NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)나 Scikit-learn, SciPy, Matplotlib, Jupyter같은 PyData 패키지를 이용합니다.  NumPy는 크리켓과 관련된 여러 스포츠 통계에 다음과 같이 쓰였습니다.

* **통계적 분석:** NumPy의 수치적 기능은 다양한 플레이어 및 게임 전술에서 관찰 데이터 또는 경기의 통계적 중요성을 추정하는 데 도움을 주거나, 생성적 또는 정적 모델과 비교하여 게임 결과를 추정합니다. 전술 분석에는 [인과 분석](https://amplitude.com/blog/2017/01/19/causation-correlation) 및 [빅데이터 접근법](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)이 쓰입니다.

* **데이터 시각화:** 그래프 그리기 및 [시각화](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b)는 다양한 데이터셋 사이의 관계를 볼 수 있는 유용한 관점을 제공해 줍니다.

## 요약

스포츠 분석은 프로 게임의 판도를 바꿀 것입니다. 특히 최근까지는 주로 "직감"이나 과거부터 내려오던 것을 답습하는 식으로 이뤄진 전략적 의사 결정에 대해서 말입니다. NumPy forms a solid foundation for a large set of Python packages which provide higher level functions related to data analytics, machine learning, and AI algorithms. These packages are widely deployed to gain real-time insights that help in decision making for game-changing outcomes, both on field as well as to draw inferences and drive business around the game of cricket. Finding out the hidden parameters, patterns, and attributes that lead to the outcome of a cricket match helps the stakeholders to take notice of game insights that are otherwise hidden in numbers and statistics.

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png" class="fig-center" alt="NumPy를 크리켓 분석에 사용했을 때의 이익을 보여주는 다이어그램" caption="**활용된 주요 NumPy 기능**" >}}
