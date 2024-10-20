---
title: "案例研究：人类有史以来首张黑洞照片"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/blackhole.jpg' title = 'Black Hole M87' alt = 'black hole image' attribution = '(Image Credits: Event Horizon Telescope Collaboration)' attributionlink = 'https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg'
{{< /figure >}}

{{< blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs" by="Katie Bouman, *Assistant Professor, Computing & Mathematical Sciences, Caltech*"
> }} 从理论上说黑洞不可能被“看见”，但是M87黑洞的成像实验正试图打破这种限制。 
> 
> {{< /blockquote >}}

## 一架和地球大小相当的望远镜

[视界望远镜(EHT)](https://eventhorizontelescope.org) 由八个地面射电望远镜组成，模拟的类似地球大小的望远镜， 其对宇宙的观测具有前所未有的敏感度和分辨率。  这台巨大的虚拟望远镜使用一种称为超长基线干涉法 (VLBI)的技术， 其角分辨率为 [20 微弧秒][resolution] —— EHT的分辨能力相当于能够在巴黎的一家人行道上的咖啡馆里阅读位于纽约的报纸！

### 主要目标和成果

* **关于宇宙的新观点:** 100年前，当 [亚瑟.爱丁顿爵士][eddington] 提出爱因斯坦的广义相对论的第一个观测证据时，就为EHT的开创性进步奠定了基础。

* **黑洞成像：** EHT 针对距离地球约5500万光年的超大质量黑洞上进行了训练，该黑洞位于处女座M87(Messier 87) 星系团的中心。 它的质量是太阳的65亿倍。 它已经被研究了 [100多年](https://www.jpl.nasa.gov/news/news.php?feature=7385)，但从来没有一个黑洞被真正视觉上“看见”过。

* **将观察结果与理论比较：** 根据爱因斯坦广义相对论， 科学家期望找到由引力弯曲和光捕获引发的阴影状区域。 科学家可以用它来测量黑洞巨大的质量。

### 面临的挑战

* **庞大的计算规模**

    EHT带来了巨大的数据处理挑战，其中包括快速的大气层相位波动、极高的记录带宽以及相异且地理位置分散的望远镜。

* **巨大的信息量**

    EHT每天生成超过350TB的观测值，这些数据存储在充满氦气的硬盘驱动器中。 在这么大的数据集上减少规模和复杂度是极其困难的。

* **对未知的探索**

    当目标是看到前所未见的事物时，科学家怎么才能确定图像是正确的？

{{< figure >}}
src = '/images/content_images/cs/dataprocessbh.png' title = 'EHT Data Processing Pipeline' alt = 'data pipeline' align = 'center' attribution = '(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)' attributionlink = 'https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57'
{{< /figure >}}

## Numpy的在其中的作用

如果数据有问题，怎么办？ 或者如果一个算法过于依赖某个特定的假设， 如果单个参数被更改，图像是否会发生剧烈变化？

EHT协作组织为了应对上述挑战，让不同的独立小组使用现有的最先进的图像重建技术来评估数据。 当结果被证明是一致时，将这些结果合并以产生黑洞的第一张图像。

他们的工作说明了Python科学计算生态系统在通过数据分析推进科学方面发挥的重要作用。

{{< figure >}}
src = '/images/content_images/cs/bh_numpy_role.png' alt = 'role of numpy' title = 'The role of NumPy in Black Hole imaging'
{{< /figure >}}

例如， [`eht-imaging`][ehtim] 软件包提供了在 VLBI 数据上模拟和执行图像重建的工具。 NumPy 是此包中数组数据处理工具的核心，下面的部分软件 依赖图说明了这一点。

{{< figure >}}
src = '/images/content_images/cs/ehtim_numpy.png' alt = 'ehtim dependency map highlighting numpy' title = 'Software dependency chart of ehtim package highlighting NumPy'
{{< /figure >}}

除了NumPy以外，许多其他软件包，例如 [SciPy](https://www.scipy.org) 和 [Pandas](https://pandas.io), 也是黑洞成像的数据处理流程的一部分。 标准天文学文件格式和时间/坐标转换 由 [Astropy][astropy]处理， 而 [Matplotlib][mpl] 被用于在整个分析管道中的数据可视化，包括生成黑洞的最终图像。

## 总结

作为Numpy的核心功能，高效且拓展性强的N维数组使研究人员能够操作大规模数据集，从而为人类有史以来首张黑洞的成像提供坚实基础。 这是整个科学史上的里程碑，它为爱因斯坦的理论提供了有力的佐证。 这项成就不仅代表着技术的突破，还见证了包括200多位科学家与世界上最好的无线电观测站之间的国际合作。  创新的算法和数据处理技术改进了现有的天文模型，帮助我们揭开宇宙的神秘面纱。

{{< figure >}}
src = '/images/content_images/cs/numpy_bh_benefits.png' alt = 'numpy benefits' title = 'Key NumPy Capabilities utilized'
{{< /figure >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
