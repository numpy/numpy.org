---
title: "Estudio de caso: Análisis de críquet, ¡el cambio radical!"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/ipl-stadium.png'
title = 'IPLT20, el festival de críquet más grande en India'
alt = 'Copa y estadio de la Premier League de Críquet de India'
attribution = '(Créditos de imagen: IPLT20 (copa y logo) & Akash Yadav (estadio))'
attributionlink = 'https://unsplash.com/@aksh1802'
{{< /figure >}}

{{< blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/" by="M S Dhoni, _Jugador Internacional de críquet, ex-capitán del equipo de India, juega para Chennai Super Kings en IPL_"

> }} No juegas para el público, juegas para el país.
> {{< /blockquote >}}

## Acerca del críquet

Sería una subestimación decir que a los indios les encanta el críquet. El juego se juega en casi cada rincón de India, rural o urbano, popular entre los jóvenes y ancianos por igual, conectando miles de millones en India a diferencia de cualquier otro deporte.
El críquet disfruta de una gran atención mediática. Hay una cantidad importante de [dinero](https://www.statista.com/topics/4543/indian-premier-league-ipl/) y fama en juego. Durante los últimos años, la tecnología ha sido literalmente un punto de inflexión. El público está plagado de opciones con los medios de streaming, los torneos, acceso asequible a la observación de críquet en vivo basado en móviles, y más.

La Premier League de India (IPL) es una liga de críquet Twenty20, fundada en 2008. Es uno de los eventos de críquet más concurridos en el mundo, valorado en [$6.7 mil millones de dólares](https://en.wikipedia.org/wiki/Indian_Premier_League) en 2019.

El críquet es un juego de números - las carreras anotadas por un bateador, los wickets alcanzados por un lanzador, los partidos ganados por un equipo de críquet, el número de veces que un bateador responde de cierta manera a un tipo de ataque de lanzamiento, etc. La capacidad de cavar en los números del críquet para mejorar el rendimiento y estudiar las oportunidades de negocio, el mercado en general y la economía del críquet a través de potentes herramientas de análisis, alimentadas por software de cálculo numérico como NumPy, es un gran negocio. El análisis del críquet proporciona ideas interesantes sobre el juego e inteligencia predictiva respecto a los resultados del juego.

Hoy en día, hay abundantes y casi infinitos tesoros de registros y estadísticas de juegos de críquet disponibles, por ejemplo, en [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) y [cricsheet](https://cricsheet.org). Estas y muchas otras bases de datos de cricket se han utilizado para el [análisis de cricket](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) utilizando los últimos algoritmos de aprendizaje automático y modelación predictiva.
Las plataformas de medios y entretenimiento, junto con organismos deportivos profesionales asociados con el juego, utilizan la tecnología y el análisis para determinar métricas clave para mejorar las posibilidades de ganar un partido:

- promedio móvil del rendimiento de bateo,
- previsión del marcador,
- obtener información sobre la forma física y el rendimiento de un jugador contra diferentes rivales,
- contribución del jugador a las victorias y derrotas para tomar decisiones estratégicas en la composición del equipo

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png'
title = 'El campo de críquet, el punto focal en el terreno de juego'
alt = 'Un campo de cricket con lanzador y bateadores'
align = 'center'
attribution = '(Image credit: Debarghya Das)'
attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### Objetivos de análisis de datos clave

- El análisis de datos deportivos se utiliza no solo en el críquet, sino en muchos [otros deportes](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) para mejorar el rendimiento general del equipo y maximizar las posibilidades de ganar.
- El análisis de datos en tiempo real puede ayudar a obtener información incluso durante el juego para cambiar tácticas por parte del equipo y de las empresas asociadas para beneficios económicos y crecimiento.
- Además del análisis histórico, se aprovechan los modelos predictivos para determinar los posibles resultados de los partidos, lo cual requiere una cantidad significativa de procesamiento de datos y conocimientos de ciencia de datos, herramientas de visualización y la capacidad de incluir nuevas observaciones en el análisis.

{{< figure >}}
src = '/images/content_images/cs/player-pose-estimator.png'
alt = 'estimador de postura'
title = 'Estimador de postura en críquet'
attribution = '(Crédito de imagen: connect.vin)'
attributionlink = 'https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/'
{{< /figure >}}

### Los desafíos

- **Limpieza de datos y preprocesamiento**

  La IPL ha expandido el críquet más allá del clásico formato de partido de prueba a una escala mucho más grande. El número de partidos jugados cada temporada a través de varios formatos ha incrementado y así también los datos, los algoritmos, las nuevas tecnologías de análisis de datos deportivos y modelos de simulación. El análisis de datos de críquet requiere mapeo del campo, seguimiento de jugadores, seguimiento de la pelota, análisis de tiros de los jugadores y varios otros aspectos relacionados con cómo se lanza la pelota, su ángulo, giro, velocidad y trayectoria. Todos estos factores juntos han incrementado la complejidad de la limpieza de datos y el preprocesamiento.

- **Modelación Dinámica**

  En el cricket, al igual que en cualquier otro deporte, puede haber una gran cantidad de variables relacionadas con el seguimiento de varios jugadores en el campo, sus atributos, la pelota y varias posibilidades de acciones potenciales. La complejidad del análisis de datos y la modelación es directamente proporcional al tipo de preguntas predictivas que se plantean durante el análisis y depende en gran medida de la representación de los datos y del modelo. Las cosas se vuelven aún más desafiantes en términos de cálculo y comparación de datos cuando se buscan predicciones dinámicas del juego de críquet, tal como habría sucedido si el bateador hubiera golpeado la bola a un ángulo o velocidad diferente.

- **Complejidad de Análisis Predictivo**

  Gran parte de la toma de decisiones en el críquet se basa en preguntas como "¿con qué frecuencia un bateador juega un cierto tipo de golpe si la entrega de la pelota es de un tipo particular?" o "¿cómo cambia un lanzador su línea y longitud si el bateador responde a su entrega de una cierta manera?".
  Este tipo de consulta de análisis predictivo requiere una disponibilidad de un conjunto de datos altamente granular y la capacidad de sintetizar datos y crear modelos generativos que sean altamente precisos.

## El rol de NumPy en el análisis del críquet

El análisis deportivo es un campo en desarrollo. Muchos investigadores y compañías [utilizan NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) y otros paquetes de PyData como Scikit-learn, SciPy, Matplotlib y Jupyter, además de utilizar las últimas técnicas de aprendizaje automático e inteligencia artificial.  NumPy se ha utilizado para varios tipos de análisis deportivos relacionados con el críquet como:

- **Análisis Estadístico:** Las capacidades numéricas de NumPy ayudan a estimar la significancia estadística de los datos observacionales o de eventos de partidos en el contexto de varias tácticas de jugadores y de juego, estimando el resultado del juego mediante la comparación con un modelo generativo o estático.
  El [análisis causal](https://amplitude.com/blog/2017/01/19/causation-correlation) y los [enfoques de big data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) se utilizan para el análisis táctico.

- **Visualización de Datos:** La creación de gráficos y la [visualización de datos](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) proporcionan información útil sobre la relación entre varios conjuntos de datos.

## Resumen

El análisis deportivo es un cambio radical cuando se trata de cómo se juegan los juegos profesionales, especialmente cómo ocurre la toma de decisiones estratégicas, que hasta hace poco se hacía basado principalmente en el presentimiento o adherencia a las tradiciones del pasado. NumPy forma una base sólida para un gran conjunto de paquetes de Python que proporcionan funciones de más alto nivel relacionadas con el análisis de datos, el aprendizaje automático y los algoritmos de inteligencia artificial.
Estos paquetes están ampliamente desplegados para obtener información en tiempo real que ayudan en la toma de decisiones para resultados que cambian el juego, tanto en el campo como para sacar conclusiones y hacer negocios alrededor del juego del críquet. Encontrar los parámetros ocultos, patrones y atributos que conducen al resultado de un partido de críquet ayuda a los interesados a tomar nota de la información del juego que de otra forma estarían ocultos en números y estadísticas.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png'
alt = 'Diagrama que muestra los beneficios de usar NumPy para análisis de críquet'
title = 'Capacidades claves de NumPy utilizadas'
{{< /figure >}}
