---
title: ニュース
sidebar: false
---

### Numpy 1.20.0 リリース

_2021年1月30日_ -- [Numpy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) が利用可能になりました。 今回のリリースは180以上のコントリビューターのおかげで、これまでで最大の Numpyのリリースとなりました。 最も重要な2つの新機能は次のとおりです。
- NumPyの大部分のコードに型注釈が追加されました。そして新しいサブモジュールである`numpy.typing`が追加されました。このサブモジュールは`ArrayLike` や`DtypeLike`という型注釈のエイリアスが定義されており、これによりユーザーやダウンストリームのライブラリはこの型注釈を使うことができます。
- X86(SSE、AVX)、ARM64(Neon)、およびPowerPC (VSX) 命令をサポートするマルチプラットフォームSIMDコンパイラの最適化が実施されました。 これにより、多くの関数で大きく パフォーマンスが向上しました (例: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPyプロジェクトの多様性

_2020年9月20日に_ 、私達は[ NumPyプロジェクトにおけるダイバーシティやインクルージョンの状況や、ソーシャルメディア上での議論についての宣言 ](/diversity_sep2020)について書きました。


### Natureに初めての公式のNumPy論文が掲載されました!

_2020年9月16日_ -- NumPyに関する最初の公式の論文 [](https://www.nature.com/articles/s41586-020-2649-2) が査読付き論文として掲載されました。 これはNumPy 1.0のリリースから14年後のことになります。 この論文では、配列プログラミングのアプリケーションと基本的なコンセプト、NumPyの上に構築された様々な科学的Pythonエコシステム、そしてCuPy、Dask、JAXのような外部の配列およびテンソルライブラリとの相互運用を容易にするために最近追加された配列プロトコルについて説明しています。


### Python 3.9 が登場し、Numpy はいつバイナリホイールをリリースするのか?

_2020年9月14日_ -- Python 3.9 は数週間後にリリースされる予定です。 もしあなたが新しいPythonのバージョンをいち早く取り入れているのであれば、NumPy（およびSciPyのような他のパッケージ）がリリース当日にバイナリホイールを用意していないことを知ってがっかりしたかもしれません。 ビルドインフラを新しいPythonのバージョンに適応させるのは大変な作業で、PyPIやconda-forgeにパッケージが掲載されるまでには通常数週間かかります。 ホイールリリースのイベントに備えて、以下を確認してください。
- `pip` が`manylinux2010` と `manylinux2014` をサポートするためにpipを少なくともバージョン 20.1 に更新する。
- [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) または `--only-binary=:all:` を`pip`がソースからビルドしようとするのを防ぐために使用します。


### Numpy 1.19.2 リリース

_2020年1月10日_ -- [Numpy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) がリリースされました。 この 1.19 シリーズの最新リリースでは、いくつかのバグが修正され、[来るべき Cython 3.xリリース](http:/docs.cython.orgenlatestsrcchanges.html)への準備が行われ、アップストリームの修正が進行中の間も distutils の動作を維持するためのsetuptoolsの固定がされています。 aarch64ホイールは最新のmanylinux2014リリースで構築されており、異なるLinuxディストリビューションで使用される異なるページサイズの問題を修正しています。

### 初めてのNumPyの調査が公開されました!!

_2020年7月2日_ -- このサーベイは、ソフトウェアとして、またコミュニティとしてのNumPyの開発に関する意思決定の指針となり、優先順位を設定するためのものになりました。 この調査結果は英語以外の8つの言語で利用可能です: バングラ, ヒンディー語, 日本語, マンダリン, ポルトガル語, ロシア語, スペイン語とフランス語.

NumPy をより良くするために、こちらの [アンケート](https://umdsurvey. umd. edu/jfe/form/SV_8bJrXjbhXf7saAl) に協力してもらえると嬉しいです。


### NumPy has a new logo!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught for the old logo that served us well for 15+ years.


### NumPy 1.19.0 release

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### Season of Docs acceptance

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 release

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPy receives a grant from the Chan Zuckerberg Initiative

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## Releases

Here is a list of NumPy releases, with links to release notes. All bugfix releases (only the `z` changes in the `x.y.z` version number) have no new features; minor releases (the `y` increases) do.

- NumPy 1.18.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 May 2020_.
- NumPy 1.18.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.3)) -- _19 Apr 2020_.
- NumPy 1.18.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _17 Mar 2020_.
- NumPy 1.18.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _6 Jan 2020_.
- NumPy 1.17.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 Jan 2020_.
- NumPy 1.18.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 Dec 2019_.
- NumPy 1.17.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _11 Nov 2019_.
- NumPy 1.17.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 Jul 2019_.
- NumPy 1.16.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 Jan 2019_.
- NumPy 1.15.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 Jul 2018_.
- NumPy 1.14.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 Jan 2018_.
