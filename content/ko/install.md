---
title: NumPy 설치
sidebar: false
---

세번째 차이점은 conda는 환경이나 패키지간 의존성을 해결하기 위한 해키지 관리 도구를 제공하지만, pip는 그를 위해서 (아주 많은) 추가적인 도구들이 필요하다는 것 입니다.
NumPy 는 `conda` 나 `pip` 를 통해서 사용하여 설치할 수 있고, 또한 macOS 및 Linux의 패키지 관리자나 [원본 코드](https://numpy.org/devdocs/user/building.html) 를 이용하여 설치할 수 있습니다. NumPy를 설치하는 유일한 선행 조건은 Python 자체입니다. 만약 아직 Python을 설치하지 않았고 가장 간단한 방법으로 시작하려면, [Anaconda 배포판](https://www.anaconda.com/distribution) 을 사용하길 권장합니다. 이 배포판에는 Python 와 NumPy 및 과학 계산 및 데이터 사이언스에 자주 사용되는 다른 패키지들이 포함되어 있습니다.
{{< /admonition >}}

The recommended method of installing NumPy depends on your preferred workflow. Below, we break down the installation methods into the following categories:

- **Project-based** (e.g., uv, pixi) *(recommended for new users)*
- **Environment-based** (e.g., pip, conda) *(the traditional workflow)*
- **System package managers** *(not recommended for most users)*
- **Building from source** *(for advanced users and development purposes)*

Choose the method that best suits your needs. If you're unsure, start with the **Environment-based** method using `conda` or `pip`.

Below are the different methods for **installing NumPy**. Click on the tabs to explore each method:
또한 `pip`를 사용할 때, 가상 환경을 사용하는 것을 추천합니다. 가상 환경을 사용하는 이유는 [재현 가능한 설치방법들](#reproducible-installs)을 참조해주세요. 가상 환경 사용에 대한 자세한 내용은 [이 가이드](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)에서 확인하실 수 있습니다.

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

Windows, macOS, Linux 등 일반적인 운영체제:

개인적인 선호나 아래의 conda 와 pip의 차이점을 설명하는 글을 읽은 유저나 또는 pip/PyPI기반의 설치 방법을 선호하는 경우 참고하십시오.

Python 패키지를 설치하고 관리하는 주요 툴은 `pip` 과 `conda` 입니다. 웹 및 범용 Python 개발을 위해 Pip뿐만 아니라 [다양한 도구](https://packaging.python.org/guides/tool-recommendations/)들이 있습니다. 고성능 컴퓨터 (HPC) 를 사용하는 경우 [Spack](https://github.com/spack/spack)를 사용하는 것을 추천합니다.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. 그 도구들의 기능은 부분적으로 겹칩지만 (e.g. both can install `numpy`), 같이 쓰일 수도 있습니다.

첫번째 차이점은, conda는 cross-language 를 지원하고, Python을 설치할 수 도 있지만, pip는 특정 Python에만 패키지를 설치하고 관리할 수 있다는 것 입니다. 또한 conda는 non-Python 라이브러리나 도구들을 설치할 수 있지만 (e.g. compilers, CUDA, HDF5), pip는 Python이 필요하기 때문에 설치할 수 없습니다.

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
세번째 차이점은 conda는 환경이나 패키지간 의존성을 해결하기 위한 해키지 관리 도구를 제공하지만, pip는 그를 위해서 (아주 많은) 추가적인 도구들이 필요하다는 것 입니다.
**Tip:** Use a virtual environment for better dependency management
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy
  ```
'''
{{< /card >}}

[[tab]] name = 'System Package Managers' content = ''' Not recommended for most users, but available for convenience.

**macOS (Homebrew):**
```bash
# 가장 좋은 방법은 기본 환경 대신에 새로운 환경을 이용하는 것입니다
conda create -n my-env
conda activate my-env
# my-env 에 conda-forge 채널을 더해줍니다
conda config --env --add channels conda-forge
# my-env 에 NumPy 를 설치합니다
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
{{< /card >}}

[[tab]] name = 'Building from Source' content = ''' For advanced users and developers who want to customize or debug **NumPy**.

A word of warning: building Numpy from source can be a nontrivial exercise. We recommend using binaries instead if those are available for your platform via one of the above methods. For details on how to build from source, see [the building from source guide in the Numpy docs](https://numpy.org/devdocs/building/).

'''
{{< /card >}}
{{< /tabs >}}

## 권장 사항

After installing NumPy, verify the installation by running the following in a Python shell or script:
```python
import numpy as np
print(np.__version__)
```

This should print the installed version of NumPy without errors.

## 트러블슈팅

아래와 같은 응답과 함께 설치에 실패한다면, [Troubleshooting ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html)를 참고하시기 바랍니다.

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

