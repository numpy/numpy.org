---
title: "Caso de estudio: DeepLabCut Estimación de Postura 3D"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="{{< blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/" by="Alexander Mathis, _Profesor Asistente, Escuela Politécnica Federal de Lausana_ ([EPFL](https://www.epfl.ch/en/))""
  by="Alexander Mathis, _Assistant Professor, École polytechnique fédérale de Lausanne_ ([EPFL](https://www.epfl.ch/en/))"
>}}
{{< /blockquote >}}

## Acerca de DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) es una caja de herramientas de código abierto que permite a los investigadores de cientos de instituciones de todo el mundo rastrear el comportamiento de animales de laboratorio, con muy pocos datos de entrenamiento, con una precisión de nivel humana. Con la tecnología DeepLabCut, los científicos pueden profundizar en la comprensión científica del control motriz y el comportamiento a través de especies animales y escalas temporales.

Muchas áreas de investigación, incluyendo la neurociencia, la medicina y la biomecánica, utilizan datos para rastrear el movimiento animal. DeepLabCut ayuda a entender lo que los humanos y otros animales están haciendo, analizando las acciones que han sido grabadas en la filmación. Utilizando la automatización para tareas laboriosas de etiquetado y monitoreo, junto con el análisis de datos basado en redes neuronales profundas, DeepLabCut realiza estudios científicos que involucran la observación de animales, tales como primates, ratones, peces, moscas, etc. de manera mucho más rápida y precisa.

{{< figure >}}
{{< /figure >}}

El rastreo del comportamiento no invasivo de animales de DeepLabCut por medio de la extracción de posturas de animales es crucial para propósitos científicos en dominios tales como la biomecánica, genética, etología y & neurociencia. Medir las poses de animales de manera no invasiva a partir de video - sin marcadores - en fondos que cambian dinámicamente es un desafío computacional, tanto técnicamente como en términos de necesidades de recursos y datos de entrenamiento requeridos.

