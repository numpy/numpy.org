---
title: "ケーススタディ: DeepLabCut 三次元姿勢推定"
sidebar: false
---

{{< figure src="/images/content_images/cs/mice-hand.gif" class="fig-center" caption="**DeepLapCutを用いたマウスの手の動きの解析 **" alt="micehandanim" attr="*(Source: www.deeplabcut.org )*" attrlink="http://www.mousemotorlab.org/deeplabcut">}}

<blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/">
    <p>オープンソースソフトウェアは生体臨床医学を加速させています。 DeepLabCut を使用すると、Deep Learningを使用して動物の行動を自動的にビデオ解析することができます。</p>
    <footer align="right">—Alexander Mathis、 <cite>准教授、École polytechnology fe’rale de Lausanne <a href="https://www.epfl.ch/en/">(EPFL)</a></cite></footer>
</blockquote>

## DeepLabCut について

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) は世界中の何百もの研究機関の研究者が、ごくわずかなトレーニングデータで、人間レベルの精度で実験動物の行動を追跡可能にするオープンソースのツールボックスです。 DeepLabCutの技術により、科学者は動物の種類と時系列のデータを元に、運動制御と行動に関する科学的な理解を深めることができるようになりました。

神経科学、医学、生体力学などのいくつかの研究分野では、動物の動きを追跡したデータを使用しています。 DeepLabCut は、動画に記録された動きを解析することで、人間やその他の動物が何をしているのかを理解することができます。 タグ付けや監視などの、手間のかかる作業に自動化を利用し、深層学習ベースのデータ解析を実施します。DeepLabCut は、霊長類、マウス、魚、ハエなどの動物を観察する科学的研究に利用されており、より速く、正確な結果をもたらしました。

{{< figure src="/images/content_images/cs/race-hore. if" class="fig-center" caption="**色のついた点は競走馬の体の位置を追跡**" alt="horserideranim" attr="*(Source: Mackenzie Mathis)*">}}

DeepLabCutによる動物の姿勢を抽出することによる、非侵襲的な行動追跡は、生体力学や、遺伝学、倫理学、神経科学などの分野における科学的な研究に必要不可欠です。 動的に変化する背景の中で、動物の姿勢をビデオデータから非侵襲的に測定することは、計算処理的に非常に困難です。 例えば、必要な計算リソースやトレーニングデータが問題になります。

DeepLabCutは、研究者が対象の姿勢をを推定することができ、Pythonベースのソフトウェアを使って効率的に対象の行動を定量化することを可能にします。  DeepLabCutを使用すると、研究者は動画から異なるフレームを識別し、数十個のフレームの特定の身体部位にデジタルなラベルを貼ることができます。また、DeepLabCutのディープラーニングベースのポーズ推定アーキテクチャが、動画の残りの部分や動物の他の類似した動画から同じ特徴を抽出する方法を学習することもできます。 ハエやマウスなどの一般的な実験動物から [チーター][cheetah-movement]のようなより珍しい動物まで、動物の種類を問わず利用する事ができます。

