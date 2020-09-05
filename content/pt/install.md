---
title: Instalando a NumPy
sidebar: false
---

O único pré-requisito para a NumPy é o próprio Python. Se você ainda não tem o Python e quer começar do jeito mais simples, nós recomendamos que você use a [Distribuição Anaconda](https://www.anaconda.com/distribution) - inclui Python, NumPy e outros pacotes comumente usados para computação científica e ciência de dados.

A NumPy pode ser instalada com `conda`, com `pip`, ou com um gerenciador de pacotes no macOS e Linux. Para obter instruções mais detalhadas, consulte nosso [guia de instalação do Python e da NumPy](#python-numpy-install-guide) abaixo.

## conda

Se você usar o `conda`, você pode instalar a NumPy com:

```bash
conda install numpy
```

## pip

Se você usar o `pip`, você pode instalar a NumPy com:

```bash
pip install numpy
```

<a name="python-numpy-install-guide"></a>

# Guia de instalação do Python e da NumPy

Instalar e gerenciar pacotes no Python pode ser complicado. Há várias soluções alternativas para a maioria das tarefas. Este guia tenta dar ao leitor um resumo das melhores soluções (ou mais populares) e dar recomendações claras. Ele se concentra em usuários do Python, NumPy e do PyData (ou cálculo numérico) em sistemas operacionais e hardware comuns.

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
- Instale pacotes não fornecidos pelo seu gerenciador de pacotes com `pip install somepackage --user`.

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


## Gerenciamento de pacotes Python

Gerenciar pacotes é um problema desafiador e, como resultado, há muitas ferramentas. Para o desenvolvimento web e de propósito geral em Python, há uma [série de ferramentas](https://packaging.python.org/guides/tool-recommendations/) complementares com pip. Para computação de alto desempenho (HPC), vale a pena considerar o [Spack](https://github.com/spack/spack). Para a maioria dos usuários NumPy, porém, [conda](https://conda.io/en/latest/) e [pip](https://pip.pypa.io/en/stable/) são as duas ferramentas mais populares.


### Pip & conda

As duas principais ferramentas que instalam pacotes do Python são `pip` e `conda`. Algumas de suas funcionalidades são redundantes (por exemplo, ambos podem instalar o `numpy`). No entanto, elas também podem trabalhar juntas. Vamos discutir as principais diferenças entre o pip e o conda aqui - é importante entender isso se você deseja gerenciar pacotes de forma efetiva.

A primeira diferença é que "conda" é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Isto também significa que o conda pode instalar bibliotecas e ferramentas não-Python das quais você pode precisar (por exemplo, compiladores, CUDA, HDF5), enquanto pip não pode.

A segunda diferença é que o pip instala do Índice de Pacotes Python (Python Packaging Index - PyPI), enquanto o conda instala de seus próprios canais (tipicamente "defaults" ou "conda-forge"). PyPI é a maior coleção de pacotes, no entanto, todos os pacotes populares também estão disponíveis para conda.

A terceira diferença é que o pip não tem um _resolvedor de dependências_ (isso pode mudar no futuro), ao contrário do conda. Para casos simples (por exemplo, você só quer NumPy, SciPy, Matplotlib, Pandas, Scikit-learn, e alguns outros pacotes) isso não importa. No entanto, para casos complicados, é de se esperar que o conda faça um trabalho melhor, mantendo tudo funcionando bem ao mesmo tempo. A única desvantagem é que usar pip é tipicamente _bem_ mais rápido que instalar usando o conda.

A quarta diferença é que o conda é uma solução integrada para gerenciar pacotes, dependências e ambientes, enquanto com o pip você pode precisar de outra ferramenta (há muitas!) para lidar com ambientes ou dependências complexas.


### Instalações reprodutíveis

Manter a instalação de todos os pacotes de que sua análise, biblioteca ou aplicação depende reprodutível é importante. Parece óbvio, mas a maioria dos usuários não pensam em fazer isso (pelo menos até que seja tarde demais).

O problema com o gerenciamento de pacotes no Python é que mais cedo ou mais tarde, alguma coisa irá quebrar. Não é frequentemente tão ruim assim,

{{< figure src="/images/content_images/python_environment_xkcd.png" alt="Python Environment XKCD image" link="https://xkcd.com/1987/" width="400" attr="_XKCD illustration - Python environment degradation_">}}

mas com o tempo pode ficar ruim. Por isso, é importante poder excluir e reconstruir o conjunto de pacotes que você instalou.

A melhor prática é usar um ambiente diferente por projeto no qual você está trabalhando, e registrar pelo menos os nomes (e de preferência versões) dos pacotes dos quais você depende diretamente em um arquivo de metadados estático. Cada ferramenta de empacotamento tem seu próprio formato de metadados para isto:
- Conda: [ambientes conda e arquivos environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
- Pip: [ambientes virtuais](https://docs.python.org/3/tutorial/venv.html) e [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
- Poetry: [ambientes virtuais e pyproject.toml](https://python-poetry.org/docs/basic-usage/)

Às vezes, é desnecessário criar e alternar entre novos ambientes para tarefas pequenas. Nesse caso, recomendamos que você não instale muitos pacotes em seu ambiente base, e acompanhe as versões dos pacotes de alguma outra maneira (por exemplo, comentários dentro de arquivos, ou imprimir `numpy.__version__` após importá-lo nos notebooks).


## Pacotes NumPy & bibliotecas de álgebra linear aceleradas

A NumPy não depende de quaisquer outros pacotes Python, no entanto, depende de uma biblioteca de álgebra linear acelerada - tipicamente [Intel MKL](https://software.intel.com/en-us/mkl) ou [OpenBLAS](https://www.openblas.net/). Os usuários não precisam se preocupar em instalar estas bibliotecas, mas ainda pode ser importante entender como o empacotamento é feito e como isso afeta o desempenho e comportamento que os usuários vêem.

As wheels da NumPy no PyPI, que é o que o pip instala, são compiladas com OpenBLAS. As bibliotecas da OpenBLAS são empacotadas dentro da wheel. Isso faz com que a wheel fique maior, e se um usário também instalar (por exemplo) a SciPy, terá agora duas cópias da OpenBLAS no disco.

No canal defaults do conda, a NumPy é compilada com a Intel MKL. MKL é um pacote separado que será instalado no ambiente do usuário quando instalar a NumPy. Esse pacote MKL é muito maior que a OpenBLAS, várias centenas de MB. A MKL é normalmente um pouco mais rápida e mais robusta do que a OpenBLAS.

No canal do conda-Forge, a NumPy é compilada com um pacote "BLAS" fictício. Quando um usuário instala a NumPy do conda-forge, esse pacote BLAS então é instalado juntamente com a biblioteca real - o padrão é OpenBLAS, mas também pode ser MKL (do canal defaults), ou até mesmo [BLIS](https://github.com/flame/blis) ou BLAS.

Além do tamanho instalado, desempenho e robustez, há mais duas coisas a se considerar:
- Intel MKL não é de código aberto. Para uso normal isto não é um problema, mas se um usuário precisa redistribuir uma aplicação construída com a NumPy, isso pode ser um problema.
- Tanto MKL quanto OpenBLAS usarão multi-threading para chamadas de função como `np.dot`, com o número de threads sendo determinado tanto por uma opção no momento da compilação quanto por uma variável de ambiente. Muitas vezes, todos os núcleos de CPU serão usados. Isto é, às vezes, inesperado para usuários; a NumPy em si não paraleliza automaticamente nenhuma chamada de função. Isso também pode ser prejudicial para o desempenho, se outro nível de paralelização for usado manualmente ou com funcionalidade do Dask ou da scikit-learn, por exemplo.

