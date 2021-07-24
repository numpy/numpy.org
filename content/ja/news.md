---
title: ニュース
sidebar: false
---

### 2021年度NumPyアンケート

_2021年7月12日_ -- NumPy ではコミュニティの力を信じています。 昨年の第1回アンケートには、75カ国から1,236名のNumPyユーザーが参加しました。 調査結果により、今後12ヶ月間、私たちがどのようなことに集中すべきかを、非常に良く理解することができました。

今年もアンケートの時間が来ました。もう一度お願いいたします。 アンケートへの回答は15分ほどで終了します。 アンケートは英語以外にも、ベンガル語、フランス語、ヒンディー語、日本語、マンダリン、ポルトガル語、ロシア語、スペイン語の8ヶ国語に対応しています。

こちらのリンク先から、アンケートを始めることができます: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSL4q.


### NumPy 1.21.0 リリース

_2021年1月23日_ -- [Numpy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) が利用可能になりました。 今回のリリースのハイライトは次のとおりです。

- より多くの機能やプラットフォームをカバーするSIMD関連の作業が継続されました。
- 新しいdtypeインフラとキャストの初期作業
- mac 版の Python 3.8 と Python 3.9 用 universal2 wheels
- ドキュメントの改善
- アノテーションの改善
- 乱数生成用の新しい `PCG64DXSM` ビット生成機

今回のNumpy リリースは、175人が貢献した581件のプルリクエストのマージの結果です。 このリリースでサポートされている Python のバージョンは 3.7-3.9 です。Python 3.10 がリリースされた後、Python 3.10 のサポートが追加されます。


### 2020年度 NumPy アンケート結果

_2021年6月22日_ -- NumPyの調査チームは、2020年に ミシガン大学とメリーランド大学の学生や教員と協力して、最初の公式NumPyコミュニティ調査を実施しました。 アンケートの結果はこちらから確認できます。 https://numpy.org/user-survey-2020/


### Numpy 1.20.0 リリース