DeepLabCut では [transfer learning](https://arxiv.org/pdf/1909.11229)という技術を使用しています。これにより必要な学習データの量を大幅に削減し、学習の収束を加速させることができます。  必要に応じて、より高速な推論を提供するさまざまなネットワークアーキテクチャ(MobileNetV2など)を選択することができ、リアルタイムの実験データフィードバックと組み合わせることもできます。 DeepLabCutはもともと、ツールの名前の元となった [DeeperCut](https://arxiv.org/abs/1605.03170)と呼ばれる、パフォーマンスの高い人像推定アーキテクチャからの特徴検出器を使用しています。 その過程で、このパッケージには、追加のアーキテクチャや、拡張メソッド、および一通りのフロントエンドユーザエクスペリエンスが得られるように大幅に変更されました。 さらに、 大規模な生物学的実験をサポートするために DeepLabCut はアクティブな学習機能を提供しています。例えば、エッジケースをカバーしたり、特定のコンテキスト内でポーズ推定アルゴリズムを堅牢にするために、時間経過しても学習データを増やすことができます。

最近、[DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo)が発表されました。これは、霊長類の顔分析から犬の姿勢まで、様々な種や実験条件に対応した事前訓練済みモデルを提供しています。 これにより、例えば、新しいデータのラベルを付けることなくクラウドで予測を実行することができたり、ニューラルネットワーク学習を実行することができます。また、プログラミング経験は必要ありません。

### 主な目標と結果

* **科学研究のための動物姿勢解析の自動化:**

  DeepLabCut 技術の主な目的は、多様な環境で動物の姿勢を測定し追跡することです。 このデータは、例えば、脳がどのように運動を制御しているかを理解するための神経科学の研究や、動物がどのように社会的に交流しているかを明らかにするために利用することができます。 研究者はDeepLabCutで [10倍のパフォーマンス向上](https://www.biorxiv.org/content/10.1101/457242v1) が可能であると発表しています。 オフラインでは最大1200フレーム/秒(FPS) で姿勢推定することができます。

* **姿勢推定のための使いやすいPythonツールキットの作成:**

  DeepLabCutは、動物の姿勢推定技術を研究者が簡単に利用できるツールとして共有したいという考えから開発されています。 そこでらはプロジェクト管理機能 を備えた、単独で機能し、使いやすいPythonツールボックスとしてこのツールを作成しました。 これにより、姿勢推定の自動化だけでなく、 データセット収集段階から共有可能て、再利用可能な分析パイプラインを作成するDeepLabCut Toolkitを提供し、プロジェクトのエンドツーエンドの管理も可能になりました。

  この[ツールキット][DLCToolkit] はオープンソースとして利用できます。

  DeepLabCut ワークフローは以下のようになります。

  - アクティブ学習によるトレーニングセットの作成と調整を行います
  - 特定の動物やシナリオに合わせたニューラルネットワークの構築
  - 動画における大規模推論のためのコード作成
  - 統合された可視化ツールを使用して推論の描画

{{< figure src="/images/content_images/cs/deeplabcut-toolkit-steps.png" class="csfigcaption" caption="**DeepLabCutによる姿勢推定のステップ**" alt="dlcsteps" align="middle" attr="(Source: DeepLabCut)" attrlink="https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1" >}}

### 課題

* **速度**

    Fast processing of animal behavior videos in order to measure their behavior and at the same time make scientific experiments more efficient, accurate. Extracting detailed animal poses for laboratory experiments, without markers, in dynamically changing backgrounds, can be challenging, both technically as well as in terms of resource needs and training data required. Coming up with a tool that is easy to use without the need for skills such as computer vision expertise that enables scientists to do research in more real-world contexts, is a non-trivial problem to solve.

* **Combinatorics**

    Combinatorics involves assembly and integration of movement of multiple limbs into individual animal behavior. Assembling keypoints and their connections into individual animal movements and linking them across time is a complex process that requires heavy-duty numerical analysis, especially in case of multi-animal movement tracking in experiment videos.

* **Data Processing**

    Last but not the least, array manipulation - processing large stacks of arrays corresponding to various images, target tensors and keypoints is fairly challenging.

{{< figure src="/images/content_images/cs/pose-estimation.png" class="csfigcaption" caption="**Pose estimation variety and complexity**" alt="challengesfig" align="middle" attr="(Source: Mackenzie Mathis)" attrlink="https://www.biorxiv.org/content/10.1101/476531v1.full.pdf" >}}

## NumPy's Role in meeting Pose Estimation Challenges

NumPy addresses DeepLabCut technology's core need of numerical computations at high speed for behavioural analytics.  Besides NumPy, DeepLabCut employs various Python software that utilize NumPy at their core, such as [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) and [Tensorflow](https://www.tensorflow.org).

The following features of NumPy played a key role in addressing the image processing, combinatorics requirements and need for fast computation in DeepLabCut pose estimation algorithms:

* Vectorization
* Masked Array Operations
* Linear Algebra
* Random Sampling
* Reshaping of large arrays

DeepLabCut utilizes NumPy’s array capabilities throughout the workflow offered by the toolkit. In particular, NumPy is used for sampling distinct frames for human annotation labeling, and for writing, editing and processing annotation data.  Within TensorFlow the neural network is trained by DeepLabCut technology over thousands of iterations to predict the ground truth annotations from frames. For this purpose, target densities (scoremaps) are created to cast pose estimation as a image-to-image translation problem. To make the neural networks robust, data augmentation is employed, which requires the calculation of target scoremaps subject to various geometric and image processing steps. To make training fast, NumPy’s vectorization capabilities are leveraged. For inference, the most likely predictions from target scoremaps need to extracted and one needs to efficiently “link predictions to assemble individual animals”.

{{< figure src="/images/content_images/cs/deeplabcut-workflow.png" class="fig-center" caption="**DeepLabCut Workflow**" alt="workflow" attr="*(Source: Mackenzie Mathis)*" attrlink="https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962">}}

## Summary

Observing and efficiently describing behavior is a core tenant of modern ethology, neuroscience, medicine, and technology. [DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf) allows researchers to estimate the pose of the subject, efficiently enabling them to quantify the behavior. With only a small set of training images, the DeepLabCut Python toolbox allows training a neural network to within human level labeling accuracy, thus expanding its application to not only behavior analysis in the laboratory, but to potentially also in sports, gait analysis, medicine and rehabilitation studies. Complex combinatorics, data processing challenges faced by DeepLabCut algorithms are addressed through the use of NumPy's array manipulation capabilities.

{{< figure src="/images/content_images/cs/numpy_dlc_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
