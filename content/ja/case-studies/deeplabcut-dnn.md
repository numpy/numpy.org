---
title: "ケーススタディ: DeepLabCut 三次元姿勢推定"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/mice-hand.gif'
title = 'Analyzing mice hand-movement using DeepLapCut'
alt = 'micehandanim'
attribution = '(Source: www.deeplabcut.org )'
attributionlink = 'http://www.mousemotorlab.org/deeplabcut'
{{< /figure >}}

{{< blockquote
cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/"
by="Alexander Mathis, _Assistant Professor, École polytechnique fédérale de Lausanne_ ([EPFL](https://www.epfl.ch/en/))"

> }}
> Open Source Software is accelerating Biomedicine. DeepLabCut を使用すると、深層学習を使用して動物の行動を自動的にビデオ解析することができます。
> {{< /blockquote >}}

## DeepLabCut について

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) is an open source toolbox that empowers researchers at hundreds of institutions worldwide to track behaviour of laboratory animals, with very little training data, at human-level accuracy. DeepLabCutの技術を使うことで、科学者は動物の種類と時系列のデータをもとに、運動制御と行動に関する科学的な理解を深めることができるようになりました。

神経科学、医学、生体力学などのいくつかの研究分野では、動物の動きを追跡したデータを使用しています。 DeepLabCutは、動画に記録された動きを解析することで、人間やその他の動物が何をしているのかを理解することができます。 タグ付けや監視などの、手間のかかる作業を自動化し、深層学習ベースのデータ解析を実施します。 DeepLabCutは、霊長類、マウス、魚、ハエなどの動物を観察する科学研究をより速く正確にしています。

{{< figure >}}
src = '/images/content_images/cs/race-horse.gif'
title = 'Colored dots track the positions of a racehorse’s body part'
alt = 'horserideranim'
attribution = '(Source: Mackenzie Mathis)'
{{< /figure >}}

DeepLabCut's non-invasive behavioral tracking of animals by extracting the poses of animals is crucial for scientific pursuits in domains such as biomechanics, genetics, ethology & neuroscience. 動的に変化する背景の中で、動物の姿勢をビデオデータから非侵襲的に測定することは、技術的にも、必要な計算リソースやトレーニングデータの点でも、非常に困難な計算処理です。

