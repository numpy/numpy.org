---
title: ニュース
sidebar: false
newsHeader: NumPy 1.26.0 がリリースされました。
date: 2023-09-16
---

### NumPy 1.26.0 がリリースされました。

_18 Aug, 2024_ -- NumPy 2.1.0 provides support for Python 3.13 and
drops support for Python 3.9. 今回のリリースは通常のバグ修正やPythonサポートの更新に加えて、NumPyが2.0の長期開発を経て、通常のリリースサイクルに戻るためのリリースでもあります。 今回のリリースのハイライトは下記の通りです。

- Python 3.12.0 のサポート
- 多くの期限切れの非推奨(Deprecation)の削除
- Array-api 2023.12 標準のサポート

Python バージョン 3.10-3.13 か、このリリースでサポートされています。

### 多くの新しい非推奨(Deprecation)の追加

_16 Jun, 2024_ -- NumPy 2.0.0 is the first major release since 2006. これは、前回の機能リリースから11か月間の開発の成果であり、1078件のプルリクエストにわたる212人の貢献者の成果となります。 このリリースには、大きく、エキサイティングな新機能と、PythonとCの両方のAPIへの変更が含まれています。  今回のリリースが、通常のマイナーリリースでは実施できなかった互換性を破壊する変更を含んでいます。これには、ABIの破壊、型昇格ルールの変更、および1.26.xでは非推奨警告が出されていなかった可能性のあるAPIの変更が含まれています。 NumPy 2.0の変更に対応する方法に関する主要なドキュメントは次のとおりです。

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

The blog post ["NumPy 2.0: an evolutionary milestone"](https://blog.scientific-python.org/numpy/numpy2/)
tells a bit of the story about how this release came together.

### NumPy 1.25.0 リリース

_23 May, 2024_ -- We are excited to announce that NumPy 2.0 is planned to be
released on June 16, 2024. このリリースは1年以上かけて我々が準備してきたもので、2006年以来のメジャーリリースとなります。 Importantly, in addition to many new
features and performance improvement, it contains **breaking changes** to the
ABI as well as the Python and C APIs. It is likely that downstream packages and
end user code needs to be adapted - if you can, please verify whether your code
works with NumPy `2.0.0rc2`. **Please see the following for more details:**

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

### NumFOCUSの年末の資金調達

_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount
on first-time PyCharm licenses. 2023年12月23日までのPyCharm購入による1年目の収益は全てNumFOCUSのプログラムに直接寄付されます。

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/
or a coupon code ISUPPORTDATASCIENCE 

### NumPy 1.20.0 リリース

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)
is now available. 今回のリリースのハイライトは次のとおりです。

- Python 3.12.0 のサポート
- Cython 3.0.0 との互換性
- Mesonビルドシステムの利用
- SIMD サポートの改善
- f2py のバグ修正, meson と bind(x) のサポート
- 更新された BLAS/LAPACK の高速化ライブラリのサポート

Numpy 1.26.0 は 1.25 からの互換性を保持しています。Mesonビルドシステムへの移行とCython 3.0.0へのサポートが目的のリリースです。
合計20人がこのリリースに貢献し、59個のプルリクエストがマージされました。

このリリースでサポートされている Python のバージョンは3.9から 3.12 です。

### numpy.orgが日本語とポルトガル語で利用可能になりました

_Aug 2, 2023_ -- numpy.org is now available in 2 additional languages:
Japanese and Portuguese. 熱心なボランティアがいなければ、このプロジェクトは不可能でした：

_Portuguese:_

- Melissa Weber Mendonça (melissawm)
- Ricardo Prins (ricardoprins)
- Getúlio Silva (getuliosilva)
- Julio Batista Silva (jbsilva)
- Alexandre de Siqueira (alexdesiqueira)
- Alexandre B A Villares (villares)
- Vini Salazar (vinisalazar)

_Japanese:_

- Atsushi Sakai (AtsushiSakai)
- KKunai
- Tom Kelly (TomKellyGenetics)
- Yuji Kanagawa (kngwyu)
- Tetsuo Koyama (tkoyama010)

