---
title: "Estudio de Caso: Descubrimiento de Ondas Gravitacionales"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
  by="David Shoemaker, _Colaboración científica LIGO_" >}}
{{< /blockquote >}}

## Acerca de [Ondas Gravitacionales](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) y [LIGO](https://www.ligo.caltech.edu)

Las ondas gravitacionales son ondulaciones en el tejido del espacio y el tiempo, generadas por
cataclismos en el universo, tales como la colisión y fusión de dos agujeros
negros o la coalescencia de estrellas binarias o supernovas. La observación de Ondas Gravitacionales no solo puede ayudar en el estudio de la gravedad, sino también en la comprensión de algunos de los fenómenos oscuros en el universo distante y su impacto.

El [Observatorio de Ondas Gravitacionales por Interferometría Láser (LIGO)](https://www.ligo.caltech.edu) fue diseñado para abrir el campo de la astrofísica de ondas gravitacionales mediante la detección directa de las ondas gravitacionales predichas por la Teoría General de la Relatividad de Einstein. Comprende dos interferómetros ampliamente separados dentro de los Estados Unidos: uno en Hanford, Washington, y el otro en Livingston, Louisiana, operando al unísono para detectar ondas gravitacionales. Cada uno de ellos tiene
detectores de ondas gravitacionales de escala de múltiples kilómetros que utilizan interferometría de láser.  La Colaboración Científica de LIGO (LSC) es un grupo de más de 1000 científicos de universidades de los Estados Unidos y de otros 14 países, respaldados por más de 90 universidades e institutos de investigación; aproximadamente 250 estudiantes contribuyen activamente a la colaboración. El nuevo descubrimiento de LIGO es la primera observación de ondas gravitacionales, realizada midiendo las diminutas perturbaciones que las ondas generan en el espacio y el tiempo a medida que pasan a través de la Tierra.  Ha abierto nuevas fronteras astrofísicas
que exploran el lado deformado del universo: objetos y fenómenos que están
hechos de espaciotiempo deformado.

### Objetivos Clave

- Aunque su [misión](https://www.ligo.caltech.edu/page/what-is-ligo) es detectar ondas gravitacionales de algunos de los procesos más violentos y energéticos del Universo, los datos que LIGO recopila pueden tener efectos de gran alcance en muchas áreas de la física, incluyendo gravitación, relatividad, astrofísica, cosmología, física de partículas y física nuclear.
- Procesar los datos observados mediante cálculos de relatividad numéricos que implican matemáticas complejas para discernir la señal del ruido, filtrar la señal relevante y estimar estadísticamente la significancia de los datos observados
- Visualización de datos para que los resultados binarios/numéricos puedan ser comprendidos.

### Los Desafíos

- **Cálculo**

  Las Ondas Gravitacionales son difíciles de detectar, ya que producen un efecto muy pequeño y tienen una diminuta interacción con la materia. Procesar y analizar todos los datos de LIGO requiere una vasta infraestructura informática. Después de ocuparse del ruido, que es miles de millones de veces mayor que la señal, aún quedan ecuaciones de relatividad muy complejas y enormes cantidades de datos que suponen un desafío computacional: [se necesitan aproximadamente O(10^7) horas de CPU para los análisis de fusiones binarias](https://youtu.be/7mcHknWWzNI), distribuidas en 6 clústeres dedicados de LIGO

- **Avalancha de Datos**

  A medida que los dispositivos de observación se vuelven más sensibles y confiables, los desafíos planteados por la avalancha de datos y encontrar una aguja en un pajar aumentan exponencialmente.
  ¡LIGO genera terabytes de datos cada día! Dar sentido a estos datos requiere de un esfuerzo enorme para todas y cada una de las detecciones. Por ejemplo, las señales recolectadas por LIGO deben ser comparadas por supercomputadoras contra cientos de miles de plantillas de posibles señales de ondas gravitacionales.

- **Visualización**

  Una vez superados los obstáculos relacionados con comprender suficientemente bien las ecuaciones de Einstein para resolverlas utilizando supercomputadoras, el siguiente gran desafío fue hacer que los datos fueran comprensibles para el cerebro humano. La modelación de simulación, así como la detección de señales, requieren técnicas de visualización efectivas.  La visualización también desempeña un papel en otorgar más credibilidad a la relatividad numérica a los ojos de los aficionados a la ciencia pura, los cuales no le daban suficiente importancia a la relatividad numérica hasta que las imágenes y simulaciones facilitaron la comprensión de los resultados para un público más amplio.
  La velocidad de los cálculos complejos y la renderización, así como la re-renderización de imágenes y simulaciones utilizando los últimos datos experimentales y conocimientos, puede ser una actividad que consume mucho tiempo y que representa un desafío para los investigadores en este campo.

{{< figure >}}
{{< /figure >}}

## El Papel de NumPy en la Detección de Ondas Gravitacionales

Las ondas gravitacionales emitidas por la fusión no pueden ser calculadas utilizando ninguna técnica excepto la relatividad numérica por fuerza bruta usando supercomputadoras.
La cantidad de datos que LIGO recopila es tan incomprensiblemente grande como pequeñas son las señales de onda
gravitacionales.

NumPy, el paquete de análisis numérico estándar para Python, fue utilizado por
el software empleado en varias tareas realizadas durante el proyecto de detección de Ondas Gravitacionales
en LIGO. NumPy ayudó a resolver las matemáticas complejas y la manipulación de datos a alta velocidad.  Aquí hay algunos ejemplos:

- [Procesamiento de Señales](https://www.uv.es/virgogroup/Denoising_ROF.html): Detección de fallos, [Identificación de ruido y caracterización de datos](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
- Recuperación de datos: Decidir qué datos pueden ser analizados, y determinar si estos contienen una señal - aguja en un pajar
- Análisis estadístico: estimar la significancia estadística de los datos observados, estimar los parámetros de señal (por ejemplo, masas de estrellas, velocidad de giro y distancia) en comparación con un modelo.
- Visualización de datos
  - Series de tiempo
  - Espectrogramas
- Cálculo de Correlaciones
- [Software clave](https://github.com/lscsoft) desarrollado en análisis de datos de Ondas Gravitacionales como [GwPy](https://gwpy.github.io/docs/stable/overview.html) y [PyCBC](https://pycbc.org) utiliza NumPy y AstroPy bajo su cubierta para proporcionar interfaces basadas en objetos para utilidades, herramientas y métodos para el estudio de datos provenientes de detectores de ondas gravitacionales.

{{< figure >}}
{{< /figure >}}

----

{{< figure >}}
{{< /figure >}}

## Resumen

La detección de ondas gravitacionales ha permitido a los investigadores descubrir fenómenos completamente inesperados, al tiempo que proporciona nuevos conocimientos sobre muchos de los fenómenos astrofísicos más profundos conocidos. El procesamiento de datos y la visualización de datos son pasos cruciales que ayudan a los científicos a obtener información a partir de los datos recopilados en las observaciones científicas y a comprender los resultados. Los cálculos son complejos y
no pueden ser comprendidos por humanos, a menos que sean visualizados utilizando simulaciones
por computador que se alimenten con datos observados reales y análisis.  NumPy, junto con otros paquetes de Python como matplotlib, pandas y scikit-learn, está [permitiendo a los investigadores](https://www.gw-openscience.org/events/GW150914/) responder preguntas complejas y descubrir nuevos horizontes en nuestra comprensión del universo.

{{< figure >}}
{{< /figure >}}
