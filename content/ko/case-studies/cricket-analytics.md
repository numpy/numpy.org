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

인도인들이 크리켓과 사랑에 빠졌다고 해도 과언이 아닙니다. 크리켓은 인도의 거의 모든 지역 구석구석에서 시골이든 도시든 상관없이 사랑받고 있습니다. 다른 스포츠와 달리 인도의 수십억 명을 연결하는 매개체 역할을 하는 데다 남녀노소 모두에게 인기가 있습니다. 크리켓은 많은 미디어의 관심을 받고 있기도 합니다. 엄청난 [돈](https://www.statista.com/topics/4543/indian-premier-league-ipl/)과 명성이 달려 있기도 하죠. 최근 몇 년 동안, 기술이 이 분야의 판도를 뒤집어 버렸습니다. 청중들은 스트리밍 미디어, 토너먼트, 모바일 기기를 통해 실시간 크리켓 경기를 저렴하게 볼 수 있습니다.

인도 프리미어 리그(IPL)는 2008년 설립되어 20개 팀으로 구성된 프로 크리켓 리그입니다. 이는 세계에서 가장 참가자가 많은 크리켓 이벤트 중 하나로, 2019년에 [67억 달러](https://en.wikipedia.org/wiki/Indian_Premier_League)에 달하는 가치로 추산됩니다.

Cricket is a game of numbers - the runs scored by a batsman, the wickets taken by a bowler, the matches won by a cricket team, the number of times a batsman responds in a certain way to a kind of bowling attack, etc. The capability to dig into cricketing numbers for both improving performance and studying the business opportunities, overall market, and economics of cricket via powerful analytics tools, powered by numerical computing software such as NumPy, is a big deal. Cricket analytics provides interesting insights into the game and predictive intelligence regarding game outcomes.

Today, there are rich and almost infinite troves of cricket game records and statistics available, e.g., [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) and [cricsheet](https://cricsheet.org). These and several such cricket databases have been used for [cricket analysis](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) using the latest machine learning and predictive modelling algorithms. Media and entertainment platforms along with professional sports bodies associated with the game use technology and analytics for determining key metrics for improving match winning chances:

* batting performance moving average,
* score forecasting,
* gaining insights into fitness and performance of a player against different opposition,
* player contribution to wins and losses for making strategic decisions on team composition

{{< figure src="/images/content_images/cs/cricket-pitch.png" class="csfigcaption" caption="**경기장의 중심이 되는 크리켓 피치**" alt="볼러와 배트맨으로 이루어진 크리켓 피치" align="middle" attr="*(사진 출처: Debarghya Das)*" attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}}

### 데이터 분석의 주요 목표

* 스포츠 데이터는 크리켓에서뿐만 아니라 [다른 스포츠](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)에서도 팀의 전체 역량과 승리 확률을 높이는 데 쓰입니다.
* 실시간 데이터 분석은 경기 중에도 팀과 관련 사업의 변화하는 전략에 대한 통찰력을 확보하여 경제적 이익과 성장을 도모하는 데 도움이 될 수 있습니다.
* Besides historical analysis, predictive models are harnessed to determine the possible match outcomes that require significant number crunching and data science know-how, visualization tools and capability to include newer observations in the analysis.

{{< figure src="/images/content_images/cs/player-pose-estimator.png" class="fig-center" alt="자세 예측" caption="**크리켓 자세 예측**" attr="*(사진 출처: connect.vin)*" attrlink="https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/" >}}

### 과제

* **데이터 정리 및 전처리**

  IPL은 크리켓을 고전적인 테스트 매치 형식에서 훨씬 더 큰 규모로 확대시켰습니다. 매 시즌 다양한 형식으로 열리는 경기의 수가 증가하고 있으며, 데이터, 알고리즘, 최신 스포츠 데이터 분석 기술, 시뮬레이션 모델 또한 증가하고 있습니다. 크리켓 데이터 분석에는 필드 매핑, 플레이어 추적, 공 추적, 플레이어의 타격 분석 및 공이 어떻게 움직이는지에 대한 각도, 스핀, 속도, 궤도 등 다른 많은 종류의 데이터를 필요로 합니다. 이 수많은 인자들은 데이터 정리 및 전처리 과정의 복잡성을 증가시켰습니다.

* **동적 모델링**

  크리켓에서는 다른 스포츠와 마찬가지로 다양한 선수의 수, 선수의 속성, 공이나 잠재적 행동의 가능성 등 여러 가능성을 추적할 때 많은 변수가 작용합니다. 데이터 분석 및 모델링의 복잡성은 분석 중 제시되는 예측 질문의 종류에 비례하며, 데이터 표현 및 모델에 크게 의존합니다. 타자가 다른 각도나 속도로 공을 쳤을 때 일어날 일과 같은 동적인 크리켓 경기를 예측할 때, 계산이나 데이터 비교 측면에서 상황이 훨씬 더 어려워집니다.

* **예측 분석의 복잡성**

  Much of the decision making in cricket is based on questions such as "how often does a batsman play a certain kind of shot if the ball delivery is of a particular type", or "how does a bowler change his line and length if the batsman responds to his delivery in a certain way". This kind of predictive analytics query requires highly granular dataset availability and the capability to synthesize data and create generative models that are highly accurate.

## 크리켓 분석에서 NumPy의 역할

스포츠 분석은 현재 매우 활발한 분야입니다. 많은 연구자들과 기업체에서는 최신 머신러닝 및 AI 기법을 쓰는 대신 [NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)나 Scikit-learn, SciPy, Matplotlib, Jupyter같은 PyData 패키지를 이용합니다.  NumPy는 크리켓과 관련된 여러 스포츠 통계에 다음과 같이 쓰였습니다.

* **통계적 분석:** NumPy의 수치적 기능은 다양한 플레이어 및 게임 전술에서 관찰 데이터 또는 경기의 통계적 중요성을 추정하는 데 도움을 주거나, 생성적 또는 정적 모델과 비교하여 게임 결과를 추정합니다. 전술 분석에는 [인과 분석](https://amplitude.com/blog/2017/01/19/causation-correlation) 및 [빅데이터 접근법](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)이 쓰입니다.

* **데이터 시각화:** 그래프 그리기 및 [시각화](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b)는 다양한 데이터셋 사이의 관계를 볼 수 있는 유용한 관점을 제공해 줍니다.

## 요약

스포츠 분석은 프로 게임의 판도를 바꿀 것입니다. 특히 최근까지는 주로 "직감"이나 과거부터 내려오던 것을 답습하는 식으로 이뤄진 전략적 의사 결정에 대해서 말입니다. NumPy는 데이터 분석, 기계 학습 및 AI 알고리즘과 관련하여 더욱 높은 수준의 기능을 제공하는 Python 패키지들의 견고한 기반을 제공합니다. 이들 패키지는 크리켓 경기뿐 아니라 크리켓 관련 추론이나 사업을 추진하면서, 판도를 바꿀만한 결정을 이끌어 내는 영감을 실시간으로 제공하는 데 널리 이용되고 있습니다. 크리켓 경기의 결과로 이어지는 숨겨진 매개변수, 패턴이나 속성을 찾는 것은 관계자가 숫자와 통계에 숨겨진 게임을 분석하는 방법을 파악하는 데 도움이 됩니다.

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png" class="fig-center" alt="NumPy를 크리켓 분석에 사용했을 때의 이익을 보여주는 다이어그램" caption="**활용된 주요 NumPy 기능**" >}}
