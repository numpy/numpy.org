---
title: "案例研究：使用DeepLabCut预测动物行为"
sidebar: false
---

{{{< figure src="/images/content_images/cs/mice-hand.gif" class="fig-center" caption="**使用DeepLapCut**分析老鼠的手部姿势</strong> " alt="micehandanim" attr="*(来源: www.deeplabcut.org)*" attrlink="http://www.mousemotorlab.org/deeplabcut">}}

<blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/">
    <p>开源软件正在加速生物医学的发展。 DeepLabCut能够使用深度学习对动物行为进行自动视频分析。</p>
    <footer align="right">— — Alexander Mathis, <cite>洛桑联邦理工大学 <a href="https://www.epfl.ch/en/">(EPFL)</a>助理教授</cite></footer>
</blockquote>

## 关于 DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) 是一个开放源码工具箱，它使世界各地数以百计的研究人员能够在训练数据非常少的情况下跟踪实验室动物的行为，而且能达到人类水平的准确性。 借助DeepLabCut技术，科学家可以更深入更科学地了解不同动物在不同时间段对运动的控制和表现行为。

包括神经科学、医学和生物力学在内的若干研究领域都使用了跟踪动物运动的数据。 DeepLabCut通过解析电影上记录的动作，帮助了解人类和其他动物行为背后的内涵。 DeepLabCut将标记和监测的繁重工作自动化，同时进行基于神经网络的深度数据分析，使得涉及观察例如灵长类动物、小鼠、鱼类和苍蝇等动物行为的科学研究更快、更准确。

{{< figure src="/images/content_images/cs/race-horse.gif" class="fig-center" caption="**通过彩色标点跟踪赛马身体位置的变化**" alt="horserideranim" attr="*(资料来源：Mackenzie Mathis)*">}}

对于生物力学、遗传学、人类学和神经科学等领域的科学研究来说，DeepLabCut通过非侵入式手段提取动物姿势至关重要。 无论从技术层面还是从庞大的资源需求和训练集来看，不带标记非侵入式的从视频中检测动物的姿势，预测动物在动态变化背景下的行为表现对计算机都极具挑战。

DeepLabCut使研究人员能够通过基于 Python 的软件工具包有效地估计该实验对象的姿势，使他们能够对实验对象的行为进行量化。  借助DeepLabCut，研究人员可以从视频中识别出不同的帧，并使用量身定制的GUI数字标记数十个帧中的特定身体部位，然后DeepLabCut中基于深度学习的姿势估计架构将学习如何从剩余视频或类似动物行为的视频中提取出相同的特征。 这种方法适用于各种动物，从常见的苍蝇和老鼠等实验室动物到不常见到的[猎豹][cheetah-movement]等动物。

DeepLabCut使用一种称为 [转移学习](https://arxiv.org/pdf/1909.11229)的原理，大大减少了所需训练数据的规模，并加快了训练周期的收敛速度。  根据不同需求，用户可以选择不同的网络结构来获得更高性能的推理模型(例如MobileNetV2)，也可以将其与实时的实验反馈相结合。 DeepLabCut最初使用了一个名为[DeeperCut](https://arxiv.org/abs/1605.03170)的高性能人物姿势评估特征探测器, 这也是DeepLabCut这个名字的由来。 现在这套软件已经作了重大更新，包含支持更多架构、算子规模的扩大和全面的前端用户体验提升。 此外， 为了支持大规模生物实验，DeepLabCut提供了主动学习的能力，因此用户可以随着时间的推移增加训练集以覆盖边缘用例，并使他们的姿势估计算法在特定场景下变的更加强大。

最近，引入了 [DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo) ，它为不同物种和不同实验条件提供预训练的模型，从灵长类动物的面部分析到狗的姿势。 有了modelzoo之后，模型就可以在云端运行，而且不用给新数据贴上任何标签，也不需要神经网络训练，也不需要任何编程经验。

### 关键目标和成果

* **对动物行为进行自动化分析以供科学研究：**

  DeepLabCut技术的主要目标是在各种环境下测量和跟踪动物的姿势。 这些数据大有用处，比如可以用于神经科学研究以了解大脑是如何控制运动的，或者阐明动物是如何进行社交互动的。 研究人员观察到DeepLabCut的 [性能提升了10倍](https://www.biorxiv.org/content/10.1101/457242v1)。 可以在单机状态下以每秒1200多帧(FPS) 的速度推断出动物姿态。

* **创建一个易于使用的 Python 工具包用于姿态估计：**

  DeepLabCut想要以易于使用的工具的形式共享其动物姿态估计技术，使得研究人员可以轻松上手。 因此这个Python工具箱甚至包含有项目管理的功能。 通过帮助使用DeepLabCut工具集的用户打通从数据收集阶段到创建可共享可重用的数据分析流程，这样不仅实现了姿态估计的自动化，而且可以端到端的管理整个项目。

  他们的 [工具包][DLCToolkit] 现在已经完全开源了。

  典型的DeepLabCut 工作流包括：

  - 通过主动学习创建和完善训练集
  - 针对特定动物和场景创建量身定制的神经网络
  - 从视频中得到大规模推理所需的代码
  - 使用集成的可视化工具得出结论

{{{< figure src="/images/content_images/cs/deeplabcut-toolkit-steps.png" class="csfigcaption" caption="**DeepLabCut的姿态估计流程**" alt="dlcsteps" align="middle" attr="(来源: DeepLabCut)" attrlink="https://twitter.com/DeepLabCut/status/1198046918284210176/phot/1" >}}

### 面临的挑战

* **性能**

    在快速处理动物行为视频以测量其行为的同时提高科学实验的效率和精度。 无论从技术层面还是从庞大的资源需求和训练集来看，不带标记非侵入式的从视频中检测动物的姿势，预测动物在动态变化背景下的行为表现对计算性能都极具挑战。 需要提出一种易于使用的工具，但不依赖诸如计算机科学家的专业知识，也不需要在近乎真实的环境中进行研究，要达成这个目标不是一件容易的事儿。

* **组合学**

    组合学涉及到将多个肢体的运动姿势组装并整合到单个动物的行为中去。 将关键姿态及其联系与个体动物不同时段的不同动作整合起来是一个复杂的过程，需要进行繁琐的数值分析，尤其是在实验视频中捕捉多个动物行为的情况下。

* **数据处理**

    最后一点但是并非不重要的一点是对数组的处理-处理与各种图像、目标张量和关键点相对应的大型数组具有相当大的挑战性。

{{< figure src="/images/content_images/cs/pose-estimation.png"
           class="csfigcaption"
           caption="**姿势估计的复杂性和多样性**"
           alt="pose estimator"
           align="middle"
           attr="(来源: Mackenzie Mathis)"
           attrlink="https://www.biorxiv.org/content/10.1101/476531v1.full.pdf" >}}

## NumPy在应对姿态估计挑战中的角色

NumPy 解决了DeepLabCut技术对行为分析进行高性能数值计算的核心需求。  除了NumPy, DeepLabCut 还使用 各种以 NumPy 为核心的 Python 软件， 例如 [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [tensorpack](https://github.com/tensorpack/tensorpack), [imgig](https://github.com/aleju/imgaug), [sikit-learning](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) 和 [Tensorflow](https://www.tensorflow.org)

NumPy 的以下功能在图像处理、组合计算和高性能DeepLabCut 姿态预测算法等方面发挥了关键作用。

* 向量化
* Mask数组操作
* 线性代数
* 随机采样
* 大规模矩阵变形

DeepLabCut在工具包提供的整个工作流中都使用了NumPy 数组。 需要特别指出的是，为了方便手工注释标注，以及便于编写、编辑和处理这些标注，NumPy被广泛应用于对不同的图像帧进行采样。  DeepLabCut对TensorFlow中的神经网络进行了成千上万次迭代训练，以预测图像 帧中注释的准确性。 为了达成这个目标，需要创建一个目标分布图(得分地图) 将姿态预测问题投射为图像之间变换的问题。 采用数据增强技术可以让神经网络变的更健壮，这就需要对遵循各种几何和图像处理流程的目标积分图进行计算。 为了加快训练速度，NumPy 的向量化功能会被充分利用起来。 在推理阶段，目标积分图中最可能的预测结果会被提取出来，然后就可以有效地“将预测结果映射到某种具体的动物”。

{{< figure src="/images/content_images/cs/deeplabcut-workflow.png" class="fig-center" caption="**DeepLabCut工作流程**" alt="workflow" attr="*(资料来源：Mackenzie Mathis)*" attrlink="https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-lab-lab-the-lab-the-work-flow-as well-the-directory-and_fig1_329185962">}}

## 总结

对行为进行精确的观测和高效的描述是现代伦理学、神经科学、医学和技术的核心内容。 [DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf) 让研究人员预测实验对象的行为成为可能，从而高效量化动物行为。 DeepLabCut Python工具箱仅需少量训练图像就可以将神经网络训练达到人类水平的标注准确性，因此它的应用范围绝不局限于实验室的行为分析，而且还可以拓展到运动、步态分析、医学和康复研究中。 通过操作NumPy数组，可以解决DeepLabCut算法面临的复杂组合计算和数据处理难题。

{{< figure src="/images/content_images/cs/numpy_dlc_benefits.png" class="fig-center" alt="NumPy benefits" caption="**NumPy核心能力的运用**" >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
