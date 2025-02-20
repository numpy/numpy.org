---
title: Instalando o NumPy
sidebar: false
---

A terceira diferença é que o conda é uma solução integrada para gerenciar pacotes, dependências e ambientes, enquanto com o pip você pode precisar de outra ferramenta (há muitas!) para lidar com ambientes ou dependências complexas.
O NumPy pode ser instalado com `conda`, com `pip`, com um gerenciador de pacotes no macOS e Linux, ou [da fonte](https://numpy.org/devdocs/building). O único pré-requisito para instalar o NumPy é o próprio Python. Se você ainda não tem o Python e quer começar do jeito mais simples, nós recomendamos que você use a [Distribuição Anaconda](https://www.anaconda.com/distribution) - inclui Python, NumPy e outros pacotes comumente usados para computação científica e ciência de dados.
{{< /admonition >}}

The recommended method of installing NumPy depends on your preferred workflow. A seguir, dividimos os métodos de instalação entre as seguintes categorias:

- **Baseados em projeto** (por exemplo, uv, pixi) *(recomendados para novos usuários)*
- **Baseados em ambientes** (por exemplo, pip, conda) *(o fluxo de trabalho tradicional)*
- **Gerenciadores de pacotes de sistema** *(não recomendados para a maioria dos usuários)*
- **A partir do código-fonte** *(para usuários avançados e para fins de desenvolvimento)*

Escolha o método mais adequado às suas necessidades. Se não tiver certeza, comece com um método **baseado em ambientes** usando `conda` ou `pip`.

Os diferentes métodos para **instalar o NumPy** são os seguintes. Clique nas abas para explorar cada método:
Também ao usar o pip, é uma boa prática usar um ambiente virtual - veja em [Instalações Reprodutíveis](#reproducible-installs) abaixo por quê, e [esse guia](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) para detalhes sobre o uso de ambientes virtuais.

[[tab]] name = 'Baseados em projetos' conteúdo = '''

Recommended for new users who want a streamlined workflow.

- **uv:** A modern Python package manager designed for speed and simplicity.
  ```bash
  uv pip install numpy
  ```

- **pixi:** A cross-platform package manager for Python and other languages.
  ```bash
  pixi add numpy
  ```

Em Windows, macOS e Linux:

Para usuários que preferem uma solução baseada em pip/PyPI, por preferência pessoal ou leitura sobre as principais diferenças entre o conda e o pip explicadas adiante, nós recomendamos:

As duas principais ferramentas que instalam pacotes do Python são `pip` e `conda`. Para o desenvolvimento web e de propósito geral em Python, há uma [série de ferramentas](https://packaging.python.org/guides/tool-recommendations/) complementares ao pip. Para computação de alto desempenho (HPC), vale a pena considerar o [Spack](https://github.com/spack/spack).

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. Elas têm algumas funcionalidades em comum (por exemplo, ambas podem instalar o `numpy`). No entanto, elas também podem trabalhar juntas.

A primeira diferença é que "conda" é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Isto também significa que o conda pode instalar bibliotecas e ferramentas não-Python das quais você pode precisar (por exemplo, compiladores, CUDA, HDF5), enquanto pip não pode.

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
A terceira diferença é que o conda é uma solução integrada para gerenciar pacotes, dependências e ambientes, enquanto com o pip você pode precisar de outra ferramenta (há muitas!) para lidar com ambientes ou dependências complexas.
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
# Recomenda-se usar um ambiente novo ao invés de instalar no ambiente-base
conda create -n my-env
conda activate my-env
# Se quiser instalar do conda-forge
conda config --env --add channels conda-forge
# O comando para instação
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

## Recomendações

After installing NumPy, verify the installation by running the following in a Python shell or script:
```python
import numpy as np
print(np.__version__)
```

This should print the installed version of NumPy without errors.

## Solução de problemas

Se sua instalação falhar com a mensagem abaixo, consulte [Solucionando ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

