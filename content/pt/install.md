---
title: Instalando o NumPy
sidebar: false
---

{{< admonition >}}
{{< /admonition >}}

O método recomendado de instalar o NumPy depende do seu fluxo de trabalho preferido. A seguir, dividimos os métodos de instalação entre as seguintes categorias:

- **Baseados em projeto** (por exemplo, uv, pixi) _(recomendados para novos usuários)_
- **Baseados em ambientes** (por exemplo, pip, conda) _(o fluxo de trabalho tradicional)_
- **Gerenciadores de pacotes de sistema** _(não recomendados para a maioria dos usuários)_
- **A partir do código-fonte** _(para usuários avançados e para fins de desenvolvimento)_

Escolha o método mais adequado às suas necessidades. Se não tiver certeza, comece com um método **baseado em ambientes** usando `conda` ou `pip`.

{{< tabs >}}

[[tab]]
name = 'Baseados em projetos'
conteúdo = '''

Recomendado para novos usuários que queiram um fluxo de trabalho simplificado.

- **uv:** Um gerenciador de pacotes Python moderno projetado para velocidade e simplicidade.
  ```bash
  uv pip install numpy
  ```

- **pixi:** Um gerenciador de pacotes multiplataforma para Python e outras linguagens.
  ```bash
  pixi add numpy
  ```

'''
{{< /card >}}

Para usuários que preferem uma solução baseada em pip/PyPI, por preferência pessoal ou leitura sobre as principais diferenças entre o conda e o pip explicadas adiante, nós recomendamos:

As duas principais ferramentas que instalam pacotes do Python são `pip` e `conda`. Para o desenvolvimento web e de propósito geral em Python, há uma [série de ferramentas](https://packaging.python.org/guides/tool-recommendations/) complementares ao pip. Para computação de alto desempenho (HPC), vale a pena considerar o <a href="https://github.com/spack/spack">Spack</a>.

A primeira diferença é que conda é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Elas têm algumas funcionalidades em comum (por exemplo, ambas podem instalar o <code>numpy</code>). No entanto, elas também podem trabalhar juntas.

A primeira diferença é que "conda" é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Isto também significa que o conda pode instalar bibliotecas e ferramentas não-Python das quais você pode precisar (por exemplo, compiladores, CUDA, HDF5), enquanto pip não pode.

A terceira diferença é que conda é uma solução integrada para gerenciar pacotes, dependências e ambientes, enquanto com pip você pode precisar de outra ferramenta (há muitas!) para lidar com ambientes ou dependências complexas.

- **Conda:** se você usar o conda, você pode instalar o NumPy do canal default ou do conda-forge:
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
name = 'Gerenciadores de Pacotes do Sistema'
conteúdo = '''
Não recomendado para a maioria dos usuários, mas disponível por conveniência.

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

[[tab]] name = 'A partir do código-fonte' conteúdo = ''' Para usuários avançados e desenvolvedores que querem personalizar ou depurar o **NumPy**.

Um pequeno aviso: construir o Numpy a partir do código-fonte pode ser um exercício não-trivial.
Recomendamos o uso de binários se eles estiverem disponíveis para a sua plataforma através de um dos métodos anteriores.
Para obter detalhes sobre como construir a partir do código-fonte, consulte [o guia de construção a partir do código-fonte na documentação do Numpy](https://numpy.org/devdocs/building/).

{{< /tabs >}}

## Recomendações

Depois de instalar o NumPy, verifique a instalação, executando o seguinte em um shell ou script Python:

```python
import numpy as np
print(np.__version__)
```

Isto deve imprimir a versão instalada do NumPy sem erros.

## Solução de problemas

Se sua instalação falhar com a mensagem abaixo, consulte [Solucionando ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

