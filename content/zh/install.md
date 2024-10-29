---
title: 安装NumPy
sidebar: false
---

安装 NumPy 的唯一前提条件是安装了 Python 。 If you don't have
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
# 最佳练习 使用环境而不是在基础环境中安装
conda create -n my-env
conda activer my-env

# 如果你想从conda-forge频道安装
conda config --env --add channel conda-full

# 实际的安装命令
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

# Python 和 NumPy 安装指南

在 Python 上安装和管理软件包很复杂，大部分工作任务都有许多可选择的解决方案。 本指南试图给读者一种最佳(或最受欢迎) 解决方案，并给出清晰的建议。 它侧重于在通用操作系统和硬件上使用Python、NumPy和PyData (或数学计算) 这些技术栈的用户。

## 建议

我们将首先根据用户的经验水平和有兴趣的操作系统提出建议。 如果您在“开始”和“高级”之间纠结，我们建议，如果您想简单点请使用"开始"，如果您想按长期最佳实践去做，请看"高级"。

### 开始用户

在所有Windows、 macOS和Linux上：

- Install [Anaconda](https://www.anaconda.com/download) (it installs all
  packages you need and all other tools mentioned below).
- For writing and executing code, use notebooks in
  [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) for
  exploratory and interactive computing, and
  [Spyder](https://www.spyder-ide.org/) or [Visual Studio Code](https://code.visualstudio.com/)
  for writing scripts and packages.
- Use [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) to
  manage your packages and start JupyterLab, Spyder, or Visual Studio Code.

### 高级用户

#### Conda

- Install [Miniforge](https://github.com/conda-forge/miniforge).
- Keep the `base` conda environment minimal, and use one or more
  [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  to install the package you need for the task or project you're working on.

#### 如果您更喜欢pip/pyPI

对出于个人喜好或看完下面 conda 和 pip之间的主要差异后更喜欢基于 pip/PyPI 的解决方案的用户，我们建议：

- Install Python from [python.org](https://www.python.org/downloads/),
  [Homebrew](https://brew.sh/), or your Linux package manager.
- Use [Poetry](https://python-poetry.org/) as the most well-maintained tool
  that provides a dependency resolver and environment management capabilities
  in a similar fashion as conda does.

## Python 软件包管理

软件包管理是一个具有挑战性的问题，因此有许多的工具出现。 For web and general purpose Python development there's a whole
[host of tools](https://packaging.python.org/guides/tool-recommendations/)
complementary with pip. For high-performance computing (HPC),
[Spack](https://github.com/spack/spack) is worth considering. For most NumPy
users though, [conda](https://conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) are the two most popular tools.

### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their
functionality partially overlaps (e.g. both can install `numpy`), however, they
can also work together. 我们将在这里讨论 pip 与 conda 的主要差异——这对于理解如何有效地管理软件包非常重要。

第一点不同是conda是跨语言的，它可以安装 Python，然而 pip 安装在您的系统的特定的 Python 之上， 并只为那一个特定的Python安装其他的软件包。 这也意味着conda 可以安装非Python 库和其他您可能需要的工具(例如编译器、CUDA、HDF5)，pip则不行。

第二个不同是 pip 以Python包索引(PyPI) 作为安装源。 而conda从自己的渠道安装(通常是"defaults"或
"conda-forge")。 PyPI 是迄今为止最大的软件包集合，不过所有流行的软件包也可用于 conda。

The third difference is that conda is an integrated solution for managing
packages, dependencies and environments, while with pip you may need another
tool (there are many!) for dealing with environments or complex dependencies.

<a name="reproducible-installs"></a>

### 可复现安装

随着库的更新，代码的运行结果可能会改变，甚至您的代码完全跑不起来。 能重建你使用的对应版本软件包集合就很重要了。 最佳做法如下：

1. 为你的每一个项目构建不同的环境
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
[OpenBLAS](https://www.openblas.net/). 用户不必担心要如何安装那些库 (他们会自动包含在所有NumPy 的安装脚本中)。
高级用户可能仍然想知道详细信息，因为使用 BLAS 会影响磁盘的性能、行为和空间：

- 用pip安装的 NumPy，线性代数库是 OpenBLAS。
  OpenBLAS 库包含在NumPy的轮子中。 This makes the wheel
  larger, and if a user installs (for example) SciPy as well, they will now
  have two copies of OpenBLAS on disk.

- 在 conda 的默认频道中，NumPy 是用 Intel MKL 构建的。 MKL is a
  separate package that will be installed in the users' environment when they
  install NumPy.

- 在 conda-forge 通道中，NumPy 是用虚构的“BLAS”软件包构建的。 When
  a user installs NumPy from conda-forge, that BLAS package then gets installed
  together with the actual library - this defaults to OpenBLAS, but it can also
  be MKL (from the defaults channel), or even
  [BLIS](https://github.com/flame/blis) or reference BLAS.

- The MKL package is a lot larger than OpenBLAS, it's about 700 MB on disk
  while OpenBLAS is about 30 MB.

- MKL通常比OpenBLAS更快，更强大。

除了安装大小、性能和强大性能外，还有两个东西需要考虑：

- Intel MKL不开源。 For normal use this is not a problem, but if
  a user needs to redistribute an application built with NumPy, this could be
  an issue.
- Both MKL and OpenBLAS will use multi-threading for function calls like
  `np.dot`, with the number of threads being determined by both a build-time
  option and an environment variable. 通常所有的CPU核心都能用上。 This is
  sometimes unexpected for users; NumPy itself doesn't auto-parallelize any
  function calls. It typically yields better performance, but can also be
  harmful - for example when using another level of parallelization with Dask,
  scikit-learn or multiprocessing.

## 故障排查

If your installation fails with the message below, see Troubleshooting
ImportError.

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```
