---
title: Instalando NumPy
sidebar: false
---

{{< admonition tip >}}
This page assumes you are comfortable using a terminal and are familiar with package managers. 
The only prerequisite for installing NumPy is Python itself. If you don't have
Python yet and want the simplest way to get started, we recommend you use the
[Anaconda Distribution](https://www.anaconda.com/download) - it includes
Python, NumPy, and many other commonly used packages for scientific computing
and data science.
{{< /admonition >}}

El método recomendado para instalar NumPy depende de tu flujo de trabajo preferido. A continuación, desglosamos los métodos de instalación en las siguientes categorías:

- **Basado en proyectos** (por ejemplo, uv, pixi) _(recomendado para nuevos usuarios)_
- **Basado en entornos** (por ejemplo, pip, conda) _(el flujo de trabajo tradicional)_
- **Administradores de paquetes de sistema** _(no recomendado para la mayoría de usuarios)_
- **Construir a partir del código fuente** _(para usuarios avanzados y para fines de desarrollo)_

Elija el método que mejor se adapte a sus necesidades. Si tienes dudas, comienza con el método **basado en el entorno** usando `conda` o `pip`.

Below are the different methods for **installing NumPy**. Click on the tabs to explore each method:
{{< tabs >}}

[[tab]]
name = 'Basado en proyectos'
contenido = '''

Recomendado para usuarios que quieran un flujo de trabajo simplificado.

- **uv:** Un gestor de paquetes de Python moderno diseñado para velocidad y simplicidad.
  ```bash
  uv pip install numpy
  ```

- **pixi:** Un administrador de paquetes multiplataforma para Python y otros lenguajes.
  ```bash
  pixi add numpy
  ```

'''

[[tab]]
name = 'Environment Based'
content = '''

Las dos herramientas principales que instalan paquetes de Python son `pip` y `conda`. Sus funcionalidades se traslapan parcialmente (por ejemplo, ambas pueden instalar `numpy`); no obstante, también pueden trabajar conjuntamente. We’ll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema e instala paquetes para esa misma versión de Python solamente. Esto también significa que conda puede instalar librerías
que no sean de Python y herramientas que usted pueda necesitar (por ejemplo, compiladores, CUDA, HDF5), mientras que
pip no.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically “defaults” or “conda-forge”). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, podrías necesitar otra herramienta (¡hay muchas!) para manejar entornos o dependencias complejas.

- **Conda:** Si utilizas conda, puedes instalar NumPy desde los canales predeterminados o los de conda-forge:
  ```bash
  conda create -n my-env
  conda activate my-env
  conda install numpy
  ```
- **Pip:**
  ```bash
  pip install numpy
  ```

{{< admonition tip >}}
**Tip:** Use a virtual environment for better dependency management
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy
  ```

'''

[[tab]]
name = 'Administradores de paquetes de sistema'
content = '''
No recomendado para la mayoría de los usuarios, pero disponible por conveniencia.

**macOS (Homebrew):**
```bash
brew install numpy
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

[[tab]]
name = 'Construir a partir del código fuente'
content = '''

Para usuarios avanzados y desarrolladores que quieren personalizar o depurar **NumPy**.

Una palabra de advertencia: construir Numpy a partir del código fuente puede ser un ejercicio no trivial.
En su lugar, recomendamos usar binarios si estos están disponibles para su plataforma, a través de uno de los métodos anteriores.
Para obtener más información sobre cómo construir desde el código fuente, revisa [la guía disponible en la documentación Numpy](https://numpy.org/devdocs/building/).
'''
{{< /tabs >}}

## Verifying the Installation

Después de instalar NumPy, verifica la instalación ejecutando lo siguiente en una terminal o en un script de Python:
```python
import numpy as np
print(np.__version__)
```

Esto debería imprimir la versión instalada de NumPy sin errores.

## Resolución de problemas

Si su instalación falla con el siguiente mensaje, revise el siguiente enlace [Resolución de problemas ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