翻訳インフラストラクチャに関するプロジェクトは、CZIからの資金援助でサポートされています。

今後も、NumPyのウェブサイトをより多くの言語に翻訳したいと思っています。
もし手伝える場合は、Slack上のNumPy翻訳チームに連絡をお願います: https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w.
(#translation チャンネルを探してください) (#translation チャンネルを探してください) また、Scientific Pythonエコシステム全体のドキュメントや教育コンテンツのローカライズに取り組む翻訳チームも 立ち上げています。 このプロジェクトにも興味がある場合は、是非Scientific Python Discordに参加してください: https://discord.gg/khWtqY6RKr. (#translation チャンネルを探してください)

### Numpy 1.23.0 リリース

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html)
is now available. 今回のリリースのハイライトは次のとおりです。

- MUSLのサポート。 MUSLのWheelが準備されました。
- 富士通のC/C++コンパイラサポート
- einsum でオブジェクト配列がサポートされるようになりました.
- Support for the inplace matrix multiplication (`@=`).

Numpy 1.25. リリースは引き続きdtypeの取り扱いと dtypeのプロモーションを改善し、実行速度を向上させ、 ドキュメントを明確化するための継続的な作業を続けて行く予定です。 将来の NumPy 2.0.0 に向けた準備作業も行われており、 多数の新規および期限切れの機能廃止が可能となってきています。

合計148人がこのリリースに貢献し、530個のプルリクエストが マージされました。

このリリースでサポートされている Python のバージョンは3.3.9 - 3.11 です。

### インクルーシブな文化の育成: 参加の募集

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

NumPyプロジェクトの多様性とインクルージョンに関して、我々はどのようなことを実施すればいいでしょうか？
Read the report and find out how to get involved
[here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy ドキュメンテーションチームのリーダーの変更

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy
documentation team leads replacing Melissa Mendonça. 私たちは、MelissaにNumPyの公式ドキュメントと教育資料に対するすべての貢献に感謝し、MukulikaとRossに新しい役割にステップアップしてもらったことに感謝します。

### NumPy 1.24.0 リリース

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html)
is now available. 今回のリリースのハイライトは次のとおりです。

- スタッキング関数のための新しい"dtype"と"casting"キーワードの追加
- F2PYの新機能追加とバグ修正
- 多くの新しい非推奨(Deprecation)の追加
- 多くの期限切れの非推奨(Deprecation)の削除

Numpy 1.25. リリースは引き続きdtypeの取り扱いと dtypeのプロモーションを改善し、実行速度を向上させ、 ドキュメントを明確化するための継続的な作業を続けて行く予定です。
dtype のプロモーションとクリーンアップの変更により、多数の新規と期限切れの非推奨が存在しています。 今回のリリースは、444個のプルリクエストと177人のコントリビューターによるものです。 サポートされている Python のバージョンは 3.8-3.11 です。

### Numpy 1.26.0 は 1.25 からの互換性を保持しています。

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html)
is now available. 今回のリリースのハイライトは次のとおりです。

- Implementation of `loadtxt` in C, greatly improving its performance.
- より簡単なデータ交換のためのPythonレベルでのDLPackの公開
- 構造化されたdtypesのプロモーションと比較方法の変更
- f2pyの改善

Numpy 1.23. リリースでは引き続きdtypeの取り扱いと
dtypeのプロモーションを改善し、実行速度を向上させ、
ドキュメントを明確化するための継続的な作業を続けて行く予定です。 今回のリリースは、494個のプルリクエストと151人のコントリビューターによるものです。 このリリースでサポートされている Python のバージョンは 3.8 - 3.10 です。
Python 3.11がrc ステージに到達すると Python 3.11 もサポートされます。

### NumFOCUS DEI研究への参加募集

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a
[research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent\&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c)
funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to
understand the barriers to participation that contributors, particularly those
from historically underrepresented groups, face in the open-source software
community. この研究チームは、新しい貢献者、プロジェクトの開発者およびメンテナー、そして過去に貢献した方々に、NumPyに参加し貢献した経験について話を聞きたいと考えています。

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe)
which contains additional information on the research goals, privacy, and
confidentiality considerations. 多様で包括的なオープンソースソフトウェアコミュニティの 成長と持続可能性のために、このプロジェクトへのあなたの参加は非常に大きな価値があります。 参加を受け入れられた人は、研究チームメンバーと30分間のインタビューに参加することになります。

