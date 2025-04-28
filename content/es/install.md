---
title: Instalando NumPy
sidebar: false
---

{{< admonition >}}
{{< /admonition >}}

El método recomendado para instalar NumPy depende de tu flujo de trabajo preferido. A continuación, desglosamos los métodos de instalación en las siguientes categorías:

- **Project-based** (e.g., uv, pixi) _(recommended for new users)_
- **Environment-based** (e.g., pip, conda) _(the traditional workflow)_
- **System package managers** _(not recommended for most users)_
- **Building from source** _(for advanced users and development purposes)_

Elija el método que mejor se adapte a sus necesidades. If you're unsure, start with the **Environment-based** method using `conda` or `pip`.

{{< tabs >}}

[[tab]]
name = 'Basado en proyectos'
contenido = '''

Recomendado para usuarios que quieran un flujo de trabajo simplificado.

- **uv:** A modern Python package manager designed for speed and simplicity.

    uv pip install numpy

- **pixi:** A cross-platform package manager for Python and other languages.

    pixi add numpy

'''

Para usuarios que conocen, por preferencia personal o leyendo acerca de las diferencias principales entre conda y pip a continuación, y prefieren una solución basada en pip/PyPI, recomendamos:

The two main tools that install Python packages are `pip` and `conda`. Their functionality partially overlaps (e.g. both can install `numpy`), however, they can also work together. Para computación de alto rendimiento (HPC), <a href="https://github.com/spack/spack">Spack</a> amerita ser considerado.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema y solamente instala paquetes para esa misma versión de Python. Sus funcionalidades se traslapan parcialmente (por ejemplo, ambas pueden instalar <code>numpy</code>); no obstante, también pueden trabajar conjuntamente.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema e instala paquetes para esa misma versión de Python solamente. Esto también significa que conda puede instalar librerías
que no sean de Python y herramientas que usted pueda necesitar (por ejemplo, compiladores, CUDA, HDF5), mientras que
pip no.

The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.

- **Conda:** If you use conda, you can install NumPy from the defaults or conda-forge channels:

    conda create -n my-env
    conda activate my-env
    conda install numpy
- **Pip:**

    pip install numpy

{{< admonition >}}
{{< /admonition >}}

  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy

'''

[[tab]]
name = 'Administradores de paquetes de sistema'
content = '''
No recomendado para la mayoría de los usuarios, pero disponible por conveniencia.

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

[[tab]]
name = 'Building from Source'
content = '''
For advanced users and developers who want to customize or debug **NumPy**.

Una palabra de advertencia: construir Numpy a partir del código fuente puede ser un ejercicio no trivial.
En su lugar, recomendamos usar binarios si estos están disponibles para su plataforma, a través de uno de los métodos anteriores.
For details on how to build from source, see [the building from source guide in the Numpy docs](https://numpy.org/devdocs/building/).

{{< /tabs >}}

## Recomendaciones

Después de instalar NumPy, verifica la instalación ejecutando lo siguiente en una terminal o en un script de Python:

```python
import numpy as np
print(np.__version__)
```

Esto debería imprimir la versión instalada de NumPy sin errores.

## Resolución de problemas

If your installation fails with the message below, see Troubleshooting
ImportError.

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

