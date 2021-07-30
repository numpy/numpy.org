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

A Primeira Liga Indiana (*Indian Premier League* - IPL) é uma liga profissional de críquete [Twenty20](https://pt.wikipedia.org/wiki/Twenty20), fundada em 2008. É um dos eventos de críquete mais assistidos no mundo, avaliado em [$6,7 bilhões de dólares](https://en.wikipedia.org/wiki/Indian_Premier_League) em 2019.

Críquete é um jogo dominado pelos números - as corridas executadas por um <en>batsman</en>, os <en>wickets</en> perdidos por um boleador, as partidas ganhas por uma equipe de críquete, o número de vezes que um batsman responde de certa maneira a um tipo de arremesso do boleador, etc. A capacidade de investigar números de críquete para melhorar o desempenho e estudar as oportunidades de negócio, mercado e economia de críquete através de poderosas ferramentas de análise, alimentadas por softwares numéricos de computação, como o NumPy, é um grande negócio. As análises de críquete fornecem informações interessantes sobre o jogo e informações preditivas sobre os resultados do jogo.

Hoje, existem conjuntos ricos e quase infinitos de estatísticas e informações sobre jogos de críquete, por exemplo, [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html) e [cricsheet](https://cricsheet.org). Estes e muitos outros bancos de dados de críquete foram usados para [análise de críquete](https://www.researchgate.net/publication/336886516_Data_visualization_and_toss_related_analysis_of_IPL_teams_and_batsmen_performances) usando os mais modernos algoritmos de aprendizagem de máquina e modelagem preditiva. Plataformas de mídia e entretenimento, juntamente com entidades de esporte profissionais associadas ao jogo usam tecnologia e análise para determinar métricas chave para melhorar as chances de vitória:

* média móvel do desempenho em rebatidas,
* previsão de pontuação,
* ganho de informações sobre desempenho e condição física de um determinado jogador contra determinado adversário,
* contribuições dos jogadores para vitórias e derrotas para a tomada de decisões estratégicas na composição do time

{{< figure src="/images/content_images/cs/cricket-pitch.png" class="csfigcaption" caption="**Pitch de críquete, o ponto focal do campo**" alt="Um pitch de críquete com um boleador e batsmen" align="middle" attr="*(Créditos de imagem: Debarghya Das)*" attrlink="http://debarghyadas.com/files/IPLpaper.pdf" >}}

### Objetivos Principais da Análise de Dados

* A análise de dados esportivos é usada não somente em críquete, mas em muitos [outros esportes](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) para melhorar o desempenho geral da equipe e maximizar as chances de vitória.
* A análise de dados em tempo real pode ajudar a obtenção de informações mesmo durante o jogo para orientar mudanças nas táticas da equipe e dos negócios associados para benefícios e crescimento econômicos.
* Além da análise histórica, os modelos preditivos explorados para determinar os possíveis resultados das partidas requerem um conhecimento significativo sobre processamento numérico e ciência de dados, ferramentas de visualização e a possibilidade de incluir observações mais recentes na análise.

{{< figure src="/images/content_images/cs/player-pose-estimator.png" class="fig-center" alt="estimador de postura" caption="**Estimador de Postura de Críquete**" attr="*(Créditos de imagem: connect.vin)*" attrlink="https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/" >}}

### Desafios

* **Limpeza e pré-processamento de dados**

  A IPL expandiu o formato de jogo clássico de cricket para uma escala muito maior. O número de partidas jogadas a cada temporada em vários formatos tem aumentado, assim como os dados, os algoritmos, as tecnologias de análise de dados mais recentes e modelos de simulação. A análise de dados de críquete requer mapeamento de campo, rastreamento do jogador, rastreamento de bola e análise de tiros do jogador, análise de lances do jogador e vários outros aspectos envolvidos em como a bola é lançada, seu ângulo, giro, velocidade e trajetória. Todos esses fatores em conjunto aumentaram a complexidade da limpeza e pré-processamento de dados.

* **Modelagem Dinâmica**

  No críquete, como em qualquer outro esporte, pode haver um grande número de variáveis relacionadas ao rastreamento de vários jogadores no campo, seus atributos, a bola e várias possibilidades de ações em potencial. A complexidade da análise e modelagem de dados é diretamente proporcional ao tipo de questões preditivas que são consideradas durante a análise e são altamente dependentes da representação de dados e do modelo. As coisas são ainda mais desafiadoras em termos de computação e comparações de dados quando previsões dinâmicas de jogo de críquete são desejadas, como o que teria acontecido se o batsman tivesse atingido a bola com um ângulo ou velocidade diferentes.

* **Complexidade da análise preditiva**

  Muito da tomada de decisões em críquete se baseia em questões como "com que frequência um batsman joga um certo tipo de lance se a recepção da bola for de um determinado tipo", ou "como um boleador muda a direção e alcance da sua jogada se o batsman responder de uma certa maneira". Esse tipo de consulta de análise preditiva requer a disponibilidade de conjuntos de dados altamente granulares e a capacidade de sintetizar dados e criar modelos generativos que sejam altamente precisos.

## Papel da NumPy na Análise de Críquete

A análise de dados esportivos é um campo próspero. Muitos pesquisadores e empresas [usam NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) e outros pacotes PyData como Scikit-learn, SciPy, Matplotlib, e Jupyter, além de usar as últimas técnicas de aprendizagem de máquina e IA.  O NumPy foi usado para vários tipos de análise esportiva relacionada a críquete, como:

* **Análise Estatística:** Os recursos numéricos do NumPy ajudam a estimar o significado estatístico de dados observados ou de eventos ocorridos em partidas no contexto de vários jogadores e táticas de jogo, bem como estimar o resultado do jogo em comparação com um modelo generativo ou estático. [Análise Causal](https://amplitude.com/blog/2017/01/19/causation-correlation) e [abordagens em *big data*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) são usados para análise tática.

* **Visualização de dados:** Gráficos e [visualizações](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) fornecem informações úteis sobre as relações entre vários conjuntos de dados.

## Resumo

A análise de dados esportivos é revolucionária quando se trata de como os jogos profissionais são jogados, especialmente se consideramos como acontece a tomada de decisões estratégicas, que até pouco tempo era principalmente feita com base na "intuição" ou adesão a tradições passadas. O NumPy forma uma fundação sólida para um grande conjunto de pacotes Python que fornecem funções de alto nível relacionadas à análise de dados, aprendizagem de máquina e algoritmos de IA. Estes pacotes são amplamente implantados para se obter informações em tempo real que ajudam na tomada de decisão para resultados decisivos, tanto em campo como para se derivar inferências e orientar negócios em torno do jogo de críquete. Encontrar os parâmetros ocultos, padrões, e atributos que levam ao resultado de uma partida de críquete ajuda os envolvidos a tomar nota das percepções do jogo que estariam de outra forma ocultas nos números e estatísticas.

{{< figure src="/images/content_images/cs/numpy_ca_benefits.png" class="fig-center" alt="Diagrama mostrando os benefícios de usar a NumPy para análise de críquete" caption="**Recursos principais da NumPy utilizados**" >}}
