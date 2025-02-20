---
title: 安装NumPy
sidebar: 假
---

{{< admonition tip >}}
NumPy 可以使用 `conda` 安装，用 `pip` 安装， 在macOS 和Linux用软件包管理器安装或用[源码安装](https://numpy.org/devdocs/building)。 安装 NumPy 的唯一前提条件是安装了 Python 。 如果您还没有Python，并且想以最简单的方式开始， 我们建议您使用[Anaconda Distribution](https://www.anaconda.com/download) - 它包括 Python, NumPy，以及许多其他常用的科学计算和数据科学软件包。
{{< /admonition >}}

The recommended method of installing NumPy depends on your preferred workflow. Below, we break down the installation methods into the following categories:

- **Project-based** (e.g., uv, pixi) *(recommended for new users)*
- **Environment-based** (e.g., pip, conda) *(the traditional workflow)*
- **System package managers** *(not recommended for most users)*
- **Building from source** *(for advanced users and development purposes)*

Choose the method that best suits your needs. If you're unsure, start with the **Environment-based** method using `conda` or `pip`.

Below are the different methods for **installing NumPy**. Click on the tabs to explore each method:
另外，当使用 pip 时，最好使用虚拟环境。查看 [Rupuable Installs](#reproducible-installs) 了解原因。 查看 [指南](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) 了解关于使用虚拟环境的详情。

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

在所有Windows、 macOS和Linux上：

对出于个人喜好或看完下面 conda 和 pip之间的主要差异后更喜欢基于 pip/PyPI 的解决方案的用户，我们建议：

安装 Python 软件包的两个主流工具是 `pip` and `conda`。 对于Web和一般Python开发有一整套能与pip互补的[工具](https://packaging.python.org/guides/tool-recommendations/)。 对于高性能计算 (HPC),[Spack](https://github.com/spack/spack) 值得考虑。

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. 他们的功能部分重叠(例如两者都可以安装 `numpy`)，但他们也可以一起工作。

第一个不同点是conda是跨语言的，它可以安装 Python，然而 pip 安装在您的系统的特定的Python环境之上， 并只为那一个特定的Python环境安装的软件包。 这也意味着conda 可以安装非Python 库和其他您可能需要的工具(例如编译器、CUDA、HDF5)，pip则不行。

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
第三个不同点，conda是依赖关系、环境和软件包管理的集成工具。而 pip 可能需要其他工具 (很多!) 用于处理环境或复杂的依赖关系。
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
# 最佳练习 使用环境而不是在基础环境中安装
conda create -n my-env
conda activer my-env

# 如果你想从conda-forge频道安装
conda config --env --add channel conda-full

# 实际的安装命令
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

## 建议

After installing NumPy, verify the installation by running the following in a Python shell or script:
```python
import numpy as np
print(np.__version__)
```

This should print the installed version of NumPy without errors.

## 疑难解答

如果你安装失败并返回下述提示消息，请参考 [导入错误](https://numpy.org/doc/stable/user/troubleshooting-importerror.html)。

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

