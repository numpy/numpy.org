---
title: "ケーススタディ：世界初のブラックホールの画像"
sidebar: false
---

{{< figure src="/images/content_images/cs/blackhole.jpg" caption="**Black Hole M87**" alt="black hole image" attr="*(Image Credits: Event Horizon Telescope Collaboration)*" attrk="https://www.jpl.nasa.gov/images/universe/90410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>M87ブラックホールを画像化することは、見ることのできないものを、あえて見ようとするようなものです。</p>
    <footer align="right"><cite>カリフォルニア工科大学 計算・数理学部</cite>のKatie Bouman助教授</footer>
</blockquote>

## 地球の大きさの望遠鏡。

[ Event Horizon telescope(EHT)](https:/eventhorizontelescope.org)は、地球サイズの解析望遠鏡を形成する8台の地上型電波望遠鏡から成るシステムで、これまでに前例のない感度と解像度で宇宙を研究することができます。  超長基線干渉法(VLBI) と呼ばれる手法を用いた巨大な仮想望遠鏡の角度分解能は、[20マイクロ秒][resolution]で、ニューヨークにある新聞をパリの歩道のカフェから読むのに十分な解像度です。

### 主な目標と結果

* **宇宙の新しい見方:** EHTの画期的な考え方の基礎が築かれたのは、100年前に [Sir Arthur Eddington][eddington] がアインシュタインの一般相対性理論に沿った最初の観測を実施したことが始まりでした。

* **ブラックホール:** EHTは、おとめ座銀河団のメシエ87銀河 (M87) の中心にある、地球から約5500万光年の距離にある超巨大ブラックホールを観測しました。 Its mass is 6.5 billion times the Sun's. It had been studied for [over 100 years](https://www.jpl.nasa.gov/news/news.php?feature=7385), but never before had a black hole been visually observed.

* **Comparing Observations to Theory:** From Einstein’s general theory of relativity, scientists expected to find a shadow-like region caused by gravitational bending and capture of light. Scientists could use it to measure the black hole's enormous mass.

### The Challenges

* **Computational scale**

    EHT poses massive data-processing challenges, including rapid atmospheric phase fluctuations, large recording bandwidth, and telescopes that are widely dissimilar and geographically dispersed.

* **Too much information**

    Each day EHT generates over 350 terabytes of observations, stored on helium-filled hard drives. Reducing the volume and complexity of this much data is enormously difficult.

* **Into the unknown**

    When the goal is to see something never before seen, how can scientists be confident the image is correct?

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**EHT Data Processing Pipeline**" alt="data pipeline" align="middle" attr="(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## NumPy’s Role

What if there's a problem with the data? Or perhaps an algorithm relies too heavily on a particular assumption. Will the image change drastically if a single parameter is changed?

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
