---
title: ニュース
sidebar: false
newsHeader: Meet the new NumPy docs team leads
date:
---

### NumPy documentation team leadership transition

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy documentation team leads replacing Melissa Mendonça. We thank Melissa for all her contributions to the NumPy official documentation and educational materials, and Mukulika and Ross for stepping up.

### Numpy 1.24.0 released

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) is now available. The highlights of the release are:

* New "dtype" and "casting" keywords for stacking functions.
* New F2PY features and fixes.
* Many new deprecations, check them out.
* Many expired deprecations,

The NumPy 1.24.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase execution speed, and clarify the documentation. There are a large number of new and expired deprecations due to changes in dtype promotion and cleanups. It is the work of 177 contributors spread over 444 pull requests. The supported Python versions are 3.8-3.11.

### Numpy 1.23.0 released

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) is now available. The highlights of the release are:

* Implementation of `loadtxt` in C, greatly improving its performance.
* Exposure of DLPack at the Python level for easy data exchange.
* Changes to the promotion and comparisons of structured dtypes.
* Improvements to f2py.

The NumPy 1.23.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, clarify the documentation, and expire old deprecations. It is the work of 151 contributors spread over 494 pull requests. The Python versions supported by this release 3.8-3.10. Python 3.11 will be supported when it reaches the rc stage.

### NumFOCUS DEI research study: call for participation

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a [research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c) funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to understand the barriers to participation that contributors, particularly those from historically underrepresented groups, face in the open-source software community. The research team would like to talk to new contributors, project developers and maintainers, and those who have contributed in the past about their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe) which contains additional information on the research goals, privacy, and confidentiality considerations. Your participation will be valuable to the growth and sustainability of diverse and inclusive open-source software communities. Accepted participants will participate in a 30-minute interview with a research team member.

### NumPy 1.19.2 リリース

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) is now available. The highlights of the release are:

* Type annotations of the main namespace are essentially complete. Upstream is a moving target, so there will likely be further improvements, but the major work is done. This is probably the most user visible enhancement in this release.
* A preliminary version of the proposed [array API Standard](https://data-apis.org/array-api/latest/) is provided (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)). This is a step in creating a standard collection of functions that can be used across libraries such as CuPy and JAX.
* NumPy now has a DLPack backend. DLPack provides a common interchange format for array (tensor) data.
* New methods for `quantile`, `percentile`, and related functions. The new methods provide a complete set of the methods commonly found in the literature.
* The universal functions have been refactored to implement most of [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html). This also unlocks the ability to experiment with the future DType API.
* A new configurable memory allocator for use by downstream projects.

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread over 609 pull requests. The Python versions supported by this release are 3.8-3.10.

### Advancing an inclusive culture in the scientific Python ecosystem

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has [awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) to support the onboarding, inclusion, and retention of people from historically marginalized groups on scientific Python projects, and to structurally improve the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/), this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) will support the creation of dedicated Contributor Experience Lead positions to identify, document, and implement practices to foster inclusive open-source communities. This project will be led by Melissa Mendonça (NumPy), with additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy), Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that should structurally improve the community dynamics of our projects. By establishing these new cross-project roles, we hope to introduce a new collaboration model to the Scientific Python communities, allowing community-building work within the ecosystem to be done more efficiently and with greater outcomes. We also expect to develop a clearer picture of what works and what doesn't in our projects to engage and retain new contributors, especially from historically underrepresented groups. Finally, we plan on producing detailed reports on the actions executed, explaining how they have impacted our projects in terms of representation and interaction with our communities.

The two-year project is expected to start by November 2021, and we are excited to see the results from this work! [You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021 NumPy survey

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 NumPy users from 75 countries participated in our inaugural survey last year. The survey findings gave us a very good understanding of what we should focus on for the next 12 months.

It’s time for another survey, and we are counting on you once again. It will take about 15 minutes of your time. Besides English, the survey questionnaire is available in 8 additional languages: Bangla, French, Hindi, Japanese, Mandarin, Portuguese, Russian, and Spanish.

Follow the link to get started: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### NumPy 1.19.0 リリース

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) is now available. The highlights of the release are:

- continued SIMD work covering more functions and platforms,
- initial work on the new dtype infrastructure and casting,
- universal2 wheels for Python 3.8 and Python 3.9 on Mac,
- improved documentation,
- improved annotations,
- new `PCG64DXSM` bitgenerator for random numbers.

