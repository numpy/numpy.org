---
title: "Case Study: Cricket Analytics, the game changer!"
sidebar: false
---

{{< figure src="/images/content_images/cs/ipl-stadium.png" caption="**IPLT20 the biggest Cricket Festival in India**" alt="IPLCricket" attr="(**Photo** - Cup and Logo: IPLT20, Cricket Stadium Akash Yadav/Unsplash)" attrlink="https://unsplash.com/@aksh1802?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyTexgt" >}}

<blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/">
    <p>You don't play for the crowd, you play for the country.</p>
    <footer align="right">—M S Dhoni, <cite>International Cricket Player, ex-captain, Indian Team, plays for Chennai Super Kings in IPL</cite></footer>
</blockquote>

## About Cricket

It would be an understatement to state that Indians love cricket. The game is played in just about every nook and cranny of India, rural or urban, popular with the young and old, connecting billions in India unlike any other sport. Cricket enjoys lots of media attention. There is a significant amount of [money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and fame at stake when it comes to Indian Cricket. The entire nation almost comes to a halt when the cricketing titans clash in tournaments such as the ICC World Cup or IPL.  Over the last several years, technology has literally been a game changer when it comes to cricket. The audience are spoilt for choice with zillions of streaming media, affordable access to mobile based live cricket watching. There is a flourishing business and economy around the game of cricket that does not shy from leveraging technology to make the most of the cricket experience. The Indian Premier League (IPL) is a professional Twenty20 cricket league, founded by the Board of Control for Cricket India (BCCI) in 2008. IPL is one of the most attended cricketing events in the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League) in 2019. 