_2021年1月30日_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) が利用可能になりました。 今回のリリースは180以上のコントリビューターのおかげで、これまでで最大の NumPyのリリースとなりました。 最も重要な2つの新機能は次のとおりです。
- NumPyの大部分のコードに型注釈が追加されました。 そして新しいサブモジュールである`numpy.typing`が追加されました。 このサブモジュールは`ArrayLike` や`DtypeLike`という型注釈のエイリアスが定義されており、これによりユーザーやダウンストリームのライブラリはこの型注釈を使うことができます。
- X86(SSE、AVX)、ARM64(Neon)、およびPowerPC (VSX) 命令をサポートするマルチプラットフォームSIMDコンパイラの最適化が実施されました。 これにより、多くの関数で大きく パフォーマンスが向上しました (例: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPyプロジェクトにおける多様性

_2020年6月24日_ -- NumPy に新しいロゴが作成されました:


### Natureに初めての公式のNumPy論文が掲載されました!

_2020年9月16日_ -- \[NumPyに関する初の公式論文\] (https://www.nature.com/articles/s41586-020-2649-2) が査読付き論文として掲載されました。 これはNumPy 1.0のリリースから14年後のことになります。 この論文では、配列プログラミングのアプリケーションと基本的なコンセプト、NumPyの上に構築された様々な科学的Pythonエコシステム、そしてCuPy、Dask、JAXのような外部の配列およびテンソルライブラリとの相互運用を容易にするために最近追加された配列プロトコルについて説明しています。


### Python 3.9のリリースに伴い、いつNumPyのバイナリwheelがリリースされるのですか？

_2020年9月14日_ -- Python 3.9 は数週間後にリリースされる予定です。 もしあなたが新しいPythonのバージョンをいち早く取り入れているのであれば、NumPy（およびSciPyのような他のパッケージ）がリリース当日にバイナリwheelを用意していないことを知ってがっかりしたかもしれません。 ビルドインフラを新しいPythonのバージョンに適応させるのは大変な作業で、PyPIやconda-forgeにパッケージが掲載されるまでには通常数週間かかります。 wheelのリリースに備えて、以下を確認してください。
- `pip` が`manylinux2010` と `manylinux2014` をサポートするためにpipを少なくともバージョン 20.1 に更新する。
- [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) または `--only-binary=:all:` を`pip`がソースからビルドしようとするのを防ぐために使用します。


### NumPy 1.19.2 リリース

_2020年1月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) がリリースされました。 この 1.19 シリーズの最新リリースでは、いくつかのバグが修正され、[来るべき Cython 3.xリリース](http:/docs.cython.orgenlatestsrcchanges.html)への準備が行われ、アップストリームの修正が進行中の間も distutils の動作を維持するためのsetuptoolsの固定がされています。 aarch64 wheelは最新のmanylinux2014リリースで構築されており、異なるLinuxディストリビューションで使用される異なるページサイズの問題を修正しています。

### 初めてのNumPyのアンケートが公開されました!!

_2020年7月2日_ -- このサーベイは、ソフトウェアとして、またコミュニティとしてのNumPyの開発に関する意思決定の指針となり、優先順位を設定するためのものになりました。 この調査結果は英語以外の8つの言語で利用可能です: バングラ, ヒンディー語, 日本語, マンダリン, ポルトガル語, ロシア語, スペイン語とフランス語.

NumPy をより良くするために、こちらの \[アンケート\](https://umdsurvey. umd. edu/jfe/form/SV_8bJrXjbhXf7saAl) に協力してもらえると嬉しいです。


### NumPyのロゴが新しくなりました。

詳細については、 [リリース ノート](https://github.com/numpy/numpy/releases/tag/v1.18.0) を参照してください。

<img src="/images/logos/numpy_logo.svg" alt="NumPyのロゴ" title="新しいNumPyのロゴ" width=300>

新しいロゴは、古いもの比べてモダンで、よりクリーンなデザインになりました。 新しいロゴをデザインしてくれたIsabela Presedo-Floydと、15年以上にわたって使用してきた旧ロゴをデザインしてくれたTravis Vaughtに感謝します。


### Numpy 1.19.0 リリース

_2020年6月20日_ -- NumPy 1.19.0 が利用可能になりました。 これのリリースは Python 2系のサポートがない最初のリリースであり、"クリーンアップ用のリリース" です。 サポートされている一番古いPython のバージョンは Python 3.6 になりました。 今回の重要な新機能は、NumPy 1.17.0で導入された乱数生成用のインフラにCythonからアクセスできるようになったことです。


### ドキュメント改善期間

_2020年5月11日_ -- NumPyは、 Googleのシーズンオブドキュメントプログラムのメンター団体の1つとして選ばれました。 NumPy のドキュメントを改善するために、テクニカルライターと協力する機会を楽しみにしています! 詳細については、 [公式ドキュメントサイト](https://developers.google.com/season-of-docs/) と [アイデアページ](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas) をご覧ください。


### Numpy 1.18.0 リリース

_2019年12月22日_ -- NumPy 1.18.0 が利用可能になりました。 このリリースは、1.17.0の主要な変更の後の、統合的なリリースです。 Python 3.5 をサポートする最後のマイナーリリースになります。 今回のリリースでは、64ビットのBLASおよびLAPACKライブラリとリンクするためのインフラの追加や、`numpy.random`のための新しいC-APIの追加などが行われました。

NumPy 1.15.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018年7月23日_.


### NumPyはChan Zuckerberg財団から助成金を受けました。

_2019年11月15日_ -- NumPyと、NumPyの重要な依存関係の1つであるOpenBLASが、Chan Zuckerberg財団の[Essential Open Source Software for Scienceプログラム](https:/chanzuckerberg.comeoss)を通じて、科学に不可欠なオープンソースツールのソフトウェアのメンテナンス、成長、開発、コミュニティへの参加を支援する195,000ドルの共同助成金を獲得したことを発表しました。

この助成金は、Numpy ドキュメント、ウェブサイトの再設計の改善に向けた取り組みを促進するために使用されます。 大規模かつ急速に拡大するユーザー基盤をより良くし、プロジェクトの長期的な持続可能性を確保するためのコミュニティ開発を行っていきます。 OpenBLASチームは、技術的に重要な問題、特にスレッド安全性、AVX-512に対処することに焦点を当てます。 また、スレッドローカルストレージ(TLS) の問題や、OpenBLASが依存するReLAPACK(再帰的なLAPACK) のアルゴリズムの改善も行っています。

提案されたイニシアチブと成果物の詳細については、 [フルグラントプロポーザル](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167) を参照してください。 この取り組みは2019年12月1日から始まり、今後12ヶ月間継続される予定です。


## 過去のリリース

こちらがより過去のNumPy リリースのリストで、各リリースノートへのリンクが記載されています。 全てのバグフィックスリリース(バージョン番号`x.y.z` の`z`だけが変更されたもの)は新しい機能追加はされず、マイナーリリース (`y` が増えたもの)は、新しい機能追加されています。

- NumPy 1.18.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _2020年1月6日_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年5月3日_.
- NumPy 1.17.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _2020年1月1日_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年4月19日_.
- NumPy 1.18.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _2020年3月17日_.
- NumPy 1.14.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018年1月7日_.
- NumPy 1.17.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _2019年7月26日_.
- NumPy 1.18.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _2019年12月22日_.
- NumPy 1.17.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _2019年10月11日_.
- NumPy 1.16.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _2019年1月14日_.
- NumPy 1.15.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018年7月23日_.
- NumPy 1.14.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018年1月7日_.