This NumPy release is the result of 581 merged pull requests contributed by 175 people.  The Python versions supported for this release are 3.7-3.9, support for Python 3.10 will be added after Python 3.10 is released.


### 2020 NumPy survey results

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students and faculty from the University of Michigan and the University of Maryland conducted the first official NumPy community survey. Find the survey results here: https://numpy.org/user-survey-2020/.


### NumPy 1.18.0 リリース

_2021年1月30日_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) が利用可能になりました。 今回のリリースは180以上のコントリビューターのおかげで、これまでで最大の NumPyのリリースとなりました。 最も重要な2つの新機能は次のとおりです。
- NumPyの大部分のコードに型注釈が追加されました。 そして新しいサブモジュールである`numpy.typing`が追加されました。 このサブモジュールは`ArrayLike` や`DtypeLike`という型注釈のエイリアスが定義されており、これによりユーザーやダウンストリームのライブラリはこの型注釈を使うことができます。
- X86(SSE、AVX)、ARM64(Neon)、およびPowerPC (VSX) 命令をサポートするマルチプラットフォームSIMDコンパイラの最適化が実施されました。 これにより、多くの関数で大きく パフォーマンスが向上しました (例: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPyプロジェクトの多様性

_2020年9月20日に_ 、私たちは[ NumPyプロジェクトにおけるダイバーシティやインクルージョンの状況や、ソーシャルメディア上での議論についての宣言 ](/diversity_sep2020)について書きました。


### Natureに初の公式NumPy論文が掲載されました!

_2020年9月16日_ -- \[NumPyに関する初の公式論文\] (https://www.nature.com/articles/s41586-020-2649-2) が査読付き論文として掲載されました。 これはNumPy 1.0のリリースから14年後のことになります。 この論文では、配列プログラミングのアプリケーションと基本的なコンセプト、NumPyの上に構築された様々な科学的Pythonエコシステム、そしてCuPy、Dask、JAXのような外部の配列およびテンソルライブラリとの相互運用を容易にするために最近追加された配列プロトコルについて説明しています。


### Python 3.9のリリースに伴い、いつNumPyのバイナリwheelがリリースされるのですか？

_2020年9月14日_ -- Python 3.9 は数週間後にリリースされる予定です。 もしあなたが新しいPythonのバージョンをいち早く取り入れているのであれば、NumPy（およびSciPyのような他のパッケージ）がリリース当日にバイナリwheelを用意していないことを知ってがっかりしたかもしれません。 ビルドインフラを新しいPythonのバージョンに適応させるのは大変な作業で、PyPIやconda-forgeにパッケージが掲載されるまでには通常数週間かかります。 wheelのリリースに備えて、以下を確認してください。
- `pip` が`manylinux2010` と `manylinux2014` をサポートするためにpipを少なくともバージョン 20.1 に更新する。
- [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) または `--only-binary=:all:` を`pip`がソースからビルドしようとするのを防ぐために使用します。


### Numpy 1.19.2 release

_2020年1月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) がリリースされました。 この 1.19 シリーズの最新リリースでは、いくつかのバグが修正され、[来るべき Cython 3.xリリース](http:/docs.cython.orgenlatestsrcchanges.html)への準備が行われ、アップストリームの修正が進行中の間も distutils の動作を維持するためのsetuptoolsの固定がされています。 aarch64 wheelは最新のmanylinux2014リリースで構築されており、異なるLinuxディストリビューションで使用される異なるページサイズの問題を修正しています。

### 初めてのNumPyの調査が公開されました!!

_2020年7月2日_ -- このサーベイは、ソフトウェアとして、またコミュニティとしてのNumPyの開発に関する意思決定の指針となり、優先順位を設定するためのものになりました。 この調査結果は英語以外の8つの言語で利用可能です: バングラ, ヒンディー語, 日本語, マンダリン, ポルトガル語, ロシア語, スペイン語とフランス語.

NumPy をより良くするために、こちらの \[アンケート\](https://umdsurvey. umd. edu/jfe/form/SV_8bJrXjbhXf7saAl) に協力してもらえると嬉しいです。


### NumPy に新しいロゴができました!

_2020年6月24日_ -- NumPy に新しいロゴが作成されました:

<img src="/images/logos/numpy_logo.svg" alt="NumPyのロゴ" title="新しいNumPyのロゴ" width=300>

新しいロゴは、古いもの比べてモダンで、よりクリーンなデザインになりました。 新しいロゴをデザインしてくれたIsabela Presedo-Floydと、15年以上にわたって使用してきた旧ロゴをデザインしてくれたTravis Vaughtに感謝します。


### NumPy 1.20.0 リリース

_2020年6月20日_ -- NumPy 1.19.0 が利用可能になりました。 これのリリースは Python 2系のサポートがない最初のリリースであり、"クリーンアップ用のリリース" です。 サポートされている一番古いPython のバージョンは Python 3.6 になりました。 今回の重要な新機能は、NumPy 1.17.0で導入された乱数生成用のインフラにCythonからアクセスできるようになったことです。


### ドキュメント受諾期間

_2020年5月11日_ -- NumPyは、 Googleのシーズンオブドキュメントプログラムのメンター団体の1つとして選ばれました。 NumPy のドキュメントを改善するために、テクニカルライターと協力する機会を楽しみにしています! 詳細については、 [公式ドキュメントサイト](https://developers.google.com/season-of-docs/) と [アイデアページ](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas) をご覧ください。


### NumPy 1.18.0 release

_2019年12月22日_ -- NumPy 1.18.0 が利用可能になりました。 このリリースは、1.17.0の主要な変更の後の、統合的なリリースです。 Python 3.5 をサポートする最後のマイナーリリースになります。 今回のリリースでは、64ビットのBLASおよびLAPACKライブラリとリンクするためのインフラの追加や、`numpy.random`のための新しいC-APIの追加などが行われました。

詳細については、 [リリース ノート](https://github.com/numpy/numpy/releases/tag/v1.18.0) を参照してください。


### NumPyはChan Zuckerberg財団から助成金を受けました。

_2019年11月15日_ -- NumPyと、NumPyの重要な依存関係の1つであるOpenBLASが、Chan Zuckerberg財団の[Essential Open Source Software for Scienceプログラム](https:/chanzuckerberg.comeoss)を通じて、科学に不可欠なオープンソースツールのソフトウェアのメンテナンス、成長、開発、コミュニティへの参加を支援する195,000ドルの共同助成金を獲得したことを発表しました。

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. OpenBLASチームは、技術的に重要な問題、特にスレッド安全性、AVX-512に対処することに焦点を当てます。 また、スレッドローカルストレージ(TLS) の問題や、OpenBLASが依存するReLAPACK(再帰的なLAPACK) のアルゴリズムの改善も行っています。

提案されたイニシアチブと成果物の詳細については、 [フルグラントプロポーザル](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167) を参照してください。 この取り組みは2019年12月1日から始まり、今後12ヶ月間継続される予定です。


## 過去のリリース

こちらがより過去のNumPy リリースのリストで、各リリースノートへのリンクが記載されています。 全てのバグフィックスリリース(バージョン番号`x.y.z` の`z`だけが変更されたもの)は新しい機能追加はされず、マイナーリリース (`y` が増えたもの)は、新しい機能追加されています。

- NumPy 1.24.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 Apr 2023_.
- NumPy 1.24.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 Feb 2023_.
- NumPy 1.24.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 Dec 2022_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年4月19日_.
- NumPy 1.23.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _19 Nov 2022_.
- NumPy 1.17.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _2019年10月11日_.
- NumPy 1.23.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 Sep 2022_.
- NumPy 1.23.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 Aug 2022_.
- NumPy 1.23.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 Jul 2022_.
- NumPy 1.23.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 Jun 2022_.
- NumPy 1.22.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 May 2022_.
- NumPy 1.21.6 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 Apr 2022_.
- NumPy 1.18.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _2020年3月17日_.
- NumPy 1.22.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 Feb 2022_.
- NumPy 1.22.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 Jan 2022_.
- NumPy 1.22.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 Dec 2021_.
- NumPy 1.21.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 Dec 2021_.
- NumPy 1.21.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 Jun 2021_.
- NumPy 1.20.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 May 2021_.
- NumPy 1.20.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 Jan 2021_.
- NumPy 1.19.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 Jan 2021_.
- NumPy 1.18.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _2020年1月6日_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年5月3日_.
- NumPy 1.17.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _2020年1月1日_.
- NumPy 1.18.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _2019年12月22日_.
- NumPy 1.17.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _2019年7月26日_.
- NumPy 1.16.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _2019年1月14日_.
- NumPy 1.15.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018年7月23日_.
- NumPy 1.14.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018年1月7日_.
