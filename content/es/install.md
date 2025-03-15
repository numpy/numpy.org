---
title: Instalando NumPy
sidebar: false
---

La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, usted podría necesitar otra herramienta (hay muchas!) para manejar entornos o dependencias complejas.
NumPy se puede instalar con `conda`, con `pip`, con un gestor de paquetes en macOS y Linux, o [a partir del código fuente](https://numpy.org/devdocs/building). El único prerrequisito para instalar NumPy es Python. Si aún no tienes Python y quieres la forma más sencilla de comenzar, te recomendamos que uses la [Distribución Anaconda](https://www.anaconda.com/download) - incluye Python, NumPy y muchos otros paquetes comúnmente utilizados para la computación científica y la ciencia de datos.
{{< /admonition >}}

The recommended method of installing NumPy depends on your preferred workflow. Below, we break down the installation methods into the following categories:

- **Project-based** (e.g., uv, pixi) *(recommended for new users)*
- **Environment-based** (e.g., pip, conda) *(the traditional workflow)*
- **System package managers** *(not recommended for most users)*
- **Building from source** *(for advanced users and development purposes)*

Choose the method that best suits your needs. If you're unsure, start with the **Environment-based** method using `conda` or `pip`.

Below are the different methods for **installing NumPy**. Click on the tabs to explore each method:
También al utilizar pip, es buena práctica utilizar un entorno virtual - vea  [Instalaciones Reproducibles](#reproducible-installs) a continuación para saber por qué, y [esta guía](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) para más detalles sobre el uso de entornos virtuales.

[[tab]] name = 'Project Based' content = '''

Recommended for new users who want a streamlined workflow.

- **uv:** A modern Python package manager designed for speed and simplicity.
  ```bash
  uv pip install numpy
  ```

- **pixi:** A cross-platform package manager for Python and other languages.
  ```bash
  pixi add numpy
  ```

Tanto en Windows, macOS y Linux:

Para usuarios que conocen, por preferencia personal o leyendo acerca de las diferencias principales entre conda y pip a continuación, y prefieren una solución basada en pip/PyPI, recomendamos:

Las dos herramientas principales que instalan paquetes de Python son `pip` y `conda`. Para desarrollo web y de propósito general en Python existe un completo [conjunto de herramientas ](https://packaging.python.org/guides/tool-recommendations/)complementario a pip. Para computación de alto rendimiento (HPC), [Spack](https://github.com/spack/spack) amerita ser considerado.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. Sus funcionalidades se traslapan parcialmente (por ejemplo, ambas pueden instalar `numpy`); no obstante, también pueden trabajar conjuntamente.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema e instala paquetes para esa misma versión de Python solamente. Esto también significa que conda puede instalar librerías que no sean de Python y herramientas que usted pueda necesitar (por ejemplo, compiladores, CUDA, HDF5), mientras que pip no.

The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.

- **Conda:** If you use conda, you can install NumPy from the defaults or conda-forge channels:
  ```bash
  conda create -n my-env
  conda activate my-env
  conda install numpy
  ```
- **Pip:**
  ```bash
  pip install numpy
  ```
La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, usted podría necesitar otra herramienta (hay muchas!) para manejar entornos o dependencias complejas.
**Tip:** Use a virtual environment for better dependency management
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy
  ```
'''

[[tab]] name = 'System Package Managers' content = ''' Not recommended for most users, but available for convenience.

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
sudo apt install python3-numpy
```
**Windows (Chocolatey):**
```bash
choco install numpy
```

'''

[[tab]] name = 'Building from Source' content = ''' For advanced users and developers who want to customize or debug **NumPy**.

A word of warning: building Numpy from source can be a nontrivial exercise. We recommend using binaries instead if those are available for your platform via one of the above methods. For details on how to build from source, see [the building from source guide in the Numpy docs](https://numpy.org/devdocs/building/).

'''
{{< /tabs >}}

## Recomendaciones

After installing NumPy, verify the installation by running the following in a Python shell or script:
```python
import numpy as np
print(np.__version__)
```

This should print the installed version of NumPy without errors.

## Resolución de problemas

Si su instalación falla con el siguiente mensaje, revise el siguiente enlace [Resolución de problemas ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
¡IMPORTANTE: POR FAVOR LEA ESTO COMO SUGERENCIA PARA RESOLVER ESTE PROBLEMA!

La importación de las extensiones-c de numpy falló. Este error puede ocurrir por varias razones, siendo frecuente debido a problemas con su configuración.
```

