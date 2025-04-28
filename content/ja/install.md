---
title: NumPyのインストール
sidebar: false
---

{{< admonition >}}
{{< /admonition >}}

NumPy のインストールする推奨の方法は、希望するワークフローによって異なります。 そこで、インストール方法を以下のカテゴリに分類しました。

- **プロジェクトベースの方法** (例: uv, pixi) _(新規ユーザーに推奨)_
- **環境ベースの方法** (例: pip, conda) _(従来のワークフロー)_
- **システムパッケージマネージャーを使う方法** _(ほとんどのユーザーには非推奨)_
- **ソース からのビルド** _(経験豊富なユーザーおよび開発者向け)_

あなたの目的に応じて最適な方法を選択してください。 どの方法を使うべきか分からない場合は、 **環境ベースの方法** を元に、conda または pip を使って開始しましょう。

{{< tabs >}}

[[tab]]
name = 'プロジェクトベースの方法'
content = '''

合理的なワークフローを求める、新規ユーザーにお勧めです。

- **uv**スピードとシンプルさを兼ね備えたモダンなPythonパッケージマネージャ。
  ```bash
  uv pip install numpy
  ```

- **pixi:** Pythonやその他の言語のためのクロスプラットフォームパッケージマネージャ
  ```bash
  pixi add numpy
  ```



個人的な好みや、下記のcondaとpipの違いを理解した上で、pip/PyPIベースの方法を使いたいユーザーには、下記をお勧めします:

`pip` と `conda` がPythonパッケージをインストールするための2つの主要なツールです。 これら二つのツールの機能は部分的に重複しますが(例えば、両方とも `numpy`をインストールできます)、一緒に動作することもできます。 ハイパフォーマンスコンピューティング(HPC)では、 <a href="https://github.com/spack/spack">Spack</a> を使うことを検討して下さい。

pipとcondaの最初の違いは、Conda は複数の言語に対応しており Python 自体をインストールできるのに対し、pip は特定の Python 環境にインストールされ、その Python に対してのみパッケージをインストールすることができることです。 これら二つのツールの機能は部分的に重複しますが(例えば、両方とも <code>numpy</code>をインストールできます)、一緒に動作することもできます。

2つ目の違いは、pipはPython Packaging Index(PyPI) からパッケージをインストールするのに対し、condaは独自のチャンネル(一般的には "defaults "や "conda-forge "など) からインストールすることです。 PyPIは最大のパッケージ管理システムですが、人気のある全てのパッケージがcondaでも利用可能です。

3つ目の違いは、condaはパッケージ、依存関係、環境を管理するための統合されたソリューションであるのに対し、pipでは環境や複雑な依存関係を扱うために別のツールであることです。(他にもたくさん存在しています！) これらのツールは様々な環境や複雑な依存関係を取り扱うことができます

- **Conda:** conda を使用している場合、デフォルトの設定先、または conda-forge チャンネルから NumPyをインストールできます。
  ```bash
  conda create -n my-env
  conda activate my-env
  conda conda install numpy
  ```
- **Pip:**
  ```bash
  pip install numpy
  ```

{{< admonition >}}
{{< /admonition >}}

  ```bash
  python -m venv my-env
  source my-env/bin/activate # macOS/Linux
  my-env\Scripts\activate # Windows
  pip install numpy
  ```



[[tab]]
name = 'システムパッケージマネージャを利用'
content = '''
ほとんどのユーザーには推奨されませんが、こちらの方が便利な人向けに利用可能です。

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



[[tab]]
name = 'ソースコードからビルドする'
content = '''
**NumPy**をカスタマイズやデバッグしたい、経験豊富なユーザーや開発者向け

警告:ソースコードからNumPyをビルドすることは簡単では無い場合があります。
前述のいずれかの方法であなたの環境NumPyを使用できる場合は、バイナリを使用することをお勧めします.
ソースからのビルドの詳細な方法については、[Numpy docsのソースガイドからのビルド](https://numpy.org/devdocs/building/)を参照してください。

{{< /tabs >}}

## 推奨方法

NumPy をインストールした後、以下のコードをPython シェルまたはスクリプトで実行して、インストールが正しく実施されているか確認してください。

```python
import numpy as np
print(np.__version__)
```

インストールに問題が無い場合は、インストールされているNumPyのバージョンが表示されるはずです。

## トラブルシューティング

以下のメッセージが表示されてインストールに失敗した場合は、トラブルシューティング
ImportErrorを参照してください。

```
重要：この問題を解決する方法についてのアドバイスを読む前に、こちらを必ずお読みください！

NumPy の C 拡張モジュールのインポートに失敗しました。このエラーは、さまざまな理由で発生する可能性があり、多くの場合は環境セットアップの問題が原因です。
```

