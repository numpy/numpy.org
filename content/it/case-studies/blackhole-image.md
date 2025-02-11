---
title: "Caso di Studio: Prima Immagine di un Buco Nero"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/blackhole.jpg' title = 'Buco Nero M87' alt = 'immagine buco nero' attribution = '(Crediti dell'Immagine: Collaborazione del Telescopio Event Horizon)' attributionlink = 'https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg'
{{< /figure >}}

{{< blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs" by="Katie Bouman, * Professore Assistente, Scienze & Matematiche Computazionali, Caltech*"
> }} L'immagine del buco nero M87 è come cercare di vedere qualcosa che per definizione è impossibile da vedere. 
> 
> {{< /blockquote >}}

## Un telescopio dalla dimensione della Terra

Il telescopio [Event Horizon (EHT)](https://eventhorizontelescope.org) è un complesso di otto radiotelescopi terrestri che formano un telescopio computazionale della dimensione della Terra, studiando l'universo con sensibilità e risoluzione senza precedenti.  L'enorme telescopio virtuale, che utilizza una tecnica chiamata interferometria a lunghissima base (VLBI), ha una risoluzione angolare di [20 micro-secondi d'arco][resolution] — abbastanza definito per leggere un giornale a New York da un bar sul marciapiede a Parigi!

### Obiettivi Principali e Risultati

* **Una Nuova Visione dell'Universo:** Le basi per l'immagine innovativa dell'EHT sono state gettate 100 anni prima, quando [Sir Arthur Eddington][eddington] ha dato il primo supporto d'osservazione della teoria della relatività generale di Einstein.

* **Il Buco Nero:** L'EHT è stato addestrato su un buco nero supermassiccio a circa 55 milioni di anni luce dalla Terra, situato al centro della galassia Messier 87 (M87) nell'ammasso della galassia Vergine. La sua massa è 6.5 miliardi di volte quella del Sole. Era stato studiato per [oltre 100 anni](https://www.jpl.nasa.gov/news/news.php?feature=7385), ma mai prima d'ora si era osservato un buco nero visivamente.

* **Paragonando Osservazioni con la Teoria:** Dalla teoria generale della relatività di Einstein, gli scienziati si aspettavano di trovare una regione richiamante un'ombra causata dalla flessione gravitazionale e dalla cattura della luce. Gli scienziati hanno potuto usarla per misurare l'enorme massa del buco nero.

### Le Sfide

* **Scala computazionale**

    L'EHT pone enormi sfide di elaborazione dei dati, tra cui rapide fluttuazioni di fase atmosferiche, grande larghezza di banda nella registrazione e telescopi che sono ampiamente dissimili e geograficamente dispersi.

* **Troppe informazioni**

    Ogni giorno l'EHT genera oltre 350 terabyte di osservazioni, memorizzati su dischi rigidi riempiti di elio. Ridurre il volume e la complessità di questa quantità di dati è estremamente difficile.

* **Dentro allo sconosciuto**

    Quando l'obiettivo è quello di vedere qualcosa mai visto prima, come possono gli scienziati essere certi che l'immagine sia corretta?

{{< figure >}}
src = '/images/content_images/cs/dataprocessbh.png' title = 'Pipeline della Processione Dati dell'EHT' alt = 'data pipeline' align = 'center' attribution = '(Crediti del Diagramma: The Astrophysical Journal, Collaborazione del Telescopio Event Horizon)' attributionlink = 'https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57'
{{< /figure >}}

## Il Ruolo di NumPy

Che cosa succede se c'è un problema con i dati? O magari se un algoritmo si basa troppo su un'assunzione particolare. src = '/images/content_images/cs/dataprocessbh.png' title = 'Pipeline della Processione Dati dell'EHT' alt = 'data pipeline' align = 'center' attribution = '(Crediti del Diagramma: The Astrophysical Journal, Collaborazione del Telescopio Event Horizon)' attributionlink = 'https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57'

La collaborazione dell'EHT ha riscontrato queste problematiche durante l'elaborazione dei dati indipendente dei gruppi di ricerca, usando tecniche di ricostruzione d'immagine ben stabilite e all'avanguardia.  Quando i risultati si sono dimostrati coerenti, sono stati combinati per produrre la prima immagine mai esistita del buco nero.

Il loro lavoro illustra il ruolo che l'ecosistema scientifico di Python gioca nell'avanzamento della scienza attraverso l'analisi collaborativa di dati.

{{< figure >}}
src = '/images/content_images/cs/bh_numpy_role.png' alt = 'ruolo di numpy' title = 'Il ruolo di NumPy nella rappresentazione del Buco Nero'
{{< /figure >}}

Ad esempio, il paccheto Python [`eht-imaging`][ehtim]  fornisce strumenti per la simulazione e la ricostruzione dell'immagine dei dati VLBI. NumPy è al centro dell'elaborazione dei dati matriciali utilizzati in questo pacchetto, come illustrato dal grafico delle dipendenze parziali del software qui sotto.

{{< figure >}}
src = '/images/content_images/cs/ehtim_numpy.png' alt = 'ehtim dependency map highlighting numpy' title = 'Diagramma delle dipendenze del Software del pacchetto ehtim evidenziando NumPy'
{{< /figure >}}

Oltre a NumPy, molti altri pacchetti, come [SciPy](https://www.scipy.org) e [Panda](https://pandas.io), fanno parte della pipeline di elaborazione dati per l’immagine del buco nero. I formati di file astronomici standard e le trasformazioni di tempo/coordinate sono stati gestiti da [Astropy][astropy], mentre [Matplotlib][mpl] è stato utilizzato per visualizzare i dati in tutta la pipeline di analisi, compresa la generazione dell'immagine finale del buco nero.

## Sommario

La gestione efficiente ed adattabile di matrici n-dimensionali, che è la caratteristica centrale di NumPy, ha permesso ai ricercatori di manipolare grandi insiemi di dati numerici, fornendo una base per la prima immagine mai osservata di un buco nero. Pietra miliare della scienza, si tratta di una splendida testimonianza visiva della teoria di Einstein.   Algoritmi innovativi e tecniche di elaborazione dati, migliorando i modelli astronomici esistenti, hanno contribuito a spiegare un mistero dell'universo.

{{< figure >}}
src = '/images/content_images/cs/numpy_bh_benefits.png' alt = 'benefici di numpy' title = 'Capacità chiave di NumPy Capabilities utilizzate'
{{< /figure >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
