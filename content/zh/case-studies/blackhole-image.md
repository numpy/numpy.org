---
title: 案例研究：人类有史以来首张黑洞照片
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/blackhole.jpg'
title = 'Black Hole M87'
alt = 'black hole image'
attribution = '(Image Credits: Event Horizon Telescope Collaboration)'
attributionlink = 'https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg'
{{< /figure >}}

{{< blockquote
cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
by="Katie Bouman, _Assistant Professor, Computing & Mathematical Sciences, Caltech_"

> }}
> Imaging the M87 Black Hole is like trying to see something that is by definition impossible to see.
> {{< /blockquote >}}

## 一架和地球大小相当的望远镜

The [Event Horizon telescope (EHT)](https://eventhorizontelescope.org) is an
array of eight ground-based radio telescopes forming a computational telescope
the size of the earth, studing the universe with unprecedented
sensitivity and resolution.  The huge virtual telescope,  which uses a technique
called very-long-baseline interferometry (VLBI), has an angular resolution of
[20 micro-arcseconds][resolution] — enough to read a newspaper in New York
from a sidewalk café in Paris!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### 关键目标和成果

- **A New View of the Universe:**
  The groundwork for the EHT's groundbreaking image had been laid 100 years
  earlier when [Sir Arthur Eddington][eddington] yielded the first
  observational support of Einstein's theory of general relativity.

- **The Black Hole:** EHT was trained on a supermassive black hole
  approximately 55 million light-years from Earth, lying at the center
  of the galaxy Messier 87 (M87) in the Virgo galaxy cluster. Its mass is
  6.5 billion times the Sun's. It had been studied for
  [over 100 years](https://www.jpl.nasa.gov/news/news.php?feature=7385), but never before
  had a black hole been visually observed.

- **Comparing Observations to Theory:** From Einstein’s general theory of
  relativity, scientists expected to find a shadow-like region caused by
  gravitational bending and capture of light. Scientists could
  use it to measure the black hole's enormous mass.

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

### 面临的挑战

- **Computational scale**

  EHT poses massive data-processing challenges, including rapid atmospheric
  phase fluctuations, large recording bandwidth, and telescopes that are
  widely dissimilar and geographically dispersed.

- **Too much information**

  Each day EHT generates over 350 terabytes of observations, stored on
  helium-filled hard drives. Reducing the volume and complexity of this much
  data is enormously difficult.

- **Into the unknown**

  When the goal is to see something never before seen, how can scientists be
  confident the image is correct?

{{< figure >}}
src = '/images/content_images/cs/dataprocessbh.png'
title = 'EHT Data Processing Pipeline'
alt = 'data pipeline'
align = 'center'
attribution = '(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)'
attributionlink = 'https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57'
{{< /figure >}}

## Numpy的角色

如果数据有问题，怎么办？ 或者一个算法过于依赖某个特定的假设。 如果单个参数被更改，图像是否会发生剧烈变化？

EHT协作组织为了应对上述挑战，让不同的独立小组使用现有的最先进的图像重建技术来评估数据。 当结果被证明是一致时，将这些结果合并以产生黑洞的第一张图像。

他们的工作说明了Python科学生态系统通过协作数据分析在
推进科学方面发挥的重要作用。

{{< figure >}}
src = '/images/content_images/cs/bh_numpy_role.png'
alt = 'role of numpy'
title = 'The role of NumPy in Black Hole imaging'
{{< /figure >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for
simulating and performing image reconstruction on VLBI data.
NumPy 是这个包中使用的数组数据处理的核心，下面的部分软件
依赖关系图说明了这一点。

{{< figure >}}
src = '/images/content_images/cs/ehtim_numpy.png'
alt = 'ehtim dependency map highlighting numpy'
title = 'Software dependency chart of ehtim package highlighting NumPy'
{{< /figure >}}

[ehtim]: https://github.com/achael/eht-imaging

Besides NumPy, many other packages, such as
[SciPy](https://www.scipy.org) and [Pandas](https://pandas.io), are part of the
data processing pipeline for imaging the black hole.
The standard astronomical file formats and time/coordinate transformations
were handled by [Astropy][astropy], while [Matplotlib][mpl] was used
in visualizing data throughout the analysis pipeline, including the generation
of the final image of the black hole.

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/

## 总结

作为Numpy的核心功能，高效且拓展性强的N维数组使研究人员能够操作大规模数据集，从而为人类有史以来首张黑洞的成像提供坚实基础。 这是整个科学史中具有里程碑意义的时刻，它为爱因斯坦的理论提供了有力的佐证。 这项成就不仅包括技术突破，还见证了包括200多位科学家与世界上最好的无线电观测站之间的国际合作。  创新的算法和数据处理技术改进了现有的天文模型，帮助我们揭开宇宙的神秘面纱。

{{< figure >}}
src = '/images/content_images/cs/numpy_bh_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
