---
title: Instalando NumPy
sidebar: false
---

La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, usted podría necesitar otra herramienta (hay muchas!) para manejar entornos o dependencias complejas.
NumPy se puede instalar con `conda`, con `pip`, con un gestor de paquetes en macOS y Linux, o [a partir del código fuente](https://numpy.org/devdocs/building). El único prerrequisito para instalar NumPy es Python. Si aún no tienes Python y quieres la forma más sencilla de comenzar, te recomendamos que uses la [Distribución Anaconda](https://www.anaconda.com/download) - incluye Python, NumPy y muchos otros paquetes comúnmente utilizados para la computación científica y la ciencia de datos.
{{< /admonition >}}

El método recomendado para instalar NumPy depende de tu flujo de trabajo preferido. A continuación, desglosamos los métodos de instalación en las siguientes categorías:

- **Basado en proyectos** (por ejemplo, uv, pixi) *(recomendado para nuevos usuarios)*
- **Basado en entornos** (por ejemplo, pip, conda) *(el flujo de trabajo tradicional)*
- **Administradores de paquetes de sistema** *(no recomendado para la mayoría de usuarios)*
- **Construir a partir del código fuente** *(para usuarios avanzados y para fines de desarrollo)*

Elija el método que mejor se adapte a sus necesidades. Si tienes dudas, comienza con el método **basado en el entorno** usando `conda` o `pip`.

A continuación se muestran los diferentes métodos para **instalar NumPy**. Haz clic en las pestañas para explorar cada método:
También al utilizar pip, es buena práctica utilizar un entorno virtual - vea  [Instalaciones Reproducibles](#reproducible-installs) a continuación para saber por qué, y [esta guía](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) para más detalles sobre el uso de entornos virtuales.

[[tab]] name = 'Basado en proyectos' contenido = '''

Recomendado para usuarios que quieran un flujo de trabajo simplificado.

- **uv:** Un gestor de paquetes de Python moderno diseñado para velocidad y simplicidad.
  ```bash
  uv pip install numpy
  ```

- **pixi:** Un administrador de paquetes multiplataforma para Python y otros lenguajes.
  ```bash
  pixi add numpy
  ```

Tanto en Windows, macOS y Linux:

Para usuarios que conocen, por preferencia personal o leyendo acerca de las diferencias principales entre conda y pip a continuación, y prefieren una solución basada en pip/PyPI, recomendamos:

Las dos herramientas principales que instalan paquetes de Python son `pip` y `conda`. Para desarrollo web y de propósito general en Python existe un completo [conjunto de herramientas ](https://packaging.python.org/guides/tool-recommendations/)complementario a pip. Para computación de alto rendimiento (HPC), [Spack](https://github.com/spack/spack) amerita ser considerado.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema y solamente instala paquetes para esa misma versión de Python. Sus funcionalidades se traslapan parcialmente (por ejemplo, ambas pueden instalar `numpy`); no obstante, también pueden trabajar conjuntamente.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema e instala paquetes para esa misma versión de Python solamente. Esto también significa que conda puede instalar librerías que no sean de Python y herramientas que usted pueda necesitar (por ejemplo, compiladores, CUDA, HDF5), mientras que pip no.

La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, podrías necesitar otra herramienta (¡hay muchas!) para manejar entornos o dependencias complejas.

- **Conda:** Si utilizas conda, puedes instalar NumPy desde los canales predeterminados o los de conda-forge:
  ```bash
  
  ```
- **Pip:**
  ```bash
  pip install numpy
  ```
La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, usted podría necesitar otra herramienta (hay muchas!) para manejar entornos o dependencias complejas.
**Tip:** Use un entorno virtual para un mejor manejo de dependencias
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy
  ```
'''

[[tab]] name = 'Administradores de paquetes de sistema' content = ''' No recomendado para la mayoría de los usuarios, pero disponible por conveniencia.

**macOS (Homebrew):**
```bash
# La mejor práctica, utilizar un entorno en lugar de instalar en el entorno base
conda create -n my-env
conda activate my-env
# Si desea instalar desde conda-forge
conda config --env --add channels conda-forge
# El comando de instalación
conda install numpy
```
**Linux (APT):**
```bash

```
**Windows (Chocolatey):**
```bash
choco install numpy
```

'''

[[tab]] name = 'Construir a partir del código fuente' content = ''' Para usuarios avanzados y desarrolladores que quieren personalizar o depurar **NumPy**.

Una palabra de advertencia: construir Numpy a partir del código fuente puede ser un ejercicio no trivial. En su lugar, recomendamos usar binarios si estos están disponibles para su plataforma, a través de uno de los métodos anteriores. Para obtener más información sobre cómo construir desde el código fuente, revisa [la guía disponible en la documentación Numpy](https://numpy.org/devdocs/building/).

'''
{{< /tabs >}}

## Recomendaciones

Después de instalar NumPy, verifica la instalación ejecutando lo siguiente en una terminal o en un script de Python:
```python
import numpy as np
print(np.__version__)
```

Esto debería imprimir la versión instalada de NumPy sin errores.

## Resolución de problemas

Si su instalación falla con el siguiente mensaje, revise el siguiente enlace [Resolución de problemas ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
¡IMPORTANTE: POR FAVOR LEA ESTO COMO SUGERENCIA PARA RESOLVER ESTE PROBLEMA!

La importación de las extensiones-c de numpy falló. Este error puede ocurrir por varias razones, siendo frecuente debido a problemas con su configuración.
```

