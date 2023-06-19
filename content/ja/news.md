---
title: ニュース
sidebar: false
newsHeader: "NumPy 1.25.0 リリース"
date: 2023-06-17
---

### NumPy 1.25.0 リリース

_2023年1月17日_ -- [Numpy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html) がリリースされました。 The highlights of the release are:

* MUSLのサポート。MUSLのWheelが準備されました。
* Support for the Fujitsu C/C++ compiler.
* Object arrays are now supported in einsum.
* Support for the inplace matrix multiplication (`@=`).

Numpy 1.25. リリースは引き続きdtypeの取り扱いと dtypeのプロモーションを改善し、実行速度を向上させ、 ドキュメントを明確化するための継続的な作業を続けて行く予定です。 将来の NumPy 2.0.0 に向けた準備作業も行われており、 多数の新規および期限切れの機能廃止が可能となってきています。

A total of 148 people contributed to this release and 530 pull requests were merged.

The Python versions supported by this release are 3.9-3.11.

### インクルーシブな文化の育成: 参加の募集

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

How can we be better when it comes to diversity and inclusion? Read the report and find out how to get involved [here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy ドキュメンテーションチームのリーダーの変更

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy documentation team leads replacing Melissa Mendonça. We thank Melissa for all her contributions to the NumPy official documentation and educational materials, and Mukulika and Ross for stepping up.

### NumPy 1.24.0 リリース

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) is now available. The highlights of the release are:

* スタッキング関数のための新しい"dtype"と"casting"キーワードの追加
* F2PYの新機能追加とバグ修正
* 多くの新しい非推奨(Deprecation)の追加
* 多くの期限切れの非推奨(Deprecation)の削除

The NumPy 1.24.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase execution speed, and clarify the documentation. There are a large number of new and expired deprecations due to changes in dtype promotion and cleanups. It is the work of 177 contributors spread over 444 pull requests. The supported Python versions are 3.8-3.11.

### Numpy 1.23.0 リリース

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) is now available. The highlights of the release are:

* `loadtxt` がCで実装されたことによる、大幅なパフォーマンス向上
* より簡単なデータ交換のためのPythonレベルでのDLPackの公開
* 構造化されたdtypesのプロモーションと比較方法の変更
* f2pyの改善

The NumPy 1.23.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, clarify the documentation, and expire old deprecations. It is the work of 151 contributors spread over 494 pull requests. The Python versions supported by this release 3.8-3.10. Python 3.11 will be supported when it reaches the rc stage.

### NumFOCUS DEI研究への参加募集

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a [research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c) funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to understand the barriers to participation that contributors, particularly those from historically underrepresented groups, face in the open-source software community. The research team would like to talk to new contributors, project developers and maintainers, and those who have contributed in the past about their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe) which contains additional information on the research goals, privacy, and confidentiality considerations. Your participation will be valuable to the growth and sustainability of diverse and inclusive open-source software communities. Accepted participants will participate in a 30-minute interview with a research team member.

### NumPy 1.19.2 リリース

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) is now available. The highlights of the release are:

* メインの名前空間の型アノテーションは基本的に完了しました。 上流のコードは常に変化するものなので、さらなる改良が必要でしょうが、大きな作業は終わったと考えています。 これはおそらく、今回のリリースで最も目に見える改良でしょう。
* 以前から提案されていた [array API 標準](https://data-apis.org/array-api/latest/) のベータ版が提供されています ( [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html) を参照) 。 これは、CuPy や JAX などのライブラリで使用できる 関数の標準的なコレクションを作成するために必要なステップです。
* NumPy に DLPack バックエンドが追加されました。 DLPack は、配列(テンソル) データ用の共通のデータ変換フォーマットを提供します。
* `quantile`, `percentile`, および関連する関数に新しいメソッドが追加されました。 これらの新しいメソッドは、論文で一般的に見られる一通りの処理を提供します。
* ユニバーサル関数は、[NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html) の多くを実装するためにリファクタリングされました。 これにより将来の DType API の処理も可能にします。
* ダウンストリームのプロジェクトで使用するための新しい設定可能なメモリー・アロケーターが追加されました。

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread over 609 pull requests. The Python versions supported by this release are 3.8-3.10.

### 科学的なPythonエコシステムにおける包括的な文化の前進

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has [awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) to support the onboarding, inclusion, and retention of people from historically marginalized groups on scientific Python projects, and to structurally improve the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/), this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) will support the creation of dedicated Contributor Experience Lead positions to identify, document, and implement practices to foster inclusive open-source communities. This project will be led by Melissa Mendonça (NumPy), with additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy), Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that should structurally improve the community dynamics of our projects. By establishing these new cross-project roles, we hope to introduce a new collaboration model to the Scientific Python communities, allowing community-building work within the ecosystem to be done more efficiently and with greater outcomes. We also expect to develop a clearer picture of what works and what doesn't in our projects to engage and retain new contributors, especially from historically underrepresented groups. Finally, we plan on producing detailed reports on the actions executed, explaining how they have impacted our projects in terms of representation and interaction with our communities.

