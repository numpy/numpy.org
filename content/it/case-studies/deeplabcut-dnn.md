---
title: "Caso Di Studio: Stima della Posa con DeepLabCut 3D"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/mice-hand.gif' title = 'Analisi del movimento di zampa dei topi usando DeepLapCut' alt = 'micehandanim' attribution = '(Source: www.deeplabcut.org )' attributionlink = 'http://www.mousemotorlab.org/deeplabcut'
{{< /figure >}}

{{< blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/" by="Alexander Mathis, *Professore Assistente, École polytechnique fédérale de Lausanne* ([EPFL](https://www.epfl.ch/en/))"
> }} I Software Open Source stanno accelerando il campo della Biomedicina. DeepLabCut consente l'analisi video automatizzata del comportamento animale utilizzando il Deep Learning. 
> 
> {{< /blockquote >}}

## Riguardo DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) è un'insieme di strumenti open source che consente ai ricercatori di centinaia di istituzioni in tutto il mondo di tracciare il comportamento degli animali da laboratorio con pochissimi dati di addestramento e con una precisione pari a quella umana. Con la tecnologia DeepLabCut, gli scienziati possono approfondire la comprensione scientifica del controllo motorio e del comportamento in tutte le specie animali ed in tutti i lassi di tempo.

Diversi settori di ricerca, tra cui neuroscienza, medicina e biomeccanica, utilizzano i dati di monitoraggio del movimento degli animali. DeepLabCut aiuta a capire ciò che gli esseri umani e gli altri animali stanno facendo analizzando le azioni che sono state registrate su pellicola. Utilizzando l'automazione per le laboriose attività di etichettatura e monitoraggio, insieme all'analisi dei dati basata su reti neurali profonde, DeepLabCut rende molto più veloci e accurati gli studi scientifici che prevedono l'osservazione di animali quali primati, topi, pesci, mosche, ecc.

{{< figure >}}
src = '/images/content_images/cs/race-horse.gif' title = 'Punti colorati tracciano le posizioni delle parti del corpo di un cavallo da corsa' alt = 'horserideranim' attribution = '(Source: Mackenzie Mathis)'
{{< /figure >}}

Il tracciamento comportamentale non invasivo di animali da parte di DeepLabCut, attraverso l'estrazione delle pose degli animali, è fondamentale per le attività scientifiche in settori quali la biomeccanica, la genetica, l'etologia e le neuroscienze. Misurare le pose degli animali in modo non invasivo da un video - senza marcatori - su sfondi che cambiano dinamicamente è una sfida computazionale, sia dal punto di vista tecnico che da quello delle risorse necessarie e dei dati di addestramento richiesti.

DeepLabCut permette ai ricercatori di stimare la posa del soggetto, consentendo loro di quantificare in modo efficiente il comportamento attraverso un insieme di strumenti software basato su Python.  Con DeepLabCut, i ricercatori possono identificare fotogrammi distinti di video, etichettare digitalmente parti del corpo specifiche in poche decine di fotogrammi con un'interfaccia grafica personalizzata; dopodiché le architetture di stima della posa basate sull'apprendimento profondo di DeepLabCut imparano a individuare quelle stesse caratteristiche nel resto del video e in altri video simili di animali. Funziona su tutte le specie di animali, dai comuni animali da laboratorio come mosche e topi ad animali più insoliti come  [ghepardi][cheetah-movement].

Funziona su tutte le specie di animali, dai comuni animali da laboratorio come mosche e topi ad animali più insoliti come  [ghepardi][cheetah-movement].  A seconda delle esigenze, gli utenti possono scegliere diverse architetture di rete che forniscono un'inferenza più rapida (ad esempio, MobileNetV2), che può anche essere combinata con un feedback sperimentale in tempo reale. DeepLabCut all'inizio utilizzava rilevatori di caratteristiche dell'architettura di stima della posa umana dalle prestazioni eccellenti, chiamata  [DeeperCut](https://arxiv.org/abs/1605.03170), che ha ispirato il nome. Il pacchetto è stato ora modificato in modo significativo per includere architetture aggiuntive, metodi di incremento e un'esperienza d'interazione con l'utente completa. Inoltre, per supportare esperimenti biologici su larga scala, DeepLabCut offre funzionalità di apprendimento attivo che consentono agli utenti di aumentare il set di addestramento nel tempo per coprire i casi limite e rendere l'algoritmo di stima della posa robusto all'interno del contesto specifico.

Recentemente è stato introdotto lo  [zoo di DeepLabCut](https://deeplabcut.github.io/DeepLabCut/docs/ModelZoo.html), che fornisce modelli pre-addestrati per varie specie e condizioni sperimentali, dall'analisi facciale nei primati alla postura dei cani. Questo può essere eseguito, ad esempio, nel cloud senza etichettatura di nuovi dati o addestramento di reti neurali, e non è necessaria alcuna esperienza di programmazione.

### Obiettivi Principali e Risultati

* **Automazione dell'analisi della posa animale per studi scientifici:**

  L'obiettivo primario della tecnologia DeepLabCut è quello di misurare e tracciare la postura di animali in ambienti diversi. Questi dati possono essere utilizzati, ad esempio, negli studi di neuroscienze per capire come il cervello controlla il movimento o per come gli animali interagiscono socialmente. I ricercatori hanno osservato un [ miglioramento delle prestazioni 10 volte superiore](https://www.biorxiv.org/content/10.1101/457242v1) con DeepLabCut. Le pose possono essere dedotte offline fino a 1200 fotogrammi al secondo (FPS).

* **Creazione di un insieme di strumenti Python facile da usare per la stima delle pose:**

  DeepLabCut ha voluto condividere la propria tecnologia di stima della posa degli animali sotto forma di uno strumento di facile utilizzo che potesse essere adottato facilmente dai ricercatori. Per questo hanno creato un pacchetto di strumenti Python completo e facile da usare, con tanto di funzioni per la gestione dei progetti. Questi permettono non solo di automatizzare la stima della posa, ma anche di gestire il progetto dall'inizio alla fine, aiutando l'utente di DeepLabCut Toolkit dalla fase di raccolta dei dati alla creazione di pipeline di analisi condivisibili e riutilizzabili.

  Il loro [toolkit][DLCToolkit] è ora disponibile come open source.

  Un tipico flusso di lavoro con DeepLabCut comprende:

  - la creazione ed il perfezionamento di gruppi di formazione attraverso l'apprendimento attivo
  - la creazione di reti neurali su misura per animali e scenari specifici
  - un codice per l'inferenza su larga scala per video
  - rappresentazione di inferenze utilizzando strumenti di visualizzazione integrati

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png' title = 'Fasi di stima della posa con DeepLabCut' alt = 'dlcsteps' align = 'center' attribution = '(Sorgente: DeepLabCut)' attributionlink = 'https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1'
{{< /figure >}}

### Le Sfide

* **Velocità**

    L'elaborazione rapida dei video del comportamento animale permette di misurarlo con precisione, rendendo al contempo gli esperimenti scientifici più efficienti e accurati. Misurare le pose degli animali in modo non invasivo da un video - senza marcatori - su sfondi che cambiano dinamicamente è una sfida computazionale, sia dal punto di vista tecnico che da quello delle risorse necessarie e dei dati di addestramento richiesti. Fornire uno strumento facile da usare, senza richiedere competenze specifiche come esperienza in visualizzazione computazionale, e che permetta agli scienziati di condurre ricerche in diversi contesti reali, è un problema non banale da risolvere.

* **Combinatoria**

    Il calcolo combinatorio prevede l'assemblaggio e l'integrazione del movimento di più arti in un comportamento individuale dell'animale. Assemblare i punti chiave, le loro connessioni nei singoli movimenti degli animali e collegarli nel tempo è un processo complesso che richiede un'analisi numerica impegnativa, soprattutto nel caso di tracciamento dei movimenti di più animali in video di esperimenti.

* **Trattamento dei Dati**

    Ultimo, ma non meno importante, la manipolazione degli arrays - l'elaborazione di grandi pile di vettori corrispondenti a varie immagini, tensori di destinazione e punti chiave, è piuttosto impegnativo.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png' title = 'Varietà e complessità della stima della posa' alt = 'challengesfig' align = 'center' attribution = '(Sorgente: Mackenzie Mathis)' attributionlink = 'https://www.biorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## Il Ruolo di NumPy verso le Sfide di Stima della Posa

NumPy affronta la necessità principale della tecnologia DeepLabCut di calcoli numerici ad alta velocità per l'analisi comportamentale.  Oltre a NumPy, DeepLabCut impiega vari software Python che utilizzano NumPy al loro centro, come [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/) [scikit-image](https://scikit-image.org) e [Tensorflow](https://www.tensorflow.org).

Le seguenti caratteristiche di NumPy hanno svolto un ruolo fondamentale nel risolvere i requisiti di elaborazione delle immagini, di combinatoria e di velocità di calcolo degli algoritmi di stima della posa di DeepLabCut:

* Vettorizzazione
* Operazioni con Arrays Mascherati
* Algebra Lineare
* Campionamento Casuale
* Riarrangiamento di arrays di grandi dimensioni

DeepLabCut utilizza le capacità di array di NumPy durante il flusso di lavoro offerto dal toolkit. In particolare, NumPy viene utilizzato per il campionamento di frame distinti per l'etichettatura dell'annotazione umana e per scrivere, modificare ed elaborare i dati di annotazione.  All'interno di TensorFlow, la rete neurale è addestrata dalla tecnologia DeepLabCut sopra migliaia di iterazioni per prevedere le annotazioni di verità fondamentali dai frames. A questo scopo, le densità obiettivo (scoremap) sono create per lanciare la stima di posa come un problema di traduzione da immagine ad immagine. Per rendere le reti neurali robuste, si ricorre all'aumento dei dati, che richiede il calcolo di scoremap del bersaglio soggetto in varie fasi di elaborazione geometrica e dell'immagine. Per rendere veloce l'addestramento, le capacità di vettorializzazione di NumPy vengono sfruttate. Per l'inferenza, le previsioni più probabili dalle scoremap di destinazione devono essere estratte e bisogna “collegare in modo efficiente le predizioni per assemblare i singoli animali”.

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png' title = 'Flusso di lavoro in DeepLabCut' alt = 'workflow' attribution = '(Sorgente: Mackenzie Mathis)' attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## Sommario

Osservare e descrivere in modo efficiente il comportamento è un principio fondamentale dell'etologia moderna, delle neuroscienze, della medicina e della tecnologia. [DeepLabCut](https://static1.squarespace.com/static/57f6d51c9f74566f55ecf271/t/5eab5ff7999bf94756b27481/1588289532243/NathMathis2019.pdf) permette ai ricercatori di stimare la posa del soggetto, consentendo in modo efficiente di di quantificare il comportamento. Con solo un piccolo insieme di immagini di addestramento, l'insieme di strumenti Python di DeepLabCut permette di addestrare una rete neurale con un'accuratezza di etichettatura al pari del livello umano, espandendo così la sua applicazione non solo all'analisi del comportamento in laboratorio, ma potenzialmente anche nello sport, nell'analisi dell'andatura e negli studi di medicina e riabilitazione. Le complesse sfide di calcolo combinatorio e di elaborazione dei dati riscontrate dagli algoritmi di DeepLabCut vengono affrontate attraverso l'uso delle capacità di NumPy di manipolazione degli array.

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png' alt = 'numpy benefits' title = 'Capacità Chiave di NumPy utilizzate'
{{< /figure >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
