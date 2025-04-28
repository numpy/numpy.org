---
title: "Caso de estudio: La primera imagen de un Agujero Negro"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
  by="Katie Bouman, _Assistant Professor, Computing & Mathematical Sciences, Caltech_"
>}}
{{< /blockquote >}}

## Un telescopio del tamaño de la Tierra

The [Event Horizon telescope (EHT)](https://eventhorizontelescope.org) is an
array of eight ground-based radio telescopes forming a computational telescope
the size of the earth, studing the universe with unprecedented
sensitivity and resolution.  The huge virtual telescope,  which uses a technique
called very-long-baseline interferometry (VLBI), has an angular resolution of
[20 micro-arcseconds][resolution] — enough to read a newspaper in New York
from a sidewalk café in Paris!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### Objetivos y Resultados Clave

- **A New View of the Universe:**
  The groundwork for the EHT's groundbreaking image had been laid 100 years
  earlier when [Sir Arthur Eddington][eddington] yielded the first
  observational support of Einstein's theory of general relativity.

- **The Black Hole:** EHT was trained on a supermassive black hole
  approximately 55 million light-years from Earth, lying at the center
  of the galaxy Messier 87 (M87) in the Virgo galaxy cluster. Its mass is
  6.5 billion times the Sun's. It had been studied for
  [over 100 years](https://www.jpl.nasa.gov/news/news.php?feature=7385), but never before
  had a black hole been visually observed.

- **Comparing Observations to Theory:** From Einstein’s general theory of
  relativity, scientists expected to find a shadow-like region caused by
  gravitational bending and capture of light. Scientists could
  use it to measure the black hole's enormous mass.

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

### Los Desafíos

- **Computational scale**

  EHT poses massive data-processing challenges, including rapid atmospheric
  phase fluctuations, large recording bandwidth, and telescopes that are
  widely dissimilar and geographically dispersed.

- **Too much information**

  Each day EHT generates over 350 terabytes of observations, stored on
  helium-filled hard drives. Reducing the volume and complexity of this much
  data is enormously difficult.

- **Into the unknown**

  When the goal is to see something never before seen, how can scientists be
  confident the image is correct?

{{< figure >}}
{{< /figure >}}

## El Rol de NumPy

¿Qué pasa si hay un problema con los datos? O tal vez un algoritmo depende demasiado de una suposición en particular. ¿Cambiará drásticamente la imagen si se cambia un solo parámetro?

La colaboración del EHT respondió a estos desafíos haciendo que los equipos independientes evaluaran los datos, utilizando técnicas de reconstrucción de imágenes ya establecidas y de vanguardia. Cuando los resultados se mostraron consistentes, se combinaron para producir la primera imagen de su tipo de un agujero negro.

Su trabajo ilustra el rol que desempeña el ecosistema científico de Python en el avance de la ciencia a través del análisis de datos colaborativos.

{{< figure >}}
{{< /figure >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for
simulating and performing image reconstruction on VLBI data.
NumPy está en el núcleo del procesamiento de datos de matrices utilizados en este paquete, como se muestra a continuación en el gráfico parcial de dependencias de software.

{{< figure >}}
{{< /figure >}}

[ehtim]: https://github.com/achael/eht-imaging

Besides NumPy, many other packages, such as
[SciPy](https://scipy.org) and [Pandas](https://pandas.pydata.org), are part of the
data processing pipeline for imaging the black hole.
The standard astronomical file formats and time/coordinate transformations
were handled by [Astropy][astropy], while [Matplotlib][mpl] was used
in visualizing data throughout the analysis pipeline, including the generation
of the final image of the black hole.

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/

## Resumen

El eficiente y adaptable arreglo n-dimensional que es la característica central de NumPy, permitió a los investigadores manipular grandes conjuntos de datos numéricos, proporcionando una base para la primera imagen de un agujero negro. Un momento histórico en la ciencia ofrece una impresionante evidencia visual de la teoría de Einstein. Este logro abarca no solo los avances tecnológicos sino también la colaboración internacional de más de 200 científicos y algunos de los mejores radio observatorios del mundo.  Algoritmos innovadores y técnicas de procesamiento de datos, mejorando los modelos astronómicos existentes, ayudaron a desvelar un misterio del universo.

{{< figure >}}
{{< /figure >}}
