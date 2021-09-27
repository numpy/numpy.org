---
title: "Case Study: Cricket Analytics, the game changer!"
sidebar: false
---

{{< figure src="/images/content_images/cs/ipl-stadium.png"
           caption="**IPLT20, the biggest Cricket Festival in India**"
           alt="Indian Premier League Cricket cup and stadium"
           attr="*(Image credits: IPLT20 (cup and logo) & Akash Yadav (stadium))*"
           attrlink="https://unsplash.com/@aksh1802" >}}

<blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/">
    <p>You don't play for the crowd, you play for the country.</p>
    <footer align="right">—M S Dhoni, <cite>International Cricket Player, ex-captain, Indian Team, plays for Chennai Super Kings in IPL</cite></footer>
</blockquote>

## About Cricket

It would be an understatement to state that Indians love cricket. The game is
played in just about every nook and cranny of India, rural or urban, popular
with the young and the old alike, connecting billions in India unlike any other sport.
Cricket enjoys lots of media attention. There is a significant amount of
[money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and
fame at stake. Over the last several years, technology has literally been a game
changer. Audiences are spoilt for choice with streaming media, tournaments,
affordable access to mobile based live cricket watching, and more.

The Indian Premier League (IPL) is a professional Twenty20 cricket
league, founded in 2008. It is one of the most attended cricketing events in
the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League)
in 2019.

Cricket is a game of numbers - the runs scored by a batsman, the wickets taken
by a bowler, the matches won by a cricket team, the number of times a batsman
responds in a certain way to a kind of bowling attack, etc. The capability to
dig into cricketing numbers for both improving performance and studying
the business opportunities, overall market, and economics of cricket via powerful
analytics tools, powered by numerical computing software such as NumPy, is a big
deal. Cricket analytics provides interesting insights into the game and
predictive intelligence regarding game outcomes.

Today, there are rich and almost infinite troves of cricket game records and
statistics available, e.g., [ESPN
cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) and
[cricsheet](https://cricsheet.org). These and several such cricket databases
have been used for [cricket
analysis](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances)
using the latest machine learning and predictive modelling algorithms.
Media and entertainment platforms along with professional sports bodies
associated with the game use technology and analytics for determining key
metrics for improving match winning chances:

* batting performance moving average,
* score forecasting,
* gaining insights into fitness and performance of a player against different opposition,
* player contribution to wins and losses for making strategic decisions on team composition

{{< figure src="/images/content_images/cs/cricket-pitch.png"
           class="csfigcaption"
           caption="**Cricket Pitch, the focal point in the field**"
           alt="A cricket pitch with bowler and batsmen"
           align="middle"
           attr="*(Image credit: Debarghya Das)*"
           attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}}

### Key Data Analytics Objectives

* Sports data analytics are used not only in cricket but many [other
  sports](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) for
  improving the overall team performance and maximizing winning chances.
* Real-time data analytics can help in gaining insights even during the game
  for changing tactics by the team and by associated businesses for economic
  benefits and growth.
* Besides historical analysis, predictive models are
  harnessed to determine the possible match outcomes that require significant
  number crunching and data science know-how, visualization tools and capability
  to include newer observations in the analysis.

{{< figure src="/images/content_images/cs/player-pose-estimator.png"
           class="fig-center"
           alt="pose estimator"
           caption="**Cricket Pose Estimator**"
           attr="*(Image credit: connect.vin)*"
           attrlink="https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/" >}}

### The Challenges

* **Data Cleaning and preprocessing**

  IPL has expanded cricket beyond the classic test match format to a much
  larger scale. The number of matches played every season across various
  formats has increased and so has the data, the algorithms, newer sports data
  analysis technologies and simulation models. Cricket data analysis requires
  field mapping, player tracking, ball tracking, player shot analysis, and
  several other aspects involved in how the ball is delivered, its angle, spin,
  velocity, and trajectory. All these factors together have increased the
  complexity of data cleaning and preprocessing.

* **Dynamic Modeling**

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

* **Predictive Analytics Complexity**

  Much of the decision making in cricket is based on questions such as "how
  often does a batsman play a certain kind of shot if the ball delivery is of a
  particular type", or "how does a bowler change his line and length if the
  batsman responds to his delivery in a certain way".
  This kind of predictive analytics query requires highly granular dataset
  availability and the capability to synthesize data and create generative
  models that are highly accurate.

## NumPy’s Role in Cricket Analytics

Sports Analytics is a thriving field. Many researchers and companies
[use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)
and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter,
besides using the latest machine learning and AI techniques.  NumPy has been used
for various kinds of cricket related sporting analytics such as:

* **Statistical Analysis:** NumPy's numerical capabilities help estimate the
  statistical significance of observational data or match events in the context
  of various player and game tactics, estimating the game outcome by comparison
  with a generative or static model.
  [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation)
  and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)
  are used for tactical analysis.

* **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provide useful insights into relationship between various datasets.

## Summary

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

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png"
           class="fig-center"
           alt="Diagram showing benefits of using NumPy for cricket analytics"
           caption="**Key NumPy Capabilities utilized**" >}}
