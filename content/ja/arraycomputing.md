---
title: 配列演算
sidebar: false
---

*Array computing is the foundation of statistical, mathematical, scientific computing in various contemporary data science and analytics applications such as data visualization, digital signal processing, image processing, bioinformatics, machine learning, AI, and several others.*

大規模なデータ処理やデータ変換には、効率的な配列演算が重要です。 データ分析や、機械学習、効率的な数値計算に最適な言語のひとつは **Python** です。

**Num**erical **Py**thon: NumPyは、Pythonにおけるデファクトスタンダードなライブラリであり、大規模な多次元配列や行列、そして、それらの配列を処理する様々な分野の数学ルーチンをサポートしています。

2006年にNumPyが発表されてから、2008年にPandasが登場し、その後、数年間にいくつかの配列演算関連のライブラリが次々と現れるようになりました。 これらの新しい配列演算ライブラリの多くは、NumPyの機能や能力を模倣しており、機械学習や人工知能向けの新しいアルゴリズムや機能を持っています。

<img
  src="/images/content_images/array_c_landscape.png"
  alt="arraycl"
  title="配列演算の概略" />

**配列演算** は **配列** のデータ構造に基づいています。 *配列* は、関連する膨大なデータ群を簡単にかつ高速に、ソート、検索、変換、数学処理できるように構成されています。

配列演算は *一度に* 配列のデータの複数の要素を操作するため、 * ユニーク* な処理と言えます。 これは、配列操作が一回の処理で、配列内の 全ての値に適用されることを意味しています。 このベクトル化手法は、速さと単純さという恩恵をもたらします。 プログラマーはループを回して個々の要素のスカラー演算を行うことなく、データの集合を操作しコーディングすることができるのです。
