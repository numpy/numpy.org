---
title: NumPy 설치하기
sidebar: false
---

{{< admonition >}}
{{< /admonition >}}

The recommended method of installing NumPy depends on your preferred workflow. 아래에 설치 방법을 다음과 같이 분류하였습니다:

- **프로젝트 기반** (예를 들어, uv, pixi) _(새로운 사용자에게 추천)_
- **Environment-based** (e.g., pip, conda) _(the traditional workflow)_
- **System package managers** _(not recommended for most users)_
- **Building from source** _(for advanced users and development purposes)_

Choose the method that best suits your needs. If you're unsure, start with the **Environment-based** method using `conda` or `pip`.

{{< tabs >}}

[[tab]]
name = 'Project Based'
content = '''

Recommended for new users who want a streamlined workflow.

- **uv:** A modern Python package manager designed for speed and simplicity.
  ```bash
  uv pip install numpy
  ```

- **pixi:** A cross-platform package manager for Python and other languages.
  ```bash
  pixi add numpy
  ```

'''
{{< /card >}}

개인적인 선호나 아래의 conda 와 pip의 차이점을 설명하는 글을 읽은 유저나 또는 pip/PyPI기반의 설치 방법을 선호하는 경우 참고하십시오.

Python 패키지를 설치하고 관리하는 주요 소프트웨어 도구는 `pip` 과 `conda` 입니다. 둘의 기능은 부분적으로 서로 겹치지만 (예를 들어 둘 다 `numpy` 설치할 수 있습니다.) 주요한 pip와 conda 사이의 차이점에 대해 여기서 이야기 할 것입니다. 이것은 효과적으로 패키지를 관리하려면 중요합니다.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. 이것이 또한 뜻하는 바는 conda 는 파이썬이 아닌 다른 언어 라이브러리와 소프트웨어 도구도 여러분이 필요하다면 설치할 수 있지만 (예를 들어 컴파일러, CUDA, HDF5), pip 는 할 수 없다는 것입니다.

첫번째 차이점은, conda는 cross-language 를 지원하고, Python을 설치할 수 도 있지만, pip는 특정 Python에만 패키지를 설치하고 관리할 수 있다는 것 입니다. PyPI 에 가장 많이 모여 있으며, 2등과는 상당한 차이가 있는 정도지만, 가장 인기 있는 패키지들은 conda 에도 있습니다.

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

{{< admonition >}}
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy
  ```

'''
{{< /card >}}

[[tab]]
name = 'System Package Managers'
content = '''
Not recommended for most users, but available for convenience.

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

A word of warning: building Numpy from source can be a nontrivial exercise.
추천하는 방식은 대신 이진 코드를 사용하는 것입니다. 여러분의 플랫폼을 위한 이진 코드가 위 방법들 중 하나로 제공된다면.
자세한 내용은 [ Numpy 문서의 소스 코드로 부터 빌드하는 법 안내](https://numpy.org/devdocs/building/)를 참고 바랍니다.

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

Importing the numpy c-extensions failed. 이 오류를 발생시킬 수 있는 원인은 여러가지 있을 수 있고, 때로는 여러분의 설정과 관련된 문제일 수 있습니다.
```

