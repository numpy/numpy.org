---
title: NumPy 설치
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

두번째 차이점은 pip는 Python Packaging Index(PyPI) 로 부터 패키지를 다운받아 설치하지만, conda는 conda 만의 채널로 설치합니다 (일반적으로 "defaults" or "conda-forge" 채널을 사용합니다). PyPI 가 가장 큰 패키지 저장소입니다만, 많은 사람들이 사용하는 패키지는 conda에서도 설치할 수 있습니다.

세번째 차이점은 conda는 환경이나 패키지간 의존성을 해결하기 위한 해키지 관리 도구를 제공하지만, pip는 그를 위해서 (아주 많은) 추가적인 도구들이 필요하다는 것 입니다.

<a name="reproducible-installs"></a>

### 재현 가능한 설치방법들

라이브러리가 업데이트되면, 코드의 실행 결과가 바뀌거나, 코드가 완전히 손상될 수 있습니다. 그러므로 사용중인 패키지 및 버전을 재구성할 수 있도록 하는 것이 중요합니다. 권장되는 방법으로는

1. 작업 중인 프로젝트마다 다른 환경을 이용하고,
2. 각각 자체 메타 데이터 형식이 있는 패키지 설치 프로그램을 통해 패키지 이름과 버전을 기록해둡니다.
   - Conda: [conda 환경들 과 environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - Pip: [가상 환경들](https://docs.python.org/3/tutorial/venv.html) 과 [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [가상 환경들 과 pyproject.toml](https://python-poetry.org/docs/basic-usage/)



## NumPy 패키지 & 고속 선형 대수 라이브러리

NumPy는 다른 Python 패키지에 의존하지 않습니다. 그러나 고속 선형 대수 라이브러리, 일반적으로 [Inter MKL](https://software.intel.com/en-us/mkl) 또는 [OpenBLAS](https://www.openblas.net/)에 의존하고 있습니다. 사용자는 이를 설치하지 않아도 됩니다 (NumPy 설치 중 설치됩니다). 고급 사용자의 경우 사용한 BLAS가 디스크의 성능, 동작 및 크기에 영향을 끼칠 수 있기 때문에 세부 정보가 필요할 수도 있습니다.

- Pip가 설치하는 PyPI의 휠 파일에 있는 NumPy의 경우는 OpenBLAS로 빌드되었습니다. OpenBLAS 라이브러리는 휠 파일에 포함되어 있습니다. 이는 휠 파일의 크기를 더 크게 만들고, 사용자가 (예를 들어) SciPy도 설치하게 되면 디스크에 2개의 OpenBLAS 사본을 가지게 됩니다.

- Conda의 기본 채널 내 NumPy는 Interl MKL로 빌드되었습니다. MKL은 NumPy를 설치할 때 사용자의 환경에 같이 설치되는 분할 패키지입니다.

- Conda-forge 채널 내 NumPy는 더미 "BLAS" 패키지로 빌드되었습니다. 사용자가 conda-forge에서 NumPy를 설치할 때 해당 BLAS 패키지가 실제 라이브러리와 함께 설치됩니다. 기본값은 OpenBLAS이나, (기본 채널에서는) MKL이 될 수도 있고, 심지어 [BLIS](https://github.com/flame/blis)나 Reference BLAS가 될 수도 있습니다.

- MKL 패키지가 OpenBLAS에 비해 더욱 큽니다. OpenBLAS가 30MB를 차지하는 반면, MKL 쪽은 700MB에 달하는 디스크 공간을 차지합니다.

- 보통 MKL이 OpenBLAS보다 더 빠르고 안정적입니다.

설치 크기, 성능 및 안정성을 제쳐 두더라도, 고려할 사항이 2가지 더 있습니다.

- Intel MKL은 오픈소스가 아닙니다. 일반적으로 사용할 때는 문제가 되지 않지만, 사용자가 NumPy로 빌드한 애플리케이션을 재배포하는 경우 문제가 될 수 있습니다.
- MKL과 OpenBLAS 모두 `np.dot`과 같이 함수를 호출하는 데 다중 스레드를 사용하며, 스레드의 수는 빌드 시간 설정과 환경 변수에 의해 결정됩니다. 보통은 모든 CPU 코어가 사용됩니다. 이로 인하여 예기치 않은 일이 발생할 수 있습니다. NumPy 자체적으로는 어떤 함수 호출도 병렬화하지 않습니다. 일반적으로 더 나은 성능을 제공해주지만, 예를 들어 Dask, scikit-learn 또는 멀티프로세싱과 함께 다른 수준의 병렬화를 사용하는 경우 좋지 않은 결과를 초래할 수 있습니다.


## 트러블슈팅

아래와 같은 응답과 함께 설치에 실패한다면, [Troubleshooting ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html)를 참고하시기 바랍니다.

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