### NumPy 1.22.0 リリース

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)
is now available. 今回のリリースのハイライトは次のとおりです。

- メインの名前空間の型アノテーションは基本的に完了しました。 Upstream is
  a moving target, so there will likely be further improvements, but the major
  work is done. This is probably the most user visible enhancement in this
  release.
- A preliminary version of the proposed
  [array API Standard](https://data-apis.org/array-api/latest/) is provided
  (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)).
  This is a step in creating a standard collection of functions that can be
  used across libraries such as CuPy and JAX.
- NumPy に DLPack バックエンドが追加されました。 DLPack provides a common interchange format
  for array (tensor) data.
- New methods for `quantile`, `percentile`, and related functions. The new
  methods provide a complete set of the methods commonly found in the
  literature.
- The universal functions have been refactored to implement most of
  [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html).
  これにより将来の DType API の処理も可能にします。
- ダウンストリームのプロジェクトで使用するための新しい設定可能なメモリー・アロケーターが追加されました。

NumPy 1.22.0は、153人の貢献者が609のプルリクエストを作成した
非常に大きなリリースです。 このリリースでサポートされている Python のバージョンは
3.8 - 3.10 です。

### 科学的なPythonエコシステムにおける包括的な文化の前進

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has
[awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)
to support the onboarding, inclusion, and retention of people from historically
marginalized groups on scientific Python projects, and to structurally improve
the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/),
this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)
will support the creation of dedicated Contributor Experience Lead positions to
identify, document, and implement practices to foster inclusive open-source
communities. このプロジェクトは、Melissa Mendonça (NumPy)が中心となって、下記の方々の追加のメンタリングとサポートにより実施されます。Ralf Gommers (NumPy、SciPy)、Hannah AizenmanとThomas Caswell (Matplotlib)、Matt Haberland  (SciPy)、そして
Joris Van den Bossche (Pandas)。

このプロジェクトは私たちのOSSプロジェクトのコミュニティダイナミクスを構造的に改善する方法を発見し、実施することを目指す野心的なプロジェクトです。 このような複数のプロジェクトの横断的な役割を確立することで、Scientific Pythonコミュニティに新しいコラボレーションモデルを導入し、エコシステム内のコミュニティ構築作業をより効率的に、より大きな成果を生めるようにしたいと考えています。 特にこのプロジェクトにより、歴史的にこれまで代表的ではなかったグループからの新しいコントリビュータを引き付け、貢献を維持するために、何がうまくいき、何がうまくいかないかを、より明確に把握できるようになると期待しています。 最後に、実施したアクションについて詳細な報告書を作成し、プロジェクトの代表者やコミュニティとの交流の面で、プロジェクトにどのような影響を与えたかを説明する予定です。

2021年11月から2年間のプロジェクトが始まると予想されており、このプロジェクトの成果を楽しみにしています!
[You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021年度NumPyアンケート

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 昨年の第1回アンケートには、75カ国から1,236名のNumPyユーザーが参加してくれました。
この調査結果により、今後12ヶ月間、私たちがどのようなことに集中すべきかを、非常に良く理解することができました。

今年もアンケートの時間が来ました。もう一度アンケートへの回答をお願いいたします。 アンケートへの回答は15分ほどで終了します。 アンケートは英語以外にも、ベンガル語、フランス語、ヒンディー語、日本語、マンダリン、ポルトガル語、ロシア語、スペイン語の8ヶ国語に対応しています。

こちらのリンク先から、アンケートを始めることができます: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSL4q.

### NumPy 1.21.0 リリース

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)
is now available. 今回のリリースのハイライトは次のとおりです。

