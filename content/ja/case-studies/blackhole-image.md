---
title: ケーススタディ：世界初のブラックホールの画像
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

## 地球の大きさの望遠鏡。

The [Event Horizon telescope (EHT)](https://eventhorizontelescope.org) is an
array of eight ground-based radio telescopes forming a computational telescope
the size of the earth, studing the universe with unprecedented
sensitivity and resolution.  The huge virtual telescope,  which uses a technique
called very-long-baseline interferometry (VLBI), has an angular resolution of
[20 micro-arcseconds][resolution] — enough to read a newspaper in New York
from a sidewalk café in Paris!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### 主な目標と結果

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

### 課題

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

## NumPyが果たした役割

データに問題がある場合はどうなるでしょう？ あるいは、アルゴリズムが特定の仮定に あまりにも大きく依存しているかもしれません。 もしあるパラメータを変更した場合、画像は大きく変化するのでしょうか？

EHTの共同研究では、最先端の画像再構成技術を使用して、それぞれのチームがデータを評価することによって、これらの課題に対処しました。 それぞれのチームの解析結果が同じであることが証明されると、それらの結果を組み合わせることで、ブラックホール画像を得ることができました。

彼らの研究は、共同のデータ解析を通じて科学を進歩させる、科学的なPythonエコシステムが果たす役割を如実に表しています。

{{< figure >}}
src = '/images/content_images/cs/bh_numpy_role.png'
alt = 'role of numpy'
title = 'The role of NumPy in Black Hole imaging'
{{< /figure >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for
simulating and performing image reconstruction on VLBI data.
NumPyは、以下のソフトウェア依存関係チャートで示されているように、このパッケージで使用される配列データ処理の中核を担っています。

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

## まとめ

NumPyの中心的な機能である、効率的で適用性の高いn次元配列は、研究者が大規模な数値データを操作することを可能にし、世界で初めてのブラックホールの画像化の基礎を築きました。 アインシュタインの理論に素晴らしい視覚的証拠を与えたのは、科学の画期的な瞬間だといえます。 この科学的に偉大な達成には、技術的の飛躍的な進歩だけでなく、200人以上の科学者と世界で 最高の電波観測所の間での国際協力も寄与しました。  革新的なアルゴリズムとデータ処理技術は、既存の天文学モデルを改良し、宇宙の謎を解き明かす助けになったといえます。

{{< figure >}}
src = '/images/content_images/cs/numpy_bh_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
