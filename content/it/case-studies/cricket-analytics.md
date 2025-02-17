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

Sarebbe un eufemismo dire che gli Indiani amano il cricket. Lo sport è giocato in praticamente ogni angolo e pertugio dell'India, rurale o urbano che sia, ed è ugualmente popolare tra giovani ed anziani, connettendo miliardi di persone in India più di qualsiasi altro sport. Il Cricket gode di una grande attenzione mediatica. C'è una notevole quantità di [soldi](https://www.statista.com/topics/4543/indian-premier-league-ipl/) e fama in gioco. Nel corso degli ultimi anni, la tecnologia è stata decisamente un punto di svolta. Il pubblico ha l'imbarazzo della scelta tra media in streaming, tornei, accesso a prezzi accessibili per guardare il cricket in diretta dal cellulare e molto altro ancora.

La Premier League Indiana (IPL) è un campionato di cricket professionale in formato Twenty20 fondato nel 2008. Si tratta di uno degli eventi di cricket più seguiti al mondo, valutato per [$6.7 miliardi](https://en.wikipedia.org/wiki/Indian_Premier_League) nel 2019.

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

  La IPL ha ampliato il cricket dal classico formato del match di prova ad una scala molto più ampia. Il numero di partite giocate ogni stagione in vari formati è aumentato e così hanno fatto i dati, gli algoritmi, le più recenti tecnologie di analisi di dati sportivi ed i modelli di simulazione. L'analisi dei dati di Cricket richiede la mappatura del campo, il tracciamento dei giocatori e delle palle, l'analisi delle battute del giocatore e diversi altri aspetti coinvolti nel modo in cui la palla viene lanciata: la sua angolazione, rotazione, velocità e traiettoria. L'insieme di tutti questi fattori ha aumentato la complessità della pulizia e del pretrattamento dei dati.

* **Modellazione Dinamica**

  Nel cricket, proprio come qualsiasi altro sport, ci può essere un gran numero di variabili relative al tracciamento di varie quantità di giocatori sul campo, i loro attributi, la palla e diverse possibilità di potenziali azioni. La complessità dell'analisi dei dati e della modellazione è direttamente proporzionale al tipo di domande predittive che vengono poste durante l'analisi e sono altamente dipendenti dalla rappresentazione dei dati e dal modello. Le cose diventano ancora più impegnative in termini di computazione e dati comparativi quando si cercano previsioni dinamiche sul gioco del cricket, come ad esempio ciò che sarebbe successo se il battitore avesse colpito la palla ad un angolo o velocità diverse.

* **Complessità Dell'Analisi Predittiva**

  Gran parte del processo decisionale nel cricket si basa su domande quali "quanto spesso un battitore colpisce la palla in un certo modo quando questa viene lanciata in una certa maniera", o "come cambia il lanciatore la sua linea e la sua lunghezza se il battitore risponde alla consegna in un certo modo". Questo tipo di questioni di analisi predittiva richiede la disponibilità di set di dati altamente granulari e la capacità di sintetizzare i dati e creare modelli generativi altamente accurati.

## Il Ruolo di NumPy nell'Analisi del Cricket

Le analisi sportive sono un settore fiorente. Molti ricercatori ed aziende [utilizzano NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) ed altri pacchetti di PyData come Scikit-learn, SciPy, Matplotlib e Jupyter, oltre ad utilizzare le più recenti tecniche di machine learning e di AI.  Molti ricercatori ed aziende [utilizzano NumPy](https://adtmag.com/blogs/dev-watch/2017/07/sports-analytics.aspx) ed altri pacchetti di PyData come Scikit-learn, SciPy, Matplotlib e Jupyter, oltre ad utilizzare le più recenti tecniche di machine learning e di AI .

* **Analisi Statistica:** Le capacità numeriche di NumPy aiutano a stimare la significatività statistica dei dati osservazionali o degli eventi di corrispondenza nel contesto di vari giocatori e tattiche di gioco, stimando il risultato di una partita a confronto con un modello generativo o statico. [L'Analisi Causale](https://amplitude.com/blog/2017/01/19/causation-correlation) e [approcci per i big data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996805/) sono utilizzati per l'analisi strategica.

* **Visualizzazione dei Dati:** La grafica dei dati e [visualizzazione](https://towardsdatascience.com/advanced-sports-visualization-with-pandas-matplotlib-and-seaborn-9c16df80a81b) forniscono utili indicazioni sulle relazioni tra i vari insiemi di dati.

## Sommario

L'Analisi Sportiva ha cambiato le carte in tavola per quanto riguarda il modo in cui vengono giocate le partite professionistiche, soprattutto per quanto riguarda il modo in cui vengono prese le decisioni strategiche, che fino a poco tempo fa si basava principalmente sulla “sensazione di pancia” o sull'aderenza alle tradizioni del passato. NumPy costituisce una solida base per un'ampia serie di pacchetti Python che forniscono funzioni di livello superiore legate all'analisi dei dati, al machine learning ed agli algoritmi d'intelligenza artificiale. Questi pacchetti sono ampiamente distribuiti per ottenere informazioni in tempo reale che aiutano nel processo decisionale in grado di cambiare le carte in tavola, sia sul campo che per trarre conclusioni e guidare il business che circonda il gioco del cricket. L'individuazione dei parametri nascosti, modelli, e gli attributi che portano al risultato di una partita di cricket aiutano gli stakeholders a prendere nota delle intuizioni di gioco che sono altrimenti nascoste in numeri e statistiche.

{{< figure >}}
src = '/images/content_images/cs/numpy_ca_benefits.png' alt = 'Diagramma che mostra i benefici dell'uso di NumPy per le analisi del cricket' title = 'Capacità Chiave di NumPy utilizzate'
{{< /figure >}}
