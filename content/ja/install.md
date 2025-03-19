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

あなたの目的に応じて最適な方法を選択してください。 どの方法を使うべきか分からない場合は、 **環境ベースの方法** を元に、`conda` または `pip` を使って開始しましょう。

以下は、**NumPyをインストールする**様々な方法です。 タブをクリックして、各種方法を確認してください。
またpipを使う場合、仮想環境を使うことをおすすめします。 [再現可能なインストール](#reproducible-installs)を参照ください。 [こちらの記事](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto)では仮想環境を使う詳細について説明されています。

[[tab]] name = 'プロジェクトベースの方法' content = '''

合理的なワークフローを求める、新規ユーザーにお勧めです。

- **uv:** スピードとシンプルさを兼ね備えたモダンなPythonパッケージマネージャ。
  ```bash
  uv pip install numpy
  ```

- **pixi:** Pythonやその他の言語のためのクロスプラットフォームパッケージマネージャ
  ```bash
  pixi add numpy
  ```

Windows、macOS、Linuxのすべてのユーザー向けには:

個人的な好みや、下記のcondaとpipの違いを理解した上で、pip/PyPIベースの方法を使いたいユーザーには、下記をお勧めします:

`pip` と `conda` がPythonパッケージをインストールするための2つの主要なツールです。 ウェブ開発と汎用的なPython開発には、こちらのようなpipを補完する [ツール](https://packaging.python.org/guides/tool-recommendations/) があります。 ハイパフォーマンスコンピューティング(HPC)では、 [Spack](https://github.com/spack/spack) を使うことを検討して下さい。

pipとcondaの最初の違いは、Conda は複数の言語に対応しており Python 自体をインストールできるのに対し、pip は特定の Python 環境にインストールされ、その Python に対してのみパッケージをインストールすることができることです。 これら二つのツールの機能は部分的に重複しますが(例えば、両方とも `numpy`をインストールできます)、一緒に動作することもできます。

2つ目の違いは、pipはPython Packaging Index(PyPI) からパッケージをインストールするのに対し、condaは独自のチャンネル(一般的には "defaults "や "conda-forge "など) からインストールすることです。 PyPIは最大のパッケージ管理システムですが、人気のある全てのパッケージがcondaでも利用可能です。

3つ目の違いは、Conda はパッケージ、依存関係、環境を管理するための統合的なソリューションであるのに対し、pip を使用する場合は、環境管理や複雑な依存関係を処理するために別のツール（様々なツールがあります！）が必要になることがある点です。

- **Conda:** conda を使用している場合、デフォルトの設定先、または conda-forge チャンネルから NumPyをインストールできます。
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
**ヒント:** より良い依存関係管理のためには仮想環境を使用しましょう。
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate # macOS/Linux
  my-env\Scripts\activate # Windows
  pip install numpy
  ```

[[tab]] name = 'システムパッケージマネージャを利用' content = ''' ほとんどのユーザーには推奨されませんが、こちらの方が便利な人向けに利用可能です。

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

[[tab]] name = 'ソースコードからビルドする' content = ''' **NumPy**をカスタマイズやデバッグしたい、経験豊富なユーザーや開発者向け

警告:ソースコードからNumPyをビルドすることは簡単では無い場合があります。 前述のいずれかの方法であなたの環境NumPyを使用できる場合は、バイナリを使用することをお勧めします. ソースからビルドする方法の詳細については、[ NumPy のドキュメントにあるソースコードからのビルドガイド](https://numpy.org/devdocs/building/)を参照してください。
{{< /tabs >}}

## 推奨方法

NumPy をインストールした後、以下のコードをPython シェルまたはスクリプトで実行して、インストールが正しく実施されているか確認してください。
```python
import numpy as np
print(np.__version__)
```

インストールに問題が無い場合は、インストールされているNumPyのバージョンが表示されるはずです。

## トラブルシューティング

インストールに失敗した場合に、下記のエラーメッセージが表示される場合は、 <a href="https://numpy.org/doc/stable/user/troubleshooting-importerror.html">トラブルシューティング ImportError</a> を参照してください。

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for different reasons, often due to issues with your setup.
```

