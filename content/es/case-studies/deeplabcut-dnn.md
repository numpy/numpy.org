---
title: "Caso de estudio: Estimación de postura 3D DeepLabCut"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/mice-hand.gif'
title = 'Analizar movimiento de las manos de los ratones usando DeepLapCut'
alt = 'micehandanim'
attribution = '(Fuente: www.deeplabcut.org )'
attributionlink = 'http://www.mousemASElab.org/deeplabcut'
{{< /figure >}}

{{< blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/" by="Alexander Mathis, _Profesor Asistente, Escuela Politécnica Federal de Lausana_ ([EPFL](https://www.epfl.ch/en/))"

> }} El software de código abierto está acelerando la biomedicina. DeepLabCut permite el análisis de video automático del comportamiento animal usando aprendizaje profundo.
> {{< /blockquote >}}

## Acerca de DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) es una caja de herramientas de código abierto que permite a los investigadores de cientos de instituciones de todo el mundo rastrear el comportamiento de animales de laboratorio, con muy pocos datos de entrenamiento, con una precisión de nivel humana. Con la tecnología DeepLabCut, los científicos pueden profundizar en la comprensión científica del control y el comportamiento motriz a través de especies animales y escalas de tiempo.

Muchas áreas de investigación, incluyendo la neurociencia, la medicina y la biomecánica, utilizan datos para rastrear el movimiento animal. DeepLabCut ayuda a entender lo que los seres humanos y otros animales están haciendo analizando las acciones que han sido grabadas en la película. Utilizando la automatización para tareas laboriosas de etiquetado y monitoreo, junto con el análisis de datos basados en redes neuronales profundas, DeepLabCut realiza estudios científicos que involucran la observación de animales, como primates, ratones, peces, moscas, etc. mucho más rápido y preciso.

{{< figure >}}
src = '/images/content_images/cs/race-horse.gif'
title = 'Puntos de colores rastrean las posiciones de una parte del cuerpo de un caballo de carreras'
alt = 'horserideranim'
attribution = '(Fuente: Mackenzie Mathis)'
{{< /figure >}}

El rastreo del comportamiento no invasivo de animales de DeepLabCut por medio de la extracción de posturas de animales es crucial para propósitos científicos en dominios tales como la biomecánica, genética, etología y & neurociencia. La medición no invasiva de las posturas del animal a partir de video - sin marcadores - en entornos dinámicamente cambiantes es un desafío computacional, tanto técnicamente como en términos de recursos necesarios y datos de entrenamientos requeridos.

DeepLabCut permite a los investigadores estimar la postura del sujeto, permitiéndoles cuantificar de manera eficiente el comportamiento a través de un conjunto de herramientas de software basado en Python.  Con DeepLabCut, los investigadores pueden identificar diferentes fotogramas de videos, etiquetar digitalmente partes específicas del cuerpo en unas pocas docenas de fotogramas con una interfaz gráfica a medida, y luego las arquitecturas de estimación de postura basadas en aprendizaje profundo en DeepLabCut aprenden cómo seleccionar esas mismas características en el resto del video y en otros videos similares de animales. Funciona en diferentes especies de animales, desde los animales de laboratorio comunes como moscas y ratones hasta animales más inusuales como los [guepardos][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut utiliza un principio llamado [aprendizaje por transferencia](https://arxiv.org/pdf/1909.11229), que reduce considerablemente la cantidad de datos de entrenamiento requeridos y acelera la convergencia del período de entrenamiento.  Dependiendo de las necesidades, los usuarios pueden seleccionar diferentes arquitecturas de red que proporcionan una inferencia más rápida (por ejemplo MobileNetV2), que también pueden combinarse con retroalimentación experimental en tiempo real. Dependiendo de las necesidades, los usuarios pueden seleccionar diferentes arquitecturas de red que proporcionan una inferencia más rápida (por ejemplo MobileNetV2), que también pueden combinarse con retroalimentación experimental en tiempo real. El paquete ahora ha cambiado significativamente para incluir arquitecturas adicionales, métodos de aumento y una experiencia de usuario de front-end completa. Además, para apoyar los experimentos biológicos a gran escala DeepLabCut proporciona capacidades de aprendizaje activo para que los usuarios puedan aumentar el conjunto de entrenamiento a lo largo del tiempo para cubrir casos borde y hacer que su algoritmo de estimación de postura sea robusto dentro de un contedxto específico.

Recientemente, se presentó el [modelo zoo de DeepLabCut](http://www.mousemotorlab.org/dlc-modelzoo), que proporciona modelos pre-entrenados para varias especies y condiciones experimentales, desde el análisis facial en primates hasta la postura de perro. Esto se puede ejecutar por ejemplo en la nube sin ningún etiquetado de datos nuevos, o entrenamiento de redes neuronales, y no es necesaria ninguna experiencia de programación.

### Objetivos clave y resultados

- **Automatización del análisis de la postura animal para estudios científicos:**

  El objetivo principal de la tecnología DeepLabCut es medir y rastrear la postura de los animales en diversos entornos. Estos datos se pueden utilizar, por ejemplo, en estudios de neurociencia para entender cómo el cerebro controla el movimiento, o para aclarar como interactúan socialmente los animales. Los investigadores han observado un [aumento de rendimiento diez veces mayor](https://www.biorxiv.org/content/10.1101/457242v1) con DeepLabCut. Las posturas se pueden inferir sin conexión hasta a 1200 fotogramas por segundo (FPS).

- **Creación de un conjunto de herramientas de Python de fácil uso para la estimación de postura:**

  DeepLabCut quería compartir su tecnología de estimación de postura animal en la forma de una herramienta de fácil uso que pueda ser adoptada fácilmente por los investigadores. Así que han creado un conjunto de herramientas de Python completo y de fácil uso, también con características de administración de proyectos. Estas permiten no solo la automatización de la estimación de postura, sino también administrar el proyecto de punta a punta ayudando al usuario del conjunto de herramientas de DeepLabCut desde la etapa de recolección del conjunto de datos para crear flujos de trabajo de análisis compartibles y reutilizables.

  Su [conjunto de herramientas][DLCToolkit] ahora está disponible como código abierto.

  En flujo de trabajo típico de DeepLabCut incluye:

  - creación y refinamiento de los conjuntos de entrenamiento a través del aprendizaje activo
  - creación de redes neuronales a medida para animales y escenarios específicos
  - código para inferencia a gran escala en videos
  - graficar las inferencias utilizando herramientas de visualización integradas

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png'
title = 'Pasos de estimación de la postura con DeepLabCut'
alt = 'dlcsteps'
align = 'center'
attribution = '(Source: DeepLabCut)'
attributionlink = 'https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1'
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### Los desafíos

- **Velocidad**

  Procesamiento rápido de videos de comportamiento animal para medir su comportamiento y al mismo tiempo hacer experimentos científicos más eficientes y precisos.
  La extracción detallada de posturas del animal para experimentos de laboratorio, sin marcadores, en entornos dinámicamente cambiantes, puede ser un desafío tanto técnico como en términos de recursos necesarios y datos de entrenamiento requeridos.
  Proponer una herramienta que sea fácil de usar sin necesidad de habilidades como experiencia en visión por computador que permita a los científicos hacer investigaciones en más contextos del mundo real, es un problema que no es trivial de resolver.

- **Combinatoria**

  La combinatoria involucra el armado e integración del movimiento de múltiples extremidades en el comportamiento animal individual. Ensamblar puntos clave y sus conexiones en movimientos individuales de animales y vincularlos a lo largo del tiempo es un proceso complejo que requiere un análisis numérico intensivo, especialmente en el caso del seguimiento de movimientos de múltiples animales en videos de experimentos.

- **Procesamiento de Datos**

  Por último, pero no menos importante, la manipulación de arreglos - procesamiento de grandes pilas de arreglos correspondientes a varias imágenes, tensores objetivo y puntos clave es bastante desafiante.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png'
title = 'Estimación de variedad y complejidad de postura'
alt = 'challengesfig'
align = 'center'
attribution = '(Fuente: Mackenzie Mathis)'
attributionlink = 'https://www.iorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## El rol de NumPy para afrontar los desafíos de la estimación de postura

NumPy aborda la necesidad central de cálculos numéricos de la tecnología DeepLabCut a alta velocidad para análisis de comportamiento.  Además de NumPy, DeepLabCut emplea varios softwares de Python que utilizan NumPy en su núcleo, como [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) y [Tensorflow](https://www.tensorflow.org).

Las siguientes características de NumPy juegan un papel clave en el tratamiento del procesamiento de imágenes, requerimientos de combinatoria y la necesidad del cálculo rápido en los algoritmos de estimación de postura de DeepLabCut:

- Vectorización
- Operaciones de arreglos enmascarados
- Álgebra lineal
- Muestreo aleatorio
- Redimensión de arreglos grandes

DeepLabCut utiliza las capacidades de arreglo de NumPy a lo largo del flujo de trabajo ofrecido por el conjunto de herramientas. En particular, NumPy se utiliza para muestrear diferentes fotogramas para etiquetado de anotaciones humanas, y para escribir, editar y procesar datos de anotación.  Dentro de TensorFlow la red neuronal es entrenada por la tecnología DeepLabCut a lo largo de miles de iteraciones para predecir las anotaciones verdaderas a partir de los fotogramas. Para este propósito, se crean densidades objetivo (mapa de puntuaciones) para moldear la estimación de postura como un problema de traducción de imagen a imagen. Para hacer robustas a las redes neuronales, se emplea aumento de datos, que requiere el cálculo de mapas de puntuaciones objetivo sujetas a varios pasos geométricos y de procesamiento de imagen. Para hacer que el entrenamiento sea rápido, se aprovechan las capacidades de vectorización de NumPy. Para la inferencia, es necesario extraer las predicciones más probables de los mapas de puntuación objetivo y necesita eficientemente "enlazar predicciones para ensamblar animales individuales".

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png'
title = 'Flujo de Trabajo de DeepLabCut'
alt = 'flujo de trabajo'
attribution = '(Fuente: Mackenzie Mathis)'
attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## Resumen

Observar y describir eficientemente el comportamiento es un punto central de la etología moderna, neurociencia, medicina y tecnología.
Observar y describir eficientemente el comportamiento es un punto central de la etología moderna, neurociencia, medicina y tecnología. Con solo un pequeño conjunto de imágenes de entrenamiento, el conjunto de herramientas de Python de DeepLabCut permite entrenar una red neuronal dentro de la precisión de etiquetado a nivel humano, expandiendo así su aplicación no solo al análisis del comportamiento en el laboratorio, sino también potencialmente en deportes, análisis de la forma de caminar, medicina y estudios de rehabilitación. Los desafíos de la combinatoria compleja y procesamiento de datos enfrentados por los algoritmos de DeepLabCut se abordan mediante el uso de las capacidades de manipulación de arreglos de NumPy.

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png'
alt = 'beneficios de NumPy'
title = 'Capacidades claves utilizadas de NumPy'
{{< /figure >}}
