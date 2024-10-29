---
title: "Estudo de Caso: Análise de Críquete, a revolução!"
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

## Sobre Críquete

Dizer que os indianos adoram o críquete seria subestimar este sentimento. O jogo é jogado praticamente em todas as localidades da Índia, rurais ou urbanas, e é popular com os jovens e os anciões, conectando bilhões de pessoas na Índia como nenhum outro esporte.
O críquete também recebe muita atenção da mídia. There is a significant amount of
[money](https://www.statista.com/topics/4543/indian-premier-league-ipl/) and
fame at stake. Ao longo dos últimos anos, a tecnologia foi literalmente uma revolução. As audiências tem uma ampla possibilidade de escolha, com mídias de streaming, torneios, acesso barato a jogos de críquete ao vivo em dispositivos móveis, e mais.

A Primeira Liga Indiana (<em x-id="3">Indian Premier League</em> - IPL) é uma liga profissional de críquete <a href="https://pt.wikipedia.org/wiki/Twenty20">Twenty20</a>, fundada em 2008. It is one of the most attended cricketing events in
the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League)
in 2019.

Críquete é um jogo dominado pelos números - as corridas executadas por um <en>batsman</en>, os <en>wickets</en> perdidos por um boleador, as partidas ganhas por uma equipe de críquete, o número de vezes que um batsman responde de certa maneira a um tipo de arremesso do boleador, etc. A capacidade de investigar números de críquete para melhorar o desempenho e estudar as oportunidades de negócio, mercado e economia de críquete através de poderosas ferramentas de análise, alimentadas por softwares numéricos de computação, como o NumPy, é um grande negócio. As análises de críquete fornecem informações interessantes sobre o jogo e informações preditivas sobre os resultados do jogo.

Today, there are rich and almost infinite troves of cricket game records and
statistics available, e.g., ESPN
cricinfo and
[cricsheet](https://cricsheet.org). These and several such cricket databases
have been used for cricket
analysis
using the latest machine learning and predictive modelling algorithms.
Plataformas de mídia e entretenimento, juntamente com entidades de esporte profissionais associadas ao jogo usam tecnologia e análise para determinar métricas chave para melhorar as chances de vitória:

- média móvel do desempenho em rebatidas,
- previsão de pontuação,
- ganho de informações sobre desempenho e condição física de um determinado jogador contra determinado adversário,
- contribuições dos jogadores para vitórias e derrotas para a tomada de decisões estratégicas na composição do time

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png'
title = 'Cricket Pitch, the focal point in the field'
alt = 'A cricket pitch with bowler and batsmen'
align = 'center'
attribution = '(Image credit: Debarghya Das)'
attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### Objetivos Principais da Análise de Dados

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

### Desafios

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

## Papel do NumPy na Análise de Críquete

A análise de dados esportivos é um campo próspero. Many researchers and companies
[use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx)
and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter,
besides using the latest machine learning and AI techniques.  O NumPy foi usado para vários tipos de análise esportiva relacionada a críquete, como:

- **Statistical Analysis:** NumPy's numerical capabilities help estimate the
  statistical significance of observational data or match events in the context
  of various player and game tactics, estimating the game outcome by comparison
  with a generative or static model.
  [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation)
  and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/)
  are used for tactical analysis.

- **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provide useful insights into relationship between various datasets.

## Resumo

A análise de dados esportivos é revolucionária quando se trata de como os jogos profissionais são jogados, especialmente se consideramos como acontece a tomada de decisões estratégicas, que até pouco tempo era principalmente feita com base na "intuição" ou adesão a tradições passadas. O NumPy forma uma fundação sólida para um grande conjunto de pacotes Python que fornecem funções de alto nível relacionadas à análise de dados, aprendizagem de máquina e algoritmos de IA.
Estes pacotes são amplamente implantados para se obter informações em tempo real que ajudam na tomada de decisão para resultados decisivos, tanto em campo como para se derivar inferências e orientar negócios em torno do jogo de críquete. Encontrar os parâmetros ocultos, padrões, e atributos que levam ao resultado de uma partida de críquete ajuda os envolvidos a tomar nota das percepções do jogo que estariam de outra forma ocultas nos números e estatísticas.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png'
alt = 'Diagram showing benefits of using NumPy for cricket analytics'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
