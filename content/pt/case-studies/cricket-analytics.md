---
title: "Estudo de Caso: Análise de Críquete, a revolução!"
sidebar: false
---

{{< figure src="/images/content_images/cs/ipl-stadium.png" caption="**IPLT20, o maior festival de Críquete da Índia**" alt="Copa e estádio da Indian Premier League Cricket" attr="*(Image credits: IPLT20 (cup and logo) & Akash Yadav (stadium))*" attrlink="https://unsplash.com/@aksh1802" >}}

<blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/">
    <p>Você não joga para a torcida, joga para o país.</p>
    <footer align="right">—M S Dhoni, <cite>Jogador Internacional de Críquete, ex-capitão, Time Indiano, joga pelo Chennai Super Kings na IPL</cite></footer>
</blockquote>

## Sobre Críquete

Dizer que os indianos adoram o críquete seria subestimar este sentimento. O jogo é jogado praticamente em todas as localidades da Índia, rurais ou urbanas, e é popular com os jovens e os anciões, conectando bilhões de pessoas na Índia como nenhum outro esporte. O cricket também recebe muita atenção da mídia. Há uma quantidade significativa de [dinheiro](https://www.statista.com/topics/4543/indian-premier-league-ipl/) e fama em jogo. Ao longo dos últimos anos, a tecnologia foi literalmente uma revolução. As audiências tem uma ampla possibilidade de escolha, com mídias de streaming, torneios, acesso barato a jogos de críquete ao vivo em dispositivos móveis, e mais.

A Primeira Liga Indiana (*Indian Premier League* - IPL) é uma liga profissional de críquete [Twenty20](https://pt.wikipedia.org/wiki/Twenty20), fundada em 2008. É um dos eventos de críquete mais assistidos no mundo avaliado em [$6,7 bilhões de dólares](https://en.wikipedia.org/wiki/Indian_Premier_League) em 2019.

Críquete é um jogo dominado pelos números - as corridas executadas por um <en>batsman</en>, os <en>wickets</en> perdidos por um boleador, as partidas ganhas por uma equipe de críquete, o número de vezes que um batsman responde de certa maneira a um tipo de arremesso do boleador, etc. A capacidade de investigar números de críquete para melhorar o desempenho e estudar as oportunidades de negócio, mercado e economia de críquete através de poderosas ferramentas de análise, alimentadas por softwares numéricos de computação, como o NumPy, é um grande negócio. As análises de críquete fornecem informações interessantes sobre o jogo e informações preditivas sobre os resultados do jogo.

Hoje, existem conjuntos ricos e quase infinitos de estatísticas e informações sobre jogos de críquete, por exemplo, [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) e [cricsheet](https://cricsheet.org). Estes e muitos outros bancos de dados de críquete foram usados para [análise de críquete](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) usando os mais modernos algoritmos de aprendizagem de máquina e modelagem preditiva. Plataformas de mídia e entretenimento, juntamente com entidades de esporte profissionais associadas ao jogo usam tecnologia e análise para determinar métricas chave para melhorar as chances de vitória:

* média móvel do desempenho em rebatidas,
* previsão de pontuação,
* ganho de informações sobre desempenho e condição física de um determinado jogador contra determinado adversário,
* player contribution to wins and losses for making strategic decisions on team composition

{{< figure src="/images/content_images/cs/cricket-pitch.png" class="csfigcaption" caption="**Cricket Pitch, the focal point in the field**" alt="A cricket pitch with bowler and batsmen" align="middle" attr="*(Image credit: Debarghya Das)*" attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}}

### Key Data Analytics Objectives

* Sports data analytics are used not only in cricket but many [other sports](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) for improving the overall team performance and maximizing winning chances.
* Real-time data analytics can help in gaining insights even during the game for changing tactics by the team and by associated businesses for economic benefits and growth.
* Besides historical analysis, predictive models are harnessed to determine the possible match outcomes that require significant number crunching and data science know-how, visualization tools and capability to include newer observations in the analysis.

{{< figure src="/images/content_images/cs/player-pose-estimator.png" class="fig-center" alt="pose estimator" caption="**Cricket Pose Estimator**" attr="*(Image credit: connect.vin)*" attrlink="https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/" >}}

### The Challenges

* **Data Cleaning and preprocessing**

  IPL has expanded cricket beyond the classic test match format to a much larger scale. The number of matches played every season across various formats has increased and so has the data, the algorithms, newer sports data analysis technologies and simulation models. Cricket data analysis requires field mapping, player tracking, ball tracking, player shot analysis, and several other aspects involved in how the ball is delivered, its angle, spin, velocity, and trajectory. All these factors together have increased the complexity of data cleaning and preprocessing.

* **Dynamic Modeling**

  In cricket, just like any other sport, there can be a large number of variables related to tracking various numbers of players on the field, their attributes, the ball, and several possibilities of potential actions. The complexity of data analytics and modeling is directly proportional to the kind of predictive questions that are put forth during analysis and are highly dependent on data representation and the model. Things get even more challenging in terms of computation, data comparisons when dynamic cricket play predictions are sought such as what would have happened if the batsman had hit the ball at a different angle or velocity.

* **Predictive Analytics Complexity**

  Much of the decision making in cricket is based on questions such as "how often does a batsman play a certain kind of shot if the ball delivery is of a particular type", or "how does a bowler change his line and length if the batsman responds to his delivery in a certain way". This kind of predictive analytics query requires highly granular dataset availability and the capability to synthesize data and create generative models that are highly accurate.

## NumPy’s Role in Cricket Analytics

Sports Analytics is a thriving field. Many researchers and companies [use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter, besides using the latest machine learning and AI techniques.  NumPy has been used for various kinds of cricket related sporting analytics such as:

* **Statistical Analysis:** NumPy's numerical capabilities help estimate the statistical significance of observational data or match events in the context of various player and game tactics, estimating the game outcome by comparison with a generative or static model. [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation) and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) are used for tactical analysis.

* **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provides useful insights into relationship between various datasets.

## Summary

Sports Analytics is a game changer when it comes to how professional games are played, especially how strategic decision making happens, which until recently was primarily done based on “gut feeling" or adherence to past traditions. NumPy forms a solid foundation for a large set of Python packages which provide higher level functions related to data analytics, machine learning, and AI algorithms. These packages are widely deployed to gain real-time insights that help in decision making for game-changing outcomes, both on field as well as to draw inferences and drive business around the game of cricket. Finding out the hidden parameters, patterns, and attributes that lead to the outcome of a cricket match helps the stakeholders to take notice of game insights that are otherwise hidden in numbers and statistics.

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png" class="fig-center" alt="Diagram showing benefits of using NumPy for cricket analytics" caption="**Key NumPy Capabilities utilized**" >}}
