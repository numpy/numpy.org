---
title: "案例研究：人类有史以来首张黑洞照片"
sidebar: false
---

{{{< figsrc="/images/content_images/cs/blackhole.jpg" caption="**Black Hole M87**" alt="black hole image" tot="*(Image Credits: Event Horizon Telesmall Collection Collaboration)*" tomlink="https://www.jpl.nasa.gov/images/universse/20190410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>理论上黑洞是不可能被“看见”，M87黑洞的成像正试图打破这种限制</p>
    <footer align="right">Katie Bouman, <cite>Assistant Professor, Computing & Mathocal Sciences, Caltech</cite></footer>
</blockquote>

## 一架和地球大小相当的望远镜

[事件视界望远镜(EHT)](https://eventhorizontelescope.org) 是由八个地面射电望远镜组成的虚拟的类似地球大小的望远镜， 可以前所未有的敏感度和分辨率来了解宇宙。  这台巨大的虚拟望远镜使用一种称为超长基线干涉法 (VLBI)的技术， 其角分辨率为 [20 微弧秒][resolution] - EHT的分辨本领相当于从巴黎的一家人行道上的咖啡馆里阅读纽约的报纸！

### 关键目标和成果

* **关于宇宙的新观点:** 100年前，当 [亚瑟.爱丁顿爵士][eddington] 提出爱因斯坦的广义相对论的第一个观测证据时，就为EHT的开创性形象奠定了基础.

* **黑洞成像：** EHT 在距离地球约5500万光年的超大质量黑洞上进行了训练，该黑洞位于处女座星系团梅西埃87(M87) 的中心。 它的质量是太阳的65亿倍。 它已经被研究了 [100多年](https://www.jpl.nasa.gov/news/news.php?feature=7385)，但从来没有一个黑洞被真正“看见”过。

* **将观察结果与理论进行比较：** 从爱因斯坦的广义相对论来看， 科学家期望找到由引力弯曲和光捕获引发的阴影状区域。 科学家可以用它来测量黑洞的巨大质量。

### 面临的挑战

* **计算规模**

    EHT带来了巨大的数据处理挑战，其中包括快速的大气层相位波动、极高的记录带宽以及相异且地理位置分散的望远镜。

* **巨大的信息量**

    EHT每天生成超过350TB的观测值，这些数据存储在充满氦气的硬盘驱动器中。 减少这么多数据的数量和复杂性是极其困难的。

* **探索未知**

    当目标是看到前所未见的事物时，科学家怎么才能确定图像是正确的？

{{< figsrc="/images/content_images/cs/dataprocessbh. ng" class="csfigcaption" caption="**EHT Data Processing Pipeline**" alt="data peline" align="middle" tot="(Diagram Credits: The Astrophysical Journal, Event Horizon Telesrole Collection Collaboration)" tourlink="https://iopscience.op.org/article/10.3847/2041-8213/ab0c57" >}}

## Numpy的角色

如果数据有问题，怎么办？ 或者一个算法过于依赖某个特定的假设。 如果单个参数被更改，图像是否会发生剧烈变化？

The EHT collaboration met these challenges by having independent teams evaluate the data, using both established and cutting-edge image reconstruction techniques. When results proved consistent, they were combined to yield the first-of-a-kind image of the black hole.

Their work illustrates the role the scientific Python ecosystem plays in advancing science through collaborative data analysis.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**The role of NumPy in Black Hole imaging**" >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for simulating and performing image reconstruction on VLBI data. NumPy is at the core of array data processing used in this package, as illustrated by the partial software dependency chart below.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Software dependency chart of ehtim package highlighting NumPy**" >}}

Besides NumPy, many other packages, such as [SciPy](https://www.scipy.org) and [Pandas](https://pandas.io), are part of the data processing pipeline for imaging the black hole. The standard astronomical file formats and time/coordinate transformations were handled by [Astropy][astropy], while [Matplotlib][mpl] was used in visualizing data throughout the analysis pipeline, including the generation of the final image of the black hole.

## Summary

The efficient and adaptable n-dimensional array that is NumPy's central feature enabled researchers to manipulate large numerical datasets, providing a foundation for the first-ever image of a black hole. A landmark moment in science, it gives stunning visual evidence of Einstein’s theory. The achievement encompasses not only technological breakthroughs but also international collaboration among over 200 scientists and some of the world's best radio observatories.  Innovative algorithms and data processing techniques, improving upon existing astronomical models, helped unfold a mystery of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
