---
title: Instalando o NumPy
sidebar: false
---

O único pré-requisito para instalar o NumPy é o próprio Python. If you don't have
Python yet and want the simplest way to get started, we recommend you use the
[Anaconda Distribution](https://www.anaconda.com/download) - it includes
Python, NumPy, and many other commonly used packages for scientific computing
and data science.

NumPy can be installed with `conda`, with `pip`, with a package manager on
macOS and Linux, or [from source](https://numpy.org/devdocs/building).
For more detailed instructions, consult our Python and NumPy
installation guide below.

**CONDA**

If you use `conda`, you can install NumPy from the `defaults` or `conda-forge`
channels:

```bash
# Recomenda-se usar um ambiente novo ao invés de instalar no ambiente-base
conda create -n my-env
conda activate my-env
# Se quiser instalar do conda-forge
conda config --env --add channels conda-forge
# O comando para instalação
conda install numpy
```

**PIP**

If you use `pip`, you can install NumPy with:

```bash
pip install numpy
```

Also when using pip, it's good practice to use a virtual environment -
see  [Reproducible Installs](#reproducible-installs) below for why, and
[this guide](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)
for details on using virtual environments.

<a name="python-numpy-install-guide"></a>

# Guia de instalação do Python e do NumPy

Instalar e gerenciar pacotes no Python pode ser complicado. Há várias soluções alternativas para a maioria das tarefas. Este guia tenta dar ao leitor um resumo das melhores (ou mais populares) soluções e dar recomendações claras. Ele se concentra em usuários do Python, NumPy e do PyData (ou computação numérica) em sistemas operacionais e hardware comuns.

## Recomendações

Vamos começar com recomendações baseadas no nível de experiência do usuário e no sistema operacional de interesse. Se você estiver entre "iniciante" e "avançado", por favor, escolha "iniciante" se você quiser manter as coisas simples, e "avançado" se você quiser trabalhar de acordo com as melhores práticas que te ajudarão a ir mais longe no futuro.

### Usuários iniciantes

Em Windows, macOS e Linux:

- Install [Anaconda](https://www.anaconda.com/download) (it installs all
  packages you need and all other tools mentioned below).
- For writing and executing code, use notebooks in
  [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) for
  exploratory and interactive computing, and
  [Spyder](https://www.spyder-ide.org/) or [Visual Studio Code](https://code.visualstudio.com/)
  for writing scripts and packages.
- Use [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) to
  manage your packages and start JupyterLab, Spyder, or Visual Studio Code.

### Usuários avançados

#### Conda

- Install [Miniforge](https://github.com/conda-forge/miniforge).
- Keep the `base` conda environment minimal, and use one or more
  [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  to install the package you need for the task or project you're working on.

#### Alternativa se você preferir pip/PyPI

Para usuários que preferem uma solução baseada em pip/PyPI, por preferência pessoal ou leitura sobre as principais diferenças entre o conda e o pip, nós recomendamos:

- Install Python from [python.org](https://www.python.org/downloads/),
  [Homebrew](https://brew.sh/), or your Linux package manager.
- Use [Poetry](https://python-poetry.org/) as the most well-maintained tool
  that provides a dependency resolver and environment management capabilities
  in a similar fashion as conda does.

## Gerenciamento de pacotes Python

Gerenciar pacotes é um problema desafiador e, como resultado, há muitas ferramentas. For web and general purpose Python development there's a whole
[host of tools](https://packaging.python.org/guides/tool-recommendations/)
complementary with pip. For high-performance computing (HPC),
[Spack](https://github.com/spack/spack) is worth considering. For most NumPy
users though, [conda](https://conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) are the two most popular tools.

### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their
functionality partially overlaps (e.g. both can install `numpy`), however, they
can also work together. Vamos discutir as principais diferenças entre o pip e o conda aqui - é importante entender isso se você deseja gerenciar pacotes de forma efetiva.

A primeira diferença é que "conda" é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Isto também significa que o conda pode instalar bibliotecas e ferramentas não-Python das quais você pode precisar (por exemplo, compiladores, CUDA, HDF5), enquanto pip não pode.

A segunda diferença é que o pip instala do Índice de Pacotes Python (Python Packaging Index - PyPI), enquanto o conda instala de seus próprios canais (tipicamente "defaults" ou "conda-forge"). PyPI é a maior coleção de pacotes, no entanto, todos os pacotes populares também estão disponíveis para conda.

The third difference is that conda is an integrated solution for managing
packages, dependencies and environments, while with pip you may need another
tool (there are many!) for dealing with environments or complex dependencies.

<a name="reproducible-installs"></a>

### Instalações reprodutíveis

À medida que as bibliotecas são atualizadas, os resultados obtidos ao executar seu código podem mudar, ou o seu código pode parar de funcionar. É importante poder reconstruir o conjunto de pacotes e versões que você está usando. A recomendação é:

1. usar um ambiente diferente para cada projeto em que você trabalha,
2. record package names and versions using your package installer;
   each has its own metadata format for this:
   - Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - Pip: [virtual environments](https://docs.python.org/3/tutorial/venv.html) and
     [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [virtual environments and pyproject.toml](https://python-poetry.org/docs/basic-usage/)

## NumPy packages & accelerated linear algebra libraries

NumPy doesn't depend on any other Python packages, however, it does depend on an
accelerated linear algebra library - typically
[Intel MKL](https://software.intel.com/en-us/mkl) or
[OpenBLAS](https://www.openblas.net/). Os usuários não precisam se preocupar com a instalação desses pacotes (eles são incluídos automaticamente em todos os métodos de instalação do NumPy).
No entanto, usuários experientes podem querer saber os detalhes, porque o BLAS usado pode afetar o desempenho, o comportamento e o tamanho em disco:

- As wheels da NumPy no PyPI, que é o que o pip instala, são compiladas com OpenBLAS.
  As bibliotecas da OpenBLAS são empacotadas dentro da wheel. This makes the wheel
  larger, and if a user installs (for example) SciPy as well, they will now
  have two copies of OpenBLAS on disk.

- No canal defaults do conda, a NumPy é compilada com a Intel MKL. MKL is a
  separate package that will be installed in the users' environment when they
  install NumPy.

- No canal do conda-Forge, a NumPy é compilada com um pacote "BLAS" fictício. When
  a user installs NumPy from conda-forge, that BLAS package then gets installed
  together with the actual library - this defaults to OpenBLAS, but it can also
  be MKL (from the defaults channel), or even
  [BLIS](https://github.com/flame/blis) or reference BLAS.

- The MKL package is a lot larger than OpenBLAS, it's about 700 MB on disk
  while OpenBLAS is about 30 MB.

- A MKL é normalmente um pouco mais rápida e mais robusta do que a OpenBLAS.

Além do tamanho instalado, desempenho e robustez, há mais duas coisas a se considerar:

- A Intel MKL não é de código aberto. For normal use this is not a problem, but if
  a user needs to redistribute an application built with NumPy, this could be
  an issue.
- Both MKL and OpenBLAS will use multi-threading for function calls like
  `np.dot`, with the number of threads being determined by both a build-time
  option and an environment variable. Muitas vezes, todos os núcleos de CPU serão usados. This is
  sometimes unexpected for users; NumPy itself doesn't auto-parallelize any
  function calls. It typically yields better performance, but can also be
  harmful - for example when using another level of parallelization with Dask,
  scikit-learn or multiprocessing.

## Solução de problemas

If your installation fails with the message below, see Troubleshooting
ImportError.

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```
