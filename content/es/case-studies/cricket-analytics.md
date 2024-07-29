---
title: "Case Study: Cricket Analytics, the game changer!"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/ipl-stadium.png' title = 'IPLT20, the biggest Cricket Festival in India' alt = 'Indian Premier League Cricket cup and stadium' attribution = '(Image credits: IPLT20 (cup and logo) & Akash Yadav (stadium))' attributionlink = 'https://unsplash.com/@aksh1802'
{{< /figure >}}

{{< blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/" by="M S Dhoni, *International Cricket Player, ex-captain, Indian Team, plays for Chennai Super Kings in IPL*"
> }} You don't play for the crowd, you play for the country. 
> 
> {{< /blockquote >}}

## About Cricket

It would be an understatement to state that Indians love cricket. The game is played in just about every nook and cranny of India, rural or urban, popular with the young and the old alike, connecting billions in India unlike any other sport. Cricket enjoys lots of media attention. There is a significant amount of [money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and fame at stake. Over the last several years, technology has literally been a game changer. Audiences are spoilt for choice with streaming media, tournaments, affordable access to mobile based live cricket watching, and more.

The Indian Premier League (IPL) is a professional Twenty20 cricket league, founded in 2008. It is one of the most attended cricketing events in the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League) in 2019.

Cricket is a game of numbers - the runs scored by a batsman, the wickets taken by a bowler, the matches won by a cricket team, the number of times a batsman responds in a certain way to a kind of bowling attack, etc. The capability to dig into cricketing numbers for both improving performance and studying the business opportunities, overall market, and economics of cricket via powerful analytics tools, powered by numerical computing software such as NumPy, is a big deal. Cricket analytics provides interesting insights into the game and predictive intelligence regarding game outcomes.

Today, there are rich and almost infinite troves of cricket game records and statistics available, e.g., [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) and [cricsheet](https://cricsheet.org). These and several such cricket databases have been used for [cricket analysis](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) using the latest machine learning and predictive modelling algorithms. Media and entertainment platforms along with professional sports bodies associated with the game use technology and analytics for determining key metrics for improving match winning chances:

* batting performance moving average,
* score forecasting,
* gaining insights into fitness and performance of a player against different opposition,
* player contribution to wins and losses for making strategic decisions on team composition

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png' title = 'Cricket Pitch, the focal point in the field' alt = 'A cricket pitch with bowler and batsmen' align = 'center' attribution = '(Image credit: Debarghya Das)' attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### Key Data Analytics Objectives

* Sports data analytics are used not only in cricket but many [other sports](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) for improving the overall team performance and maximizing winning chances.
* Real-time data analytics can help in gaining insights even during the game for changing tactics by the team and by associated businesses for economic benefits and growth.
* Besides historical analysis, predictive models are harnessed to determine the possible match outcomes that require significant number crunching and data science know-how, visualization tools and capability to include newer observations in the analysis.

{{< figure >}}
src = '/images/content_images/cs/player-pose-estimator.png' alt = 'pose estimator' title = 'Cricket Pose Estimator' attribution = '(Image credit: connect.vin)' attributionlink = 'https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/'
{{< /figure >}}

### The Challenges

* **Data Cleaning and preprocessing**

  IPL has expanded cricket beyond the classic test match format to a much larger scale. The number of matches played every season across various formats has increased and so has the data, the algorithms, newer sports data analysis technologies and simulation models. Cricket data analysis requires field mapping, player tracking, ball tracking, player shot analysis, and several other aspects involved in how the ball is delivered, its angle, spin, velocity, and trajectory. All these factors together have increased the complexity of data cleaning and preprocessing.

* **Dynamic Modeling**

  In cricket, just like any other sport, there can be a large number of variables related to tracking various numbers of players on the field, their attributes, the ball, and several possibilities of potential actions. The complexity of data analytics and modeling is directly proportional to the kind of predictive questions that are put forth during analysis and are highly dependent on data representation and the model. Las cosas se vuelven aún más desafiantes en términos de cálculo y comparación de datos cuando se buscan predicciones dinámicas del juego de críquet, tal como habría sucedido si el bateador hubiera golpeado la bola a un ángulo o velocidad diferente.

* **Complejidad de Análisis Predictivo**

  Gran parte de la toma de decisiones en el críquet se basa en preguntas como "¿con qué frecuencia un bateador juega un cierto tipo de golpe si la entrega de la pelota es de un tipo particular?" o "¿cómo cambia un lanzador su línea y longitud si el bateador responde a su entrega de una cierta manera?". Este tipo de consulta de análisis predictivo requiere una disponibilidad de un conjunto de datos altamente granular y la capacidad de sintetizar datos y crear modelos generativos que sean altamente precisos.

## El Papel de NumPy en el Análisis del Críquet

El análisis deportivo es un campo en desarrollo. Muchos investigadores y compañías [utilizan NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) y otros paquetes de PyData como Scikit-learn, SciPy, Matplotlib y Jupyter, además de utilizar las últimas técnicas de aprendizaje automático e inteligencia artificial.  NumPy se ha utilizado para varios tipos de análisis deportivos relacionados con el críquet tales como:

* **Análisis Estadístico:** Las capacidades numéricas de NumPy ayudan a estimar la significancia estadística de los datos observacionales o de eventos de partidos en el contexto de varias tácticas de jugadores y de juego, estimando el resultado del juego mediante la comparación con un modelo generativo o estático. El [análisis causal](https://amplitude.com/blog/2017/01/19/causation-correlation) y los [enfoques de big data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) se utilizan para el análisis táctico.

* **Visualización de Datos:** La creación de gráficos y la [visualización de datos](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) proporcionan información útil sobre la relación entre varios conjuntos de datos.

## Resumen

El análisis deportivo ha revolucionado la forma en que se juegan los partidos profesionales, especialmente en cuanto a la toma de decisiones estratégicas, que hasta hace poco se basaba principalmente en la "intuición" o en la adherencia a tradiciones pasadas. NumPy constituye una base sólida para un gran conjunto de paquetes de Python que brindan funciones de nivel superior relacionadas con análisis de datos, el aprendizaje automático y los algoritmos de IA. Estos paquetes están ampliamente desplegados para obtener información en tiempo real que ayudan en la toma de decisiones para resultados revolucionarios, tanto en el campo como para sacar conclusiones y hacer negocios alrededor del juego del críquet. Encontrar los parámetros ocultos, patrones y atributos que conducen al resultado de un partido de críquet ayuda a los interesados a tomar nota de la información del juego que de otra forma estarían ocultos en números y estadísticas.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png' alt = 'Diagrama que muestra los beneficios de usar NumPy para análisis de críquet' title = 'Capacidades claves de NumPy utilizadas'
{{< /figure >}}
