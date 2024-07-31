---
title: "Estudio de Caso: Descubrimiento de Ondas Gravitacionales"
sidebar: falso
---

{{< figure >}}
src = '/images/content_images/cs/gw_sxs_image. ng' title = 'Ondas Gravitacionales' alt = 'coalescencia de un agujero negro binario generando ondas gravitacionales' atribución = '(Créditos de imagen: El proyecto Simulación de Espacio-tiempos eXtreme (SXS) en LIGO)' attributionlink = 'https://youtu. e/Zt8Z_uzG71o'
{{< /figure >}}

{{< blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs" by="David Shoemaker, *Colaboración científica LIGO*" >}} El ecosistema científico de Python es una infraestructura crítica para la investigación realizada en LIGO.
{{< /blockquote >}}

## Acerca de [Ondas Gravitacionales](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) y [LIGO](https://www.ligo.caltech.edu)

Las ondas gravitacionales son ondulaciones en el tejido del espacio y el tiempo, generadas por eventos cataclísmicos en el universo, tales como la colisión y fusión de dos agujeros negros o la coalescencia de estrellas binarias o supernovas. La observación de Ondas Gravitacionales no solo puede ayudar en el estudio de la gravedad, sino también en la comprensión de algunos de fenómenos más oscuros en el universo distante y su impacto.

El [Observatorio de Ondas Gravitacionales por Interferometría Láser (LIGO)](https://www.ligo.caltech.edu) fue diseñado para abrir el campo de la astrofísica de ondas gravitacionales mediante la detección directa de las ondas gravitacionales predichas por la Teoría General de la Relatividad de Einstein. Comprende dos interferómetros ampliamente separados dentro de los Estados Unidos: uno en Hanford, Washington, y el otro en Livingston, Louisiana, operando al unísono para detectar ondas gravitacionales. Cada uno de ellos tiene detectores de ondas gravitacionales de escala de múltiples kilómetros que utilizan interferometría de láser.  La Colaboración Científica de LIGO (LSC) es un grupo de más de 1000 científicos de universidades de los Estados Unidos y de otros 14 países, respaldados por más de 90 universidades e institutos de investigación; aproximadamente 250 estudiantes contribuyen activamente a la colaboración. El nuevo descubrimiento de LIGO es la primera observación de ondas gravitacionales, realizada midiendo las diminutas perturbaciones que las ondas generan en el espacio y el tiempo a medida que pasan a través de la Tierra.  Ha abierto nuevas fronteras astrofísicas que exploran el lado distorsionado del universo: objetos y fenómenos que se forman a partir del espacio-tiempo deformado.


### Objetivos Clave

* Aunque su [misión](https://www.ligo.caltech.edu/page/what-is-ligo) es detectar ondas gravitacionales de algunos de los procesos más violentos y energéticos del Universo, los datos que LIGO recopila pueden tener efectos de gran alcance en muchas áreas de la física, incluyendo gravitación, relatividad, astrofísica, cosmología, física de partículas y física nuclear.
* Procesar los datos observados mediante cálculos de relatividad numérica que implican matemáticas complejas para discernir la señal del ruido, filtrar la señal relevante y estimar estadísticamente la significancia de los datos observados
* Visualización de datos para que los resultados binarios/numéricos puedan ser comprendidos.



### Los desafíos

* **Cálculo**

    Las Olas Gravitacionales son difíciles de detectar, ya que producen un efecto muy pequeño y tienen una diminuta interacción con la materia. Procesar y analizar todos los datos de LIGO requiere una vasta infraestructura informática. Después de ocuparse del ruido, que es miles de millones de veces mayor que la señal, aún quedan ecuaciones de relatividad muy complejas y enormes cantidades de datos que suponen un desafío computacional: [se necesitan aproximadamente O(10^7) horas de CPU para los análisis de fusiones binarias](https://youtu.be/7mcHknWWzNI), distribuidas en 6 clústeres dedicados de LIGO

* **Avalancha de Datos**

    A medida que los dispositivos de observación se vuelven más sensibles y confiables, los desafíos planteados por la avalancha de datos y encontrar una aguja en un pajar aumentan exponencialmente. ¡LIGO genera terabytes de datos cada día! Dar sentido a estos datos requiere de un esfuerzo enorme para cada detección. Por ejemplo, las señales recolectadas por LIGO deben ser comparadas por supercomputadoras contra cientos de miles de plantillas de posibles señales de ondas gravitacionales.

* **Visualization**

    Once the obstacles related to understanding Einstein’s equations well enough to solve them using supercomputers are taken care of, the next big challenge was making data comprehensible to the human brain. La modelación de simulación, así como la detección de señales, requieren técnicas de visualización efectivas.  La visualización también desempeña un papel en otorgar más credibilidad a la relatividad numérica a los ojos de los aficionados a la ciencia pura, los cuales no le daban suficiente importancia a la relatividad numérica hasta que las imágenes y simulaciones facilitaron la comprensión de los resultados para un público más amplio. Speed of complex computations and rendering, re-rendering images and simulations using latest experimental inputs and insights can be a time consuming activity that challenges researchers in this domain.

{{< figure >}}
src = '/images/content_images/cs/gw_strain_amplitude.png' alt = 'gravitational waves strain amplitude' title = 'Estimated gravitational-wave strain amplitude from GW150914' attribution = '(Graph Credits: Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)' attributionlink = 'https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger'
{{< /figure >}}

## NumPy’s Role in the Detection of Gravitational Waves

Gravitational waves emitted from the merger cannot be computed using any technique except brute force numerical relativity using supercomputers. The amount of data LIGO collects is as incomprehensibly large as gravitational wave signals are small.

NumPy, the standard numerical analysis package for Python,  was utilized by the software used for various tasks performed during the GW detection project at LIGO. NumPy helped in solving complex maths and data manipulation at high speed.  Here are some examples:

* [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
* Data retrieval: Deciding which data can be analyzed, figuring out whether it contains a signal - needle in a haystack
* Statistical analysis: estimate the statistical significance of observational data, estimating the signal parameters (e.g. masses of stars, spin velocity, and distance) by comparison with a model.
* Visualization of data
  - Time series
  - Spectrograms
* Compute Correlations
* Key [Software](https://github.com/lscsoft) developed in GW data analysis such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for providing object based interfaces to utilities, tools, and methods for studying data from gravitational-wave detectors.

{{< figure >}}
src = '/images/content_images/cs/gwpy-numpy-dep-graph.png' alt = 'gwpy-numpy depgraph' title = 'Dependency graph showing how GwPy package depends on NumPy'
{{< /figure >}}

----

{{< figure >}}
src = '/images/content_images/cs/PyCBC-numpy-dep-graph.png' alt = 'PyCBC-numpy depgraph' title = 'Dependency graph showing how PyCBC package depends on NumPy'
{{< /figure >}}

## Summary

GW detection has enabled researchers to discover entirely unexpected phenomena while providing new insight into many of the most profound astrophysical phenomena known. Number crunching and data visualization is a crucial step that helps scientists gain insights into data gathered from the scientific observations and understand the results. The computations are complex and cannot be comprehended by humans unless it is visualized using computer simulations that are fed with the real observed data and analysis.  NumPy along with other Python packages such as matplotlib, pandas, and scikit-learn is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to answer complex questions and discover new horizons in our understanding of the universe.

{{< figure >}}
src = '/images/content_images/cs/numpy_gw_benefits.png' alt = 'numpy benefits' title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
