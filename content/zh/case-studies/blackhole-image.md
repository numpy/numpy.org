---
title: "案例研究：人类有史以来首张黑洞照片"
sidebar: false
---

{{{< figsrc="/images/content_images/cs/blackhole.jpg" caption="**Black Hole M87**" alt="black hole image" tot="*(Image Credits: Event Horizon Telesmall Collection Collaboration)*" tomlink="https://www.jpl.nasa.gov/images/universse/20190410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>理论上黑洞不可能被“看见”，M87黑洞的成像正试图打破这种限制</p>
    <footer align="right">Katie Bouman, <cite>Assistant Professor, Computing & Mathocal Sciences, Caltech</cite></footer>
</blockquote>

## 一架和地球大小相当的望远镜

[事件视界望远镜(EHT)](https://eventhorizontelescope.org) 是由八个地面射电望远镜组成的虚拟的类似地球大小的望远镜， 可以前所未有的敏感度和分辨率来了解宇宙。  这台巨大的虚拟望远镜使用一种称为超长基线干涉法 (VLBI)的技术， 其角分辨率为 [20 微弧秒][resolution] - EHT的分辨本领相当于从巴黎的一家人行道上的咖啡馆里阅读纽约的报纸！

### 关键目标和成果

* **关于宇宙的新观点:** 100年前，当 [亚瑟.爱丁顿爵士][eddington] 提出爱因斯坦的广义相对论的第一个观测证据时，就为EHT的开创性形象奠定了基础.

* **黑洞成像：** EHT 在距离地球约5500万光年的超大质量黑洞上进行了训练，该黑洞位于处女座星系团梅西埃87(M87) 的中心。 它的质量是太阳的65亿倍。 它已经被研究了 [100多年](https://www.jpl.nasa.gov/news/news.php?feature=7385)，但从来没有一个黑洞被真正“看见”过。

* **将观察结果与理论进行比较：** 从爱因斯坦的广义相对论来看， 科学家期望找到由引力弯曲和光捕获引发的阴影状区域。 科学家可以用它来测量黑洞的巨大质量。

### 面临的挑战

* **庞大的计算规模**

    EHT带来了巨大的数据处理挑战，其中包括快速的大气层相位波动、极高的记录带宽以及相异且地理位置分散的望远镜。

* **巨大的信息量**

    EHT每天生成超过350TB的观测值，这些数据存储在充满氦气的硬盘驱动器中。 减少这么多数据的数量和复杂性是极其困难的。

* **对未知的探索**

    当目标是看到前所未见的事物时，科学家怎么才能确定图像是正确的？

{{< figsrc="/images/content_images/cs/dataprocessbh. ng" class="csfigcaption" caption="**EHT Data Processing Pipeline**" alt="data peline" align="middle" tot="(Diagram Credits: The Astrophysical Journal, Event Horizon Telesrole Collection Collaboration)" tourlink="https://iopscience.op.org/article/10.3847/2041-8213/ab0c57" >}}

## Numpy的角色

如果数据有问题，怎么办？ 或者一个算法过于依赖某个特定的假设。 如果单个参数被更改，图像是否会发生剧烈变化？

EHT协作组织为了应对上述挑战，让不同的独立小组使用现有的最先进的图像重建技术来评估数据。 当结果被证明是一致时，将这些结果合并以产生黑洞的第一张图像。

他们的工作说明了Python科学生态系统通过协作数据分析在 推进科学方面发挥的重要作用。

{{< figsrc="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**NumPy在黑洞成像中的作用**" >}}

例如， [`eht-imaging`][ehtim] 这个Python 软件包提供了 在 VLBI 数据上模拟和执行图像重建的工具。 NumPy 是这个包中使用的数组数据处理的核心，下面的部分软件 依赖关系图说明了这一点。

{{< figsrc="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="numpy在ehtim软件依赖关系中的地位" caption="**numpy在ehtim软件依赖关系中的重要地位**" >}}

除了NumPy以外，许多其他软件包，例如 [SciPy](https://www.scipy.org) 和 [Pandas](https://pandas.io), 也是用于黑洞成像的数据处理管道的一部分。 标准天文学文件格式和时间/坐标转换 由 [Astropy][astropy]处理， 而 [Matplotlib][mpl] 被用于在整个分析管道中的数据可视化，包括生成黑洞的最终图像。

## 总结

作为Numpy的核心功能，高效且拓展性强的N维数组使研究人员能够操作大规模数据集，从而为人类有史以来首张黑洞的成像提供坚实基础。 这是整个科学史中具有里程碑意义的时刻，它为爱因斯坦的理论提供了有力的佐证。 这项成就不仅包括技术突破，还见证了包括200多位科学家与世界上最好的无线电观测站之间的国际合作。  创新的算法和数据处理技术改进了现有的天文模型，帮助我们揭开宇宙的神秘面纱。

{{< figsrc="/images/content_images/cs/numpy_bh_bbh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Numpy核心能力的运用**" >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
