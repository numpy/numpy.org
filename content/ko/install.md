---
title: NumPy 설치
sidebar: false
---

NumPy 설치를 위해서는 Python만 필요합니다. 만양 파이썬이 설치되지 않았다면, Python, NumPy, 그리고 다양한 데이터 과학과 과학 계산을 위해 일반적으로 많이 사용되는 패키지를 한번에 설치할 수 있는 [Anaconda Distribution](https://www.anaconda.com/distribution)을 활용하여 설치하는 것을 추천합니다.

NumPy 는 `conda`, `pip` 그리고 macOS과 Linux의 패키지 매니저를 사용하거나 또는 [소스](https://numpy.org/devdocs/user/building.html)로 부터 설치할 수 있습니다. 보다 상세한 설치 과정과 방법은 [Python and NumPy 설치 가이드](#python-numpy-install-guide)의 아래쪽에 있습니다.

**CONDA**

만약 `conda`를 사용해 설치하는 경우, `defaults` 또는 `conda-forge` 채널을 활용해서 설치할 수 있습니다.

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

만약 `pip`로 NumPy를 설치하는 경우

```bash
pip install numpy
```
또한 pip를 사용할 때, 가상환경을 만들어보고, 만들어진 가상환경에 설치하는 것이 좋습니다. 상세한 내용은 [Reproducible Installs](#reproducible-installs)를 참조하십시오. 또한 가상환경을 사용하는 상세한 내용은 [가이드](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)를 참조하십시오.

<a name="python-numpy-install-guide"></a>

# Python, Numpy 설치 가이드

파이썬만 활용해서 패키지를 설치하고 관리하는 것은 복잡하기 때문에, 다양한 대안들이 많이 있습니다. 이 가이드에는 가장 보편적이고, 명확한 방식을 알려줍니다. 이 가이드는 통상적으로 사용되는 운영체제와 하드웨어에서 Python과 NumPy 그리고 수치 계산을 해주는 PyData를 사용하는 유저를 위한 자료입니다.

## Recommendations

사용자의 전문성과 사용하는 운영체제를 기준으로 추천하는 방식을 알려드리겠습니다. 만약 당신이 초심자 또는 숙련자범위에 속해있다면, 간단하게 설치하고 싶다면 초심자로, 추후에 작업을 위해서 보다 구체적인 연습을 하고 싶다면 숙련자 자료를 참고하십시오.

### 초심자 유저

Windows, macOS, Linux 등 모든 일반적인 운영체제:

- [Anaconda](https://www.anaconda.com/distribution/) 를 설치하십시오.(당신이 필요로 하는 패키지를 설치하고, 아래에 언급될 다양한 도구들을 제공합니다.)
- 코드를 작성하거나 실행할 때, 데이터를 분석하거나 대화형으로 코드를 작업하는 경우에는 [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) 의 notebooks를 사용하십시오. 그리고 코드를 작성하거나 패키지를 작성할 때는 [Spyder](https://www.spyder-ide.org/)나 [Visual Studio Code](https://code.visualstudio.com/)를 사용하십시오.
- 패키지를 관리하거나 JupyterLab, Spyder, Visual Studio Code 를 사용하는 경우 [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/)를 사용하십시오.


### 숙련자 유저

#### Windows, macOS

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)를 설치하십시오.
- `base` 라는 이름의 콘다 가상환경은 초기 최소 상태를 유지하고, [콘다 가상환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)을 만들어서, 해당 가상환경에 진행하고자 하는 일이나 프로젝트를 위해서 필요한 패키지를 설치하십시오.
- `기본 채널`로 충분하지 않다면, `conda-forge` [채널 우선순위 설정](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge)을 통해서 원하는 채널을설정할 수 있습니다..


#### Linux

만약 약간 하위 버전의 패키지나, 최신 버전이 아닌 보다 안정적인 패키지를 설치하고 싶은 경우에 참고하십시오.
- OS에서 사용 가능한 패키지 매니저를 활용하여 설치하십시오 (Python itself, NumPy, and other libraries).
- 설치한 패키지 매니저가 라이브러리를 설치해주지 않는다면, `pip install somepackage --user`를 명령 프롬프트에 입력하십시오.

GPU를 사용하는 경우:
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)를 설치하십시오.
- `base` 라는 이름의 콘다 가상환경은 초기 최소 상태를 유지하고, [콘다 가상환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)을 만들어서, 해당 가상환경에 진행하고자 하는 일이나 프로젝트를 위해서 필요한 패키지를 설치하십시오.
- `기본 콘다 채널`을 활용해 주십시오.(`conda-forge` GPU 패키지를 지원하는 좋은 채널을 아직 제공하지 않습니다.).

기타:
- [Miniforge](https://github.com/conda-forge/miniforge)를 설치하십시오.
- `base` 라는 이름의 콘다 가상환경은 초기 최소 상태를 유지하고, [콘다 가상환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)을 만들어서, 해당 가상환경에 진행하고자 하는 일이나 프로젝트를 위해서 필요한 패키지를 설치하십시오.


#### Pip/PyPI를 활용하는 경우:

개인적인 선호나 아래의 conda 와 pip의 차이점을 설명하는 글을 읽은 유저나 또는 pip/PyPI기반의 설치 방법을 선호하는 경우 참고하십시오.
- [python.org](https://www.python.org/downloads/) 이나 [Homebrew](https://brew.sh/), Linux package manager를 활용해서 Python을 설치하십시오.
- Conda와 동일한 수준의 가상환경 관리와 패키지 의존성을 해결을 도와주는 [Poetry](https://python-poetry.org/)를 유지관리 도구로 사용하십시오.


## Python 패키지 관리

패키지 관리는 아주 중요하기 때문에, 사용할 수 있는 도구들이 많다, 웹 및 범용 Python 개발을 위해 Pip뿐만 아니라 [다양한 도구](https://packaging.python.org/guides/tool-recommendations/)들이 있다. For high-performance computing (HPC), [Spack](https://github.com/spack/spack) is worth considering. For most NumPy users though, [conda](https://conda.io/en/latest/) and [pip](https://pip.pypa.io/en/stable/) are the two most popular tools.


### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their functionality partially overlaps (e.g. both can install `numpy`), however, they can also work together. We'll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

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