DeepLabCut permite a los investigadores estimar la postura del sujeto, permitiéndoles eficientemente cuantificar el comportamiento a través de una caja de herramientas de software basada en Python.  Con DeepLabCut, los investigadores pueden identificar fotogramas distintos de videos, etiquetar digitalmente partes específicas del cuerpo en unas pocas docenas de fotogramas con una GUI personalizada, y luego las arquitecturas de estimación de posturas basadas en aprendizaje profundo en DeepLabCut aprenden a identificar esas mismas características en el resto del video y en otros videos similares de animales. Funciona en diferentes especies de animales, desde los animales de laboratorio comunes como moscas y ratones hasta animales más inusuales como los [guepardos][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut utiliza un principio llamado [aprendizaje por transferencia](https://arxiv.org/pdf/1909.11229), que reduce considerablemente la cantidad de datos de entrenamiento requeridos y acelera la convergencia del período de entrenamiento.  Dependiendo de las necesidades, los usuarios pueden seleccionar diferentes arquitecturas de red que proporcionan una inferencia más rápida (por ejemplo MobileNetV2), que también pueden combinarse con retroalimentación experimental en tiempo real. Dependiendo de las necesidades, los usuarios pueden seleccionar diferentes arquitecturas de red que proporcionan una inferencia más rápida (por ejemplo MobileNetV2), que también pueden combinarse con retroalimentación experimental en tiempo real. El paquete ahora ha sido significativamente modificado para incluir arquitecturas adicionales, métodos de aumento y una experiencia de usuario completa en el front-end. Además, para apoyar los experimentos biológicos a gran escala, DeepLabCut proporciona capacidades de aprendizaje activo para que los usuarios puedan aumentar el conjunto de entrenamiento a lo largo del tiempo para cubrir casos límite y hacer que su algoritmo de estimación de postura sea robusto dentro de un contexto específico.

Recientemente, se presentó el [modelo zoo de DeepLabCut](https://deeplabcut.github.io/DeepLabCut/docs/ModelZoo.html) que proporciona modelos pre-entrenados para varias especies y condiciones experimentales, desde análisis facial en primates hasta posturas en caninos. Esto se puede ejecutar, por ejemplo, en la nube sin ningún etiquetado de datos nuevos o entrenamiento de redes neuronales, y no es necesaria ninguna experiencia de programación.

### Objetivos y Resultados Clave

- **Automatización del análisis de la postura animal para estudios científicos:**

  El objetivo principal de la tecnología DeepLabCut es medir y rastrear la postura de los animales en diversos entornos. Estos datos se pueden utilizar, por ejemplo, en estudios de neurociencia para entender cómo el cerebro controla el movimiento, o para aclarar como interactúan socialmente los animales. Los investigadores han observado un [aumento de rendimiento diez veces mayor](https://www.biorxiv.org/content/10.1101/457242v1) con DeepLabCut. Las posturas se pueden inferir sin conexión hasta a 1200 fotogramas por segundo (FPS).

- **Creación de un conjunto de herramientas de Python de fácil uso para la estimación de postura:**

  DeepLabCut quería compartir su tecnología de estimación de postura animal en la forma de una herramienta de fácil uso que pueda ser adoptada fácilmente por los investigadores. Así que han creado un conjunto de herramientas de Python completo y de fácil uso, también con características de administración de proyectos. Estas permiten no solo la automatización de la estimación de postura, sino también administrar el proyecto de punta a punta ayudando al usuario del conjunto de herramientas de DeepLabCut desde la etapa de recolección del conjunto de datos para crear flujos de trabajo de análisis compartibles y reutilizables.

  Su [conjunto de herramientas][DLCToolkit] ahora está disponible como código abierto.

  En flujo de trabajo típico de DeepLabCut incluye:

  - creación y refinamiento de los conjuntos de entrenamiento a través del aprendizaje activo
  - creación de redes neuronales a la medida para animales y escenarios específicos
  - código para inferencia a gran escala en videos
  - graficar las inferencias utilizando herramientas de visualización integradas

{{< figure >}}
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### Los Desafíos

- **Velocidad**

  Procesamiento rápido de videos de comportamiento animal para medir su comportamiento y al mismo tiempo hacer experimentos científicos más eficientes y precisos.
  La extracción detallada de posturas del animal para experimentos de laboratorio, sin marcadores, en entornos dinámicamente cambiantes, puede ser un desafío tanto técnico como en términos de recursos necesarios y datos de entrenamiento requeridos.
  Proponer una herramienta que sea fácil de usar sin necesidad de habilidades como experiencia en visión por computador que permita a los científicos hacer investigaciones en más contextos del mundo real, es un problema que no es trivial de resolver.

- **Combinatoria**

  La combinatoria involucra el armado e integración del movimiento de múltiples extremidades en el comportamiento animal individual. Ensamblar puntos clave y sus conexiones en movimientos individuales de animales y vincularlos a lo largo del tiempo es un proceso complejo que requiere un análisis numérico intensivo, especialmente en el caso del seguimiento de movimientos de múltiples animales en videos de experimentos.

- **Procesamiento de Datos**

  Por último, pero no menos importante, la manipulación de arreglos - procesamiento de grandes pilas de arreglos correspondientes a varias imágenes, tensores objetivo y puntos clave es bastante desafiante.

{{< figure >}}
{{< /figure >}}

## El Papel de NumPy para afrontar los desafíos de la estimación de postura

NumPy aborda la necesidad central de la tecnología de DeepLabCut de realizar cálculos numéricos a alta velocidad para el análisis del comportamiento.  Además de NumPy, DeepLabCut emplea varios softwares de Python que utilizan NumPy en su núcleo, como [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) y [Tensorflow](https://www.tensorflow.org).

Las siguientes características de NumPy jugaron un papel clave en abordar el procesamiento de imágenes, los requisitos de combinatoria y la necesidad de cálculos rápidos en los algoritmos de estimación de posturas de DeepLabCut:

- Vectorización
- Operaciones con Arreglos Enmascarados
- Álgebra lineal
- Muestreo Aleatorio
- Redimensionamiento de arreglos grandes

DeepLabCut utiliza las capacidades de arreglos de NumPy a lo largo del flujo de trabajo ofrecido por el conjunto de herramientas. En particular, NumPy se utiliza para muestrear diferentes fotogramas para etiquetado de anotaciones humanas, y para escribir, editar y procesar datos de anotación.  Dentro de TensorFlow, la red neuronal es entrenada por la tecnología DeepLabCut durante miles de iteraciones para predecir las anotaciones de referencia a partir de fotogramas. Para este propósito, se crean densidades objetivo (mapas de puntuación) para plantear la estimación de poses como un problema de traducción de imagen a imagen. Para hacer que las redes neuronales sean robustas, se emplea el aumento de datos, lo que requiere el cálculo de mapas de puntuación objetivo sujetos a varios pasos geométricos y de procesamiento de imágenes. Para hacer que el entrenamiento sea rápido, se aprovechan las capacidades de vectorización de NumPy. Para la inferencia, es necesario extraer las predicciones más probables de los mapas de puntuación objetivo y "vincular eficientemente las predicciones para ensamblar animales individuales".

{{< figure >}}
{{< /figure >}}

## Resumen

Observar y describir eficientemente el comportamiento es un punto central de la etología moderna, neurociencia, medicina y tecnología.
Observar y describir eficientemente el comportamiento es un punto central de la etología moderna, neurociencia, medicina y tecnología. Con solo un pequeño conjunto de imágenes de entrenamiento, el conjunto de herramientas de Python de DeepLabCut permite entrenar una red neuronal con una precisión de etiquetado a nivel humano, expandiendo así su aplicación no solo al análisis del comportamiento en el laboratorio, sino también potencialmente en deportes, análisis de marcha, medicina y estudios de rehabilitación. Los desafíos de la combinatoria compleja y procesamiento de datos enfrentados por los algoritmos de DeepLabCut se abordan mediante el uso de las capacidades de manipulación de arreglos de NumPy.

{{< figure >}}
{{< /figure >}}
