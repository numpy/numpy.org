---
title: "사례 연구: 판도를 뒤집은 크리켓 통계!"
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

## 크리켓이란

인도인들이 크리켓과 사랑에 빠졌다고 해도 과언이 아닙니다. 크리켓은 인도의 거의 모든 지역 구석구석에서 시골이든 도시든 상관없이 사랑받고 있습니다. 다른 스포츠와 달리 인도의 수십억 명을 연결하는 매개체 역할을 하는 데다 남녀노소 모두에게 인기가 있습니다.
크리켓은 많은 미디어의 관심을 받고 있기도 합니다. There is a significant amount of
[money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and
fame at stake. 최근 몇 년 동안, 기술이 이 분야의 판도를 뒤집어 버렸습니다. 청중들은 스트리밍 미디어, 토너먼트, 모바일 기기를 통해 실시간 크리켓 경기를 저렴하게 볼 수 있습니다.

인도 프리미어 리그(IPL)는 2008년 설립되어 20개 팀으로 구성된 프로 크리켓 리그입니다. It is one of the most attended cricketing events in
the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League)
in 2019.

크리켓은 숫자의 게임이다 - 타자가 득점하고, 위켓이 가져간다.
크리켓 팀이 이긴 경기, 타자가 이긴 횟수
일종의 볼링 공격 등에 특정한 방식으로 반응합니다. NumPy와 같은 수치 컴퓨팅 소프트웨어로 구동되는 강력한 분석 도구를 통해 크리켓의 성능 향상과 사업 기회, 전반적인 시장, 경제학을 연구하기 위한 크리켓 숫자를 파헤칠 수 있는 능력은 큰 일이다. 크리켓 분석은 게임에 대한 흥미로운 통찰력과 게임 결과에 대한 예측 지능을 제공한다.

Today, there are rich and almost infinite troves of cricket game records and
statistics available, e.g., ESPN
cricinfo and
[cricsheet](https://cricsheet.org). These and several such cricket databases
have been used for cricket
analysis
using the latest machine learning and predictive modelling algorithms.
게임과 관련된 전문 스포츠 기관과 함께 미디어 및 엔터테인먼트 플랫폼은 경기 승리 기회를 향상시키기 위한 주요 측정 기준을 결정하기 위한 기술 및 분석을 사용합니다.

- 타격 성적 이동 평균,
- 점수 예측,
- 다른 상대에 맞서 선수의 체력과 경기력에 대한 통찰력을 얻기,
- 팀 구성에 대한 전략적 결정을 내리는 플레이어의 승패 기여도

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png'
title = 'Cricket Pitch, the focal point in the field'
alt = 'A cricket pitch with bowler and batsmen'
align = 'center'
attribution = '(Image credit: Debarghya Das)'
attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### 데이터 분석의 주요 목표

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

### 과제

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

## 크리켓 분석에서 NumPy의 역할

스포츠 분석은 현재 매우 활발한 분야입니다. Many researchers and companies
[use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)
and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter,
besides using the latest machine learning and AI techniques.  NumPy는 크리켓과 관련된 여러 스포츠 통계에 다음과 같이 쓰였습니다.

- **Statistical Analysis:** NumPy's numerical capabilities help estimate the
  statistical significance of observational data or match events in the context
  of various player and game tactics, estimating the game outcome by comparison
  with a generative or static model.
  [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation)
  and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)
  are used for tactical analysis.

- **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provide useful insights into relationship between various datasets.

## 요약

스포츠 분석은 프로 게임의 판도를 바꿀 것입니다. 특히 최근까지는 주로 "직감"이나 과거부터 내려오던 것을 답습하는 식으로 이뤄진 전략적 의사 결정에 대해서 말입니다. NumPy는 데이터 분석, 기계 학습 및 AI 알고리즘과 관련하여 더욱 높은 수준의 기능을 제공하는 Python 패키지들의 견고한 기반을 제공합니다.
이들 패키지는 크리켓 경기뿐 아니라 크리켓 관련 추론이나 사업을 추진하면서, 판도를 바꿀만한 결정을 이끌어 내는 영감을 실시간으로 제공하는 데 널리 이용되고 있습니다. 크리켓 경기의 결과로 이어지는 숨겨진 매개변수, 패턴이나 속성을 찾는 것은 관계자가 숫자와 통계에 숨겨진 게임을 분석하는 방법을 파악하는 데 도움이 됩니다.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png'
alt = 'Diagram showing benefits of using NumPy for cricket analytics'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
