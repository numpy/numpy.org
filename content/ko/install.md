---
title: Installing NumPy
sidebar: false
---

NumPy를 설치하는 유일한 선행 조건은 Python 자체입니다. 만약 아직 Python을 설치하지 않았고 가장 간단한 방법으로 시작하려면, [Anaconda 배포판](https://www.anaconda.com/distribution) 을 사용하길 권장합니다. 이 배포판에는 Python 와 NumPy 및 과학 계산 및 데이터 사이언스에 자주 사용되는 다른 패키지들이 포함되어 있습니다.

NumPy 는 `conda` 나 `pip` 를 통해서 사용하여 설치할 수 있고, 또한 macOS 및 Linux의 패키지 관리자나 [원본 코드](https://numpy.org/devdocs/user/building.html) 를 이용하여 설치할 수 있습니다. 더 자세한 설명은 아래의 [Python 및 NumPy 설치 가이드](#python-numpy-install-guide)를 확인해주세요.

**CONDA**

`conda`를 사용한다면, NumPy를 `defaults` 또는 `conda-forge` 채널에서 설치할 수 있습니다:

```bash
# 가장 좋은 방법은 기본 환경 대신에 새로운 환경을 이용하는 것입니다
conda create -n my-env
conda activate my-env
# my-env 에 conda-forge 채널을 더해줍니다
conda config --env --add channels conda-forge
# my-env 에 NumPy 를 설치합니다
conda install numpy
```

**PIP**

`pip`를 사용한다면, NumPy를 다음과 같이 설치할 수 있습니다:

```bash
pip install numpy
```
또한 `pip`를 사용할 때, 가상 환경을 사용하는 것을 추천합니다. 가상 환경을 사용하는 이유는 [재현 가능한 설치방법들](#reproducible-installs)을 참조해주세요. 가상 환경 사용에 대한 자세한 내용은 [이 가이드](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)에서 확인하실 수 있습니다.


<a name="python-numpy-install-guide"></a>

# Python 및 NumPy 설치 가이드

Python에서 패키지를 설치하고 관리하는 것은 복잡한 작업이기에, 대부분의 작업에 대해 다양한 대안적인 해결책이 있습니다. 이 가이드는 독자분들에게 가장 좋은 (또는 가장 인기 있는) 해결책을 이해시키고 명확한 권장 사항을 제공하려고 노력합니다. 이 가이드는 일반적인 운영 체제와 하드웨어에서 Python, NumPy 및 PyData (또는 숫자 계산) 사용자에 중점을 둡니다.

## 권장 사항

사용자의 경험과 사용하는 운영체제를 기준으로 추천하는 방식을 먼저 이야기 하겠습니다. 만약 당신이 초심자 또는 숙련자범위에 속해있다면, 간단하게 설치하고 싶다면 초심자로, 추후에 작업을 위해서 보다 구체적인 연습을 하고 싶다면 숙련자 자료를 참고하십시오.

### 초심자 유저

Windows, macOS, Linux 등 일반적인 운영체제:

- [Anaconda](https://www.anaconda.com/distribution/) 를 설치하십시오.(당신이 필요로 하는 패키지를 설치하고, 아래에 언급될 다양한 도구들을 제공합니다.)
- 코드를 작성하거나 실행할 때, 데이터를 분석하거나 대화형으로 코드를 작업하는 경우에는 [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) 의 notebooks를 사용하십시오. 그리고 코드를 작성하거나 패키지를 작성할 때는 [Spyder](https://www.spyder-ide.org/)나 [Visual Studio Code](https://code.visualstudio.com/)를 사용하십시오.
- 패키지를 관리하거나 JupyterLab, Spyder, Visual Studio Code 를 사용하는 경우 [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/)를 사용하십시오.


### 숙련자 유저

#### Conda

- [Miniforge](https://github.com/conda-forge/miniforge)를 설치하십시오.
- `base` 라는 이름의 콘다 가상환경은 최소 상태를 유지하고, [콘다 가상환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)을 만들어서, 해당 가상환경에 필요한 패키지를 설치하십시오.

#### Pip/PyPI를 활용하는 경우:

개인적인 선호나 아래의 conda 와 pip의 차이점을 설명하는 글을 읽은 유저나 또는 pip/PyPI기반의 설치 방법을 선호하는 경우 참고하십시오.
- [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/), or Linux package manager를 활용해서 Python을 설치하십시오.
- Conda와 동일한 수준의 가상환경 관리와 패키지 의존성을 해결을 도와주는 [Poetry](https://python-poetry.org/)를 유지관리 도구로 사용하십시오.


## Python 패키지 관리

패키지 관리는 아주 중요하기 때문에, 사용할 수 있는 도구들이 많습니다. 웹 및 범용 Python 개발을 위해 Pip뿐만 아니라 [다양한 도구](https://packaging.python.org/guides/tool-recommendations/)들이 있습니다. 고성능 컴퓨터 (HPC) 를 사용하는 경우 [Spack](https://github.com/spack/spack)를 사용하는 것을 추천합니다. 대부분 Numpy를 사용하는 유저는, [conda](https://conda.io/en/latest/) 와 [pip](https://pip.pypa.io/en/stable/)를 가장 많이 사용합니다.


### Pip & conda

Python 패키지를 설치하고 관리하는 주요 툴은 `pip` 과 `conda` 입니다. 그 도구들의 기능은 부분적으로 겹칩지만 (e.g. both can install `numpy`), 같이 쓰일 수도 있습니다. 곧 pip와 conda의 차이점에 대해서 논의해볼 것입니다. - 패키지 관리를 효율적으로 하기 위해서는 차이를 이해하는게 중요합니다.

첫번째 차이점은, conda는 cross-language 를 지원하고, Python을 설치할 수 도 있지만, pip는 특정 Python에만 패키지를 설치하고 관리할 수 있다는 것 입니다. 또한 conda는 non-Python 라이브러리나 도구들을 설치할 수 있지만 (e.g. compilers, CUDA, HDF5), pip는 Python이 필요하기 때문에 설치할 수 없습니다.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically "defaults" or "conda-forge"). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.

<a name="reproducible-installs"></a>

### Reproducible installs

As libraries get updated, results from running your code can change, or your code can break completely. It's important to be able to reconstruct the set of packages and versions you're using. Best practice is to:

1. use a different environment per project you're working on,
2. record package names and versions using your package installer; each has its own metadata format for this:
   - Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
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

