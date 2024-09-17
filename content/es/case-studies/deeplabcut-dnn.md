---
title: "Caso de estudio: Estimación de Postura 3D DeepLabCut"
sidebar: falso
---

{{< figure >}}
src = '/images/content_images/cs/mice-hand.gif' title = 'Analizar movimiento del ratón usando DeepLapCut' alt = 'micehandanim' attribution = '(Fuente: www.deeplabcut.org )' attributionlink = 'http://www.mousemASElab.org/deeplabcut'
{{< /figure >}}

{{< blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/" by="Alexander Mathis, *Profesor Asistente, Escuela Politécnica Federal de Lausana* ([EPFL](https://www.epfl.ch/en/))"
> }} El software de código abierto está acelerando la biomedicina. DeepLabCut permite el análisis automatizado de video del comportamiento animal utilizando Aprendizaje Profundo. 
> 
> {{< /blockquote >}}

## Acerca de DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) es una caja de herramientas de código abierto que permite a los investigadores de cientos de instituciones de todo el mundo rastrear el comportamiento de animales de laboratorio, con muy pocos datos de entrenamiento, con una precisión de nivel humana. Con la tecnología DeepLabCut, los científicos pueden profundizar en la comprensión científica del control motriz y el comportamiento a través de especies animales y escalas de tiempo.

Muchas áreas de investigación, incluyendo la neurociencia, la medicina y la biomecánica, utilizan datos para rastrear el movimiento animal. DeepLabCut ayuda a entender lo que los humanos y otros animales están haciendo, analizando las acciones que han sido grabadas en la filmación. Utilizando la automatización para tareas laboriosas de etiquetado y monitoreo, junto con el análisis de datos basado en redes neuronales profundas, DeepLabCut realiza estudios científicos que involucran la observación de animales, tales como primates, ratones, peces, moscas, etc. de manera mucho más rápida y precisa.

{{< figura >}}
src = '/images/content_images/cs/race-horse.gif' title = 'Puntos de colores rastrean las posiciones de una parte del cuerpo de un caballo de carreras' alt = 'horserideranim' attribution = '(Fuente: Mackenzie Mathis)'
{{< /figure >}}

El rastreo del comportamiento no invasivo de animales de DeepLabCut por medio de la extracción de posturas de animales es crucial para propósitos científicos en dominios tales como la biomecánica, genética, etología y & neurociencia. Medir las poses de animales de manera no invasiva a partir de video - sin marcadores - en fondos que cambian dinámicamente es un desafío computacional, tanto técnicamente como en términos de necesidades de recursos y datos de entrenamiento requeridos.

DeepLabCut permite a los investigadores estimar la postura del sujeto, permitiéndoles eficientemente cuantificar el comportamiento a través de una caja de herramientas de software basada en Python.  Con DeepLabCut, los investigadores pueden identificar fotogramas distintos de videos, etiquetar digitalmente partes específicas del cuerpo en unas pocas docenas de fotogramas con una GUI personalizada, y luego las arquitecturas de estimación de posturas basadas en aprendizaje profundo en DeepLabCut aprenden a identificar esas mismas características en el resto del video y en otros videos similares de animales. Funciona en diferentes especies de animales, desde los animales de laboratorio comunes como moscas y ratones hasta animales más inusuales como los [guepardos][cheetah-movement].

DeepLabCut utiliza un principio llamado [aprendizaje por transferencia](https://arxiv.org/pdf/1909.11229), que reduce considerablemente la cantidad de datos de entrenamiento requeridos y acelera la convergencia del período de entrenamiento.  Dependiendo de las necesidades, los usuarios pueden seleccionar diferentes arquitecturas de red que proporcionan una inferencia más rápida (por ejemplo MobileNetV2), que también pueden combinarse con retroalimentación experimental en tiempo real. DeepLabCut utilizó originalmente los detectores de características de una arquitectura de estimación de postura humana de alto rendimiento, llamada [DeeperCut](https://arxiv.org/abs/1605.03170), que inspiró el nombre. El paquete ahora ha sido significativamente modificado para incluir arquitecturas adicionales, métodos de aumento y una experiencia de usuario completa en el front-end. Además, para apoyar los experimentos biológicos a gran escala, DeepLabCut proporciona capacidades de aprendizaje activo para que los usuarios puedan aumentar el conjunto de entrenamiento a lo largo del tiempo para cubrir casos límite y hacer que su algoritmo de estimación de postura sea robusto dentro de un contexto específico.

Recientemente, se presentó el [modelo zoo de DeepLabCut](http://www.mousemotorlab.org/dlc-modelzoo), que proporciona modelos pre-entrenados para varias especies y condiciones experimentales, desde el análisis facial en primates hasta la postura de perro. Esto se puede ejecutar, por ejemplo, en la nube sin ningún etiquetado de datos nuevos o entrenamiento de redes neuronales, y no es necesaria ninguna experiencia de programación.

### Objetivos y Resultados Clave

* **Automatización del análisis de la postura animal para estudios científicos:**

  El objetivo principal de la tecnología DeepLabCut es medir y rastrear la postura de los animales en diversos entornos. Estos datos se pueden utilizar, por ejemplo, en estudios de neurociencia para entender cómo el cerebro controla el movimiento, o para dilucidar como interactúan socialmente los animales. Los investigadores han observado un [aumento de rendimiento diez veces mayor](https://www.biorxiv.org/content/10.1101/457242v1) con DeepLabCut. Las posturas se pueden inferir sin conexión hasta a 1200 fotogramas por segundo (FPS).

* **Creación de un conjunto de herramientas de Python de fácil uso para la estimación de postura:**

  DeepLabCut quería compartir su tecnología de estimación de postura animal en la forma de una herramienta de fácil uso que pueda ser adoptada fácilmente por los investigadores. Así que han creado un conjunto de herramientas de Python completo y de fácil uso, también con características de administración de proyectos. Estas permiten no solo la automatización de la estimación de postura, sino también administrar el proyecto de punta a punta ayudando al usuario del conjunto de herramientas de DeepLabCut desde la etapa de recolección del conjunto de datos para crear flujos de trabajo de análisis compartibles y reutilizables.

  Su [conjunto de herramientas][DLCToolkit] ahora está disponible como código abierto.

  En flujo de trabajo típico de DeepLabCut incluye:

  - creación y refinamiento de los conjuntos de entrenamiento a través del aprendizaje activo
  - creación de redes neuronales a la medida para animales y escenarios específicos
  - código para inferencia a gran escala en videos
  - graficar las inferencias utilizando herramientas de visualización integradas

{{< figura >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png' title = 'Postura de estimación de pasos con DeepLabCut' alt = 'dlcsteps' align = 'center' atribución = '(Source: DeepLabCut)' attributionlink = 'https://twitter. om/DeepLabCut/status/1198046918284210176/foto/1'
{{< /figura >}}

### Los Desafíos

* **Velocidad**

    Procesamiento rápido de videos de comportamiento animal para medir su comportamiento y al mismo tiempo hacer experimentos científicos más eficientes y precisos. La extracción detallada de posturas del animal para experimentos de laboratorio, sin marcadores, en entornos dinámicamente cambiantes, puede ser un desafío tanto técnico como en términos de recursos necesarios y datos de entrenamiento requeridos. Proponer una herramienta que sea fácil de usar sin necesidad de habilidades como experiencia en visión por computador que permita a los científicos hacer investigaciones en más contextos del mundo real, es un problema que no es trivial de resolver.

* **Combinatoria**

    La combinatoria involucra el armado e integración del movimiento de múltiples extremidades en el comportamiento animal individual. Ensamblar puntos clave y sus conexiones en movimientos individuales de animales y vincularlos a lo largo del tiempo es un proceso complejo que requiere un análisis numérico intensivo, especialmente en el caso del seguimiento de movimientos de múltiples animales en videos de experimentos.

* **Procesamiento de Datos**

    Por último, pero no menos importante, la manipulación de arreglos - procesamiento de grandes pilas de arreglos correspondientes a varias imágenes, tensores objetivo y puntos clave es bastante desafiante.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png' title = 'Estimación de variedad y complejidad de postura' alt = 'challengesfig' align = 'centro' atribución = '(Fuente: Mackenzie Mathis)' attributionlink = 'https://www. iorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## El Papel de NumPy para afrontar los desafíos de la estimación de postura

NumPy aborda la necesidad central de la tecnología de DeepLabCut de realizar cálculos numéricos a alta velocidad para el análisis del comportamiento.  Además de NumPy, DeepLabCut emplea varios softwares de Python que utilizan NumPy en su núcleo, como [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) y [Tensorflow](https://www.tensorflow.org).

Las siguientes características de NumPy jugaron un papel clave en abordar el procesamiento de imágenes, los requisitos de combinatoria y la necesidad de cálculos rápidos en los algoritmos de estimación de posturas de DeepLabCut:

* Vectorización
* Operaciones con Arreglos Enmascarados
* Álgebra lineal
* Muestreo Aleatorio
* Redimensionamiento de arreglos grandes

DeepLabCut utilizes NumPy’s array capabilities throughout the workflow offered by the toolkit. In particular, NumPy is used for sampling distinct frames for human annotation labeling, and for writing, editing and processing annotation data.  Within TensorFlow the neural network is trained by DeepLabCut technology over thousands of iterations to predict the ground truth annotations from frames. For this purpose, target densities (scoremaps) are created to cast pose estimation as a image-to-image translation problem. To make the neural networks robust, data augmentation is employed, which requires the calculation of target scoremaps subject to various geometric and image processing steps. To make training fast, NumPy’s vectorization capabilities are leveraged. For inference, the most likely predictions from target scoremaps need to extracted and one needs to efficiently “link predictions to assemble individual animals”.

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png' title = 'DeepLabCut Workflow' alt = 'workflow' attribution = '(Source: Mackenzie Mathis)' attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## Summary

Observing and efficiently describing behavior is a core tenant of modern ethology, neuroscience, medicine, and technology. [DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf) permite a los investigadores estimar la postura del sujeto, permitiéndoles de manera eficiente cuantificar el comportamiento. Con solo un pequeño conjunto de imágenes de entrenamiento, el conjunto de herramientas de Python de DeepLabCut permite entrenar una red neuronal con una precisión de etiquetado a nivel humano, expandiendo así su aplicación no solo al análisis del comportamiento en el laboratorio, sino también potencialmente en deportes, análisis de marcha, medicina y estudios de rehabilitación. Los desafíos de la combinatoria compleja y procesamiento de datos enfrentados por los algoritmos de DeepLabCut se abordan mediante el uso de las capacidades de manipulación de arreglos de NumPy.

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png' alt = 'beneficios de NumPy' title = 'Capacidades claves de NumPy utilizadas'
{{< /figure >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
