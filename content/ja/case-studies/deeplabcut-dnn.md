---
title: "ケーススタディ: DeepLabCut 三次元姿勢推定"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="{{< blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/" by="Alexander Mathis、 _准教授、École polytechnology fe’rale de Lausanne_ ([EPFL](https://www.epfl.ch/en/))""
  by="Alexander Mathis, _Assistant Professor, École polytechnique fédérale de Lausanne_ ([EPFL](https://www.epfl.ch/en/))"
>}}
{{< /blockquote >}}

## DeepLabCut について

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut)は、ごくわずかなトレーニングデータで人間レベルの精度で実験動物の行動を追跡可能にするオープンソースのツールボックスです。 DeepLabCutの技術を使うことで、科学者は動物の種類と時系列のデータをもとに、運動制御と行動に関する科学的な理解を深めることができるようになりました。 DeepLabCutの技術を使うことで、科学者は動物の種類と時系列のデータをもとに、運動制御と行動に関する科学的な理解を深めることができるようになりました。

神経科学、医学、生体力学などのいくつかの研究分野では、動物の動きを追跡したデータを使用しています。 DeepLabCutは、動画に記録された動きを解析することで、人間やその他の動物が何をしているのかを理解することができます。 タグ付けや監視などの、手間のかかる作業を自動化し、深層学習ベースのデータ解析を実施します。 DeepLabCutは、霊長類、マウス、魚、ハエなどの動物を観察する科学研究をより速く正確にしています。

{{< figure >}}
{{< /figure >}}

DeepLabCutは、動物の姿勢を抽出することで非侵襲的な行動追跡を行います。 これは、生体力学、遺伝学、倫理学、神経科学などの分野での研究に必要不可欠です。 動的に変化する背景の中で、動物の姿勢をビデオデータから非侵襲的に測定することは、技術的にも、必要な計算リソースやトレーニングデータの点でも、非常に困難な計算処理です。 動的に変化する背景の中で、動物の姿勢をビデオデータから非侵襲的に測定することは、技術的にも、必要な計算リソースやトレーニングデータの点でも、非常に困難な計算処理です。

