---
title: NumPy に貢献する
sidebar: false
---

NumPyプロジェクトを成功させるには、あなたの専門知識とプロジェクトに関する熱意が必要です。 NumPyに貢献する方法はコーディングだけではありません。

- [コードを書く]({{< relref "contribute.md#writing-code" >}})

以外にも、下記の貢献の方法があります:

- [プルリクエストをレビューする]({{< relref "contribute.md#reviewing-pull-requests" >}})
- [チュートリアル・プレゼンテーションなど教育的資料を作成する]({{< relref "contribute.md#developing-educational-materials" >}})
- [イシューをトリアージする]({{< relref "contribute.md#issue-triaging" >}})
- [ウェブサイトをメンテナンスをする]({{< relref "contribute.md#website-development" >}})
- [グラフィックデザインに貢献する]({{< relref "contribute.md#graphic-design" >}})
- [ウェブサイトを翻訳する]({{< relref "contribute.md#translating-website-content" >}})
- [コミュニティのコーディネーターをつとめる]({{< relref "contribute.md#community-coordination-and-outreach" >}})
- [助成金のプロポーザルを書くなど、資金調達をサポートする]({{< relref "contribute.md#fundraising" >}})

もしどこから始めればいいか、あなたのスキルをどう生かせばいいかがわからない場合は、 _是非ご連絡下さい。_ 連絡の方法としては、 [メーリングリスト](https://mail.python.org/mailman/listinfo/numpy-discussion) 、 [GitHub](http://github.com/numpy/numpy)、 [イシューの作成](https://github.com/numpy/numpy/issues) 、関連するイシューへのコメントがあります。

これらが私たちにとって好ましい連絡手段ですが(元来、オープンソースプロジェクトはオープンな方法を好みます)、もしどうしても非公開の方法で連絡を取りたい場合は、コミュニティコーディネーターに連絡して下さい。連絡先としては、 <numpy-team@googlegroups.com> または、[Slack](https://numpy-team.slack.com) (グループに招待するためにこちらに連絡お願いします: <numpy-team@googlegroups.com>)があります。

また、隔週の _コミュニティミーティング_もあり、詳細は [メーリングリスト](https://mail.python.org/mailman/listinfo/numpy-discussion) で発表されています。あなたの参加を大いに歓迎します。オープンソースプロジェクトに貢献するのが初めての方は、是非、 [このガイド](https://opensource.guide/how-to-contribute/) を読んでみて下さい。

私たちのコミュニティは、誰もが平等に扱われ、すべての貢献を平等に評価することを目指しています。 私たちはオープンで居心地の良いコミュニティを作るために [行動基準](/ja/code-of-conduct) を制定しています。

### コードを書く

プログラマーの方には、こちらの [ガイド](https://numpy.org/devdocs/dev/index.html#development-process-summary)でNumPyのコードに貢献する方法を説明しています。

### プルリクエストのレビュー
NumPyプロジェクトには現時点で250以上のオープンなプルリクエストがあり、多くの 改善要求と多くのレビュワーからのフィードバックを待っています。 もしあなたがNumPy を使ったことがある場合、 たとえNumPyコードベースに慣れていない場合でも貢献する方法はあります。 例えば、
* 長期にわたる議論をまとめる
* ドキュメントのPRをトリアージする
* 提案された変更をテストする


### 教育用の資料を作成する

NumPy の [ユーザガイド](https://numpy.org/devdocs) は現在、大規模な再設計中です。 新しいNumPyのWebページは、新しいチュートリアルや、NumPyの使い方、NumPy内部の深い説明など必要としており、サイト全体にも再設計と再構築が必要です。 このウェブサイトの再構築の作業は、ドキュメントを書くだけではありません。 コード例や、ノートブック、ビデオなどの作成も歓迎しています。 [NEP 44 — Restructuring the NumPyDocumentation](https://numpy.org/neps/nep-0044-restructuring-numpy-docs.html)に、ウェブサイトの再構築についての詳細が説明されています。


### イシューのトリアージ

[NumPyのイシュートラッカー](https://github.com/numpy/numpy/issues) には、 _沢山の_Open状態のイシューがあります。すでに解決されたもの、優先順位付けされるべきもの、 初心者が取り組むのに適したものがあります。あなたができることは、いくつもあります:

* 古いバグがまだ残っているか確認する
* 重複したイシューを見つけ、お互いに関連づける
* 問題を再現するコードを作成する
* イシューに正しいラベル付けをする (トリアージ権が必要なので、連絡下さい)

ぜひ、やってみて下さい。


### ウェブサイトの開発

私たちはちょうどウェブサイトを作り直し始めたところですが、それらはまだ完了していません。Web開発が好きなら、この[イシュー](https://github.com/numpy/numpy.org/issues?q=is%3Aissue+is%3Aopen+label%3Adesign) に未完成な要求が列挙されています。ぜひ、あなたのアイデアを共有してください。


### グラフィックデザイン

グラフィックデザイナーの方が可能な貢献は、枚挙にいとまがありません。私たちのドキュメントには可視化が必要で、私たちの拡大しているウェブサイトには良い画像が必要です。貢献する機会は沢山あります。


### ウェブサイトの翻訳

私たちは、[numpy.org](https://numpy.org) を複数言語に翻訳し、NumPyを母国語でアクセスできるようにしたいと思っています。 これを実現するには、ボランティアの翻訳者が必要です。  詳しくは[このイシュー](https://numpy.org/neps/nep-0028-website-redesign.html#translation-multilingual-i18n)を参照してください。 [この GitHubイシュー](https://github.com/numpy/numpy.org/issues/55) にコメントしてサインアップしてください。


### コミュニティとの連携とアウトリーチ

コミュニティとのコミュニケーションを通じて、私たちは、NumPyより広く知ってもらい、どこに問題があるのかを知りたいと思っています。 私たちは、[Twitter](https://twitter.com/numpy_team) アカウントや、NumPy[コードスプリント](https://scisprints.github.io/)の開催、ニュースレターの発行、そしておそらくブログなどを通じて、より沢山の人にコミュニティに参加して欲しいと思っていす。

### 資金調達

NumPyは何年にも渡ってボランティアだけ活動していましたが、その重要性が高まるにつれ、安定性と成長のためには資金面での支援が必要であることがわかってきました。 こちらの[SciPy'19のプレゼン](https://www.youtube.com/watch?v=dBTJD_FDVjU) では、資金的なサポートを受けたことで、どれだけ違いが出たかを説明しています。 他の非営利団体のように、私たちは助成金や、スポンサーシップ、その他の資金支援を常に探しています。 私たちはすでにいくつかの資金調達のアイデアを持っていますが、他にもより多くを資金調達を受けたいと思っています。 資金調達に関する知識は、我々には不足しているスキルです。是非、あなたのサポートをお待ちしています。

