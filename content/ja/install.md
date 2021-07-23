---
title: NumPyのインストール
sidebar: false
---

Numpy をインストールするための必ず必要なものはPython本体です。 NumPy をインストールするために必ず必要なものはPython本体です。もしまだPythonをインストールしていないのであれば、最もシルプルな始め方として、[Anaconda Distribution](https://www.anaconda.com/distribution)を推奨します。AnacondaはPython・NumPyの他に、科学技術計算やデータサイエンスのために一般的に使用される沢山のパッケージが含まれています。

NumPyは`conda`、`pip` 、macOSやLinuxのパッケージマネージャー、または [ソースコード](https://numpy.org/devdocs/user/building.html)からインストールすることが出来ます。 詳細な手順について、以下の [Python と NumPyの インストールガイド](#python-numpy-install-guide) を参照してください。 詳細な手順については、以下の [Python と Numpyの インストールガイド](#python-numpy-install-guide) を参照してください。

**CONDA**

`conda`を使用する場合、 `defaults` または `conda-forge` のチャンネルから NumPy をインストールできます。

```bash
# base envにインストールするのでなく、environmentを作成するのがベストプラクティスです
conda create -n my-env
conda activate my-env
# conda-forgeからインストールする場合
conda config --env --add channels conda-forge
# インストールコマンド
conda install numpy
```

**PIP**

`pip`を使用する場合、以下のようにNumPyをインストールできます:

```bash
pip install numpy
```
またpipを使う場合、仮想環境を使うことをおすすめします。[再現可能なインストール](#reproducible-installs)を参照ください。[こちらの記事](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)では仮想環境を使う詳細について説明されています。

<a name="python-numpy-install-guide"></a>

# PythonとNumPyの インストールガイド

Pythonパッケージのインストールと管理は複雑なので、ほとんどのタスクには数多くの代替ツールがあります。 このガイドでは、読者に最適な(または最も人気のある) 方法と明確な指針を提供したいと思います。 このガイドでは、一般的なオペレーティングシステムとハードウェア上での、 Python、NumPy、PyData (または数値計算) スタックのユーザに焦点を当てています。 このガイドでは、読者に最適な(または最も人気のある) 方法と明確な指針を提供したいと思います。 このガイドでは、一般的なオペレーティングシステムとハードウェア上での、 Python、NumPy、PyData (または数値計算) スタックのユーザに焦点を当てています。

## 推奨方法

まずはユーザの経験のレベルと、関心のあるOSに基づいた推奨方法から説明していきたいと思います。 PythonやNumpyの経験が「初級」と「上級」の間の方や、シンプルにインストールしたい方は「初級」を、より長い視点にたったベストプラクティスに沿ってインストールしたい方は「上級」を参照下さい。

### 初級ユーザ

Windows、macOS、Linuxのすべてのユーザー向けには:

- [Anaconda](https://www.anaconda.com/distribution/) をインストールします（必要な パッケージと以下に挙げるすべてのツールがインストールされます）。
- コードを書いたり、実行してみましょう。探索的・対話的コンピューティングには[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html)のノートブックが便利です。スクリプトやパッケージの作成には[Spyder](https://www.spyder-ide.org/)や[Visual Studio Code](https://code.visualstudio.com/)を利用できます。
- [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) を使ってパッケージを管理し、JupyterLab、Spyder、Visual Studio Codeを使い始められます。


### 上級ユーザー

#### WindowsまたはmacOS

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) をインストールします。
- `base` のconda環境を出来るだけ小さく保って下さい。 そして、一つか二つ個別の[`conda environment`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)を使って、作業中のタスクやプロジェクトに必要なパッケージをインストールしましょう。
- もし、あなたの必要なパッケージが`defaults` チャンネルだけで足りない場合は、`conda-forge`をこちらの [チャンネルプライオリティの設定](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge)でデフォルトチャンネルに設定できます。


#### Linux

もしあなたが最新バージョンのライブラリを使用するよりも、少し古いパッケージで安定性を求める場合は:
- Python本体やNumPy、その他のライブラリのインストールに、可能な限りOSのパッケージマネージャーを使用してください。。
- `pip install somepackage --user` でパッケージマネージャによって提供されていないパッケージをインストールすることができます。

GPUを使用する場合:
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) をインストールして下さい。
- `base` のconda環境を出来るだけ小さく保って下さい。 そして、一つか二つ個別の[`conda environment`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)を使って、作業中のタスクやプロジェクトに必要なパッケージをインストールしましょう。
- また、`デフォルトの` conda channel (`conda-forge` は GPU パッケージをまだサポートしていません) を使用してください。

上記以外の場合
- [Miniforge](https://github.com/conda-forge/miniforge) をインストールします。
- `base` のconda環境を出来るだけ小さく保って下さい。 そして、一つか二つ個別の[`conda environment`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)を使って、作業中のタスクやプロジェクトに必要なパッケージをインストールしましょう。


#### pip/PyPI を利用したい場合

個人的な好みや、下記のcondaとpipの違いを理解した上で、pip/PyPIベースの方法を使いたいユーザーには、下記をお勧めします:
- [python.org](https://www.python.org/downloads/)からや、Macを使っている場合は[Homebrew](https://brew.sh/)、 Linuxを使っている場合は、Linuxのパッケージマネージャーを使ってPythonをインストールします。
- 依存関係の解決と環境の管理を提供する最もよくメンテナンスされているツールとして、[Poetry](https://python-poetry.org/) をconda と同様な方法で使用することができます。


## Pythonにおけるパッケージ管理

パッケージの管理は難しいので、その結果、たくさんのツールが存在しています。 パッケージの管理は難しいため、たくさんのツールが存在しています。 ウェブ開発と汎用的なPython開発には、こちらのようなpipを補完する [ツール](https://packaging.python.org/guides/tool-recommendations/) があります。 ハイパフォーマンスコンピューティング(HPC)では、 [Spack](https://github.com/spack/spack) を使うことを検討して下さい。 NumPyのほとんどのユーザーにとっては、 [conda](https://conda.io/en/latest/) と [pip](https://pip.pypa.io/en/stable/) が最も広く利用されているツールです。 ハイパフォーマンスコンピューティング(HPC)では、 [Spack](https://github.com/spack/spack) を使うことを検討して下さい。 NumPyのほとんどのユーザーにとっては、 [conda](https://conda.io/en/latest/) と [pip](https://pip.pypa.io/en/stable/) が最も広く利用されているツールです。


### Pipとconda

`pip` と `conda` がPythonパッケージをインストールするための2つの主要なツールです。 これら二つのツールの機能は部分的に重複しますが(例えば、両方とも `numpy`をインストールできます)、一緒に動作することもできます。ここでは、pip とcond の主要な違いについて説明します。これは、パッケージをどのように効果的に管理するかを理解したい場合、重要な知識です。 これらの二つのツールの機能は部分的に重複しますが(例えば、両方とも `numpy`をインストールできます)、これらは一緒に動作することもできます。 ここでは、pip とconda の主要な違いについて説明します。パッケージをどのように効果的に管理するかを理解することが重要です。

最初の違いは、condaは複数言語に対応可能で、Python自体をインストールできることです。pip はシステム上の特定の Python にインストールされ、パッケージはそのPython用にのみインストールします。そのため、condaはPython 以外のライブラリや必要なツール (コンパイラ、CUDA、HDF5など) をインストールできますが、pip はできません。 また、condaはPython 以外のライブラリや必要なツール (コンパイラ、CUDA、HDF5など) をインストールできますが、pip はできません。

2つ目の違いは、pipはPython Packaging Index(PyPI) からパッケージをインストールするのに対し、condaは独自のチャンネル(一般的には "defaults "や "conda-forge "など) からインストールすることです。 PyPIは最大のパッケージ管理システムですが、人気のある全てのパッケージがcondaでも利用可能です。 PyPIは、最大のパッケージ管理システムですが、すべての代表的なパッケージは、condaにも利用可能です。

3つ目の違いは、condaはパッケージ、依存関係、環境を管理するための統合されたソリューションであるのに対し、pipでは環境や複雑な依存関係を扱うために別のツール(たくさん存在しています！) が必要になるかもしれないということです。


### 再現可能なインストール

ライブラリが更新されると、コードの実行結果が変わったり、コードが完全に 壊れたりする可能性があります。なので重要なことは、使用しているパッケージの組み合わせと各バージョンのセットを再構築できるようにしておくことです。 ベストプラクティスは次の通りです: なので重要なことは、使用しているパッケージの組み合わせと各バージョンのセットを再構築できるようにしておくことです。 ベストプラクティスは次の通りです:

1. プロジェクトごとに異なる仮想環境を使用して下さい。
2. パッケージインストーラを使用してパッケージ名とバージョンを記録するようにして下さい。それぞれ、独自のメタデータフォーマットがあります:
   - condaの場合: [conda environmentsとenvironment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
   - condaのデフォルトチャンネルでは、NumPy はインテル® MKLを使ってビルドされます。MKLはNumPyのインストール時に、独立したパッケージとしてユーザー環境にインストールされます。
   - conda-forgeのチャンネルでは、NumPyはダミーの「BLAS」パッケージを使ってビルドされています。 ユーザーがconda-forgeからNumPyをインストールすると、BLASパッケージが実際のライブラリと一緒にインストールされます。デフォルトはOpenBLASですが、MKL(default チャンネルの場合)や [BLIS](https://github.com/flame/blis)、またはBLASを利用することもできます。



## NumPyパッケージと高速線形代数ライブラリ

NumPy は他の Python パッケージに依存していませんが、高速な線形代数ライブラリに依存しています。典型的には、[インテル® MKL](https://software.intel.com/en-us/mkl)や[OpenBLAS](https://www.openblas.net/)がこれにあたります。ユーザーは、これらの線形代数ライブラリのインストールを心配する必要はありません (NumPyのインストール方法に、あらかじめ含まれているためです)。 高度なユーザーは、使用されているBLASがパフォーマンスや、動作、ディスク上のサイズに影響を与えるため、より詳細を知りたがるかもしれません。 ユーザーはこれらの線形代数ライブラリのインストールを心配する必要はありません (Numpy install メソッドが自動的に実施します)。 パワーユーザーの中には、使用されているBLASがパフォーマンスや、動作、ディスク上のサイズに影響を与えるため、より詳細を知りたいと思っているかもしれません。

- pipでインストールされるPyPI上の NumPy wheelは、OpenBLASを使ってビルドされます。つまりwheelにはOpenBLASライブラリが含まれています。そのため、ユーザが（例えば）SciPyも同じようにインストールした場合、ディスク上にOpenBLASのコピーをNumPyのものと2つ持つことになります つまりwheelにはOpenBLASライブラリが含まれています。 これにより、ユーザが（例えば）SciPyをインストールした場合、ディスク上にOpenBLASのコピーをNumpyのものと、2つ持つことになります

- Condaのデフォルトチャンネルでは、Numpy はインテル® MKLを使ってビルドされます。 MKL はNumpy をインストールしたときにユーザーの環境にインストールされるのとは、別のパッケージです。

- conda-forgeのチャンネルでは、Numpyはダミーの「BLAS」パッケージを使ってビルドされています。 ユーザーがconda-forgeからNumPyをインストールすると、BLASパッケージが実際のライブラリと一緒にインストールされます - デフォルトはOpenBLASですが、MKL(default チャンネルの場合)やBLIS<a>、またはBLASを利用することもできます。</p></li> 
  
  <li>
    <p spaces-before="0">
      OpenBLASは約30MBですが、MKLパッケージはOpenBLASよりもはるかに大きく、ディスク上の約700MBです。
    </p>
  </li>
  
  <li>
    <p spaces-before="0">
      MKLは通常、OpenBLASよりも少し速く、より安定した解を得られます。
    </p>
  </li></ul> 
  
  <p spaces-before="0">
    インストールサイズ、パフォーマンスとロバスト性に加えて、考慮すべき2つの点があります:
  </p>
  
  <ul>
    <li>
      <p spaces-before="0">
        インテル® MKL はオープンソースではありません。 通常の使用では問題ではありませんが、 ユーザーが NumPy で構築されたアプリケーションを再配布する必要がある場合、これは 問題が発生する可能性があります。 通常の使用では問題ではありませんが、 ユーザーが Numpy で構築されたアプリケーションを再配布する必要がある場合、これは 問題が発生する可能性があります。
      </p>
    </li>
    <li>
      <p spaces-before="0">
        MKLとOpenBLASの両方とも、 <code>np.dot</code>のような関数呼び出しにマルチスレッドを使用し、スレッド数はビルド時オプションと環境変数の両方で決定されます。 多くの場合、すべての CPU コアが使用されます。 これにユーザーにとっては予想外のことかもしれません。NumPy 自体は、関数呼び出しを自動的に並列化しないからです。 自動並列化により、一般にはパフォーマンスが向上しますが、逆にパフォーマンスが悪化する場合もあります。例えば、Daskやscikit-learn、multiprocessingなど別のレベルの並列化を使用している場合です。 多くの場合、すべての CPU コアが使用されます。 これによりユーザーに予期しないことが起こることがあります。例えばNumPy 自体は、関数呼び出しを自動的に並列化しないことです。 線形代数ライブラリの配列処理は、一般的にはより良いパフォーマンスが得られますが、Daskやscikit-learn、マルチプロセシングなどの別のレベルの並列化を使用している場合などに、逆に悪い結果をもたらすことがあります。
      </p>
    </li>
  </ul>
  
  


<h2 spaces-before="0">
  トラブルシューティング
</h2>

<p spaces-before="0">
  インストールに失敗した場合に、下記のエラーメッセージが表示される場合は、 <a href="https://numpy.org/doc/stable/user/troubleshooting-importerror.html">トラブルシューティング ImportError</a> を参照してください。
</p>

<pre><code>IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for different reasons, often due to issues with your setup.
</code></pre>

