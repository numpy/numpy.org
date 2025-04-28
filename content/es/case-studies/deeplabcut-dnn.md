---
title: "Caso de estudio: DeepLabCut Estimación de Postura 3D"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/"
  by="Alexander Mathis, _Assistant Professor, École polytechnique fédérale de Lausanne_ ([EPFL](https://www.epfl.ch/en/))"
>}}
{{< /blockquote >}}

## Acerca de DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) is an open source toolbox that empowers researchers at hundreds of institutions worldwide to track behaviour of laboratory animals, with very little training data, at human-level accuracy. Con la tecnología DeepLabCut, los científicos pueden profundizar en la comprensión científica del control motriz y el comportamiento a través de especies animales y escalas temporales.

Muchas áreas de investigación, incluyendo la neurociencia, la medicina y la biomecánica, utilizan datos para rastrear el movimiento animal. DeepLabCut ayuda a entender lo que los humanos y otros animales están haciendo, analizando las acciones que han sido grabadas en la filmación. Utilizando la automatización para tareas laboriosas de etiquetado y monitoreo, junto con el análisis de datos basado en redes neuronales profundas, DeepLabCut realiza estudios científicos que involucran la observación de animales, tales como primates, ratones, peces, moscas, etc. de manera mucho más rápida y precisa.

{{< figure >}}
{{< /figure >}}

DeepLabCut's non-invasive behavioral tracking of animals by extracting the poses of animals is crucial for scientific pursuits in domains such as biomechanics, genetics, ethology & neuroscience. Medir las poses de animales de manera no invasiva a partir de video - sin marcadores - en fondos que cambian dinámicamente es un desafío computacional, tanto técnicamente como en términos de necesidades de recursos y datos de entrenamiento requeridos.

DeepLabCut permite a los investigadores estimar la postura del sujeto, permitiéndoles eficientemente cuantificar el comportamiento a través de una caja de herramientas de software basada en Python.  Con DeepLabCut, los investigadores pueden identificar fotogramas distintos de videos, etiquetar digitalmente partes específicas del cuerpo en unas pocas docenas de fotogramas con una GUI personalizada, y luego las arquitecturas de estimación de posturas basadas en aprendizaje profundo en DeepLabCut aprenden a identificar esas mismas características en el resto del video y en otros videos similares de animales. It works across species of animals, from common laboratory animals such as flies and mice to more unusual animals like [cheetahs][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut uses a principle called [transfer learning](https://arxiv.org/pdf/1909.11229), which greatly reduces the amount of training data required and speeds up the convergence of the training period.  Dependiendo de las necesidades, los usuarios pueden seleccionar diferentes arquitecturas de red que proporcionan una inferencia más rápida (por ejemplo MobileNetV2), que también pueden combinarse con retroalimentación experimental en tiempo real. DeepLabCut originally used the feature detectors from a top-performing human pose estimation architecture, called [DeeperCut](https://arxiv.org/abs/1605.03170), which inspired the name. El paquete ahora ha sido significativamente modificado para incluir arquitecturas adicionales, métodos de aumento y una experiencia de usuario completa en el front-end. Además, para apoyar los experimentos biológicos a gran escala, DeepLabCut proporciona capacidades de aprendizaje activo para que los usuarios puedan aumentar el conjunto de entrenamiento a lo largo del tiempo para cubrir casos límite y hacer que su algoritmo de estimación de postura sea robusto dentro de un contexto específico.

Recently, the [DeepLabCut model zoo](https://deeplabcut.github.io/DeepLabCut/docs/ModelZoo.html) was introduced, which provides pre-trained models for various species and experimental conditions from facial analysis in primates to dog posture. Esto se puede ejecutar, por ejemplo, en la nube sin ningún etiquetado de datos nuevos o entrenamiento de redes neuronales, y no es necesaria ninguna experiencia de programación.

### Objetivos y Resultados Clave

- **Automation of animal pose analysis for scientific studies:**

  The primary objective of DeepLabCut technology is to measure and track posture
  of animals in a diverse settings. This data can be used, for example, in
  neuroscience studies to understand how the brain controls movement, or to
  elucidate how animals socially interact. Researchers have observed a
  [tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1)
  with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second
  (FPS).

- **Creation of an easy-to-use Python toolkit for pose estimation:**

  DeepLabCut wanted to share their animal pose-estimation technology in the form
  of an easy to use tool that can be adopted by researchers easily. So they have
  created a complete, easy-to-use Python toolbox with project management features
  as well. These enable not only automation of pose-estimation but also
  managing the project end-to-end by helping the DeepLabCut Toolkit user right
  from the dataset collection stage to creating shareable and reusable analysis
  pipelines.

  Their [toolkit][DLCToolkit] is now available as open source.

  En flujo de trabajo típico de DeepLabCut incluye:

  - creación y refinamiento de los conjuntos de entrenamiento a través del aprendizaje activo
  - creación de redes neuronales a la medida para animales y escenarios específicos
  - código para inferencia a gran escala en videos
  - graficar las inferencias utilizando herramientas de visualización integradas

{{< figure >}}
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### Los Desafíos

- **Speed**

  Fast processing of animal behavior videos in order to measure their behavior
  and at the same time make scientific experiments more efficient, accurate.
  Extracting detailed animal poses for laboratory experiments, without
  markers, in dynamically changing backgrounds, can be challenging, both
  technically as well as in terms of resource needs and training data required.
  Coming up with a tool that is easy to use without the need for skills such
  as computer vision expertise that enables scientists to do research in more
  real-world contexts, is a non-trivial problem to solve.

- **Combinatorics**

  Combinatorics involves assembly and integration of movement of multiple
  limbs into individual animal behavior. Assembling keypoints and their
  connections into individual animal movements and linking them across time
  is a complex process that requires heavy-duty numerical analysis, especially
  in case of multi-animal movement tracking in experiment videos.

- **Data Processing**

  Last but not the least, array manipulation - processing large stacks of
  arrays corresponding to various images, target tensors and keypoints is
  fairly challenging.

{{< figure >}}
{{< /figure >}}

## El Papel de NumPy para afrontar los desafíos de la estimación de postura

NumPy aborda la necesidad central de la tecnología de DeepLabCut de realizar cálculos numéricos a alta velocidad para el análisis del comportamiento.  Besides NumPy, DeepLabCut employs
various Python software that utilize NumPy at their core, such as
[SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org),
[matplotlib](https://matplotlib.org),
[Tensorpack](https://github.com/tensorpack/tensorpack),
[imgaug](https://github.com/aleju/imgaug),
[scikit-learn](https://scikit-learn.org/stable/),
[scikit-image](https://scikit-image.org) and
[Tensorflow](https://www.tensorflow.org).

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
[DeepLabCut](https://static1.squarespace.com/static/57f6d51c9f74566f55ecf271/t/5eab5ff7999bf94756b27481/1588289532243/NathMathis2019.pdf)
allows researchers to estimate the pose of the subject, efficiently enabling
them to quantify the behavior. Con solo un pequeño conjunto de imágenes de entrenamiento, el conjunto de herramientas de Python de DeepLabCut permite entrenar una red neuronal con una precisión de etiquetado a nivel humano, expandiendo así su aplicación no solo al análisis del comportamiento en el laboratorio, sino también potencialmente en deportes, análisis de marcha, medicina y estudios de rehabilitación. Los desafíos de la combinatoria compleja y procesamiento de datos enfrentados por los algoritmos de DeepLabCut se abordan mediante el uso de las capacidades de manipulación de arreglos de NumPy.

{{< figure >}}
{{< /figure >}}