The two-year project is expected to start by November 2021, and we are excited to see the results from this work! [You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021年度NumPyアンケート

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 NumPy users from 75 countries participated in our inaugural survey last year. The survey findings gave us a very good understanding of what we should focus on for the next 12 months.

It’s time for another survey, and we are counting on you once again. It will take about 15 minutes of your time. Besides English, the survey questionnaire is available in 8 additional languages: Bangla, French, Hindi, Japanese, Mandarin, Portuguese, Russian, and Spanish.

Follow the link to get started: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### NumPy 1.19.0 リリース

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) is now available. The highlights of the release are:

- より多くの機能やプラットフォームをカバーするためのSIMD関連の改善が実施されました。
- dtypeのための新しいインフラとキャストの準備
- Mac 版の Python 3.8 と Python 3.9 用 universal2 wheel
- ドキュメントの改善
- アノテーションの改善
- 乱数生成用の新しい `PCG64DXSM` ビット生成機

This NumPy release is the result of 581 merged pull requests contributed by 175 people.  The Python versions supported for this release are 3.7-3.9, support for Python 3.10 will be added after Python 3.10 is released.


### 2020年度 NumPy アンケート結果

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students and faculty from the University of Michigan and the University of Maryland conducted the first official NumPy community survey. Find the survey results here: https://numpy.org/user-survey-2020/.


### NumPy 1.18.0 リリース

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) is now available. This is the largest NumPy release to date, thanks to 180+ contributors. The two most exciting new features are:
- NumPyの大部分のコードに型注釈が追加されました。 そして新しいサブモジュールである`numpy.typing`が追加されました。 このサブモジュールは`ArrayLike` や`DtypeLike`という型注釈のエイリアスが定義されており、これによりユーザーやダウンストリームのライブラリはこの型注釈を使うことができます。
- X86(SSE、AVX)、ARM64(Neon)、およびPowerPC (VSX) 命令をサポートするマルチプラットフォームSIMDコンパイラの最適化が実施されました。 これにより、多くの関数で大きく パフォーマンスが向上しました (例: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPyプロジェクトの多様性

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).


### Natureに初の公式NumPy論文が掲載されました!

_Sep 16, 2020_ -- We are pleased to announce the publication of [the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2) as a review article in Nature. This comes 14 years after the release of NumPy 1.0. The paper covers applications and fundamental concepts of array programming, the rich scientific Python ecosystem built on top of NumPy, and the recently added array protocols to facilitate interoperability with external array and tensor libraries like CuPy, Dask, and JAX.


### Python 3.9のリリースに伴い、いつNumPyのバイナリwheelがリリースされるのですか？

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. If you are an early adopter of Python versions, you may be dissapointed to find that NumPy (and other binary packages like SciPy) will not have binary wheels ready on the day of the release. It is a major effort to adapt the build infrastructure to a new Python version and it typically takes a few weeks for the packages to appear on PyPI and conda-forge. In preparation for this event, please make sure to
- `pip` が`manylinux2010` と `manylinux2014` をサポートするためにpipを少なくともバージョン 20.1 に更新する。
- [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) または `--only-binary=:all:` を`pip`がソースからビルドしようとするのを防ぐために使用します。


### NumPy 1.19.2 リリース

_Sep 10, 2020_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) is now available. This latest release in the 1.19 series fixes several bugs, prepares for the [upcoming Cython 3.x release](http://docs.cython.org/en/latest/src/changes.html) and pins setuptools to keep distutils working while upstream modifications are ongoing. The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

### 初めてのNumPyの調査が公開されました!!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. The survey is available in 8 additional languages besides English: Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey [here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy に新しいロゴができました!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught for the old logo that served us well for 15+ years.


### NumPy 1.20.0 リリース

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### ドキュメント受諾期間

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### Numpy 1.18.0 リリース

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPyはChan Zuckerberg財団から助成金を受けました。

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## 過去のリリース

Here is a list of NumPy releases, with links to release notes. Bugfix releases (only the `z` changes in the `x.y.z` version number) have no new features; minor releases (the `y` increases) do.

- NumPy 1.25.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _2023年6月17日_.
- NumPy 1.24.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _2023年4月22日_.
- NumPy 1.24.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _2023年2月5日_.
- NumPy 1.24.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _2022年12月26日_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年4月19日_.
- NumPy 1.23.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _2022年11月19日_.
- NumPy 1.23.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _2022年10月12日_.
- NumPy 1.23.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _2022年9月9日_.
- NumPy 1.23.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _2022年8月14日_.
- NumPy 1.23.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _2022年7月8日_.
- NumPy 1.23.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _2022年6月22日_.
- NumPy 1.22.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _2022年5月20日_.
- NumPy 1.21.6 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _2022年4月12日_.
- NumPy 1.22.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _2022年3月7日_.
- NumPy 1.22.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _2022年2月3日_.
- NumPy 1.22.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _2022年1月14日_.
- NumPy 1.22.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _2021年12月31日_.
- NumPy 1.21.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _2021年12月19日_.
- NumPy 1.21.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _2021年6月22日_.
- NumPy 1.20.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _2021年5月10日_.
- NumPy 1.20.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _2021年1月30日_.
- NumPy 1.19.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _2021年1月5日_.
- NumPy 1.19.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _2020年6月20日_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年5月3日_.
- NumPy 1.17.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _2020年1月1日_.
- NumPy 1.18.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _2019年12月22日_.
- NumPy 1.17.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _2019年7月26日_.
- NumPy 1.16.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _2019年1月14日_.
- NumPy 1.15.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018年7月23日_.
- NumPy 1.14.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018年1月7日_.