Cricket is a game of numbers - the runs scored by a batsman, the wickets taken by a bowler, or the matches won by a cricket team, the number of times a batsman responds in a certain way to a kind of bowling attack, etc. The capability to dig into cricketing numbers for both improving performance as well as to study the business opportunity, overall market and economics of cricket via powerful analytics tools, powered by numerical computing software such as NumPy, is a big deal. Cricket analytics provide interesting insights into the game and predictive intelligence regarding the game outcome. That is of added value to the fans and also the [betting economy](https://economictimes.indiatimes.com/news/sports/betting-market-on-fire-for-cricket-world-cup/articleshow/69551830.cms?from=mdr) that runs alongside the game as a micro-industry. And then there are fans who don’t have the time to watch the entire match and so they put their Python and NumPy skills to use and  [extract interesting highlights](https://www.analyticsvidhya.com/blog/2019/09/guide-automatic-highlight-generation-python-without-machine-learning/) of the match in order to save on precious time.  

Today, there are rich and almost infinite troves of cricket games records and statistics available, for e.g., [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html), [cricsheet](https://cricsheet.org). These and several such cricket databases have been used for [cricket analysis](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) using the latest machine learning and prediction modeling algorithms. There are media and entertainment platforms along with professional sporting bodies associated with the game that use technology and analytics for determining batting performance moving average, score forecasting, gaining insights into fitness and performance of a player against different oppositions, player contribution to wins and losses in the game to make strategic decisions on building cricket teams, improving match winning chances and enriching the overall experience for the cricket loving audience.

{{< figure src="/images/content_images/cs/cricket-pitch.png" class="csfigcaption" caption="**Cricket Pitch, the focal point in the field**" alt="cricket pitch" align="middle" attr="(Image Credits: IPLPaper)" attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}} 

### Key Data Analytics Objectives

* Sports data analytics are used not only in cricket but several [other sports](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) for improving the overall team performance and maximize chances of wins.
* Real-time data analytics can help in gaining insights even while the game is on for changing tactics by the team and by associated businesses for economic benefits and growth. 
* Besides historical analysis, predictive models are harnessed  to determine the possible match outcomes that require significant number crunching and data science know-how, visualization tools and capability to include newer observations in the analysis.

{{< figure src="/images/content_images/cs/player-pose-estimator.png" class="fig-center" alt="pose estimator" caption="**Cricket Pose Estimator**" attr="(Image Credits: AI for Cricket)" attrlink="https://www.youtube.com/watch?v=nH5W7tQUSrI" >}}

### The Challenges 

* **Data Cleaning and preprocessing**

   There are several public and proprietary sources of cricket data, latter are mostly with the broadcasting corporations that hold rights to various seasons and matches played. IPL has expanded cricket beyond the classic test match format to a much larger scale. The number of matches played every season across various formats has increased and so has the data, the algorithms, newer technologies and simulation models. Real time video analysis requires field mapping, player tracking, ball tracking, player shot analysis and several other aspects involved in how the ball is delivered, its angle, spin, velocity and trajectory. 

* **Data Representation**

    One of the most trickiest of challenges with sports analytics is getting the right data representation. What this means is getting the raw data in a form such that it can be laid out for comparison and building models. If the initial representation itself is incorrect, everything that follows is akin to fitting noise to detect a signal. In cricket, just like any other sport, there can be a large number of variables related to tracking various numbers of players on the field, their attributes, the ball and several possibilities of potential actions.  The complexity of data analytics and representation is directly proportional to the kind of predictive questions that are put forth during analysis and are highly dependent on data representation and the model.  Things get even more challenging in terms of computation, data comparisons when dynamic cricket play predictions are sought such as what would have happened if the batsman had hit the ball at a different angle or velocity?

* **Predictive Analytics Complexity**

     In cricket, some of the decision making is based on questions such as how often a batsman plays a kind of shot if the ball delivery is of a certain type, or say how does a bowler change his line and length if the batsman responds to his delivery in a certain way, or how often does a team decide to bat after winning a toss or switches the batting order, etc. This kind of predictive analytics queries requires highly granular dataset availability and the capability to synthesize data and create generative models that are highly accurate.
 
## NumPy’s Role Cricket Analytics 
	
Sports Analytics is a thriving field. It utilizes several Python based software including NumPy, Matplotlib, Sci-kit learn, PyCharm, Jupyter and [others](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) in addition to latest machine learning and AI techniques.

NumPy, the standard numerical analysis package for Python,  has been utilized for various kinds of cricket related sporting analytics such as:

* **Data Correlation:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provides useful insights into relationship between various datasets, [causation](https://amplitude.com/blog/2017/01/19/causation-correlation), [stratification](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) for tactical analysis. NumPy offers the core foundation for several such analyses.

* **Statistical Analysis:** NumPy Compute processing helps estimate the statistical significance of observational data or match events in the context of various player and game tactics, estimating the game outcome by comparison with a generative or static model.

* **Data Visualization:** NumPy is used as the primary [numerical compute processing](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) engine for the cricket datasets. Pandas used as the data processing and I/O. Matplotlib used as the basic visualization for players. Seaborn package used as the modern visualization for Toss related analysis as well as for team and player insights.

{{< figure src="/images/content_images/cs/cricket-stats.png" class="fig-center" alt="role of numpy" caption="**IPL Data Analytics**" attr="(Source: mc.ai)" attrlink="https://mc.ai/predicting-the-outcome-of-cricket-matches-using-ai/" >}}

## Summary

Sports Analytics have changed the way professional games are played, especially regarding decision making which was not so long ago, primarily done based on “gut” feeling or adherence to past traditions. It is no secret that the Indian cricket teams rely heavily on data analytics to decide their strategy for an upcoming match or fine tune their tactics during the game.  NumPy forms the solid foundation used by several Python based softwares to provide higher level functions related to data analytics, machine learning and AI algorithms. These software are widely deployed to gain real-time insights that help in decision making for game-changing outcomes, both on field as well as to draw inferences and drive business around the game of cricket.  Finding out the hidden parameters, patterns and attributes that lead to the outcome of a cricket match helps the stakeholders to take notice of game insights that are otherwise hidden in numbers and statistics. 

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}
