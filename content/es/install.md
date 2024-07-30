---
title: Installing NumPy
sidebar: false
---

The only prerequisite for installing NumPy is Python itself. If you don't have Python yet and want the simplest way to get started, we recommend you use the [Anaconda Distribution](https://www.anaconda.com/download) - it includes Python, NumPy, and many other commonly used packages for scientific computing and data science.

NumPy can be installed with `conda`, with `pip`, with a package manager on macOS and Linux, or [from source](https://numpy.org/devdocs/building). For more detailed instructions, consult our [Python and NumPy installation guide](#python-numpy-install-guide) below.

**CONDA**

If you use `conda`, you can install NumPy from the `defaults` or `conda-forge` channels:

```bash
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

**PIP**

If you use `pip`, you can install NumPy with:

```bash
pip install numpy
```
Also when using pip, it's good practice to use a virtual environment - see  [Reproducible Installs](#reproducible-installs) below for why, and [this guide](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) for details on using virtual environments.


<a name="python-numpy-install-guide"></a>

# Python and NumPy installation guide

Instalar y administrar paquetes en Python es complicado, hay un número de soluciones alternativas para la mayoría de tareas. Esta guía intenta dar al lector una idea de las mejores (o más populares) soluciones y dar recomendaciones claras. Se enfoca en los usuarios de Python, NumPy y del stack de PyData (o computación numérica) en sistemas operativos y hardware comunes.

## Recomendaciones

Empezaremos con recomendaciones basadas en el nivel de experiencia del usuario y el sistema operativo de interés. Si se encuentra entre "principiante" y "avanzado", por favor diríjase a "principiante" si quiere mantener las cosas simples, y a "avanzado" si quiere trabajar de acuerdo a las mejores prácticas que le servirán de mucho en el futuro.

### Usuarios principiantes

Tanto en Windows, macOS y Linux:

- Instale [Anaconda](https://www.anaconda.com/download) (esto instala todos los paquetes que necesita y todas las demás herramientas mencionadas a continuación).
- Para escribir y ejecutar código, utilice notebooks en [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) para computación exploratoria e interactiva, y [Spyder](https://www.spyder-ide.org/) o [Visual Studio Code](https://code.visualstudio.com/) para escribir scripts y paquetes.
- Utilice [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) para administrar sus paquetes e iniciar JupyterLab, Spyder o Visual Studio Code.


### Usuarios avanzados

#### Conda

- Instale [Miniforge](https://github.com/conda-forge/miniforge).
- Mantenga el entorno conda `base` mínimo, y utilice uno o más [entornos conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) para instalar el paquete que necesite para la tarea o proyecto en que está trabajando.

#### Alternativa si prefiere pip/PyPI

Para usuarios que conocen, por preferencia personal o leyendo acerca de las diferencias principales entre conda y pip a continuación, y prefieren una solución basada en pip/PyPI, recomendamos:
- Instalar Python desde [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/) o su administrador de paquetes Linux.
- Utilice [Poetry](https://python-poetry.org/) como la herramienta mejor mantenida que proporciona una resolución de dependencias y capacidades de administración de entornos de forma similar a la que lo hace conda.


## Gestión de paquetes de Python

La gestión de los paquetes es un problema desafiante y, como resultado, hay muchas herramientas. Para desarrollo web y de propósito general en Python existe un completo [conjunto de herramientas ](https://packaging.python.org/guides/tool-recommendations/)complementario a pip. Para computación de alto rendimiento (HPC), [Spack](https://github.com/spack/spack) amerita ser considerado. Sin embargo, para la mayoría de usuarios de NumPy, [conda](https://conda.io/en/latest/) y [pip](https://pip.pypa.io/en/stable/) son las dos herramientas más populares.


### Pip & conda

Las dos herramientas principales que instalan paquetes de Python son `pip` y `conda`. Sus funcionalidades se traslapan parcialmente (por ejemplo, ambas pueden instalar `numpy`); no obstante, también pueden trabajar conjuntamente. Discutiremos las principales diferencias entre pip y conda aquí - esto es importante comprenderlo si usted desea gestionar paquetes de manera efectiva.

La primera diferencia radica en que conda es multi-lenguaje y puede instalar Python, mientras que pip es instalado para una versión particular de Python en su sistema e instala paquetes para esa misma versión de Python solamente. Esto también significa que conda puede instalar librerías que no sean de Python y herramientas que usted pueda necesitar (por ejemplo, compiladores, CUDA, HDF5), mientras que pip no.

La segunda diferencia es que pip instala desde el Índice de Empaquetado de Python (PyPI - Python Packaging Index), mientras que conda instala desde sus propios canales (típicamente "defaults" o "conda-forge"). PyPI es, de lejos, la colección de paquetes más grande; sin embargo, todos los paquetes populares están también disponibles para conda.

La tercera diferencia consiste en que conda es una solución integrada para gestionar paquetes, dependencias y entornos; mientras que con pip, usted podría necesitar otra herramienta (hay muchas!) para manejar entornos o dependencias complejas.

<a name="reproducible-installs"></a>

### Instalaciones reproducibles

En la medida en que las librerías son actualizadas, los resultados al correr su código pueden cambiar, o su código puede fallar por completo. Es importante que sea capaz de reconstruir el conjunto de paquetes y versiones que usted está utilizando. La mejor práctica es:

1. usar un entorno diferente por cada proyecto en el cual usted esté trabajando,
2. almacenar los nombres de paquetes y versiones utilizando su instalador de paquetes, cada uno de los cuales tiene su propio formato de metadata para esto:
   - Conda: [entornos conda y environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - Pip: [entornos virtuales](https://docs.python.org/3/tutorial/venv.html) y [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [entornos virtuales y pyproject.toml](https://python-poetry.org/docs/basic-usage/)



## Paquetes NumPy & librerías de álgebra lineal aceleradas

NumPy no depende de ningún otro paquete de Python; sin embargo, sí depende de una librería de álgebra lineal acelerada - típicamente [Intel MKL](https://software.intel.com/en-us/mkl) u [OpenBLAS](https://www.openblas.net/). Los usuarios no tienen que preocuparse por instalar éstas (se incluyen automáticamente en todos los métodos de instalación de NumPy). Los usuarios avanzados podrían querer, de todas maneras, conocer los detalles, ya que la utilización BLAS puede afectar el desempeño, comportamiento y tamaño en disco:

- Las ruedas NumPy en PyPI, que son las que pip instala, están construidas con OpenBLAS. Las librerías de OpenBLAS están incluidas en la rueda. Esto vuelve a la rueda más grande, y si un usuario instala (por ejemplo) SciPy también, tendrá dos copias de OpenBLAS en disco.

- En el canal defaults o predeterminado de conda, NumPy está basado en Intel MKL. MKL es un paquete separado que se instalará en el entorno de usuario al instalar NumPy.

- En el canal conda-forge, Numpy está basado en un paquete "BLAS" ficticio o dummy. Cuando un usuario instala NumPy desde conda-forge, ese paquete BLAS es instalado junto con la librería - éste por defecto es OpenBLAS, pero también puede ser MKL (desde el canal defaults o predeterminado), o incluso [BLIS](https://github.com/flame/blis) o referencia BLAS.

- El paquete MKL es mucho más grande que OpenBLAS, de alrededor de 700 MB en disco, mientras que OpenBLAS es aproximadamente de 30MB.

- MKL es normalmente un poco más rápido y más robusto que OpenBLAS.

Además del tamaño de instalación, desempeño y robustez, hay dos aspectos más a considerar:

- Intel MKL no es de código abierto. Para uso normal esto no es un problema, pero si un usuario necesita redistribuir una aplicación construida con NumPy, esto podría ser un inconveniente.
- MKL y OpenBLAS utilizan funciones multihilo como `np.dot`, siendo el número de hilos determinado tanto por una opción de tiempo de compilación como por una variable de entorno. Todos los núcleos de la CPU usualmente serán utilizados. Esto es en ocasiones inesperado para los usuarios. NumPy en sí mismo no paraleliza automáticamente ninguna llamada a función. Normalmente produce un mejor rendimiento, pero también puede ser perjudicial - por ejemplo cuando se utiliza otro nivel de paralelización con Dask, el aprendizaje de la ciencia o multiprocesamiento.


## Resolución de problemas

Si su instalación falla con el siguiente mensaje, revise el siguiente enlace [Resolución de problemas ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
¡IMPORTANTE: POR FAVOR LEA ESTO COMO SUGERENCIA PARA RESOLVER ESTE PROBLEMA!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