- より多くの機能やプラットフォームをカバーするためのSIMD関連の改善が実施されました。
- dtypeのための新しいインフラとキャストの準備
- Mac 版の Python 3.8 と Python 3.9 用 universal2 wheel
- ドキュメントの改善
- アノテーションの改善
- new `PCG64DXSM` bitgenerator for random numbers.

今回のNumpy リリースは、175人による581件のプルリクエストのマージの結果です。  このリリースでサポートされている Python のバージョンは 3.7-3.9 です。Python 3.10 がリリースされた後、Python 3.10 のサポートが追加されます。

### 2020年度 NumPy アンケート結果

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students
and faculty from the University of Michigan and the University of Maryland
conducted the first official NumPy community survey. アンケートの結果はこちらから確認できます。 https://numpy.org/user-survey-2020/

### Numpy 1.20.0 リリース

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)
is now available. 今回のリリースは180 人以上のコントリビューターのおかげで、これまでで最大の NumPyのリリースとなりました。 最も重要な2つの新機能は次のとおりです。

- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule
  containing `ArrayLike` and `DtypeLike` aliases that users and downstream
  libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE,
  AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant
  performance improvements for many functions (examples:
  [sin/cos](https://github.com/numpy/numpy/pull/17587),
  [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPyプロジェクトにおける多様性

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).

### Natureに初めての公式のNumPy論文が掲載されました!

_Sep 16, 2020_ -- We are pleased to announce the publication of
[the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2)
as a review article in Nature. これはNumPy 1.0のリリースから14年後のことになりました。
この論文では、配列プログラミングのアプリケーションと基本的なコンセプト、NumPyの上に構築された様々な科学的Pythonエコシステム、そしてCuPy、Dask、JAXのような外部の配列およびテンソルライブラリとの相互運用を容易にするために最近追加された配列プロトコルについて説明しています。

### Python 3.9のリリースに伴い、いつNumPyのバイナリwheelがリリースされるのですか？

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. もしあなたが新しいPythonのバージョンをいち早く利用している場合、NumPy（およびSciPyのような他のパッケージ）がリリース当日にバイナリwheelを用意していないことを知ってがっかりしたかもしれませんね。 ビルド用のインフラを新しいPythonのバージョンに適応させるのは非常に大変な作業で、PyPIやconda-forgeにパッケージが掲載されるまでには通常数週間かかります。 今後のwheelのリリースに備えて、以下を確認してください。

- update your `pip` to version 20.1 at least to support `manylinux2010` and
  `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from
  trying to build from source.

### NumPy 1.19.2 リリース

_Sep 10, 2020_ -- NumPy
1.19.2 is now available.
This latest release in the 1.19 series fixes several bugs, prepares for the
upcoming Cython 3.x
release and pins
setuptools to keep distutils working while upstream modifications are ongoing.
aarch64 wheelは最新のmanylinux2014リリースでビルドされており、異なるLinuxディストリビューションで使用される異なるページサイズの問題が修正されています。

### 初めてのNumPyのアンケートが公開されました!!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for
decision-making about the development of NumPy as software and as a community.
この調査結果は英語以外のこれらの8つの言語で利用可能です: バングラ, ヒンディー語, 日本語, マンダリン, ポルトガル語, ロシア語, スペイン語とフランス語.

Please help us make NumPy better and take the survey
[here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).

### Numpy のロゴが新しくなりました!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img
src="/images/logos/numpy_logo.svg"
alt="NumPy logo"
title="The new NumPy logo"
width=300>

新しいロゴは、古いロゴに比べて、モダンでよりクリーンなデザインになりました。 新しいロゴをデザインしてくれたIsabela Presedo-Floydと、15年以上にわたって使用してきた旧ロゴをデザインしてくれたTravis Vaughtに感謝します。

### Numpy 1.19.0 リリース

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. このバージョンは Python 2系のサポートがない最初のリリースであり、"クリーンアップ用のリリース" です。 サポートされている一番古いPython のバージョンは Python 3.6 になりました。 また、今回の重要な新機能はNumPy 1.17.0で導入された乱数生成用のインフラにCythonからアクセスできるようになったことです。

### ドキュメント改善期間

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for
the Google Season of Docs program. NumPy のドキュメントを改善するために、テクニカルライターと協力するこの機会を楽しみにしています! For more
details, please see
[the official Season of Docs site](https://developers.google.com/season-of-docs/) and our
[ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).

### Numpy 1.18.0 リリース

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. このリリースは、1.17.0での主要な変更の後の、まとめのようなリリースです。 Python 3.5 をサポートする最後のマイナーリリースになります。 Highlights of the release includes the addition of basic
infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.

### NumPyはChan Zuckerberg財団からの助成金を獲得しました。

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

この助成金は、Numpy ドキュメントやウェブサイトの再設計などの改善に向けた取り組みを促進するために使用されます。 大規模かつ急速に拡大するユーザーの体験をより良くし、プロジェクトの長期的な持続可能性を確保するためのコミュニティ開発を行っていきます。 OpenBLASチームは、技術的に非常に重要な問題である、スレッド安全性、AVX-512に対処することに注力します。 また、スレッドローカルストレージ(TLS) の問題や、OpenBLASが依存するReLAPACK(再帰的なLAPACK) のアルゴリズムの改善も実施します。

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). この取り組みは2019年12月1日から始まり、今後12ヶ月間継続実施される予定です。

<a name="releases"></a>

## 過去のリリース

こちらがより過去のNumPyリリースのリストで、各リリースノートへのリンクが記載されています。 Bugfix
releases (only the `z` changes in the `x.y.z` version number) have no new
features; minor releases (the `y` increases) do.

- NumPy 2.1.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.2)) -- _5 Oct 2024_.
- NumPy 2.1.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.1)) -- _3 Sep 2024_.
- NumPy 2.0.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.2)) -- _26 Aug 2024_.
- NumPy 2.1.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.0)) -- _18 Aug 2024_.
- NumPy 2.0.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.1)) -- _21 Jul 2024_.
- NumPy 2.0.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.0)) -- _16 Jun 2024_.
- NumPy 1.26.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.4)) -- _5 Feb 2024_.
- NumPy 1.26.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _2 Jan 2024_.
- NumPy 1.26.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _12 Nov 2023_.
- NumPy 1.26.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _14 Oct 2023_.
- NumPy 1.26.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _16 Sep 2023_.
- NumPy 1.25.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.2)) -- _31 Jul 2023_.
- NumPy 1.25.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _8 Jul 2023_.
- NumPy 1.24.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _26 Jun 2023_.
- NumPy 1.25.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _17 Jun 2023_.
- NumPy 1.24.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 Apr 2023_.
- NumPy 1.24.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 Feb 2023_.
- NumPy 1.24.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 Dec 2022_.
- NumPy 1.24.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.0)) -- _18 Dec 2022_.
- NumPy 1.23.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _19 Nov 2022_.
- NumPy 1.23.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _12 Oct 2022_.
- NumPy 1.23.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 Sep 2022_.
- NumPy 1.23.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 Aug 2022_.
- NumPy 1.23.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 Jul 2022_.
- NumPy 1.23.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 Jun 2022_.
- NumPy 1.22.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 May 2022_.
- NumPy 1.21.6 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 Apr 2022_.
- NumPy 1.22.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.3)) -- _7 Mar 2022_.
- NumPy 1.22.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 Feb 2022_.
- NumPy 1.22.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 Jan 2022_.
- NumPy 1.22.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 Dec 2021_.
- NumPy 1.21.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 Dec 2021_.
- NumPy 1.21.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 Jun 2021_.
- NumPy 1.20.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 May 2021_.
- NumPy 1.20.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 Jan 2021_.
- NumPy 1.19.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 Jan 2021_.
- NumPy 1.19.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _20 Jun 2020_.
- NumPy 1.18.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 May 2020_.
- NumPy 1.17.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 Jan 2020_.
- NumPy 1.18.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 Dec 2019_.
- NumPy 1.17.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 Jul 2019_.
- NumPy 1.16.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 Jan 2019_.
- NumPy 1.15.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 Jul 2018_.
- NumPy 1.14.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 Jan 2018_.
