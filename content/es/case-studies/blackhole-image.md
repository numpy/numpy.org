---
title: "Caso de estudio: Primera imagen de un agujero negro"
sidebar: false
---

{{< figure src="/images/content_images/cs/blackhole.jpg" caption="**Agujero Negro M87**" alt=black hole image" attr="*(Créditos de imagen: Colaboración del Telescopio de Horizonte de Sucesos)*" attrlink="https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg">}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>Retratar el agujero negro M87 es como tratar de ver algo que por definición es imposible de ver.</p>
    <footer align="right">Katie Bouman, <cite>Profesor asistente, Ciencias matemáticas y computación, Caltech</cite></footer>
</blockquote>

## Un telescopio del tamaño del mundo

El [ telescopio del Horizonte de Sucesos (EHT) ](https://eventhorizontelescope.org), es un arreglo de ocho radiotelescopios terrestres que forman un telescopio computacional del tamaño del mundo, estudiando el universo con una sensibilidad y resolución sin precedente.  El enorme telescopio virtual, que utiliza una técnica llamada interferometría de línea de base muy larga (VLBI), tiene una resolución angular de [20 microsegundos de arco][resolution] — ¡suficiente para leer un periódico en Nueva York desde un café en la acera en París!

### Objetivos clave y resultados

* **Una nueva vista del universo:** El trabajo preliminar para la innovadora imagen de EHT se había establecido 100 años antes, cuando [Sir Arthur Eddington][eddington] dio el primer apoyo observacional a la teoría de la relatividad general de Einstein.

* **El agujero negro:** EHT apuntó a un enorme agujero negro aproximadamente a 55 millones de años luz de la tierra, situada en el centro de la galaxia Messier 87 (M87) en el cúmulo de Virgo. Su masa es 6.5 mil millones de veces la del sol. Se había estudiado por [más de 100 años](https://www.jpl.nasa.gov/news/news.php?feature=7385), pero nunca antes se había observado un agujero negro.

* **Comparando las observaciones con la teoría:** A partir de la teoría de la relatividad general de Einstein, los científicos esperaban encontrar una región similar a las sombras causada por la flexión gravitacional y la captura de la luz. Los científicos pudieron utilizarla para medir la enorme masa del agujero negro.

### Los desafíos

* **Escala computacional**

    EHT plantea desafíos de procesamiento de datos masivos, incluyendo rápidas fluctuaciones de fase atmosféricas, amplio ancho de banda de registro, y telescopios que son ampliamente disímiles y geográficamente dispersos.

* **Demasiada información**

    Cada día EHT genera más de 350 terabytes de observaciones, almacenados en discos duros llenos de helio. Reducir el volumen y complejidad de estos datos es enormemente difícil.

* **Hacia lo desconocido**

    Cuando el objetivo es ver algo nunca antes visto, ¿cómo pueden los científicos estar seguros de que la imagen es correcta?

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**Pipeline de procesamiento de datos de EHT**" alt="data pipeline" align="middle" attr="(Créditos del diagrama: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## El rol de NumPy

¿Qué pasa si hay un problema con los datos? O tal vez un algoritmo depende demasiado de un supuesto en particular. ¿Cambiará drásticamente la imagen si se cambia un sólo parámetro?

La alianza de EHT respondió a estos desafíos haciendo que los equipos independientes evalúen los datos, utilizando técnicas establecidas y de reconstrucción de imagen de vanguardia. Cuando los resultados se mostraron consistentes, se combinaron para producir la primera imagen de un agujero negro.

Su trabajo ilustra el rol que desempeña el ecosistema científico de Python en el avance de la ciencia a través del análisis de datos colaborativos.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**El rol de NumPy en la fotografía del Agujero Negro**" >}}

Por ejemplo, el paquete de Python [`eht-imaging`][ehtim] proporciona herramientas para simular y realizar reconstrucción de imágenes en datos VLBI. NumPy está en el núcleo del procesamiento de datos de arreglos utilizados en este paquete, como se muestra en el gráfico de dependencias de software parcial a continuación.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Gráfico de dependencias de software del paquete ehtim destacando NumPy**" >}}

Además de NumPy, muchos otros paquetes, como [SciPy](https://www.scipy.org) y [Pandas](https://pandas.io), son parte del pipeline de procesamiento de datos para fotografiar el agujero negro. Los formatos de archivo astronómicos estándar y transformaciones de tiempo/coordenadas fueron manejados por [Astropy][astropy], mientras que [Matplotlib][mpl] fue utilizado en la visualización de datos a través del pipeline de análisis, incluyendo la generación de la imagen final del agujero negro.

## Resumen

The efficient and adaptable n-dimensional array that is NumPy's central feature enabled researchers to manipulate large numerical datasets, providing a foundation for the first-ever image of a black hole. A landmark moment in science, it gives stunning visual evidence of Einstein’s theory. The achievement encompasses not only technological breakthroughs but also international collaboration among over 200 scientists and some of the world's best radio observatories.  Innovative algorithms and data processing techniques, improving upon existing astronomical models, helped unfold a mystery of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Capacidades clave de NumPy utilizadas**" >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
