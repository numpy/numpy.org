---
title: NumPyのインストール
sidebar: false
---

3つ目の違いは、condaはパッケージ、依存関係、環境を管理するための統合されたソリューションであるのに対し、pipでは環境や複雑な依存関係を扱うために別のツール(たくさん存在しています！
NumPyは`conda`、`pip` 、macOSやLinuxのパッケージマネージャー、または [ソースコード](https://numpy.org/devdocs/user/building.html)からインストールすることが出来ます。 NumPyは`conda`、`pip` 、macOSやLinuxのパッケージマネージャー、または [ソースコード](https://numpy.org/devdocs/building)からインストールすることが出来ます。 詳細な手順については、以下の [Python と Numpyの インストールガイド](#python-numpy-install-guide) を参照してください。
{{< /admonition >}}

NumPy のインストールする推奨の方法は、希望するワークフローによって異なります。 そこで、インストール方法を以下のカテゴリに分類しました。

- **プロジェクトベースの方法** (例: uv, pixi) *(新規ユーザーに推奨)*
- **環境ベースの方法** (例: pip, conda) *(従来のワークフロー)*
- **システムパッケージマネージャーを使う方法** *(ほとんどのユーザーには非推奨)*
- **ソース** *からのビルド (経験豊富なユーザーおよび開発者向け)*

Choose the method that best suits your needs. If you're unsure, start with the **Environment-based** method using `conda` or `pip`.

Below are the different methods for **installing NumPy**. Click on the tabs to explore each method:
またpipを使う場合、仮想環境を使うことをおすすめします。 [再現可能なインストール](#reproducible-installs)を参照ください。 [こちらの記事](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)では仮想環境を使う詳細について説明されています。

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

Windows、macOS、Linuxのすべてのユーザー向けには:

個人的な好みや、下記のcondaとpipの違いを理解した上で、pip/PyPIベースの方法を使いたいユーザーには、下記をお勧めします:

`pip` と `conda` がPythonパッケージをインストールするための2つの主要なツールです。 ウェブ開発と汎用的なPython開発には、こちらのようなpipを補完する [ツール](https://packaging.python.org/guides/tool-recommendations/) があります。 ハイパフォーマンスコンピューティング(HPC)では、 [Spack](https://github.com/spack/spack) を使うことを検討して下さい。

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. これら二つのツールの機能は部分的に重複しますが(例えば、両方とも `numpy`をインストールできます)、一緒に動作することもできます。

2つ目の違いは、pipはPython Packaging Index(PyPI) からパッケージをインストールするのに対し、condaは独自のチャンネル(一般的には "defaults "や "conda-forge "など) からインストールすることです。 PyPIは最大のパッケージ管理システムですが、人気のある全てのパッケージがcondaでも利用可能です。

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
3つ目の違いは、condaはパッケージ、依存関係、環境を管理するための統合されたソリューションであるのに対し、pipでは環境や複雑な依存関係を扱うために別のツール(たくさん存在しています！
**Tip:** Use a virtual environment for better dependency management
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate  # macOS/Linux
  my-env\Scripts\activate     # Windows
  pip install numpy
  ```

[[tab]] name = 'System Package Managers' content = ''' Not recommended for most users, but available for convenience.

**macOS (Homebrew):**
```bash
# base envにインストールするのでなく、environmentを作成するのがベストプラクティスです
conda create -n my-env
conda activate my-env
# conda-forgeからインストールする場合
conda config --env --add channels conda-forge
# インストールコマンド
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

[[tab]] name = 'Building from Source' content = ''' For advanced users and developers who want to customize or debug **NumPy**.

A word of warning: building Numpy from source can be a nontrivial exercise. We recommend using binaries instead if those are available for your platform via one of the above methods. For details on how to build from source, see [the building from source guide in the Numpy docs](https://numpy.org/devdocs/building/).
{{< /tabs >}}

## 推奨方法

After installing NumPy, verify the installation by running the following in a Python shell or script:
```python
import numpy as np
print(np.__version__)
```

This should print the installed version of NumPy without errors.

## トラブルシューティング

インストールに失敗した場合に、下記のエラーメッセージが表示される場合は、 <a href="https://numpy.org/doc/stable/user/troubleshooting-importerror.html">トラブルシューティング ImportError</a> を参照してください。

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for different reasons, often due to issues with your setup.
```

