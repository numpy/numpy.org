---
title: "Caso di Studio: Analisi del Cricket, il punto di svolta!"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/ipl-stadium.png' title = 'IPLT20, il più grande Festival del Cricket in India' alt = 'Premier League indiana del Cricket e stadio' attribution = '(Crediti dell'immagine: IPLT20 (torneo e logo) & Akash Yadav (stadio))' attributionlink = 'https://unsplash.com/@aksh1802'
{{< /figure >}}

{{< blockquote cite="https://www.scoopwhoop.com/sports/ms-dhoni/" by="M S Dhoni, *Giocatore Internazionale di Cricket, ex-capitano, Squadra Indiana, gioca per i Chennai Super Kings nel IPL*"
> }} Non giochi per la folla, giochi per il paese. 
> 
> {{< /blockquote >}}

## Riguardo al Cricket

It would be an understatement to state that Indians love cricket. Lo sport è giocato in praticamente ogni angolo e pertugio dell'India, rurale o urbano che sia, ed è ugualmente popolare tra giovani ed anziani, connettendo miliardi di persone in India più di qualsiasi altro sport. Il Cricket gode di una grande attenzione mediatica. C'è una notevole quantità di [soldi](https://www.statista.com/topics/4543/indian-premier-league-ipl/) e fama in gioco. Nel corso degli ultimi anni, la tecnologia è stata decisamente un punto di svolta. Il pubblico ha l'imbarazzo della scelta tra media in streaming, tornei, accesso a prezzi accessibili per guardare il cricket in diretta dal cellulare e molto altro ancora.

La Premier League Indiana (IPL) è un campionato di cricket professionale in formato Twenty20 fondato nel 2008. It is one of the most attended cricketing events in the world, valued at [$6.7 billion](https://en.wikipedia.org/wiki/Indian_Premier_League) in 2019.

Il cricket è un gioco di numeri: i punti segnati da un battitore, le eliminazioni effettuate da un lanciatore, le partite vinte da una squadra di cricket, il numero di volte in cui un battitore risponde in un determinato modo a un tipo di lancio, ecc. La possibilità di investigare tra i numeri del cricket sia per migliorare le prestazioni che per studiare le opportunità commerciali, il mercato complessivo o l'economia del gioco attraverso potenti strumenti di analisi, alimentati da software di calcolo numerico come NumPy, è una grossa questione. L'analisi del Cricket fornisce approfondimenti interessanti riguardanti il gioco e predizioni intelligenti dei risultati delle partite.

Oggi sono disponibili serie ricche e quasi infinite di dati e statistiche sulle partite di cricket, come ad esempio [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html)  e [cricsheet](https://cricsheet.org). Oggi sono disponibili serie ricche e quasi infinite di dati e statistiche sulle partite di cricket, come ad esempio [ESPN cricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html)  e [cricsheet](https://cricsheet.org). Le piattaforme di media e intrattenimento, insieme ad enti sportivi professionali associati al gioco, utilizzano la tecnologia e l'analisi per determinare le metriche chiave per migliorare le possibilità di vittoria delle partite:

* media mobile delle prestazioni di battuta,
* previsione del punteggio,
* ottenere informazioni sulla forma fisica e sulle prestazioni di un giocatore contro avversari diversi,
* contributo dei giocatori alle vittorie e alle sconfitte per prendere decisioni strategiche sulla composizione della squadra

{{< figure >}}
src = '/images/content_images/cs/cricket-pitch.png' title = 'Il Cricket Pitch, punto focale del campo' alt = 'Un cricket pitch con un lanciatore e battitore' align = 'center' attribution = '(Crediti dell'immagine: Debarghya Das)' attributionlink = 'http://debarghyadas.com/files/IPLpaper.pdf'
{{< /figure >}}

### Obiettivi Principali Dell'Analisi Dati

* L'analisi dei dati sportivi viene utilizzata non solo nel cricket ma anche in molti  [altri sport ](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) per migliorare le prestazioni complessive della squadra e massimizzare le possibilità di vittoria.
* L'analisi dei dati in tempo reale può aiutare ad ottenere informazioni anche durante la partita stessa per modificare le tattiche della squadra e delle aziende associate per ottenere vantaggi economici e di crescita.
* Oltre all'analisi storica, i modelli predittivi vengono sfruttati per determinare i possibili risultati delle partite, che richiedono una notevole quantità di numeri e conoscenze di scienza dei dati, strumenti di visualizzazione e la capacità di includere nuove osservazioni nell'analisi.

{{< figure >}}
src = '/images/content_images/cs/player-pose-estimator.png' alt = 'stimatore della posa' title = 'Stimatore della Posa nel Cricket' attribution = '(Crediti dell'immagine: connect.vin)' attributionlink = 'https://connect.vin/2019/05/ai-for-cricket-batsman-pose-analysis/'
{{< /figure >}}

### Le Sfide

* **Pulizia e pretrattamento dei dati**

  IPL has expanded cricket beyond the classic test match format to a much larger scale. The number of matches played every season across various formats has increased and so has the data, the algorithms, newer sports data analysis technologies and simulation models. Cricket data analysis requires field mapping, player tracking, ball tracking, player shot analysis, and several other aspects involved in how the ball is delivered, its angle, spin, velocity, and trajectory. All these factors together have increased the complexity of data cleaning and preprocessing.

* **Dynamic Modeling**

  In cricket, just like any other sport, there can be a large number of variables related to tracking various numbers of players on the field, their attributes, the ball, and several possibilities of potential actions. The complexity of data analytics and modeling is directly proportional to the kind of predictive questions that are put forth during analysis and are highly dependent on data representation and the model. Things get even more challenging in terms of computation, data comparisons when dynamic cricket play predictions are sought such as what would have happened if the batsman had hit the ball at a different angle or velocity.

* **Predictive Analytics Complexity**

  Much of the decision making in cricket is based on questions such as "how often does a batsman play a certain kind of shot if the ball delivery is of a particular type", or "how does a bowler change his line and length if the batsman responds to his delivery in a certain way". This kind of predictive analytics query requires highly granular dataset availability and the capability to synthesize data and create generative models that are highly accurate.

## NumPy’s Role in Cricket Analytics

Sports Analytics is a thriving field. Many researchers and companies [use NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) and other PyData packages like Scikit-learn, SciPy, Matplotlib, and Jupyter, besides using the latest machine learning and AI techniques.  NumPy has been used for various kinds of cricket related sporting analytics such as:

* **Statistical Analysis:** NumPy's numerical capabilities help estimate the statistical significance of observational data or match events in the context of various player and game tactics, estimating the game outcome by comparison with a generative or static model. [Causal analysis](https://amplitude.com/blog/2017/01/19/causation-correlation) and [big data approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) are used for tactical analysis.

* **Data Visualization:** Data graphing and [visualization](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) provide useful insights into relationship between various datasets.

## Summary

Sports Analytics is a game changer when it comes to how professional games are played, especially how strategic decision making happens, which until recently was primarily done based on “gut feeling" or adherence to past traditions. NumPy forms a solid foundation for a large set of Python packages which provide higher level functions related to data analytics, machine learning, and AI algorithms. These packages are widely deployed to gain real-time insights that help in decision making for game-changing outcomes, both on field as well as to draw inferences and drive business around the game of cricket. Finding out the hidden parameters, patterns, and attributes that lead to the outcome of a cricket match helps the stakeholders to take notice of game insights that are otherwise hidden in numbers and statistics.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png' alt = 'Diagram showing benefits of using NumPy for cricket analytics' title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
