---
title: ケーススタディ：世界初のブラックホール画像
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
  by="{{< blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs" by="_カリフォルニア工科大学 計算・数理学部_のKatie Bouman助教授""
>}}
{{< /blockquote >}}

## 地球大の望遠鏡

[Event Horizon telescope(EHT)](https:/eventhorizontelescope.org)は、地球サイズの解析望遠鏡を形成する8台の地上型電波望遠鏡から成るシステムで、これまでに前例のない感度と解像度で宇宙を研究することができます。  超長基線干渉法(VLBI) と呼ばれる手法を用いた巨大な仮想望遠鏡の角度分解能は、[20マイクロ秒][resolution]で、ニューヨークにある新聞をパリの歩道のカフェから読むのに十分な解像度です!  The huge virtual telescope,  which uses a technique
called very-long-baseline interferometry (VLBI), has an angular resolution of
[20 micro-arcseconds][resolution] — enough to read a newspaper in New York
from a sidewalk café in Paris!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### 主な目標と結果

- **宇宙の新しい見方:** EHTの画期的な考え方の基礎が築かれたのは、100年前に [Sir Arthur Eddington][eddington]がアインシュタインの一般相対性理論に沿った最初の観測を実施したことが始まりでした。

- **ブラックホール:** EHTは、おとめ座銀河団のメシエ87銀河 (M87) の中心にある、地球から約5500万光年の距離にある超巨大ブラックホールを観測しました。 その質量は、太陽の65億倍です。 [100年以上](https://www.jpl.nasa.gov/news/news.php?feature=7385)に渡る研究が行われてもなお、これまでに視覚的にブラックホールを観測できたことはありませんでした。 Its mass is
  6.5 billion times the Sun's. It had been studied for
  [over 100 years](https://www.jpl.nasa.gov/news/news.php?feature=7385), but never before
  had a black hole been visually observed.

- **Comparing Observations to Theory:** From Einstein’s general theory of
  relativity, scientists expected to find a shadow-like region caused by
  gravitational bending and capture of light. **観測と理論の比較:** 科学者たちの間で、アインシュタインの一般相対性理論から、重力による光の曲げや光の捕獲による影のような領域が観測できるのではないかと期待されていました。 これはブラックホールの巨大な質量を測定するために利用することができます。

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

### 課題

- **大規模な計算**

  EHTは膨大なデータ処理の課題を抱えていました。 大気の位相変動は急速で、記録帯域の幅は大きく、望遠鏡はそれぞれ異なっていて地理的にも分散しています。

- **大量のデータ**

  EHTは一日で350テラバイトを超える観測データを生成し、ヘリウムで満たされたハードドライブに保存しています。 この大量のデータとデータの複雑さを軽減することは非常に難しいことです。 Reducing the volume and complexity of this much
  data is enormously difficult.

- **よくわからないものを観測する**

  今までに見たことのないものを見るのが研究の目標なら、どうやって科学者はその画像が正しいと確信することができるのでしょうか?

{{< figure >}}
{{< /figure >}}

## NumPyが果たした役割

データに問題がある場合はどうなるでしょう？ あるいは、アルゴリズムが特定の仮定に あまりにも大きく依存しているかもしれません。 もしあるパラメータを変更した場合、画像は大きく変化するのでしょうか？

EHTの共同研究では、最先端の画像再構成技術を使用して、それぞれのチームがデータを評価することによって、これらの課題に対処しました。 それぞれのチームの解析結果が同じであることが証明されると、それらの結果を組み合わせることで、ブラックホール画像を得ることができました。

彼らの研究は、共同のデータ解析を通じて科学を進歩させる、科学的なPythonエコシステムが果たす役割を如実に表しています。

{{< figure >}}
{{< /figure >}}

例えば、 [`eht-imaging`][ehtim] というPython パッケージは VLBI データで画像の再構築をシミュレートし、実行するためのツールです。 NumPyは、以下のソフトウェア依存関係チャートで示されているように、このパッケージで使用される配列データ処理の中核を担っています。
NumPyは、以下のソフトウェア依存関係チャートで示されているように、このパッケージで使用される配列データ処理の中核を担っています。

{{< figure >}}
{{< /figure >}}

[ehtim]: https://github.com/achael/eht-imaging

Besides NumPy, many other packages, such as
[SciPy](https://scipy.org) and [Pandas](https://pandas.pydata.org), are part of the
data processing pipeline for imaging the black hole.
NumPyだけでなく、[SciPy](https://www.scipy.org)や[Pandas](https://pandas.io)などのパッケージもブラックホール画像化におけるデータ処理パイプラインに利用されています。 天文学の標準的なファイル形式や時間/座標変換 は[Astropy][astropy]で実装され、ブラックホールの最終画像の生成を含め、解析パイプライン全体でのデータ可視化には [Matplotlib][mpl]が利用されました。

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/

## まとめ

NumPyの中心的な機能である、効率的で適用性の高いn次元配列は、研究者が大規模な数値データを操作することを可能にし、世界で初めてのブラックホールの画像化の基礎を築きました。 アインシュタインの理論に素晴らしい視覚的証拠を与えたのは、科学の画期的な瞬間だといえます。 この科学的に偉大な達成には、技術的の飛躍的な進歩だけでなく、200人以上の科学者と世界で 最高の電波観測所の間での国際協力も寄与しました。  革新的なアルゴリズムとデータ処理技術は、既存の天文学モデルを改良し、宇宙の謎を解き明かす助けになったといえます。

{{< figure >}}
{{< /figure >}}
