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

* **Automation of animal pose analysis for scientific studies:**

  The primary objective of DeepLabCut technology is to measure and track posture of animals in a diverse settings. This data can be used, for example, in neuroscience studies to understand how the brain controls movement, or to elucidate how animals socially interact. Researchers have observed a [tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1) with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second (FPS).

* **Creation of an easy-to-use Python toolkit for pose estimation:**

  DeepLabCut wanted to share their animal pose-estimation technology in the form of an easy to use tool that can be adopted by researchers easily. So they have created a complete, easy-to-use Python toolbox with project management features as well. These enable not only automation of pose-estimation but also managing the project end-to-end by helping the DeepLabCut Toolkit user right from the dataset collection stage to creating shareable and reusable analysis pipelines.

  Their [toolkit][DLCToolkit] is now available as open source.

  A typical DeepLabCut Workflow includes:

  - creation and refining of training sets via active learning
  - creation of tailored neural networks for specific animals and scenarios
  - code for large-scale inference on videos
  - draw inferences using integrated visualization tools

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png' title = 'Pose estimation steps with DeepLabCut' alt = 'dlcsteps' align = 'center' attribution = '(Source: DeepLabCut)' attributionlink = 'https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1'
{{< /figure >}}

### The Challenges

* **Speed**

    Fast processing of animal behavior videos in order to measure their behavior and at the same time make scientific experiments more efficient, accurate. Extracting detailed animal poses for laboratory experiments, without markers, in dynamically changing backgrounds, can be challenging, both technically as well as in terms of resource needs and training data required. Coming up with a tool that is easy to use without the need for skills such as computer vision expertise that enables scientists to do research in more real-world contexts, is a non-trivial problem to solve.

* **Combinatorics**

    Combinatorics involves assembly and integration of movement of multiple limbs into individual animal behavior. Assembling keypoints and their connections into individual animal movements and linking them across time is a complex process that requires heavy-duty numerical analysis, especially in case of multi-animal movement tracking in experiment videos.

* **Data Processing**

    Last but not the least, array manipulation - processing large stacks of arrays corresponding to various images, target tensors and keypoints is fairly challenging.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png' title = 'Pose estimation variety and complexity' alt = 'challengesfig' align = 'center' attribution = '(Source: Mackenzie Mathis)' attributionlink = 'https://www.biorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## NumPy's Role in meeting Pose Estimation Challenges

NumPy addresses DeepLabCut technology's core need of numerical computations at high speed for behavioural analytics.  Besides NumPy, DeepLabCut employs various Python software that utilize NumPy at their core, such as [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) and [Tensorflow](https://www.tensorflow.org).

The following features of NumPy played a key role in addressing the image processing, combinatorics requirements and need for fast computation in DeepLabCut pose estimation algorithms:

* Vectorization
* Masked Array Operations
* Linear Algebra
* Random Sampling
* Reshaping of large arrays

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
