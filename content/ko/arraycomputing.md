---
title: Array Computing
sidebar: false
---

_Array computing is the foundation of statistical, mathematical, scientific computing
in various contemporary data science and analytics applications such as data
visualization, digital signal processing, image processing, bioinformatics,
machine learning, AI, and several others._

대규모의 데이터의 조작과 연산은 고효율, 고성능의 행렬 연산에 달려있습니다. The language of choice for data analytics,
machine learning, and productive numerical computing is **Python.**

**Num**erical **Py**thon or NumPy is its de-facto standard Python programming
language library that supports large, multi-dimensional arrays and matrices,
and comes with a vast collection of high-level mathematical functions to
operate on these arrays.

2006년에 NumPy가 출시된 이후로, 2008년에 이를 기반으로 Pandas가 나타났습니다. 그리고 몇년전까지도, 다양한 행렬 연산 라이브러리가 잇따라 나오며 행렬 연산 분야가 더욱 활발해 졌습니다.
최신의 라이브러리들중 대부분은 NumPy 같은 특징과 성능을 품고, 새로운 알고리즘이나 머신러닝이나 인공지능 어플리케이션을 위한 특화된 기능을 포함하고 있습니다.

<img
src="/images/content_images/array_c_landscape.png"
alt="arraycl"
title="Array Computing Landscape">

**Array computing** is based on **arrays** data structures. _Arrays_ are used
to organize vast amounts of data such that a related set of values can be easily
sorted, searched, mathematically manipulated, and transformed easily and quickly.

Array computing is _unique_ as it involves operating on the data array _at
once_. 다시 말해서, 모든 행렬 연산은 전체 데이터에 한번에 적용됩니다. 이 벡터화 접근법은 행렬 연산을 위해 루프를 활용하여 개별적인 데이터에 접근하여 연산하는 코드를 작성하지 않고, 행렬에 바로 연산하는 코드를 작성하여, 개발자가 보다 개발 빠르고 간단하게 할수 있게 해줍니다.
