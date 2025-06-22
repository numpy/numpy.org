---
title: "Caso de estudio: La primera imagen de un Agujero Negro"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
  by="{{< blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs" by="Katie Bouman, _Profesora Asistente, Ciencias de la Computación & Matemáticas, Caltech_""
>}}
{{< /blockquote >}}

## Un telescopio del tamaño de la Tierra

El [ Telescopio Event Horizon (EHT) ](https://eventhorizontelescope.org), es un conjunto de ocho radiotelescopios terrestres que forman un telescopio computacional del tamaño de la Tierra, estudiando al universo con una sensibilidad y resolución sin precedente.  El enorme telescopio virtual, que utiliza una técnica llamada Interferometría de línea de base muy larga (VLBI), tiene una resolución angular de [20 microsegundos de arco][resolution] — ¡suficiente para leer un periódico en Nueva York desde un café en la acera en París!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### Objetivos y Resultados Clave

- **Una nueva vista del universo:** El trabajo preliminar de la innovadora imagen de EHT se había establecido 100 años antes, cuando [Sir Arthur Eddington][eddington] dio el primer apoyo observacional a la teoría de la relatividad general de Einstein.

- **El agujero negro:** EHT se entrenó en un enorme agujero negro supermasivo aproximadamente a 55 millones de años luz de la Tierra, situado en el centro de la galaxia Messier 87 (M87) en el cúmulo de galaxias Virgo. Su masa es 6.5 mil millones de veces la del sol. Se había estudiado por [más de 100 años](https://www.jpl.nasa.gov/news/news.php?feature=7385), pero nunca antes se había observado un agujero negro.

- **Comparando las observaciones con la teoría:** A partir de la teoría general de la relatividad de Einstein, los científicos esperaban encontrar una región similar a una sombra causada por la flexión gravitacional y la captura de la luz. Los científicos pudieron utilizarla para medir la enorme masa del agujero negro.

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

### Los Desafíos

- **Escala computacional**

  EHT plantea enormes desafíos de procesamiento de datos, incluyendo las rápidas fluctuaciones de fase atmosféricas, amplio ancho de banda de grabación, y telescopios que son ampliamente disímiles y geográficamente dispersos.

- **Demasiada información**

  Cada día, el EHT genera más de 350 terabytes de observaciones, almacenados en discos duros llenos de helio. Reducir el volumen y complejidad de estos datos es enormemente difícil.

- **Hacia lo desconocido**

  Cuando el objetivo es ver algo nunca antes visto, ¿cómo pueden los científicos estar seguros de que la imagen es correcta?

{{< figure >}}
{{< /figure >}}

## El Rol de NumPy

¿Qué pasa si hay un problema con los datos? O tal vez un algoritmo depende demasiado de una suposición en particular. ¿Cambiará drásticamente la imagen si se cambia un solo parámetro?

La colaboración del EHT respondió a estos desafíos haciendo que los equipos independientes evaluaran los datos, utilizando técnicas de reconstrucción de imágenes ya establecidas y de vanguardia. Cuando los resultados se mostraron consistentes, se combinaron para producir la primera imagen de su tipo de un agujero negro.

Su trabajo ilustra el rol que desempeña el ecosistema científico de Python en el avance de la ciencia a través del análisis de datos colaborativos.

{{< figure >}}
{{< /figure >}}

Por ejemplo, el paquete de Python [`eht-imaging`][ehtim] proporciona herramientas para simular y realizar reconstrucción de imágenes en datos VLBI.
NumPy está en el núcleo del procesamiento de datos de matrices utilizados en este paquete, como se muestra a continuación en el gráfico parcial de dependencias de software.

{{< figure >}}
{{< /figure >}}

[ehtim]: https://github.com/achael/eht-imaging

Además de NumPy, muchos otros paquetes, como [SciPy](https://scipy.org) y [Pandas](https://pandas.pydata.org), son parte del flujo de procesamiento de datos para fotografiar el agujero negro.
Los formatos estándar de archivos astronómicos y transformaciones de tiempo/coordenadas fueron manejados por [Astropy][astropy], mientras que [Matplotlib][mpl] fue utilizado en la visualización de datos a través del flujo de análisis, incluyendo la generación de la imagen final del agujero negro.

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/

## Resumen

El eficiente y adaptable arreglo n-dimensional que es la característica central de NumPy, permitió a los investigadores manipular grandes conjuntos de datos numéricos, proporcionando una base para la primera imagen de un agujero negro. Un momento histórico en la ciencia ofrece una impresionante evidencia visual de la teoría de Einstein. Este logro abarca no solo los avances tecnológicos sino también la colaboración internacional de más de 200 científicos y algunos de los mejores radio observatorios del mundo.  Algoritmos innovadores y técnicas de procesamiento de datos, mejorando los modelos astronómicos existentes, ayudaron a desvelar un misterio del universo.

{{< figure >}}
{{< /figure >}}
