---
title: 安装NumPy
sidebar: 假
---

安装 NumPy 的唯一前提条件是安装了 Python 。 如果您还没有Python，并且想以最简单的方式开始， 我们建议您使用[Anaconda Distribution](https://www.anaconda.com/download) - 它包括 Python, NumPy，以及许多其他常用的科学计算和数据科学软件包。

NumPy 可以使用 `conda` 安装，用 `pip` 安装， 在macOS 和Linux用软件包管理器安装或用[源码安装](https://numpy.org/devdocs/building)。 更详细的说明，查阅下方的 [ Python和NumPy安装指南 ](#python-numpy-install-guide)。

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

在 Python 上安装和管理软件包很复杂，大部分工作任务都有许多可选择的解决方案。 本指南试图给读者一种最佳(或最受欢迎) 解决方案，并给出清晰的建议。 它侧重于在通用操作系统和硬件上使用Python、NumPy和PyData (或数学计算) 这些技术栈的用户。

## 建议

我们将首先根据用户的经验水平和有兴趣的操作系统提出建议。 如果您在“开始”和“高级”之间纠结，我们建议，如果您想简单点请使用"开始"，如果您想按长期最佳实践去做，请看"高级"。

### 开始用户

在所有Windows、 macOS和Linux上：

- 安装 [Anaconda](https://www.anaconda.com/download) (包含了您需要的所有软件包以及下面提到的所有其他工具)。
- 编写和执行代码，使用[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) 的notebooks 用于探索式和交互式计算， 使用 [Spyder](https://www.spyder-ide.org/) 或 [Visual Studio Code](https://code.visualstudio.com/) 编写脚本和软件包。
- 用 [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) 管理你的软件包并启动JupyterLab, Spyder或Visual Studio Code.


### 高级用户

#### Conda

- 安装 [Miniforge](https://github.com/conda-forge/miniforge).
- 保持 `base` conda 环境最小化， 并使用一个或多个[conda 环境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 用于安装你需要的包以完成你正在做的任务或项目。

#### 如果您更喜欢pip/PyPI

对出于个人喜好或看完下面 conda 和 pip之间的主要差异后更喜欢基于 pip/PyPI 的解决方案的用户，我们建议：
- 从 [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/)或 Linux 软件包管理器安装 Python。
- 使用 [Poetry](https://python-poetry.org/) ，它是具有与conda 相似的依赖解析器和环境管理能力的完善工具。


## Python 软件包管理

管理包是一个具有挑战性的问题，因此有大量的 工具。 对于Web和一般Python开发有一整套能与pip互补的[工具](https://packaging.python.org/guides/tool-recommendations/)。 对于高性能计算 (HPC),[Spack](https://github.com/spack/spack) 值得考虑。 但对于大多数NumPy 用户来说， [conda](https://conda.io/en/latest/) 和 [pip](https://pip.pypa.io/en/stable/) 是两个最受欢迎的工具。


### Pip & conda

安装 Python 软件包的两个主流工具是 `pip` and `conda`。 他们的功能部分重叠(例如两者都可以安装 `numpy`)，但他们也可以一起工作。 我们将在这里讨论 pip 与 conda 的主要差异——这对于理解如何有效地管理软件包非常重要。

第一个不同点是conda是跨语言的，它可以安装 Python，然而 pip 安装在您的系统的特定的Python环境之上， 并只为那一个特定的Python环境安装的软件包。 这也意味着conda 可以安装非Python 库和其他您可能需要的工具(例如编译器、CUDA、HDF5)，pip则不行。

第二个不同是 pip 以Python包索引(PyPI) 作为安装源。 而conda从自己的渠道安装(通常是"defaults"或"conda-forge")。 PyPI 是迄今为止最大的软件包集合网站，不过所有流行的软件包也可在conda找到。

第三个不同点，conda是依赖关系、环境和软件包管理的集成工具。而 pip 可能需要其他工具 (很多!) 用于处理环境或复杂的依赖关系。

<a name="reproducible-installs"></a>

### 可重复安装

随着库的更新，运行代码的结果可能会改变，甚至您的代码可能会完全中断。 所以能够重建你使用的对应版本软件包集合就很重要了。 最佳做法如下：

1. 为你的每一个项目构建不同的环境
2. 用软件包管理器记录软件包名称和版本； 每个包管理器都有自己的元数据格式：
   - Conda: [conda environment and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - Pip: [虚拟环境](https://docs.python.org/3/tutorial/venv.html)和 [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [虚拟环境和 pyproject.toml](https://python-poetry.org/docs/basic-usage/)



## NumPy包和快速线性代数库

NumPy 不依赖任何其他Python 包。 不过它依赖于一个快速线性代数库 —— 它通常是[Intel MKL](https://software.intel.com/en-us/mkl) 或者 [OpenBLAS](https://www.openblas.net/)。 用户不必担心要如何安装那些库 (他们会自动包含在所有NumPy 的安装脚本中)。 但是高级用户可能仍然想知道详细信息，因为使用 BLAS 会影响磁盘的性能、行为和空间：

- 用pip安装的 NumPy，其线性代数库是 OpenBLAS。 OpenBLAS 库包含在NumPy的轮子中。 这让轮子变得更大，而且如果用户安装了 (假设) SciPy，他们现在会在磁盘上有两份OpenBLAS 副本。

- 在 conda 的默认频道中，NumPy 是用 Intel MKL 构建的。 MKL 是个单独的软件包，在安装Numpy时会将它安装到用户环境中。

- 在 conda-forge 通道中，NumPy 是用虚构的“BLAS”软件包构建的。 当用户从conda-forge安装NumPy时，BLAS 软件包就会与实际库一起安装 - 默认是OpenBLAS ，不过它也可以是 MKL (默认频道)，乃至是[BLIS](https://github.com/flame/blis) 或者 reference BLAS。

- MKL包比OpenBLAS大得多，它在磁盘上有大约700MB，而OpenBLAS 大约只有30MB。

- MKL通常比OpenBLAS更快，更强大。

除了安装大小和性能外，还有两个东西需要考虑：

- Intel MKL不是开源的。 对于正常使用，这倒不是一个问题。 但如果用户需要重新发布基于 NumPy 构建的应用程序，这可能引发一些问题。
- MKL 和 OpenBLAS 都将使用多线程函数调用，例如 `np. ot`, 由建造时间选项和环境变量决定线程的数量。 通常所有的CPU核心都能被使用。 这有时并不是用户期望的；NumPy本身并不进行任何自动并行函数调用。 多线程通常能产生更好的性能，但也可能降低性能――例如，当使用 Dask、scikit-learn 或 multiprocessing 的另一个并行化等级时。


## 疑难解答

如果你安装失败并返回下述提示消息，请参考 [导入错误](https://numpy.org/doc/stable/user/troubleshooting-importerror.html)。

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

