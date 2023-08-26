---
title: "Caso de estudio: La primera imagen de un Agujero Negro"
sidebar: false
---

{{< figure src="/images/content_images/cs/blackhole.jpg" caption="**Agujero Negro M87**" alt="imagen de un agujero negro" attr="*(Créditos de la imagen: Colaboración del Telescopio de Horizonte de Sucesos)*" attrlink="https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>Fotografiar el agujero negro M87 es como tratar de ver algo que por definición es imposible de ver.</p>
    <footer align="right">Katie Bouman, <cite>Profesor asistente, Ciencias Matemáticas y de Computación, Caltech</cite></footer>
</blockquote>

## Un telescopio del tamaño de la Tierra

El [ telescopio de Horizonte de Sucesos (EHT) ](https://eventhorizontelescope.org), es un conjunto de ocho radiotelescopios terrestres que forman un telescopio computacional del tamaño de la tierra, estudiando al universo con una sensibilidad y resolución sin precedente.  El enorme telescopio virtual, que utiliza una técnica llamada Interferometría de línea de base muy larga (VLBI), tiene una resolución angular de [20 microsegundos de arco][resolution] — ¡suficiente para leer un periódico en Nueva York desde un café en la acera en París!

### Objetivos clave y resultados

* **Una nueva vista del universo:** El trabajo preliminar de la innovadora imagen de EHT se había establecido 100 años antes, cuando [Sir Arthur Eddington][eddington] dio el primer apoyo observacional a la teoría de la relatividad general de Einstein.

* **El agujero negro:** EHT se entrenó en un enorme agujero negro aproximadamente a 55 millones de años luz de la tierra, situada en el centro de la galaxia Messier 87 (M87) en el cúmulo de Virgo. Su masa es 6.5 mil millones de veces la del sol. Se había estudiado por [más de 100 años](https://www.jpl.nasa.gov/news/news.php?feature=7385), pero nunca antes se había observado un agujero negro.

* **Comparando las observaciones con la teoría:** A partir de la teoría de la relatividad general de Einstein, los científicos esperaban encontrar una región similar a las sombras causadas por la flexión gravitacional y la captura de la luz. Los científicos pudieron utilizarla para medir la enorme masa del agujero negro.

### Los desafíos

* **Escala computacional**

    EHT plantea desafíos de procesamiento de datos masivos, incluyendo rápidas fluctuaciones de fase atmosféricas, amplio ancho de banda de grabación, y telescopios que son ampliamente disímiles y geográficamente dispersos.

* **Demasiada información**

    Cada día el EHT genera más de 350 terabytes de observaciones, almacenados en discos duros llenos de helio. Reducir el volumen y complejidad de estos datos es enormemente difícil.

* **Hacia lo desconocido**

    Cuando el objetivo es ver algo nunca antes visto, ¿cómo pueden los científicos estar seguros de que la imagen es correcta?

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**EHT Data Processing Pipeline**" alt="data pipeline" align="middle" attr="(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## NumPy’s Role

What if there's a problem with the data? Or perhaps an algorithm relies too heavily on a particular assumption. Will the image change drastically if a single parameter is changed?

The EHT collaboration met these challenges by having independent teams evaluate the data, using both established and cutting-edge image reconstruction techniques. When results proved consistent, they were combined to yield the first-of-a-kind image of the black hole.

Their work illustrates the role the scientific Python ecosystem plays in advancing science through collaborative data analysis.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**The role of NumPy in Black Hole imaging**" >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for simulating and performing image reconstruction on VLBI data. NumPy is at the core of array data processing used in this package, as illustrated by the partial software dependency chart below.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Software dependency chart of ehtim package highlighting NumPy**" >}}

Besides NumPy, many other packages, such as [SciPy](https://www.scipy.org) and [Pandas](https://pandas.io), are part of the data processing pipeline for imaging the black hole. The standard astronomical file formats and time/coordinate transformations were handled by [Astropy][astropy], while [Matplotlib][mpl] was used in visualizing data throughout the analysis pipeline, including the generation of the final image of the black hole.

## Summary

The efficient and adaptable n-dimensional array that is NumPy's central feature enabled researchers to manipulate large numerical datasets, providing a foundation for the first-ever image of a black hole. A landmark moment in science, it gives stunning visual evidence of Einstein’s theory. The achievement encompasses not only technological breakthroughs but also international collaboration among over 200 scientists and some of the world's best radio observatories.  Innovative algorithms and data processing techniques, improving upon existing astronomical models, helped unfold a mystery of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