DeepLabCutは、研究者が対象の姿勢を推定し、Pythonベースのソフトウェアを使って効率的に対象の行動を定量化することを可能にします。  DeepLabCutを使用すると、研究者は動画から異なるフレームを識別し、数十個のフレームの特定の身体部位を、よくできたGUIによってラベルづけできます。 すると、DeepLabCutの深層学習ベースのポーズ推定アーキテクチャにより、動画の残りの部分や動物の他の類似した動画から同じ特徴を抽出する方法を学習できます。 It works across species of animals, from common laboratory animals such as flies and mice to more unusual animals like [cheetahs][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut uses a principle called [transfer learning](https://arxiv.org/pdf/1909.11229), which greatly reduces the amount of training data required and speeds up the convergence of the training period.  必要に応じて、より高速な推論を提供するさまざまなネットワークアーキテクチャ(MobileNetV2など)を選択することができ、リアルタイムの実験データフィードバックと組み合わせることもできます。 DeepLabCut originally used the feature detectors from a top-performing human pose estimation architecture, called [DeeperCut](https://arxiv.org/abs/1605.03170), which inspired the name. 今ではこのパッケージは大幅に変更され、追加のアーキテクチャ・データの水増し・一通りのユーザー用フロントエンドを含んでいます。 さらに、 大規模な生物学的実験をサポートするため、DeepLabCutはオンライン学習の機能を提供しています。 これにより、動画の時間をこえて学習データを増やすことができ、エッジケースをカバーしたり、特定のコンテキスト内でポーズ推定アルゴリズムを堅牢にしたりできます。

Recently, the [DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo) was introduced, which provides pre-trained models for various species and experimental conditions from facial analysis in primates to dog posture. これにより、例えば、新しいデータのラベルを付けることなくクラウドで予測を実行することができたり、ニューラルネットワークの学習を実行することができます。 プログラミング経験は必要ありません。

### 主な目標と結果

- **Automation of animal pose analysis for scientific studies:**

  The primary objective of DeepLabCut technology is to measure and track posture
  of animals in a diverse settings. This data can be used, for example, in
  neuroscience studies to understand how the brain controls movement, or to
  elucidate how animals socially interact. Researchers have observed a
  [tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1)
  with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second
  (FPS).

- **Creation of an easy-to-use Python toolkit for pose estimation:**

  DeepLabCut wanted to share their animal pose-estimation technology in the form
  of an easy to use tool that can be adopted by researchers easily. So they have
  created a complete, easy-to-use Python toolbox with project management features
  as well. These enable not only automation of pose-estimation but also
  managing the project end-to-end by helping the DeepLabCut Toolkit user right
  from the dataset collection stage to creating shareable and reusable analysis
  pipelines.

  Their [toolkit][DLCToolkit] is now available as open source.

  典型的なDeepLabCutワークフローは以下のようになります。

  - オンライン学習によるトレーニングセットの作成と調整
  - 特定の動物やシナリオに合わせたニューラルネットワークの構築
  - 動画における大規模推論のためのコード作成
  - 統合された可視化ツールを使用した推論の描画

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png'
title = 'Pose estimation steps with DeepLabCut'
alt = 'dlcsteps'
align = 'center'
attribution = '(Source: DeepLabCut)'
attributionlink = 'https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1'
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### 課題

- **Speed**

  Fast processing of animal behavior videos in order to measure their behavior
  and at the same time make scientific experiments more efficient, accurate.
  Extracting detailed animal poses for laboratory experiments, without
  markers, in dynamically changing backgrounds, can be challenging, both
  technically as well as in terms of resource needs and training data required.
  Coming up with a tool that is easy to use without the need for skills such
  as computer vision expertise that enables scientists to do research in more
  real-world contexts, is a non-trivial problem to solve.

- **Combinatorics**

  Combinatorics involves assembly and integration of movement of multiple
  limbs into individual animal behavior. Assembling keypoints and their
  connections into individual animal movements and linking them across time
  is a complex process that requires heavy-duty numerical analysis, especially
  in case of multi-animal movement tracking in experiment videos.

- **Data Processing**

  Last but not the least, array manipulation - processing large stacks of
  arrays corresponding to various images, target tensors and keypoints is
  fairly challenging.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png'
title = 'Pose estimation variety and complexity'
alt = 'challengesfig'
align = 'center'
attribution = '(Source: Mackenzie Mathis)'
attributionlink = 'https://www.biorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## 姿勢推定の課題に対応するためのNumPyの役割

NumPy は DeepLabCutにおける、行動分析の高速化のための数値計算の核となっています。  Besides NumPy, DeepLabCut employs
various Python software that utilize NumPy at their core, such as
[SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org),
[matplotlib](https://matplotlib.org),
[Tensorpack](https://github.com/tensorpack/tensorpack),
[imgaug](https://github.com/aleju/imgaug),
[scikit-learn](https://scikit-learn.org/stable/),
[scikit-image](https://scikit-image.org) and
[Tensorflow](https://www.tensorflow.org).

以下に挙げるNumPyの特徴が、DeepLabCutの姿勢推定アルゴリズムでの画像処理・組み合わせ処理・高速計算において、重要な役割を果たしました。

- ベクトル化
- マスクされた配列操作
- 線形代数
- ランダムサンプリング
- 大きな配列の再構成

DeepLabCutは、ツールキットが提供するワークフローを通じてNumPyの配列機能を利用しています。 特に、NumPyはヒューマンアノテーションのラベル付けや、アノテーションの書き込み、編集、処理のために、特定のフレームをサンプリングするために使用されています。  TensorFlowを使ったニューラルネットワークは、DeepLabCutの技術によって何千回も訓練され、 フレームから真のアノテーション情報を予測します。 この目的のため、姿勢推定問題を画像-画像変換問題として変換する目標密度(スコアマップ) を作成します。 ニューラルネットワークのロバスト化のため、データの水増しを使用していますが、このためには幾何学・画像的処理を施したスコアマップの計算を行うことが必要になります。 また学習を高速化するため、NumPyのベクトル化機能が利用されています。 推論には、目標のスコアマップから最も可能性の高い予測値を抽出し、効率的に「予測値をリンクさせて個々の動物を組み立てる」ことが必要になります。

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png'
title = 'DeepLabCut Workflow'
alt = 'workflow'
attribution = '(Source: Mackenzie Mathis)'
attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## まとめ

行動を観察し、効率的に表現することは、現代倫理学、神経科学、医学、工学の根幹です。
[DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf)
allows researchers to estimate the pose of the subject, efficiently enabling
them to quantify the behavior. DeepLabCutというPythonツールボックスを使えば、わずかな学習画像のセットでニューラルネットワークを人間レベルのラベリング精度で学習することができ、実験室での行動分析だけでなく、スポーツ、歩行分析、医学、リハビリテーション研究などへの応用が可能になります。 DeepLabCutアルゴリズムに必要な複雑な組み合わせ処理やデータ処理の問題を、NumPyの配列操作機能が解決しています。

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
