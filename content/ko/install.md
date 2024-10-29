---
title: NumPy 설치
sidebar: false
---

NumPy 설치를 위해서는 Python만 필요합니다. If you don't have
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
# 기본 환경보다 가상환경을 설치하여 활용하는 것이 좋습니다.
# Anaconda가 설치된 환경에서 cmd에서 하기 명령어를 입력합니다.
conda create -n my-env # my-env 라는 이름의 가상환경 생성
conda activate my-env # 활성화 된 가상환경을 my-env로 변경
# conda-forge로 설치하는 경우하기 명령어 입력
conda config --env --add channels conda-forge
# 실제 설치 명령어
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

# Python, Numpy 설치 가이드

파이썬만 활용해서 패키지를 설치하고 관리하는 것은 복잡하기 때문에, 다양한 대안들이 많이 있습니다. 이 가이드에는 가장 보편적이고, 명확한 방식을 알려줍니다. 이 가이드는 통상적으로 사용되는 운영체제와 하드웨어에서 Python과 NumPy 그리고 수치 계산을 해주는 PyData를 사용하는 유저를 위한 자료입니다.

## 권장 사항

사용자의 전문성과 사용하는 운영체제를 기준으로 추천하는 방식을 알려드리겠습니다. 만약 당신이 초심자 또는 숙련자범위에 속해있다면, 간단하게 설치하고 싶다면 초심자로, 추후에 작업을 위해서 보다 구체적인 연습을 하고 싶다면 숙련자 자료를 참고하십시오.

### 초심자 유저

Windows, macOS, Linux 등 모든 일반적인 운영체제:

- Install [Anaconda](https://www.anaconda.com/download) (it installs all
  packages you need and all other tools mentioned below).
- For writing and executing code, use notebooks in
  [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) for
  exploratory and interactive computing, and
  [Spyder](https://www.spyder-ide.org/) or [Visual Studio Code](https://code.visualstudio.com/)
  for writing scripts and packages.
- Use [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) to
  manage your packages and start JupyterLab, Spyder, or Visual Studio Code.

### 숙련자 유저

#### Conda

- Install [Miniforge](https://github.com/conda-forge/miniforge).
- Keep the `base` conda environment minimal, and use one or more
  [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  to install the package you need for the task or project you're working on.

#### Pip/PyPI를 활용하는 경우:

개인적인 선호나 아래의 conda 와 pip의 차이점을 설명하는 글을 읽은 유저나 또는 pip/PyPI기반의 설치 방법을 선호하는 경우 참고하십시오.

- Install Python from [python.org](https://www.python.org/downloads/),
  [Homebrew](https://brew.sh/), or your Linux package manager.
- Use [Poetry](https://python-poetry.org/) as the most well-maintained tool
  that provides a dependency resolver and environment management capabilities
  in a similar fashion as conda does.

## Python 패키지 관리

패키지 관리는 아주 중요하기 때문에, 사용할 수 있는 도구들이 많습니다. For web and general purpose Python development there's a whole
[host of tools](https://packaging.python.org/guides/tool-recommendations/)
complementary with pip. For high-performance computing (HPC),
[Spack](https://github.com/spack/spack) is worth considering. For most NumPy
users though, [conda](https://conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) are the two most popular tools.

### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their
functionality partially overlaps (e.g. both can install `numpy`), however, they
can also work together. 곧 pip와 conda의 차이점에 대해서 논의해볼 것입니다. - 패키지 관리를 잘 하기 위해서는 알고 계시는 것이 좋습니다.

첫번째 차이점은, conda는 cross-language 를 지원하고, Python을 설치할 수 도있습니다. 하지만 pip는 특정 설치된 Python에만 패키지를 설치하고 관리할 수 있습니다. 따라서 해당 Python에 모든 패키지가 설치됩니다. 또한 conda는 non-Python 라이브러리나 도구들을 설치할 수 있습니다. (e.g. compilers, CUDA, HDF5), 하지만 pip는 Python이 필요하기 때문에 설치할 수 없습니다.

두번째 차이점은 pip는 Python Packaging Index(PyPI) 로 부터 패키지를 다운받아 설치합니다. 반면에 conda는 conda 만의 채널로 설치합니다. (일반적으로 "defaults" or "conda-forge"). PyPI 가 가장 큰 패키지 저장소입니다만, 많은 사람들이 사용하는 패키지는 conda에서도 설치할 수 있습니다.

The third difference is that conda is an integrated solution for managing
packages, dependencies and environments, while with pip you may need another
tool (there are many!) for dealing with environments or complex dependencies.

<a name="reproducible-installs"></a>

### 재구성 가능한 설치

라이브러리가 업데이트되면, 코드의 실행 결과가 바뀌거나, 코드가 완전히 손상될 수 있습니다. 사용중인 패키지 및 버전을 재구성할 수 있도록 하는 것이 중요합니다. 가장 좋은 방법으로는

1. 작업 중인 프로젝트마다 다른 환경을 이용하고,
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
[OpenBLAS](https://www.openblas.net/). 사용자는 이를 설치하지 않아도 됩니다 (NumPy 설치 중 저절로 설치됨).
고급 사용자의 경우 사용한 BLAS가 디스크의 성능, 동작 및 크기에 영향을 끼칠 수 있기 때문에 세부 정보를 알고 싶을 수도 있습니다.

- PIP가 설치하는 PyPI의 휠 파일에 있는 NumPy의 경우는 OpenBLAS로 빌드되었습니다.
  OpenBLAS 라이브러리가 휠 파일에 포함되어 있습니다. This makes the wheel
  larger, and if a user installs (for example) SciPy as well, they will now
  have two copies of OpenBLAS on disk.

- Conda의 기본 채널 내 NumPy는 Interl MKL로 빌드되었습니다. MKL is a
  separate package that will be installed in the users' environment when they
  install NumPy.

- conda-forge 채널 내 NumPy는 더미 "BLAS" 패키지로 빌드되었습니다. When
  a user installs NumPy from conda-forge, that BLAS package then gets installed
  together with the actual library - this defaults to OpenBLAS, but it can also
  be MKL (from the defaults channel), or even
  [BLIS](https://github.com/flame/blis) or reference BLAS.

- The MKL package is a lot larger than OpenBLAS, it's about 700 MB on disk
  while OpenBLAS is about 30 MB.

- 보통 MKL이 OpenBLAS보다 더 빠르고 안정적입니다.

설치 크기, 성능 및 안정성을 제쳐 두더라도, 고려할 사항이 2가지 더 있습니다.

- Intel MKL은 오픈소스가 아닙니다. For normal use this is not a problem, but if
  a user needs to redistribute an application built with NumPy, this could be
  an issue.
- Both MKL and OpenBLAS will use multi-threading for function calls like
  `np.dot`, with the number of threads being determined by both a build-time
  option and an environment variable. 보통은 모든 CPU 코어가 사용됩니다. This is
  sometimes unexpected for users; NumPy itself doesn't auto-parallelize any
  function calls. It typically yields better performance, but can also be
  harmful - for example when using another level of parallelization with Dask,
  scikit-learn or multiprocessing.

## 문제 해결

If your installation fails with the message below, see Troubleshooting
ImportError.

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```
