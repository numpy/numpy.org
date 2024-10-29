---
title: 案例研究：使用DeepLabCut预测动物行为
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
> Open Source Software is accelerating Biomedicine. DeepLabCut能够使用深度学习对动物行为进行自动视频分析。
> {{< /blockquote >}}

## 关于 DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) is an open source toolbox that empowers researchers at hundreds of institutions worldwide to track behaviour of laboratory animals, with very little training data, at human-level accuracy. 借助DeepLabCut技术，科学家可以更深入更科学地了解不同动物在不同时间段对运动的控制和表现行为。

包括神经科学、医学和生物力学在内的若干研究领域都使用了跟踪动物运动的数据。 DeepLabCut通过解析电影上记录的动作，帮助了解人类和其他动物行为背后的内涵。 DeepLabCut将标记和监测的繁重工作自动化，同时进行基于神经网络的深度数据分析，使得涉及观察例如灵长类动物、小鼠、鱼类和苍蝇等动物行为的科学研究更快、更准确。

{{< figure >}}
src = '/images/content_images/cs/race-horse.gif'
title = 'Colored dots track the positions of a racehorse’s body part'
alt = 'horserideranim'
attribution = '(Source: Mackenzie Mathis)'
{{< /figure >}}

DeepLabCut's non-invasive behavioral tracking of animals by extracting the poses of animals is crucial for scientific pursuits in domains such as biomechanics, genetics, ethology & neuroscience. 无论从技术层面还是从庞大的资源需求和训练集来看，不带标记非侵入式的从视频中检测动物的姿势，预测动物在动态变化背景下的行为表现对计算机都极具挑战。

DeepLabCut使研究人员能够通过基于 Python 的软件工具包有效地估计该实验对象的姿势，使他们能够对实验对象的行为进行量化。  借助DeepLabCut，研究人员可以从视频中识别出不同的帧，并使用量身定制的GUI数字标记数十个帧中的特定身体部位，然后DeepLabCut中基于深度学习的姿势估计架构将学习如何从剩余视频或类似动物行为的视频中提取出相同的特征。 It works across species of animals, from common laboratory animals such as flies and mice to more unusual animals like [cheetahs][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut uses a principle called [transfer learning](https://arxiv.org/pdf/1909.11229), which greatly reduces the amount of training data required and speeds up the convergence of the training period.  根据不同需求，用户可以选择不同的网络结构来获得更高性能的推理模型(例如MobileNetV2)，也可以将其与实时的实验反馈相结合。 DeepLabCut originally used the feature detectors from a top-performing human pose estimation architecture, called [DeeperCut](https://arxiv.org/abs/1605.03170), which inspired the name. 现在这套软件已经作了重大更新，包含支持更多架构、算子规模的扩大和全面的前端用户体验提升。 此外， 为了支持大规模生物实验，DeepLabCut提供了主动学习的能力，因此用户可以随着时间的推移增加训练集以覆盖边缘用例，并使他们的姿势估计算法在特定场景下变的更加强大。

Recently, the [DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo) was introduced, which provides pre-trained models for various species and experimental conditions from facial analysis in primates to dog posture. 有了modelzoo之后，模型就可以在云端运行，而且不用给新数据贴上任何标签，也不需要神经网络训练，也不需要任何编程经验。

### 关键目标和成果

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

  典型的DeepLabCut 工作流包括：

  - 通过主动学习创建和完善训练集
  - 针对特定动物和场景创建量身定制的神经网络
  - 从视频中得到大规模推理所需的代码
  - 使用集成的可视化工具得出结论

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png'
title = 'Pose estimation steps with DeepLabCut'
alt = 'dlcsteps'
align = 'center'
attribution = '(Source: DeepLabCut)'
attributionlink = 'https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1'
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### 面临的挑战

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

## Numpy在应对姿态估计挑战中的角色

NumPy 解决了DeepLabCut技术对行为分析进行高性能数值计算的核心需求。  Besides NumPy, DeepLabCut employs
various Python software that utilize NumPy at their core, such as
[SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org),
[matplotlib](https://matplotlib.org),
[Tensorpack](https://github.com/tensorpack/tensorpack),
[imgaug](https://github.com/aleju/imgaug),
[scikit-learn](https://scikit-learn.org/stable/),
[scikit-image](https://scikit-image.org) and
[Tensorflow](https://www.tensorflow.org).

NumPy 的以下功能在图像处理、组合计算和高性能DeepLabCut 姿态预测算法等方面发挥了关键作用。

- 向量化
- Mask数组操作
- 线性代数
- 随机采样
- 大规模矩阵变形

DeepLabCut在工具包提供的整个工作流中都使用了NumPy 数组。 需要特别指出的是，为了方便手工注释标注，以及便于编写、编辑和处理这些标注，Numpy被广泛应用于对不同的图像帧进行采样。  DeepLabCut对TensorFlow中的神经网络进行了成千上万次迭代训练，以预测图像
帧中注释的准确性。 为了达成这个目标，需要创建一个目标分布图(得分地图) 将姿态预测问题投射为图像之间变换的问题。 采用数据增强技术可以让神经网络变的更健壮，这就需要对遵循各种几何和图像处理流程的目标积分图进行计算。 为了加快训练速度，NumPy 的向量化功能会被充分利用起来。 在推理阶段，目标积分图中最可能的预测结果会被提取出来，然后就可以有效地“将预测结果映射到某种具体的动物”。

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png'
title = 'DeepLabCut Workflow'
alt = 'workflow'
attribution = '(Source: Mackenzie Mathis)'
attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## 总结

对行为进行精确的观测和高效的描述是现代伦理学、神经科学、医学和技术的核心内容。
[DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf)
allows researchers to estimate the pose of the subject, efficiently enabling
them to quantify the behavior. DeepLabCut Python工具箱仅需少量训练图像就可以将神经网络训练达到人类水平的标注准确性，因此它的应用范围绝不局限于实验室的行为分析，而且还可以拓展到运动、步态分析、医学和康复研究中。 通过操作Numpy数组，可以解决DeepLabCut算法面临的复杂组合计算和数据处理难题。

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
