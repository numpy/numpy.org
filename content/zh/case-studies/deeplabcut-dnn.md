---
title: "案例研究：使用DeepLabCut预测动物行为"
sidebar: false
---

{{{< figsrc="/images/content_images/cs/mice-hand.gif" class="fig-center" caption="**使用DeepLapCut**分析老鼠的手部姿势</strong> " alt="micehandanim" tot="*(来源: www.deeplabcut.org)*" totlink="http://www.mousemotorlab.org/deeplabcut">}}

<blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/">
    <p>开源软件正在加速生物医学的发展。 DeepLabCut能够使用深度学习对动物行为进行自动视频分析。</p>
    <footer align="right">— — Alexander Mathis, <cite>洛桑联邦理工大学 <a href="https://www.epfl.ch/en/">(EPFL)</a>助理教授</cite></footer>
</blockquote>

## 关于 DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) 是一个开放源码工具箱，它使世界各地数以百计的研究人员能够在训练数据非常少的情况下跟踪实验室动物的行为，而且能达到人类水平的准确性。 借助DeepLabCut技术，科学家可以更深入更科学地了解不同动物在不同时间段对运动的控制和表现行为。

包括神经科学、医学和生物力学在内的若干研究领域都使用了跟踪动物运动的数据。 DeepLabCut通过解析电影上记录的动作，帮助了解人类和其他动物行为背后的内涵。 DeepLabCut将标记和监测的繁重工作自动化，同时进行基于神经网络的深度数据分析，使得涉及观察例如灵长类动物、小鼠、鱼类和苍蝇等动物行为的科学研究更快、更准确。

{{< figsrc="/images/content_images/cs/race-horse. gif" class="fig-center" caption="**通过彩色标点跟踪赛马身体位置的变化**" alt="horserideranim" totel="*(资料来源：Mackenzie Mathis)*">}}

对于生物力学、遗传学、人类学和神经科学等领域的科学研究来说，DeepLabCut通过非侵入式手段提取动物姿势至关重要。 无论从技术层面还是从庞大的资源需求和训练集来看，不带标记非侵入式的从视频中检测动物的姿势，预测动物在动态变化背景下的行为表现对计算机都极具挑战。

DeepLabCut使研究人员能够通过基于 Python 的软件工具包有效地估计该实验对象的姿势，使他们能够对实验对象的行为进行量化。  借助DeepLabCut，研究人员可以从视频中识别出不同的帧，并使用量身定制的GUI数字标记数十个帧中的特定身体部位，然后DeepLabCut中基于深度学习的姿势估计架构将学习如何从剩余视频或类似动物行为的视频中提取出相同的特征。 这种方法适用于各种动物，从常见的苍蝇和老鼠等实验室动物到不常见到的[猎豹][cheetah-movement]等动物。

DeepLabCut使用一种称为 [转移学习](https://arxiv.org/pdf/1909.11229)的原理，大大减少了所需训练数据的规模，并加快了训练周期的收敛速度。  根据不同需求，用户可以选择不同的网络结构来获得更高性能的推理模型(例如MobileNetV2)，也可以将其与实时的实验反馈相结合。 DeepLabCut最初使用了一个名为[DeeperCut](https://arxiv.org/abs/1605.03170)的高性能人物姿势评估特征探测器, 这也是DeepLabCut这个名字的由来。 现在这套软件已经作了重大更新，包含支持更多架构、算子规模的扩大和全面的前端用户体验提升。 此外， 为了支持大规模生物实验，DeepLabCut提供了主动学习的能力，因此用户可以随着时间的推移增加训练集以覆盖边缘用例，并使他们的姿势估计算法在特定场景下变的更加强大。

最近，引入了 [DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo) ，它为不同物种和不同实验条件提供预训练的模型，从灵长类动物的面部分析到狗的姿势。 有了modelzoo之后，模型就可以在云端运行，而且不用给新数据贴上任何标签，也不需要神经网络训练，也不需要任何编程经验。

### 关键目标和成果

* **对动物进行自动化分析以供科学研究：**

  DeepLabCut技术的主要目标是在各种环境下测量和跟踪动物的姿势。 This data can be used, for example, in neuroscience studies to understand how the brain controls movement, or to elucidate how animals socially interact. Researchers have observed a [tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1) with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second (FPS).

* **Creation of an easy-to-use Python toolkit for pose estimation:**

  DeepLabCut wanted to share their animal pose-estimation technology in the form of an easy to use tool that can be adopted by researchers easily. So they have created a complete, easy-to-use Python toolbox with project management features as well. These enable not only automation of pose-estimation but also managing the project end-to-end by helping the DeepLabCut Toolkit user right from the dataset collection stage to creating shareable and reusable analysis pipelines.

  Their [toolkit][DLCToolkit] is now available as open source.

  A typical DeepLabCut Workflow includes:

  - creation and refining of training sets via active learning
  - creation of tailored neural networks for specific animals and scenarios
  - code for large-scale inference on videos
  - draw inferences using integrated visualization tools

{{< figure src="/images/content_images/cs/deeplabcut-toolkit-steps.png" class="csfigcaption" caption="**Pose estimation steps with DeepLabCut**" alt="dlcsteps" align="middle" attr="(Source: DeepLabCut)" attrlink="https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1" >}}

### The Challenges

* **Speed**

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

[cheetah-movement]: https://www. technologynetworks. com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
