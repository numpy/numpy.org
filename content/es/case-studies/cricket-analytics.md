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

It would be an understatement to state that Indians love cricket. The game is played in just about every nook and cranny of India, rural or urban, popular with the young and the old alike, connecting billions in India unlike any other sport. Cricket enjoys lots of media attention. Hay una cantidad importante de [dinero](https://www.statista.com/topics/4543/indian-premier-league-ipl/) y fama en juego. En los últimos años, la tecnología ha cambiado literalmente las reglas del juego. El público tiene muchas opciones para elegir entre streaming de medios, torneos, acceso asequible a la visualización de críquet en vivo desde dispositivos móviles y más.

La Premier League de India (IPL) es una liga profesional de críquet Twenty20, fundada en 2008. Es uno de los eventos de críquet más concurridos en el mundo, valorado en [$6.7 mil millones de dólares](https://en.wikipedia.org/wiki/Indian_Premier_League) en 2019.

El críquet es un juego de números - las carreras anotadas por un bateador, los wickets tomados por un lanzador, los partidos ganados por un equipo de críquet, el número de veces que un bateador responde de cierta manera a un tipo de ataque de lanzamiento, etc. La capacidad de profundizar en los números del críquet tanto para mejorar el rendimiento como para estudiar las oportunidades de negocio, el mercado en general y la economía del cricket mediante potentes herramientas de análisis, impulsadas por software de computación numérica como NumPy, es algo muy importante. El análisis del críquet proporciona ideas interesantes sobre el juego e inteligencia predictiva respecto a los resultados del juego.

Hoy en día, hay abundantes y casi infinitos tesoros de registros y estadísticas de juegos de críquet disponibles, por ejemplo, en [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) y [cricsheet](https://cricsheet.org). Estas y muchas otras bases de datos de cricket se han utilizado para el [análisis de cricket](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) utilizando los últimos algoritmos de aprendizaje automático y modelación predictiva. Las plataformas de medios y entretenimiento, junto con los organismos deportivos profesionales asociados con el juego, utilizan la tecnología y el análisis para determinar métricas clave que mejoren las posibilidades de ganar los partidos:

* promedio móvil del rendimiento de bateo,
* pronóstico del marcador,
* obtener información sobre la condición física y el rendimiento de un jugador contra diferentes oponentes,
* contribución del jugador a las victorias y derrotas para tomar decisiones estratégicas sobre la composición del equipo

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

  IPL has expanded cricket beyond the classic test match format to a much larger scale. The number of matches played every season across various formats has increased and so has the data, the algorithms, newer sports data analysis technologies and simulation models. Cricket data analysis requires field mapping, player tracking, ball tracking, player shot analysis, and several other aspects involved in how the ball is delivered, its angle, spin, velocity, and trajectory. Todos estos factores juntos han incrementado la complejidad de la limpieza de datos y el preprocesamiento.

* **Modelación Dinámica**

  En el cricket, al igual que en cualquier otro deporte, puede haber una gran cantidad de variables relacionadas con el seguimiento de varios jugadores en el campo, sus atributos, la pelota y varias posibilidades de acciones potenciales. The complexity of data analytics and modeling is directly proportional to the kind of predictive questions that are put forth during analysis and are highly dependent on data representation and the model. Las cosas se vuelven aún más desafiantes en términos de cálculo y comparación de datos cuando se buscan predicciones dinámicas del juego de críquet, tal como habría sucedido si el bateador hubiera golpeado la bola a un ángulo o velocidad diferente.

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
