---
title: 安装NumPy
sidebar: false
---

安装 NumPy 的唯一前提条件是安装了 Python 。 如果您还没有Python，并且想以最简单的方式开始， 我们建议您使用[Anaconda Distribution](https://www.anaconda.com/distribution) - 它包括 Python, NumPy，以及许多其他常用的科学计算和数据科学软件包。

NumPy 可以使用 `conda` 安装，用 `pip` 安装， 在macOS 和Linux用软件包管理器安装或用[源码安装](https://numpy.org/devdocs/user/building.html)。 更详细的说明，查阅下方的 [ Python和NumPy安装指南 ](#python-numpy-install-guide)。

**CONDA**

如果您使用 `conda`，您可以从 `defaults` 或 `conda-forge` 频道安装 NumPy

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

如果您使用 `pip`，您可以用如下命令安装NumPy：

```bash
pip install numpy
```
另外，当使用 pip 时，最好使用虚拟环境。查看 [Rupuable Installs](#reproducible-installs) 了解原因。 查看 [指南](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) 了解关于使用虚拟环境的详情。

<a name="python-numpy-install-guide"></a>

# Python 和 NumPy 安装指南

在 Python 上安装和管理软件包很复杂，大多数任务有许多替代解决方案。 本指南试图给读者一种最佳(或最受欢迎) 解决办法，并给出清晰的建议。 It focuses on users of Python, NumPy, and the PyData (or numerical computing) stack on common operating systems and hardware.

## 建议

我们将首先根据用户的经验水平和有兴趣的操作系统提出建议。 如果您在“开始”和“高级”之间纠结，我们建议如果您想要保持简单，请使用"开始"， 如果您想要按照更长远的最佳做法去做，请使用"高级"。

### 开始用户

在所有Windows、 macOS和Linux上：

- 安装 [Anaconda](https://www.anaconda.com/distribution/) (包含了您需要的所有软件包以及下面提到的所有其他工具)。
- 编写和执行代码，使用[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) 的notebooks 用于探索式和交互式计算， 使用 [Spyder](https://www.spyder-ide.org/) 或 [Visual Studio Code](https://code.visualstudio.com/) 编写脚本和软件包。
- 用 [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) 管理你的软件包并启动JupyterLab, Spyder或Visual Studio Code.


### 高级用户

#### Windows 或 macOS

- 安装 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)。
- 保持 `base` conda 环境最小化， 并使用一个或多个[conda 环境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) 用于安装你需要的包以完成你正在做的任务或项目。
- 除非你只需要 `defaults` 频道的包， 否则请通过 [设置频道优先级](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge) 将 `conda-forge` 设为您的默认频道


#### Linux

If you're fine with slightly outdated packages and prefer stability over being able to use the latest versions of libraries:
- Use your OS package manager for as much as possible (Python itself, NumPy, and other libraries).
- Install packages not provided by your package manager with `pip install somepackage --user`.

如果您使用GPU：
- 安装 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)。
- 保持 `base` conda 环境最小化， 并使用一个或多个[conda 环境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) 用于安装你需要的包以完成你正在做的任务或项目。
- 使用 `defaults` conda 频道 (`conda-forge` 尚不支持 GPU 软件包)。

否则：
- 安装[Miniforge](https://github.com/conda-forge/miniforge).
- 保持 `base` conda 环境最小化， 并使用一个或多个[conda 环境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) 用于安装你需要的包以完成你正在做的任务或项目。


#### Alternative if you prefer pip/PyPI

For users who know, from personal preference or reading about the main differences between conda and pip below, they prefer a pip/PyPI-based solution, we recommend:
- 从 [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/)或 Linux 软件包管理器安装 Python。
- 使用 [Poetry](https://python-poetry.org/) ，它是具有与conda 相似的依赖解析器和环境管理能力的完善工具。


## Python 软件包管理

软件包管理是一个具有挑战性的问题，因此有许多的工具出现。 对于Web和一般Python开发有一整套能与pip互补的[工具](https://packaging.python.org/guides/tool-recommendations/)。 对于高性能计算 (HPC),[Spack](https://github.com/spack/spack) 值得考虑。 但对于大多数NumPy用户来说， [conda](https://conda.io/en/latest/) 和 [pip](https://pip.pypa.io/en/stable/) 是两个最受欢迎的工具。


### Pip & conda

安装 Python 软件包的两个主要工具是 `pip` and `conda`。 他们的功能部分重叠(例如两者都可以安装 `numpy`)，但他们也可以一起工作。 We'll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can't.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically "defaults" or "conda-forge"). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.


### Reproducible installs

As libraries get updated, results from running your code can change, or your code can break completely. It's important to be able to reconstruct the set of packages and versions you're using. Best practice is to:

1. use a different environment per project you're working on,
2. record package names and versions using your package installer; each has its own metadata format for this:
   - Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
   - Pip: [virtual environments](https://docs.python.org/3/tutorial/venv.html) and [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [virtual environments and pyproject.toml](https://python-poetry.org/docs/basic-usage/)



## NumPy packages & accelerated linear algebra libraries

NumPy doesn't depend on any other Python packages, however, it does depend on an accelerated linear algebra library - typically [Intel MKL](https://software.intel.com/en-us/mkl) or [OpenBLAS](https://www.openblas.net/). Users don't have to worry about installing those (they're automatically included in all NumPy install methods). Power users may still want to know the details, because the used BLAS can affect performance, behavior and size on disk:

- The NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS. The OpenBLAS libraries are included in the wheel. This makes the wheel larger, and if a user installs (for example) SciPy as well, they will now have two copies of OpenBLAS on disk.

- In the conda defaults channel, NumPy is built against Intel MKL. MKL is a separate package that will be installed in the users' environment when they install NumPy.

- In the conda-forge channel, NumPy is built against a dummy "BLAS" package. When a user installs NumPy from conda-forge, that BLAS package then gets installed together with the actual library - this defaults to OpenBLAS, but it can also be MKL (from the defaults channel), or even [BLIS](https://github.com/flame/blis) or reference BLAS.

- The MKL package is a lot larger than OpenBLAS, it's about 700 MB on disk while OpenBLAS is about 30 MB.

- MKL is typically a little faster and more robust than OpenBLAS.

Besides install sizes, performance and robustness, there are two more things to consider:

- Intel MKL is not open source. For normal use this is not a problem, but if a user needs to redistribute an application built with NumPy, this could be an issue.
- Both MKL and OpenBLAS will use multi-threading for function calls like `np.dot`, with the number of threads being determined by both a build-time option and an environment variable. Often all CPU cores will be used. This is sometimes unexpected for users; NumPy itself doesn't auto-parallelize any function calls. It typically yields better performance, but can also be harmful - for example when using another level of parallelization with Dask, scikit-learn or multiprocessing.


## Troubleshooting

If your installation fails with the message below, see [Troubleshooting ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