DeepLabCutは、研究者が対象の姿勢を推定し、Pythonベースのソフトウェアを使って効率的に対象の行動を定量化することを可能にします。  DeepLabCutを使用すると、研究者は動画から異なるフレームを識別し、数十個のフレームの特定の身体部位を、よくできたGUIによってラベルづけできます。 すると、DeepLabCutの深層学習ベースのポーズ推定アーキテクチャにより、動画の残りの部分や動物の他の類似した動画から同じ特徴を抽出する方法を学習できます。 It works across species of animals, from common laboratory animals such as flies and mice to more unusual animals like [cheetahs][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut uses a principle called [transfer learning](https://arxiv.org/pdf/1909.11229), which greatly reduces the amount of training data required and speeds up the convergence of the training period.  必要に応じて、より高速な推論を提供するさまざまなネットワークアーキテクチャ(MobileNetV2など)を選択することができ、リアルタイムの実験データフィードバックと組み合わせることもできます。 DeepLabCut originally used the feature detectors from a top-performing human pose estimation architecture, called [DeeperCut](https://arxiv.org/abs/1605.03170), which inspired the name. 今ではこのパッケージは大幅に変更され、追加のアーキテクチャ・データの水増し・一通りのユーザー用フロントエンドを含んでいます。 さらに、 大規模な生物学的実験をサポートするため、DeepLabCutはオンライン学習の機能を提供しています。 これにより、動画の時間をこえて学習データを増やすことができ、エッジケースをカバーしたり、特定のコンテキスト内でポーズ推定アルゴリズムを堅牢にしたりできます。

最近、[DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo)が発表されました。 これは、霊長類の顔分析から犬の姿勢まで、様々な種や実験条件に対応した事前訓練済みモデルを提供しています。 これにより、例えば、新しいデータのラベルを付けることなくクラウドで予測を実行することができたり、ニューラルネットワークの学習を実行することができます。 プログラミング経験は必要ありません。 これにより、例えば、新しいデータのラベルを付けることなくクラウドで予測を実行することができたり、ニューラルネットワークの学習を実行することができます。 プログラミング経験は必要ありません。

### 主な目標と結果

- **科学研究のための動物姿勢解析の自動化:**

  DeepLabCutという技術の主な目的は、多様な環境で動物の姿勢を測定し追跡することです。 このデータは例えば神経科学の研究において、脳がどのように運動を制御しているかを理解するためのや、動物がどのように社会的に交流しているかを明らかにするために利用することができます。 研究者はDeepLabCutで [10倍のパフォーマンス向上](https://www.biorxiv.org/content/10.1101/457242v1) が可能であると発表しています。 オフラインでは最大1200フレーム/秒(FPS) で姿勢を推定することができます。 This data can be used, for example, in
  neuroscience studies to understand how the brain controls movement, or to
  elucidate how animals socially interact. Researchers have observed a
  [tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1)
  with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second
  (FPS).

- **姿勢推定のための使いやすいPythonツールキットの作成:**

  DeepLabCut wanted to share their animal pose-estimation technology in the form
  of an easy to use tool that can be adopted by researchers easily. So they have
  created a complete, easy-to-use Python toolbox with project management features
  as well. These enable not only automation of pose-estimation but also
  managing the project end-to-end by helping the DeepLabCut Toolkit user right
  from the dataset collection stage to creating shareable and reusable analysis
  pipelines.

  この[ツールキット][DLCToolkit] はオープンソースとして利用できます。

  典型的なDeepLabCutワークフローは以下のようになります。

  - オンライン学習によるトレーニングセットの作成と調整
  - 特定の動物やシナリオに合わせたニューラルネットワークの構築
  - 動画における大規模推論のためのコード作成
  - 統合された可視化ツールを使用した推論の描画

{{< figure >}}
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### 課題

- **速度**

  動物行動動画の高速な処理は、動物の行動を測定し、科学実験をより効率的で正確にするために重要です。 動的に変化する背景の中で、マーカーを使用せずに、実験室での実験のために動物の詳細な姿勢を抽出することは、技術的にも、必要なリソース的にも、必要なトレーニングデータの面でも、困難な場合があります。 科学者が、より現実的な状況で研究を行うために、コンピュータビジョンなどの専門知識のスキルを必要とせずに使うことができるツールを開発することは、解決すべき重要な問題です。
  Extracting detailed animal poses for laboratory experiments, without
  markers, in dynamically changing backgrounds, can be challenging, both
  technically as well as in terms of resource needs and training data required.
  Coming up with a tool that is easy to use without the need for skills such
  as computer vision expertise that enables scientists to do research in more
  real-world contexts, is a non-trivial problem to solve.

- **組み合わせ問題**

  Combinatorics involves assembly and integration of movement of multiple
  limbs into individual animal behavior. 組合せ問題とは、複数の四肢の動きを個々の動物行動に統合することを指します。 キーポイントと、その個々の動物行動との関連性を組み合わせ、時間的に結びつけることは、複雑なプロセスであり、非常に膨大な数値解析が必要となります。 特に、実験映像の中で複数の動物の動きを追跡する場合は大変です。

- **データ処理**

  最後に、配列の操作もかなり難しい問題です。 様々な画像や、目標のテンソル、キーポイントに対応する大きな配列のスタックを処理しなければならないからです。

{{< figure >}}
{{< /figure >}}

## 姿勢推定の課題に対応するためのNumPyの役割

NumPy は DeepLabCutにおける、行動分析の高速化のための数値計算の核となっています。  NumPy は DeepLabCutにおける、行動分析の高速化のための数値計算の核となっています。  NumPyだけでなく、DeepLabCutは様々なNumPyをベースとしているPythonライブラリを利用しています。 [SciPy](https://www.scipy.org)、[Pandas](https://pandas.pydata.org)、[matplotlib](https://matplotlib.org)、[Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug)、[scikit-learn](https://scikit-learn.org/stable/)、[scikit-image](https://scikit-image.org)、[Tensorflow](https://www.tensorflow.org)などです。

以下に挙げるNumPyの特徴が、DeepLabCutの姿勢推定アルゴリズムでの画像処理・組み合わせ処理・高速計算において、重要な役割を果たしました。

- ベクトル化
- マスクされた配列操作
- 線形代数
- ランダムサンプリング
- 大きな配列の再構成

DeepLabCutは、ツールキットが提供するワークフローを通じてNumPyの配列機能を利用しています。 特に、NumPyはヒューマンアノテーションのラベル付けや、アノテーションの書き込み、編集、処理のために、特定のフレームをサンプリングするために使用されています。  TensorFlowを使ったニューラルネットワークは、DeepLabCutの技術によって何千回も訓練され、 フレームから真のアノテーション情報を予測します。 この目的のため、姿勢推定問題を画像-画像変換問題として変換する目標密度(スコアマップ) を作成します。 ニューラルネットワークのロバスト化のため、データの水増しを使用していますが、このためには幾何学・画像的処理を施したスコアマップの計算を行うことが必要になります。 また学習を高速化するため、NumPyのベクトル化機能が利用されています。 推論には、目標のスコアマップから最も可能性の高い予測値を抽出し、効率的に「予測値をリンクさせて個々の動物を組み立てる」ことが必要になります。

{{< figure >}}
{{< /figure >}}

## まとめ

行動を観察し、効率的に表現することは、現代倫理学、神経科学、医学、工学の根幹です。
行動を観察し、効率的に表現することは、現代倫理学、神経科学、医学、工学の根幹です。 [DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf) により、研究者は対象の姿勢を推定し、行動を効率的に定量化できるようになりました。 DeepLabCutというPythonツールボックスを使えば、わずかな学習画像のセットでニューラルネットワークを人間レベルのラベリング精度で学習することができ、実験室での行動分析だけでなく、スポーツ、歩行分析、医学、リハビリテーション研究などへの応用が可能になります。 DeepLabCutアルゴリズムに必要な複雑な組み合わせ処理やデータ処理の問題を、NumPyの配列操作機能が解決しています。 DeepLabCutというPythonツールボックスを使えば、わずかな学習画像のセットでニューラルネットワークを人間レベルのラベリング精度で学習することができ、実験室での行動分析だけでなく、スポーツ、歩行分析、医学、リハビリテーション研究などへの応用が可能になります。 DeepLabCutアルゴリズムに必要な複雑な組み合わせ処理やデータ処理の問題を、NumPyの配列操作機能が解決しています。

{{< figure >}}
{{< /figure >}}
