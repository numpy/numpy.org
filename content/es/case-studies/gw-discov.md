---
title: "Estudio de Caso: Descubrimiento de Ondas Gravitacionales"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
  by="David Shoemaker, _LIGO Scientific Collaboration_"
>}}
{{< /blockquote >}}

## About [Gravitational Waves](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) and [LIGO](https://www.ligo.caltech.edu)

Las ondas gravitacionales son ondulaciones en el tejido del espacio y el tiempo, generadas por
cataclismos en el universo, tales como la colisión y fusión de dos agujeros
negros o la coalescencia de estrellas binarias o supernovas. La observación de Ondas Gravitacionales no solo puede ayudar en el estudio de la gravedad, sino también en la comprensión de algunos de los fenómenos oscuros en el universo distante y su impacto.

The [Laser Interferometer Gravitational-Wave Observatory (LIGO)](https://www.ligo.caltech.edu)
was designed to open the field of gravitational-wave astrophysics through the
direct detection of gravitational waves predicted by Einstein’s General Theory
of Relativity. Comprende dos interferómetros ampliamente separados dentro de los Estados Unidos: uno en Hanford, Washington, y el otro en Livingston, Louisiana, operando al unísono para detectar ondas gravitacionales. Cada uno de ellos tiene
detectores de ondas gravitacionales de escala de múltiples kilómetros que utilizan interferometría de láser.  La Colaboración Científica de LIGO (LSC) es un grupo de más de 1000 científicos de universidades de los Estados Unidos y de otros 14 países, respaldados por más de 90 universidades e institutos de investigación; aproximadamente 250 estudiantes contribuyen activamente a la colaboración. El nuevo descubrimiento de LIGO es la primera observación de ondas gravitacionales, realizada midiendo las diminutas perturbaciones que las ondas generan en el espacio y el tiempo a medida que pasan a través de la Tierra.  Ha abierto nuevas fronteras astrofísicas
que exploran el lado deformado del universo: objetos y fenómenos que están
hechos de espaciotiempo deformado.

### Objetivos Clave

- Though its [mission](https://www.ligo.caltech.edu/page/what-is-ligo) is to
  detect gravitational waves from some of the most violent and energetic
  processes in the Universe, the data LIGO collects may have far-reaching
  effects on many areas of physics including gravitation, relativity,
  astrophysics, cosmology, particle physics, and nuclear physics.
- Crunch observed data via numerical relativity computations that involves
  complex maths in order to discern signal from noise, filter out relevant
  signal and statistically estimate significance of observed data
- Data visualization so that the binary / numerical results can be
  comprehended.

### Los Desafíos

- **Computation**

  Gravitational Waves are hard to detect as they produce a very small effect
  and have tiny interaction with matter. Processing and analyzing all of
  LIGO's data requires a vast computing infrastructure.After taking care of
  noise, which is billions of times of the signal, there is still very
  complex relativity equations and huge amounts of data which present a
  computational challenge:
  [O(10^7) CPU hrs needed for binary merger analyses](https://youtu.be/7mcHknWWzNI)
  spread on 6 dedicated LIGO clusters

- **Data Deluge**

  As observational devices become more sensitive and reliable, the challenges
  posed by data deluge and finding a needle in a haystack rise multi-fold.
  ¡LIGO genera terabytes de datos cada día! Making sense of this data
  requires an enormous effort for each and every detection. For example, the
  signals being collected by LIGO must be matched by supercomputers against
  hundreds of thousands of templates of possible gravitational-wave signatures.

- **Visualization**

  Once the obstacles related to understanding Einstein’s equations well
  enough to solve them using supercomputers are taken care of, the next big
  challenge was making data comprehensible to the human brain. Simulation
  modeling as well as  signal detection requires effective visualization
  techniques.  Visualization also plays a role in lending more credibility
  to numerical relativity in the eyes of pure science aficionados, who did
  not give enough importance to numerical relativity until imaging and
  simulations made it easier to comprehend results for a larger audience.
  Speed of complex computations and rendering, re-rendering images and
  simulations using latest experimental inputs and insights can be a time
  consuming activity that challenges researchers in this domain.

{{< figure >}}
{{< /figure >}}

## El Papel de NumPy en la Detección de Ondas Gravitacionales

Las ondas gravitacionales emitidas por la fusión no pueden ser calculadas utilizando ninguna técnica excepto la relatividad numérica por fuerza bruta usando supercomputadoras.
La cantidad de datos que LIGO recopila es tan incomprensiblemente grande como pequeñas son las señales de onda
gravitacionales.

NumPy, el paquete de análisis numérico estándar para Python, fue utilizado por
el software empleado en varias tareas realizadas durante el proyecto de detección de Ondas Gravitacionales
en LIGO. NumPy ayudó a resolver las matemáticas complejas y la manipulación de datos a alta velocidad.  Aquí hay algunos ejemplos:

- [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch
  detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf)
  (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
- Data retrieval: Deciding which data can be analyzed, figuring out whether it
  contains a signal - needle in a haystack
- Statistical analysis: estimate the statistical significance of observational
  data, estimating the signal parameters (e.g. masses of stars, spin velocity,
  and distance) by comparison with a model.
- Visualización de datos
  - Series de tiempo
  - Espectrogramas
- Cálculo de Correlaciones
- Key [Software](https://github.com/lscsoft) developed in GW data analysis
  such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and
  [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for
  providing object based interfaces to utilities, tools, and methods for
  studying data from gravitational-wave detectors.

{{< figure >}}
{{< /figure >}}

----

{{< figure >}}
{{< /figure >}}

## Resumen

La detección de ondas gravitacionales ha permitido a los investigadores descubrir fenómenos completamente inesperados, al tiempo que proporciona nuevos conocimientos sobre muchos de los fenómenos astrofísicos más profundos conocidos. El procesamiento de datos y la visualización de datos son pasos cruciales que ayudan a los científicos a obtener información a partir de los datos recopilados en las observaciones científicas y a comprender los resultados. Los cálculos son complejos y
no pueden ser comprendidos por humanos, a menos que sean visualizados utilizando simulaciones
por computador que se alimenten con datos observados reales y análisis.  NumPy
along with other Python packages such as matplotlib, pandas, and scikit-learn
is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to
answer complex questions and discover new horizons in our understanding of the
universe.

{{< figure >}}
{{< /figure >}}
