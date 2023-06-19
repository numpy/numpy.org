---
title: ニュース
sidebar: false
newsHeader: "NumPy 1.25.0 リリース"
date: 2023-06-17
---

### NumPy 1.25.0 リリース

_2023年1月17日_ -- [Numpy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html) がリリースされました。 このリリースの目玉機能は下記の通りです。

* MUSLのサポート。MUSLのWheelが準備されました。
* 富士通のC/C++コンパイラサポート
* Object arrays are now supported in einsum
* Support for inplace matrix multiplication (`@=`).

The NumPy 1.25.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, and clarify the documentation. There has also been preparatory work for the future NumPy 2.0.0, resulting in a large number of new and expired deprecations.

A total of 148 people contributed to this release and 530 pull requests were merged.  The Python versions supported are 3.9-3.11.

### Fostering an Inclusive Culture: Call for Participation

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

How can we be better when it comes to diversity and inclusion? Read the report and find out how to get involved [here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy documentation team leadership transition

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy documentation team leads replacing Melissa Mendonça. We thank Melissa for all her contributions to the NumPy official documentation and educational materials, and Mukulika and Ross for stepping up.

### NumPy 1.24.0 released

_2022年12月18日_ -- [Numpy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) がリリースされました。 The highlights of the release are:

* New "dtype" and "casting" keywords for stacking functions.
* New F2PY features and fixes.
* Many new deprecations, check them out.
* Many expired deprecations,

The NumPy 1.24.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase execution speed, and clarify the documentation. There are a large number of new and expired deprecations due to changes in dtype promotion and cleanups. It is the work of 177 contributors spread over 444 pull requests. The supported Python versions are 3.8-3.11.

### Numpy 1.23.0 リリース

_2022年1月22日_ -- [Numpy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) がリリースされました。 今回のリリースのハイライトは次のとおりです。

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

_2021年12月31日_ -- [Numpy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) がリリースされました。 今回のリリースのハイライトは次のとおりです。

* メインの名前空間の型アノテーションは基本的に完了しました。 上流のコードは常に変化するものなので、さらなる改良が必要でしょうが、大きな作業は終わったと考えています。 これはおそらく、今回のリリースで最も目に見える改良でしょう。
* 以前から提案されていた [array API 標準](https://data-apis.org/array-api/latest/) のベータ版が提供されています ( [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html) を参照) 。 これは、CuPy や JAX などのライブラリで使用できる 関数の標準的なコレクションを作成するために必要なステップです。
* NumPy に DLPack バックエンドが追加されました。 DLPack は、配列(テンソル) データ用の共通のデータ変換フォーマットを提供します。
* `quantile`, `percentile`, および関連する関数に新しいメソッドが追加されました。 これらの新しいメソッドは、論文で一般的に見られる一通りの処理を提供します。
* ユニバーサル関数は、[NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html) の多くを実装するためにリファクタリングされました。 これにより将来の DType API の処理も可能にします。
* ダウンストリームのプロジェクトで使用するための新しい設定可能なメモリー・アロケーターが追加されました。

NumPy 1.22.0は、153人の貢献者が609のプルリクエストを作成した 非常に大きなリリースです。 このリリースでサポートされている Python のバージョンは 3.8 - 3.10 です。

### 科学的なPythonエコシステムにおける包括的な文化の前進

_ 2021年8月31日_ -- この度、Chan Zuckerberg Initiativeより、科学的なPythonプロジェクトにおいて、歴史的に疎外されてきたグループの人々のオンボーディング、インクルージョン、リテンションを支援し、NumPy、SciPy、Matplotlib、Pandasのコミュニティダイナミクスを構造的に改善するための [ 助成金を授与されました ](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) ことをお知らせします。

[ CZIのEssential Open Source Software for Scienceプログラム ](https://chanzuckerberg.com/eoss/)の一環として、この[ Diversity & Inclusion補助金 ](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)は、開けたなオープンソースコミュニティを育成するためにやるべきことを特定したり、文書化したり、実施したりするためのコントリビュータ体験のリーダー専任職の創設を支援することになります。 このプロジェクトは、Melissa Mendonça (NumPy) が中心となって、下記の方々の追加のメンタリングとサポートにより実施されます。Ralf Gommers (NumPy、SciPy)、Hannah AizenmanとThomas Caswell (Matplotlib)、Matt Haberland (SciPy)、そして Joris Van den Bossche (Pandas)。

このプロジェクトは私たちのOSSプロジェクトのコミュニティダイナミクスを構造的に改善する方法を発見し、実施することを目指す野心的なプロジェクトです。 このような複数のプロジェクトの横断的な役割を確立することで、Scientific Pythonコミュニティに新しいコラボレーションモデルを導入し、エコシステム内のコミュニティ構築作業をより効率的に、より大きな成果を生めるようにしたいと考えています。 特にこのプロジェクトにより、歴史的にこれまで代表的ではなかったグループからの新しいコントリビュータを引き付け、貢献を維持するために、何がうまくいき、何がうまくいかないかを、より明確に把握できるようになると期待しています。 最後に、実施したアクションについて詳細な報告書を作成し、プロジェクトの代表者やコミュニティとの交流の面で、プロジェクトにどのような影響を与えたかを説明する予定です。

2021年11月から2年間のプロジェクトが始まると予想されており、このプロジェクトの成果を楽しみにしています! このプロジェクトの提案書に関しては、[こちら](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063) から全文を読むことができます.

### 2021年度NumPyアンケート

_2021年7月12日_ -- NumPy ではコミュニティの力を信じています。 昨年の第1回アンケートには、75カ国から1,236名のNumPyユーザーが参加してくれました。 この調査結果により、今後12ヶ月間、私たちがどのようなことに集中すべきかを、非常に良く理解することができました。

今年もアンケートの時間が来ました。もう一度アンケートへの回答をお願いいたします。 アンケートへの回答は15分ほどで終了します。 アンケートは英語以外にも、ベンガル語、フランス語、ヒンディー語、日本語、マンダリン、ポルトガル語、ロシア語、スペイン語の8ヶ国語に対応しています。

こちらのリンク先から、アンケートを始めることができます: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSL4q.


### NumPy 1.19.0 リリース

_2021年1月23日_ -- [Numpy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) がリリースされました。 今回のリリースのハイライトは次のとおりです。

- より多くの機能やプラットフォームをカバーするためのSIMD関連の改善が実施されました。
- dtypeのための新しいインフラとキャストの準備
- Mac 版の Python 3.8 と Python 3.9 用 universal2 wheel
- ドキュメントの改善
- アノテーションの改善
- 乱数生成用の新しい `PCG64DXSM` ビット生成機

今回のNumpy リリースは、175人による581件のプルリクエストのマージの結果です。  このリリースでサポートされている Python のバージョンは 3.7-3.9 です。Python 3.10 がリリースされた後、Python 3.10 のサポートが追加されます。


### 2020年度 NumPy アンケート結果

_2021年6月22日_ -- NumPyの調査チームは、2020年に ミシガン大学とメリーランド大学の学生や教員と協力して、最初の公式NumPyコミュニティ調査を実施しました。 アンケートの結果はこちらから確認できます。 https://numpy.org/user-survey-2020/


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


### NumPy 1.19.2 リリース

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


### Numpy 1.18.0 リリース

_2019年12月22日_ -- NumPy 1.18.0 が利用可能になりました。 このリリースは、1.17.0の主要な変更の後の、統合的なリリースです。 Python 3.5 をサポートする最後のマイナーリリースになります。 今回のリリースでは、64ビットのBLASおよびLAPACKライブラリとリンクするためのインフラの追加や、`numpy.random`のための新しいC-APIの追加などが行われました。

詳細については、 [リリース ノート](https://github.com/numpy/numpy/releases/tag/v1.18.0) を参照してください。


### NumPyはChan Zuckerberg財団から助成金を受けました。

_2019年11月15日_ -- NumPyと、NumPyの重要な依存関係の1つであるOpenBLASが、Chan Zuckerberg財団の[Essential Open Source Software for Scienceプログラム](https:/chanzuckerberg.comeoss)を通じて、科学に不可欠なオープンソースツールのソフトウェアのメンテナンス、成長、開発、コミュニティへの参加を支援する195,000ドルの共同助成金を獲得したことを発表しました。

この助成金は、Numpy ドキュメントやウェブサイトの再設計などの改善に向けた取り組みを促進するために使用されます。 大規模かつ急速に拡大するユーザーの体験をより良くし、プロジェクトの長期的な持続可能性を確保するためのコミュニティ開発を行っていきます。 OpenBLASチームは、技術的に重要な問題、特にスレッド安全性、AVX-512に対処することに焦点を当てます。 また、スレッドローカルストレージ(TLS) の問題や、OpenBLASが依存するReLAPACK(再帰的なLAPACK) のアルゴリズムの改善も行っています。

提案されたイニシアチブと成果物の詳細については、 [フルグラントプロポーザル](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167) を参照してください。 この取り組みは2019年12月1日から始まり、今後12ヶ月間継続される予定です。


## 過去のリリース

こちらがより過去のNumPy リリースのリストで、各リリースノートへのリンクが記載されています。 全てのバグフィックスリリース(バージョン番号`x.y.z` の`z`だけが変更されたもの)は新しい機能追加はされず、マイナーリリース (`y` が増えたもの)は、新しい機能追加されています。

- NumPy 1.25.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _17 Jun 2023_.
- NumPy 1.24.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 Apr 2023_.
- NumPy 1.24.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 Feb 2023_.
- NumPy 1.24.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 Dec 2022_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年4月19日_.
- NumPy 1.23.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _19 Nov 2022_.
- NumPy 1.17.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _2019年10月11日_.
- NumPy 1.23.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 Sep 2022_.
- NumPy 1.23.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 Aug 2022_.
- NumPy 1.23.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 Jul 2022_.
- NumPy 1.23.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 Jun 2022_.
- NumPy 1.22.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 May 2022_.
- NumPy 1.21.6 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 Apr 2022_.
- NumPy 1.18.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _2020年3月17日_.
- NumPy 1.22.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 Feb 2022_.
- NumPy 1.22.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 Jan 2022_.
- NumPy 1.22.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 Dec 2021_.
- NumPy 1.21.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 Dec 2021_.
- NumPy 1.21.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 Jun 2021_.
- NumPy 1.20.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 May 2021_.
- NumPy 1.20.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 Jan 2021_.
- NumPy 1.19.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 Jan 2021_.
- NumPy 1.18.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _2020年1月6日_.
- NumPy 1.18.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _2020年5月3日_.
- NumPy 1.17.5 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _2020年1月1日_.
- NumPy 1.18.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _2019年12月22日_.
- NumPy 1.17.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _2019年7月26日_.
- NumPy 1.16.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _2019年1月14日_.
- NumPy 1.15.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _2018年7月23日_.
- NumPy 1.14.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _2018年1月7日_.
