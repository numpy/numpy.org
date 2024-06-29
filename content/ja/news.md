---
title: ニュース
sidebar: false
newsHeader: "NumPy 2.0. がリリースされました!"
date: 2023-09-16
---

### NumPy 2.0 リリース日: 6月16日

_2024年6月16日_ -- Numpy 2.0.0 は2006年以来のメジャーリリースです。 これは、前回の機能リリースから11か月間の開発の成果であり、1078件のプルリクエストにわたる212人の貢献者の成果となります。 このリリースには、大きく、エキサイティングな新機能と、PythonとCの両方のAPIへの変更が含まれています。  今回のリリースが、通常のマイナーリリースでは実施できなかった互換性を破壊する変更を含んでいます。これには、ABIの破壊、型昇格ルールの変更、および1.26.xでは非推奨警告が出されていなかった可能性のあるAPIの変更が含まれています。 NumPy 2.0の変更に対応する方法に関する主要なドキュメントは次のとおりです。

- [NumPy 2.0移行ガイド](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- [2.0.0 リリース ノート](https://numpy.org/devdocs/release/2.0.0-notes.html)
- ステータスアップデートお知らせに関する問題: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

ブログ記事 ["NumPy 2.0: 進化のマイルストーン"](https://blog.scientific-python.org/numpy/numpy2/) は、今回のメジャーバージョンリリースがどのようにして決定されたかについてのストーリーを少し伝えています。


### NumPy 2.0 リリース日: 6月16日

_ 2024年5月23日_ -- NumPy 2.0が2024年6月16日にリリースされる予定になりました！ このリリースは1年以上かけて我々が準備してきたもので、2006年以来のメジャーリリースとなります。 このリリースで重要なことは、多くの新機能とパフォーマンスの向上に加えて、 このリリースは、 **破壊的な変更** である Python と C API を含む、ABI への変更 が含まれています。 NumPyに依存しているパッケージやエンドユーザーのコードがこのは破壊的変更に適応する必要がある可能性があります。可能であれば、あなたのコードがNumPy `2.0.0rc2`で動作するかどうか確認をお願いします。 **詳細は下記をご覧ください:**

- [NumPy 2.0移行ガイド](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- [2.0.0 リリースノート](https://numpy.org/devdocs/release/2.0.0-notes.html)
- ステータス更新のお知らせイシューチケット: [numpy#24300](https://github.com/numpy/numpy/issues/24300)


### NumFOCUSの年末の資金調達
_2023年12月19日_ -- NumFOCUSは、年末キャンペーンでPyCharmチームと協力し、PyCharmライセンスの初回購入に30%の割引を提供しています。 2023年12月23日までのPyCharm購入による1年目の収益は全てNumFOCUSのプログラムに直接寄付されます。

購入される方はこちらのURLか:  https://lp.jetbrains.com/support-data-science/ こちらのクーポンコードを利用してください: ISUPPORTDATASCIENCE 

### NumPy 1.26.0 がリリースされました。

_2023年9月16日_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)がリリースされました。 今回のリリースの目玉機能は次のとおりです。

* Python 3.12.0 のサポート
* Cython 3.0.0 への互換性
* Mesonビルドシステムの利用
* SIMD サポートの改善
* f2py のバグ修正, meson と bind(x) のサポート
* 更新された BLAS/LAPACK の高速化ライブラリのサポート

Numpy 1.26.0 は 1.25 からの互換性を保持しています。Mesonビルドシステムへの移行とCython 3.0.0へのサポートが目的のリリースです。 合計20人がこのリリースに貢献し、59個のプルリクエストがマージされました。

このリリースでサポートされている Python のバージョンは3.9から 3.12 です。

### numpy.orgが日本語とポルトガル語で利用可能になりました

_2023年4月2日_ -- numpy.orgが2つの言語で利用可能になりました： 日本語とポルトガル語。 熱心なボランティアがいなければ、このプロジェクトは不可能でした：

_ポルトガル語_
* Melissa Weber Mendonça (melissawm)
* Ricardo Prins (ricardoprins)
* Getúlio Silva (getuliosilva)
* Julio Batista Silva (jbsilva)
* Alexandre de Siqueira (alexdesiqueira)
* Alexandre B A Villares (villares)
* Vini Salazar (vinisalazar)

_日本語：_
* Atsushi Sakai (AtsushiSakai)
* KKunai
* Tom Kelly (TomKellyGenetics)
* Yuji Kanagawa (kngwyu)
* Tetsuo Koyama (tkoyama010)

翻訳インフラストラクチャに関するプロジェクトは、CZIからの資金援助でサポートされています。

今後も、NumPyのウェブサイトをより多くの言語に翻訳したいと思っています。 もし手伝える場合は、Slack上のNumPy翻訳チームに連絡をお願います: https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w. (#translation チャンネルを探してください) また、Scientific Pythonエコシステム全体のドキュメントや教育コンテンツのローカライズに取り組む翻訳チームも 立ち上げています。 このプロジェクトにも興味がある場合は、是非Scientific Python Discordに参加してください: https://discord.gg/khWtqY6RKr. (#translation チャンネルを探してください)

### NumPy 1.25.0 リリース

_2023年1月17日_ -- [Numpy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html) がリリースされました。 今回のリリースの目玉機能は次のとおりです。

* MUSLのサポート。MUSLのWheelが準備されました。
* 富士通のC/C++コンパイラサポート
* einsum でオブジェクト配列がサポートされるようになりました.
* 行列の置き換え(inplace)掛け算のサポート (`@=`).

Numpy 1.25. リリースは引き続きdtypeの取り扱いと dtypeのプロモーションを改善し、実行速度を向上させ、 ドキュメントを明確化するための継続的な作業を続けて行く予定です。 将来の NumPy 2.0.0 に向けた準備作業も行われており、 多数の新規および期限切れの機能廃止が可能となってきています。

合計148人がこのリリースに貢献し、530個のプルリクエストが マージされました。

このリリースでサポートされている Python のバージョンは3.3.9 - 3.11 です。

### インクルーシブな文化の育成: 参加の募集

_2023年5月10日_ -- インクルーシブ・カルチャーの育成: 参加募集

NumPyプロジェクトの多様性とインクルージョンに関して、我々はどのようなことを実施すればいいでしょうか？ 興味がある方はこちらの [レポート](https://contributor-experience.org/docs/posts/dei-report/) を読んで参加する方法を確認してください。

### NumPy ドキュメンテーションチームのリーダーの変更

_2023年1月6日_ –- Mukulika PahariとRoss Barnowskiは、Melissa MendoncAudioに代わるNumPyドキュメンテーションチームの新しいリーダーとして任命されました。 私たちは、MelissaにNumPyの公式ドキュメントと教育資料に対するすべての貢献に感謝し、MukulikaとRossに新しい役割にステップアップしてもらったことに感謝します。

### NumPy 1.24.0 リリース

_2022年12月18日_ -- [Numpy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) がリリースされました。 今回のリリースのハイライトは次のとおりです。

* スタッキング関数のための新しい"dtype"と"casting"キーワードの追加
* F2PYの新機能追加とバグ修正
* 多くの新しい非推奨(Deprecation)の追加
* 多くの期限切れの非推奨(Deprecation)の削除

Numpy 1.25. リリースは引き続きdtypeの取り扱いと dtypeのプロモーションを改善し、実行速度を向上させ、 ドキュメントを明確化するための継続的な作業を続けて行く予定です。 dtype のプロモーションとクリーンアップの変更により、多数の新規と期限切れの非推奨が存在しています。 今回のリリースは、444個のプルリクエストと177人のコントリビューターによるものです。 サポートされている Python のバージョンは 3.8-3.11 です。

### Numpy 1.23.0 リリース

_2022年1月22日_ -- [Numpy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) がリリースされました。 今回のリリースの目玉機能は次のとおりです。

* `loadtxt` がCで実装されたことによる、大幅なパフォーマンス向上
* より簡単なデータ交換のためのPythonレベルでのDLPackの公開
* 構造化されたdtypesのプロモーションと比較方法の変更
* f2pyの改善

Numpy 1.23. リリースでは引き続きdtypeの取り扱いと dtypeのプロモーションを改善し、実行速度を向上させ、 ドキュメントを明確化するための継続的な作業を続けて行く予定です。 今回のリリースは、494個のプルリクエストと151人のコントリビューターによるものです。 このリリースでサポートされている Python のバージョンは 3.8 - 3.10 です。 Python 3.11がrc ステージに到達すると Python 3.11 もサポートされます。

### NumFOCUS DEI研究への参加募集

_2022年4月13日_ -- NumPyは、[NumFOCUS](http://numfocus.org/)と協力して、[ある研究プロジェクト](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c)を進めており、これは[Gordon & Betty Moore Foundation](https://www.moore.org/)によって資金提供されています。このプロジェクトでは、オープンソースソフトウェアコミュニティにおいて、特に歴史的に代表されてこなかったグループからの貢献者が参加する際の障壁を理解することを目的としています。 この研究チームは、新しい貢献者、プロジェクトの開発者およびメンテナー、そして過去に貢献した方々に、NumPyに参加し貢献した経験について話を聞きたいと考えています。

**あなたの経験を共有することに興味がありますか?**

もし興味がある場合は、研究目標、プライバシー、および 守秘義務に関する追加情報が記載されている、この簡単な[参加者の興味](https://numfocus.typeform.com/to/WBWVJSqe)フォームに記入をお願いします。 多様で包括的なオープンソースソフトウェアコミュニティの 成長と持続可能性のために、このプロジェクトへのあなたの参加は非常に大きな価値があります。 参加を受け入れられた人は、研究チームメンバーと30分間のインタビューに参加することになります。

### NumPy 1.19.2 リリース

_2021年12月31日_ -- [Numpy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) がリリースされました。 今回のリリースの目玉機能は次のとおりです。

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

_2021年1月23日_ -- [Numpy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) がリリースされました。 今回のリリースのハイライトは下記の通りです。

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

_2021年1月30日_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) がリリースされました。 今回のリリースは180 人以上のコントリビューターのおかげで、これまでで最大の NumPyのリリースとなりました。 最も重要な2つの新機能は次のとおりです。
- NumPyの大部分のコードに型注釈が追加されました。 そして新しいサブモジュールである`numpy.typing`が追加されました。 このサブモジュールは`ArrayLike` や`DtypeLike`という型注釈のエイリアスが定義されており、これによりユーザーやダウンストリームのライブラリはこの型注釈を使うことができます。
- X86(SSE、AVX)、ARM64(Neon)、およびPowerPC (VSX) 命令をサポートするマルチプラットフォームSIMDコンパイラの最適化が実施されました。 これにより、多くの関数で大きく パフォーマンスが向上しました (例: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPyプロジェクトの多様性

_2020年9月20日に_ 、私たちは[ NumPyプロジェクトにおけるダイバーシティやインクルージョンの状況や、ソーシャルメディア上での議論についての宣言 ](/diversity_sep2020)について書きました。


### Natureに初の公式NumPy論文が掲載されました!

_2020年9月16日_ -- NumPyに関する [ 最初の公式の論文 ](https://www.nature.com/articles/s41586-020-2649-2)がNatureに査読付き論文として掲載されました。 これはNumPy 1.0のリリースから14年後のことになりました。 この論文では、配列プログラミングのアプリケーションと基本的なコンセプト、NumPyの上に構築された様々な科学的Pythonエコシステム、そしてCuPy、Dask、JAXのような外部の配列およびテンソルライブラリとの相互運用を容易にするために最近追加された配列プロトコルについて説明しています。


### Python 3.9のリリースに伴い、いつNumPyのバイナリwheelがリリースされるのですか？

_2020年9月14日_ -- Python 3.9 は数週間後にリリースされる予定です。 もしあなたが新しいPythonのバージョンをいち早く利用している場合、NumPy（およびSciPyのような他のパッケージ）がリリース当日にバイナリwheelを用意していないことを知ってがっかりしたかもしれませんね。 ビルド用のインフラを新しいPythonのバージョンに適応させるのは非常に大変な作業で、PyPIやconda-forgeにパッケージが掲載されるまでには通常数週間かかります。 今後のwheelのリリースに備えて、以下を確認してください。
- `pip` が`manylinux2010` と `manylinux2014` をサポートするためにpipを少なくともバージョン 20.1 に更新する。
- [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) または `--only-binary=:all:` を`pip`がソースからビルドしようとするのを防ぐために使用します。


### NumPy 1.19.2 リリース

_2020年9月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) がリリースされました。 この 1.19 シリーズの最新リリースでは、いくつかのバグが修正され、[ 来るべき Cython 3.xリリース ](http:/docs.cython.orgenlatestsrcchanges.html)への準備が行われ、アップストリームの修正が進行中の間も distutils の動作を維持するためのsetuptoolsのバージョンの固定が実施されています。 aarch64 wheelは最新のmanylinux2014リリースでビルドされており、異なるLinuxディストリビューションで使用される異なるページサイズの問題が修正されています。

### 初めてのNumPyの調査が公開されました!!

_2020年7月2日_ -- このアンケート調査は、NumPyにおける、ソフトウェアとしてとコミュニティの両方における意思決定の指針となり、優先順位を決定する役に立ちました。 この調査結果は英語以外のこれらの8つの言語で利用可能です: バングラ, ヒンディー語, 日本語, マンダリン, ポルトガル語, ロシア語, スペイン語とフランス語.

NumPy をより良くするために、こちらの [アンケート](https://umdsurvey. umd. edu/jfe/form/SV_8bJrXjbhXf7saAl) に協力してもらえると助かります。


### NumPy に新しいロゴができました!

_2020年6月24日_ -- NumPyのロゴが新しくなりました:

<img src="/images/logos/numpy_logo.svg" alt="NumPyのロゴ" title="新しいNumPyロゴ" width=300>

新しいロゴは、古いロゴに比べて、モダンでよりクリーンなデザインになりました。 新しいロゴをデザインしてくれたIsabela Presedo-Floydと、15年以上にわたって使用してきた旧ロゴをデザインしてくれたTravis Vaughtに感謝します。


### NumPy 1.20.0 リリース

_2020年6月20日_ -- NumPy 1.19.0 がリリースされました。 このバージョンは Python 2系のサポートがない最初のリリースであり、"クリーンアップ用のリリース" です。 サポートされている一番古いPython のバージョンは Python 3.6 になりました。 また、今回の重要な新機能はNumPy 1.17.0で導入された乱数生成用のインフラにCythonからアクセスできるようになったことです。


### ドキュメント受諾期間

_2020年5月11日_ -- NumPyは、 Googleのシーズンオブドキュメントプログラムのメンター団体の1つとして選ばれました。 NumPy のドキュメントを改善するために、テクニカルライターと協力するこの機会を楽しみにしています! 詳細については、 [シーズンオブドキュメント公式サイト](https://developers.google.com/season-of-docs/) と [アイデアページ](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas) をご覧ください。


### Numpy 1.18.0 リリース

_2019年12月22日_ -- NumPy 1.18.0 がリリースされました。 このリリースは、1.17.0での主要な変更の後の、まとめのようなリリースです。 Python 3.5 をサポートする最後のマイナーリリースになります。 今回のリリースでは、64ビットのBLASおよびLAPACKライブラリとリンクするためのインフラの追加や、`numpy.random`のための新しいC-APIの追加などが行われました。

詳細については、 [リリースノート](https://github.com/numpy/numpy/releases/tag/v1.18.0) を参照してください。


### NumPyはChan Zuckerberg財団から助成金を受けました。

_2019年11月15日_ -- NumPyと、NumPyの重要な依存ライブラリの1つであるOpenBLASが、Chan Zuckerberg財団の[Essential Open Source Software for Scienceプログラム](https:/chanzuckerberg.comeoss)を通じて、科学に不可欠なオープンソースツールのソフトウェアのメンテナンス、成長、開発、コミュニティへの参加などを支援する195,000ドルの共同助成金を獲得したことを発表しました。

この助成金は、Numpy ドキュメントやウェブサイトの再設計などの改善に向けた取り組みを促進するために使用されます。 大規模かつ急速に拡大するユーザーの体験をより良くし、プロジェクトの長期的な持続可能性を確保するためのコミュニティ開発を行っていきます。 OpenBLASチームは、技術的に非常に重要な問題である、スレッド安全性、AVX-512に対処することに注力します。 また、スレッドローカルストレージ(TLS) の問題や、OpenBLASが依存するReLAPACK(再帰的なLAPACK) のアルゴリズムの改善も実施します。

提案されたイニシアチブとその成果の詳細については、 [フルグラントプロポーザル](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167) を参照してください。 この取り組みは2019年12月1日から始まり、今後12ヶ月間継続実施される予定です。


<a name="releases"></a>

## 過去のリリース

こちらは、より以前のNumPyリリースのリストで、各リリースノートへのリンクが記載されています。 全てのバグフィックスリリース(バージョン番号`x.y.z` の`z`だけが変更されたもの)は新しい機能追加はされず、マイナーリリース (`y` が増えたもの)は、新しい機能追加されています。

- NumPy 2.0.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v2.0.0)) -- _2024年6月16日_.
- NumPy 1.26.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _ 2024年1月2日_.
- NumPy 1.26.3 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _ 2024年1月2日_.
- NumPy 1.26.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _2023年11月12日_.
- NumPy 1.26.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _2023年10月14日_.
- NumPy 1.26.0 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _2023年9月16日_.
- NumPy 1.25.2 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.25.2)) -- _2023年7月31日_.
- NumPy 1.25.1 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _2023年7月8日_.
- NumPy 1.24.4 ([リリースノート](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _2023年6月26日_.
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
