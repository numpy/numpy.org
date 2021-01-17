---
title: Numpyのインストール
sidebar: false
---

Numpy をインストールするための必ず必要なものはPython本体です。 もしまだPythonをインストールしていないのであれば、最もシルプルな始め方として、こちらがあります: [Anaconda Distribution](https://www.anaconda.com/distribution)。このanacondaはPythonだけでなく、NumPyや、その他科学技術計算やデータサイエンスのために一般的に使用される沢山のパッケージが含まれています。

NumPyは`conda`や`pip` 、Mac OSやLinuxのパッケージマネージャー、または [ソースコード](https://numpy.org/devdocs/user/building.html)からインストールすることが出来ます。 詳細な手順については、以下の [Python と Numpyの インストールガイド](#python-numpy-install-guide) を参照してください。

**CONDA**

`conda`を使用する場合、 `defaults` または `conda-forge` のチャンネルから NumPy をインストールできます。

```bash
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

**PIP**

`pip`を使用している場合は、 NumPy を以下のようにインストールできます:

```bash
pip install numpy
```
またpipを使う場合、仮想環境を使うことをおすすめします - 参考  [再現可能なインストール](#reproducible-installs) 。 [こちらの記事](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)では仮想環境を使う詳細について説明されています。

<a name="python-numpy-install-guide"></a>

# Python と Numpy インストールガイド

Pythonパッケージのインストールと管理は複雑なで、ほとんどのタスクには数多くの代替ツールがあります。 このガイドでは、読者に最適な(または最も人気のある) 方法と明確な指針を提供したいと思います。 このガイドでは、一般的なオペレーティングシステムとハードウェア上での、 Python、NumPy、PyData (または数値計算) スタックのユーザに焦点を当てています。

## 推奨方法

まずはユーザの経験のレベルと、関心のあるOSに基づいた推奨方法から説明していきたいと思います。 PythonやNumpyの経験が「初級」と「上級」の間の方や、シンプルにインストールしたい方は「初級」を、より長い視点にたったベストプラクティスに沿ってインストールしたい方は「上級」を参照下さい。

### 初級ユーザ

Windows、macOS、Linuxのすべてのユーザー向けには:

- [Anaconda](https://www.anaconda.com/distribution/) をインストールします（必要な パッケージと以下に挙げるすべてのツールがインストールされます）。
- コードを書いたり、実行するために[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) でnotebookを利用することができます。また探索的、対話的コンピューティングも可能です。[Spyder](https://www.spyder-ide.org/) 、[Visual Studio Code](https://code.visualstudio.com/)はスクリプトを作成したり、パッケージを作成することができます。
- 是非、[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) を使用して パッケージを管理し、JupyterLab、Spyder、Visual Studio Code を利用してみて下さい。


### 上級ユーザー

#### WindowsまたはmacOS

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) をインストールします。
- `ベース` のconda環境を出来るだけ小さく保ちます。 そして、作業中のタスクやプロジェクトに必要なパッケージは個別の` ` [conda 環境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) を使用して、インストールするようにします。
- もし、あなたの必要なパッケージが`defaults` チャンネルだけで足りない場合は、`conda-forge` こちらの [チャンネルプライオリティの設定](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge)でデフォルトチャンネルを設定することができます。


#### Linux

もしあなたが最新バージョンのライブラリを使用するよりも、少し古いパッケージで安定性を求める場合は:
- 可能な限りOS付帯のパッケージマネージャーを使用してください (Python本体やNumPy、 その他のライブラリのインストールに)。
- `pip install somepackage --user` でパッケージマネージャによって提供されていないパッケージをインストールすることができます。

GPUを使用する場合:
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) をインストールして下さい。
- `ベース` のconda環境を出来るだけ小さく保ちます。 そして、作業中のタスクやプロジェクトに必要なパッケージは個別の` ` [conda 環境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) を使用して、インストールするようにします。
- また、`デフォルトの` conda channel (`conda-forge` は GPU パッケージをまだサポートしていません) を使用してください。

上記以外の場合
- [Miniforge](https://github.com/conda-forge/miniforge) をインストールします。
- `ベース` のconda環境を出来るだけ小さく保ちます。 そして、作業中のタスクやプロジェクトに必要なパッケージは個別の` ` [conda 環境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) を使用して、インストールするようにします。


#### pip/PyPI を利用したい場合

個人的な好みや、下記のcondaとpipの違いを理解した上で、pip/PyPIベースの方法を使いたいユーザーには、下記をお勧めします:
- Pythonをインストールします。例えば、 [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/), または Linux パッケージマネージャを使うことができます。
- 依存関係の解決と環境の管理を提供する最もよくメンテナンスされているツールとして、[Poetry](https://python-poetry. org/) をconda と同様な方法で使用することができます。


## Python パッケージ管理

パッケージの管理は難しいので、その結果、たくさんのツールが存在しています。 ウェブ開発と汎用的なPython開発には、こちらのようなpipを補完する [ツール](https://packaging.python.org/guides/tool-recommendations/) があります。 ハイパフォーマンスコンピューティング(HPC)では、 [Spack](https://github.com/spack/spack) を使うことを検討して下さい。 NumPyのほとんどのユーザーにとっては、 [conda](https://conda.io/en/latest/) と [pip](https://pip.pypa.io/en/stable/) が最も広く利用されているツールです。


### Pip & conda

Python パッケージをインストールするための2 つの主要なツールは `pip` と `conda` です。 これらの二つのツールの機能は部分的に重複しますが(例えば、両方とも `numpy`をインストールできます)、これらは一緒に動作することもできます。 ここでは、pip とconda の主要な違いについて説明します。パッケージをどのように効果的に管理するかを理解することが重要です。

最初の違いは、condaは複数言語に対応可能であり、condaからPythonをインストールできることです。pip はシステム上の特定の Python にインストールされ、パッケージはそのPythonにのみインストールします。 また、condaはPython 以外のライブラリや必要なツール (コンパイラ、CUDA、HDF5など) をインストールできますが、pip はできません。

2つ目の違いは、pipはPython Packaging Index(PyPI) からパッケージをインストールするのに対し、condaは独自のチャンネル(一般的には "defaults "や "conda-forge "など) からインストールすることです。 PyPIは、最大のパッケージ管理システムですが、すべての代表的なパッケージは、condaにも利用可能です。

3つ目の違いは、condaはパッケージ、依存関係、環境を管理するための統合されたソリューションであるのに対し、pipでは環境や複雑な依存関係を扱うために別のツール(たくさん存在しています！) が必要になるかもしれないということです。


### 再現可能なインストール

ライブラリが更新されると、コードの実行結果が変わったり、コードが壊れたりする可能性があります。 なので重要なことは、使用しているパッケージの組み合わせと各バージョンのセットを再構築できるようにしておくことです。 ベストプラクティスは次の通りです:

1. プロジェクトごとに異なる仮想環境を使用してください。
2. パッケージインストーラを使用してパッケージ名とバージョンを記録するようにします( それぞれに独自のメタデータフォーマットがあります)。
   - Condaの場合: [conda environments, environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
   - pipの場合: [仮想環境](https://docs.python.org/3/tutorial/venv.html) と [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetryの場合: [仮想環境と pyproject.toml](https://python-poetry.org/docs/basic-usage/)



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

