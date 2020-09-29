---
title: Instalando o NumPy
sidebar: false
---

O único pré-requisito para o NumPy é o próprio Python. Se você ainda não tem o Python e quer começar do jeito mais simples, nós recomendamos que você use a [Distribuição Anaconda](https://www.anaconda.com/distribution) - inclui Python, NumPy e outros pacotes comumente usados para computação científica e ciência de dados.

O NumPy pode ser instalado com `conda`, com `pip`, ou com um gerenciador de pacotes no macOS e Linux. Para obter instruções mais detalhadas, consulte nosso [guia de instalação do Python e do NumPy](#python-numpy-install-guide) abaixo.

## conda

Se você usa o `conda`, você pode instalar o NumPy com:

```bash
conda install numpy
```

## pip

Se você usa o `pip`, você pode instalar o NumPy com:

```bash
pip install numpy
```

<a name="python-numpy-install-guide"></a>

# Guia de instalação do Python e do NumPy

Instalar e gerenciar pacotes no Python pode ser complicado. Há várias soluções alternativas para a maioria das tarefas. Este guia tenta dar ao leitor um resumo das melhores (ou mais populares) soluções e dar recomendações claras. Ele se concentra em usuários do Python, NumPy e do PyData (ou cálculo numérico) em sistemas operacionais e hardware comuns.

## Recomendações

Vamos começar com recomendações baseadas no nível de experiência do usuário e no sistema operacional de interesse. Se você estiver entre "iniciante" e "avançado", por favor, escolha "iniciante" se você quiser manter as coisas simples, e "avançado" se você quiser trabalhar de acordo com as melhores práticas que te ajudarão a ir mais longe no futuro.

### Usuários iniciantes

Em Windows, macOS e Linux:

- Instale o [Anaconda](https://www.anaconda.com/distribution/) (instala todos os pacotes que você precisa e todas as outras ferramentas mencionadas abaixo).
- Para escrever e executar código, use notebooks no [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) para a computação exploratória e interativa, e o [Spyder](https://www.spyder-ide.org/) ou [Visual Studio Code](https://code.visualstudio.com/) para escrever scripts e pacotes.
- Use o [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) para gerenciar seus pacotes e iniciar o JupyterLab, Spyder ou o Visual Studio Code.


### Usuários avançados

#### Windows ou macOS

- Instale o [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Mantenha o ambiente conda `base` mínimo, e use um ou mais [ambientes conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) para instalar o pacote que você precisa para a tarefa ou projeto em que você está trabalhando.
- A menos que você esteja satisfeito com apenas os pacotes no canal `defaults`, faça do `conda-forge` seu canal padrão [definindo a prioridade do canal](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge).


#### Linux

Se você não tiver problemas em ter pacotes um pouco desatualizados e preferir estabilidade ao invés de ser capaz de usar as últimas versões das bibliotecas:
- Use seu gerenciador de pacotes do SO o máximo possível (para o Python, NumPy e outras bibliotecas).
- Instale pacotes não fornecidos pelo seu gerenciador de pacotes com `pip install algumpacote --user`.

Se você usa uma GPU:
- Instale o [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Mantenha o ambiente conda `base` mínimo, e use um ou mais [ambientes conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) para instalar o pacote que você precisa para a tarefa ou projeto em que você está trabalhando.
- Use o canal conda`defaults` (`conda-forge` não tem bom suporte para pacotes de GPU).

Caso contrário:
- Instale o [Miniforge](https://github.com/conda-forge/miniforge).
- Mantenha o ambiente conda `base` mínimo, e use um ou mais [ambientes conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) para instalar o pacote que você precisa para a tarefa ou projeto em que você está trabalhando.


#### Alternativa se você preferir pip/PyPI

Para usuários que preferem uma solução baseada em pip/PyPI, por preferência pessoal ou leitura sobre as principais diferenças entre a conda e o pip, nós recomendamos:
- Instale o Python a partir de, por exemplo, [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/), ou seu gerenciador de pacotes Linux.
- Use [Poetry](https://python-poetry.org/) como a ferramenta mais bem mantida que fornece um resolvedor de dependências e recursos de gerenciamento de ambiente de forma semelhante ao que o conda faz.


## Troubleshooting ImportError

If your installation fails with the message below, see [Troubleshooting ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

## Building from source

See [Building from source](https://numpy.org/devdocs/user/building.html).


## Python package management

Managing packages is a challenging problem, and, as a result, there are lots of tools. For web and general purpose Python development there's a whole [host of tools](https://packaging.python.org/guides/tool-recommendations/) complementary with pip. For high-performance computing (HPC), [Spack](https://github.com/spack/spack) is worth considering. For most NumPy users though, [conda](https://conda.io/en/latest/) and [pip](https://pip.pypa.io/en/stable/) are the two most popular tools.


### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their functionality partially overlaps (e.g. both can install `numpy`), however, they can also work together. We'll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can't.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically "defaults" or "conda-forge"). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

The third difference is that pip does not have a _dependency resolver_ (this is expected to change in the near future), while conda does. For simple cases (e.g. you just want NumPy, SciPy, Matplotlib, Pandas, Scikit-learn, and a few other packages) that doesn't matter, however, for complicated cases conda can be expected to do a better job keeping everything working well together. The flip side of that coin is that installing with pip is typically a _lot_ faster than installing with conda.

The fourth difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.


### Instalações reprodutíveis

Making the installation of all the packages your analysis, library or application depends on reproducible is important. Sounds obvious, yet most users don't think about doing this (at least until it's too late).

The problem with Python packaging is that sooner or later, something will break. It's not often this bad,

{{< figure src="/images/content_images/python_environment_xkcd.png" alt="Python Environment XKCD image" link="https://xkcd.com/1987/" width="400" attr="_XKCD illustration - Python environment degradation_">}}

but it does degrade over time. Hence, it's important to be able to delete and reconstruct the set of packages you have installed.

Best practice is to use a different environment per project you're working on, and record at least the names (and preferably versions) of the packages you directly depend on in a static metadata file. Each packaging tool has its own metadata format for this:
- Conda: [ambientes conda e arquivos environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
- Pip: [ambientes virtuais](https://docs.python.org/3/tutorial/venv.html) e [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
- Poetry: [ambientes virtuais e pyproject.toml](https://python-poetry.org/docs/basic-usage/)

Sometimes it's too much overhead to create and switch between new environments for small tasks. In that case we encourage you to not install too many packages into your base environment, and keep track of versions of packages some other way (e.g. comments inside files, or printing `numpy.__version__` after importing it in notebooks).


## NumPy packages & accelerated linear algebra libraries

NumPy doesn't depend on any other Python packages, however, it does depend on an accelerated linear algebra library - typically [Intel MKL](https://software.intel.com/en-us/mkl) or [OpenBLAS](https://www.openblas.net/). Users don't have to worry about installing those, but it may still be important to understand how the packaging is done and how it affects performance and behavior users see.

The NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS. The OpenBLAS libraries are shipped within the wheels itself. This makes those wheels larger, and if a user installs (for example) SciPy as well, they will now have two copies of OpenBLAS on disk.

In the conda defaults channel, NumPy is built against Intel MKL. MKL is a separate package that will be installed in the users' environment when they install NumPy. That MKL package is a lot larger than OpenBLAS, several hundred MB. MKL is typically a little faster and more robust than OpenBLAS.

In the conda-forge channel, NumPy is built against a dummy "BLAS" package. When a user installs NumPy from conda-forge, that BLAS package then gets installed together with the actual library - this defaults to OpenBLAS, but it can also be MKL (from the defaults channel), or even [BLIS](https://github.com/flame/blis) or reference BLAS.

Besides install sizes, performance and robustness, there are two more things to consider:
- Intel MKL não é de código aberto. Para uso normal isto não é um problema, mas se um usuário precisa redistribuir uma aplicação construída com a NumPy, isso pode ser um problema.
- Tanto MKL quanto OpenBLAS usarão multi-threading para chamadas de função como `np.dot`, com o número de threads sendo determinado tanto por uma opção no momento da compilação quanto por uma variável de ambiente. Muitas vezes, todos os núcleos de CPU serão usados. Isto é, às vezes, inesperado para usuários; a NumPy em si não paraleliza automaticamente nenhuma chamada de função. Isso também pode ser prejudicial para o desempenho, se outro nível de paralelização for usado manualmente ou com funcionalidade do Dask ou da scikit-learn, por exemplo.

