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

    L'elaborazione rapida dei video del comportamento animale permette di misurarlo con precisione, rendendo al contempo gli esperimenti scientifici più efficienti e accurati. Extracting detailed animal poses for laboratory experiments, without markers, in dynamically changing backgrounds, can be challenging, both technically as well as in terms of resource needs and training data required. Coming up with a tool that is easy to use without the need for skills such as computer vision expertise that enables scientists to do research in more real-world contexts, is a non-trivial problem to solve.

* **Combinatorics**

    Combinatorics involves assembly and integration of movement of multiple limbs into individual animal behavior. Assembling keypoints and their connections into individual animal movements and linking them across time is a complex process that requires heavy-duty numerical analysis, especially in case of multi-animal movement tracking in experiment videos.

* **Data Processing**

    Last but not the least, array manipulation - processing large stacks of arrays corresponding to various images, target tensors and keypoints is fairly challenging.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png' title = 'Pose estimation variety and complexity' alt = 'challengesfig' align = 'center' attribution = '(Source: Mackenzie Mathis)' attributionlink = 'https://www.biorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## NumPy's Role in meeting Pose Estimation Challenges

NumPy addresses DeepLabCut technology's core need of numerical computations at high speed for behavioural analytics.  Besides NumPy, DeepLabCut employs various Python software that utilize NumPy at their core, such as [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) and [Tensorflow](https://www.tensorflow.org).

The following features of NumPy played a key role in addressing the image processing, combinatorics requirements and need for fast computation in DeepLabCut pose estimation algorithms:

* Vectorization
* Masked Array Operations
* Linear Algebra
* Random Sampling
* Reshaping of large arrays

DeepLabCut utilizes NumPy’s array capabilities throughout the workflow offered by the toolkit. In particular, NumPy is used for sampling distinct frames for human annotation labeling, and for writing, editing and processing annotation data.  Within TensorFlow the neural network is trained by DeepLabCut technology over thousands of iterations to predict the ground truth annotations from frames. For this purpose, target densities (scoremaps) are created to cast pose estimation as a image-to-image translation problem. To make the neural networks robust, data augmentation is employed, which requires the calculation of target scoremaps subject to various geometric and image processing steps. To make training fast, NumPy’s vectorization capabilities are leveraged. For inference, the most likely predictions from target scoremaps need to extracted and one needs to efficiently “link predictions to assemble individual animals”.

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png' title = 'DeepLabCut Workflow' alt = 'workflow' attribution = '(Source: Mackenzie Mathis)' attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## Sommario

Observing and efficiently describing behavior is a core tenant of modern ethology, neuroscience, medicine, and technology. [DeepLabCut](https://static1.squarespace.com/static/57f6d51c9f74566f55ecf271/t/5eab5ff7999bf94756b27481/1588289532243/NathMathis2019.pdf) allows researchers to estimate the pose of the subject, efficiently enabling them to quantify the behavior. With only a small set of training images, the DeepLabCut Python toolbox allows training a neural network to within human level labeling accuracy, thus expanding its application to not only behavior analysis in the laboratory, but to potentially also in sports, gait analysis, medicine and rehabilitation studies. Complex combinatorics, data processing challenges faced by DeepLabCut algorithms are addressed through the use of NumPy's array manipulation capabilities.

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png' alt = 'numpy benefits' title = 'Key NumPy Capabilities utilized'
{{< /figure >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
