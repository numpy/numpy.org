---
title: Instalando o NumPy
sidebar: false
---

O único pré-requisito para instalar o NumPy é o próprio Python. Se você ainda não tem o Python e quer começar do jeito mais simples, nós recomendamos que você use a [Distribuição Anaconda](https://www.anaconda.com/distribution) - inclui Python, NumPy e outros pacotes comumente usados para computação científica e ciência de dados.

O NumPy pode ser instalado com `conda`, com `pip`, com um gerenciador de pacotes no macOS e Linux, ou [da fonte](https://numpy.org/devdocs/user/building.html). Para obter instruções mais detalhadas, consulte nosso [guia de instalação do Python e do NumPy](#python-numpy-install-guide) abaixo.

**CONDA**

Se você usar o `conda`, você pode instalar o NumPy do canal `default` ou do `conda-forge`:

```bash
# Recomenda-se usar um ambiente novo ao invés de instalar no ambiente-base
conda create -n my-env
conda activate my-env
# Se quiser instalar do conda-forge
conda config --env --add channels conda-forge
# O comando para instação
conda install numpy
```

**PIP**

Se você usa o `pip`, você pode instalar o NumPy com:

```bash
pip install numpy
```
Também ao usar o pip, é uma boa prática usar um ambiente virtual - veja em [Instalações Reprodutíveis](#reproducible-installs) abaixo por quê, e [esse guia](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) para detalhes sobre o uso de ambientes virtuais.

<a name="python-numpy-install-guide"></a>

# Guia de instalação do Python e do NumPy

Instalar e gerenciar pacotes no Python pode ser complicado. Há várias soluções alternativas para a maioria das tarefas. Este guia tenta dar ao leitor um resumo das melhores (ou mais populares) soluções e dar recomendações claras. Ele se concentra em usuários do Python, NumPy e do PyData (ou computação numérica) em sistemas operacionais e hardware comuns.

## Recomendações

Vamos começar com recomendações baseadas no nível de experiência do usuário e no sistema operacional de interesse. Se você estiver entre "iniciante" e "avançado", por favor, escolha "iniciante" se você quiser manter as coisas simples, e "avançado" se você quiser trabalhar de acordo com as melhores práticas que te ajudarão a ir mais longe no futuro.

### Usuários iniciantes

Em Windows, macOS e Linux:

- Instale o [Anaconda](https://www.anaconda.com/distribution/) (instala todos os pacotes que você precisa e todas as outras ferramentas mencionadas abaixo).
- Para escrever e executar código, use notebooks no [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) para a computação exploratória e interativa, e o [Spyder](https://www.spyder-ide.org/) ou [Visual Studio Code](https://code.visualstudio.com/) para escrever scripts e pacotes.
- Use o [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) para gerenciar seus pacotes e iniciar o JupyterLab, Spyder ou o Visual Studio Code.


### Usuários avançados

#### Conda

- Instale o [Miniforge](https://github.com/conda-forge/miniforge).
- Mantenha o ambiente conda `base` mínimo, e use um ou mais [ambientes conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) para instalar o pacote que você precisa para a tarefa ou projeto em que você está trabalhando.

#### Alternativa se você preferir pip/PyPI

Para usuários que preferem uma solução baseada em pip/PyPI, por preferência pessoal ou leitura sobre as principais diferenças entre o conda e o pip, nós recomendamos:
- Instale o Python a partir de, por exemplo, [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/), ou seu gerenciador de pacotes Linux.
- Use [Poetry](https://python-poetry.org/) como a ferramenta mais bem mantida que fornece um resolvedor de dependências e recursos de gerenciamento de ambiente de forma semelhante ao que o conda faz.


## Gerenciamento de pacotes Python

Gerenciar pacotes é um problema desafiador e, como resultado, há muitas ferramentas. Para o desenvolvimento web e de propósito geral em Python, há uma [série de ferramentas](https://packaging.python.org/guides/tool-recommendations/) complementares com pip. Para computação de alto desempenho (HPC), vale a pena considerar o [Spack](https://github.com/spack/spack). Para a maioria dos usuários NumPy, porém, o [conda](https://conda.io/en/latest/) e o [pip](https://pip.pypa.io/en/stable/) são as duas ferramentas mais populares.


### Pip & conda

As duas principais ferramentas que instalam pacotes do Python são `pip` e `conda`. Algumas de suas funcionalidades são redundantes (por exemplo, ambos podem instalar o `numpy`). No entanto, elas também podem trabalhar juntas. Vamos discutir as principais diferenças entre o pip e o conda aqui - é importante entender isso se você deseja gerenciar pacotes de forma efetiva.

A primeira diferença é que "conda" é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Isto também significa que o conda pode instalar bibliotecas e ferramentas não-Python das quais você pode precisar (por exemplo, compiladores, CUDA, HDF5), enquanto pip não pode.

A segunda diferença é que o pip instala do Índice de Pacotes Python (Python Packaging Index - PyPI), enquanto o conda instala de seus próprios canais (tipicamente "defaults" ou "conda-forge"). PyPI é a maior coleção de pacotes, no entanto, todos os pacotes populares também estão disponíveis para conda.

A terceira diferença é que o conda é uma solução integrada para gerenciar pacotes, dependências e ambientes, enquanto com o pip você pode precisar de outra ferramenta (há muitas!) para lidar com ambientes ou dependências complexas.

<a name="reproducible-installs"></a>

### Instalações reprodutíveis

À medida que as bibliotecas são atualizadas, os resultados obtidos ao executar seu código podem mudar, ou o seu código pode parar de funcionar. É importante poder reconstruir o conjunto de pacotes e versões que você está usando. A recomendação é:

1. usar um ambiente diferente para cada projeto em que você trabalha,
2. gravar nomes de pacotes e versões usando seu instalador de pacotes; cada um tem seu próprio formato de metadados para essa tarefa:
   - Conda: [ambientes conda e arquivos environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - Pip: [ambientes virtuais](https://docs.python.org/3/tutorial/venv.html) e [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [ambientes virtuais e pyproject.toml](https://python-poetry.org/docs/basic-usage/)



## Pacotes NumPy & bibliotecas de álgebra linear aceleradas

O NumPy não depende de quaisquer outros pacotes Python. No entanto, depende de uma biblioteca de álgebra linear acelerada - tipicamente [Intel MKL](https://software.intel.com/en-us/mkl) ou [OpenBLAS](https://www.openblas.net/). Os usuários não precisam se preocupar com a instalação desses pacotes (eles são incluídos automaticamente em todos os métodos de instalação do NumPy). No entanto, usuários experientes podem querer saber os detalhes, porque o BLAS usado pode afetar o desempenho, o comportamento e o tamanho em disco:

- As wheels da NumPy no PyPI, que é o que o pip instala, são compiladas com OpenBLAS. As bibliotecas da OpenBLAS são empacotadas dentro da wheel. Isso faz com que a wheel fique maior, e se um usário também instalar (por exemplo) a SciPy, terá agora duas cópias da OpenBLAS no disco.

- No canal defaults do conda, a NumPy é compilada com a Intel MKL. MKL é um pacote separado que será instalado no ambiente do usuário quando instalar a NumPy.

- No canal do conda-Forge, a NumPy é compilada com um pacote "BLAS" fictício. Quando um usuário instala o NumPy do conda-forge, esse pacote BLAS então é instalado juntamente com a biblioteca real - o padrão é OpenBLAS, mas também pode ser MKL (do canal defaults), ou até mesmo [BLIS](https://github.com/flame/blis) ou *reference BLAS*.

- O pacote MKL é muito maior que o OpenBLAS, ocupa cerca de 700 MB no disco enquanto OpenBLAS ocupa cerca de 30 MB.

- A MKL é normalmente um pouco mais rápida e mais robusta do que a OpenBLAS.

Além do tamanho instalado, desempenho e robustez, há mais duas coisas a se considerar:

- A Intel MKL não é de código aberto. Para uso normal isto não é um problema, mas se um usuário precisa redistribuir uma aplicação compilada com a NumPy, isso pode ser um problema.
- Tanto MKL quanto OpenBLAS usarão multi-threading para chamadas de função como `np.dot`, com o número de threads sendo determinado tanto por uma opção no momento da compilação quanto por uma variável de ambiente. Muitas vezes, todos os núcleos de CPU serão usados. Isto é, às vezes, inesperado para usuários; o NumPy em si não paraleliza automaticamente nenhuma chamada de função. Normalmente, isso produz melhor desempenho, mas também pode ser prejudicial - por exemplo, ao usar outro nível de paralelização com Dask, scikit-learn ou multiprocessamento.


## Solução de problemas

Se sua instalação falhar com a mensagem abaixo, consulte [Solucionando ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

