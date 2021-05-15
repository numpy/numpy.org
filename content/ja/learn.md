---
title: Numpyの学び方
sidebar: false
---

**公式の Numpy ドキュメント** については [numpy.org/doc/stable](https://numpy.org/doc/stable) を参照してください。

## NumPy のチュートリアル

[Numpy のチュートリアル](https://numpy.org/numpy-tutorials) では、Numpy コミュニティによるチュートリアルや教材が手に入ります｡ このページの目標は、NumPy プロジェクトによる自己学習と授業のための高品質な教材を Jupyter Notebooks の形式で提供することです。 独自のコンテンツを追加したい場合は、GitHubの [numpy-tutorials リポジトリ](https://github.com/numpy/numpy-tutorials)を確認してください。

***

以下は、厳選された外部の教材です。 こちらのリストに貢献するには、 [このページの末尾](#add-to-this-list) を参照してください。

## 初学者向け

NumPyについての情報はたくさん見つかります。 初心者の方にはこちらの資料をお勧めします：

<i class="fas fa-chalkboard"></i> **チュートリアル**

* [NumPy Quickstart チュートリアル](https://numpy.org/devdocs/user/quickstart.html)
* [イラストで学ぶNumPy *by Lev Maximov*](https://betterprogramming.pub/3b1d4976de1d?sk=57b908a77aa44075a49293fa1631dd9b)
* [SciPyレクチャー](https://scipy-lectures.org/) NumPyだけでなく、科学Pythonソフトウェアのエコシステムを広く紹介しています。
* [Numpy初心者のための基礎](https://numpy.org/devdocs/user/absolute_beginners.html)
* [機械学習プラス - ndarray入門](https://www.machinelearningplus.com/python/numpy-tutorial-part1-array-python-examples/)
* [Edureka - 例題で学ぶ NumPy配列 ](https://www.edureka.co/blog/python-numpy-tutorial/)
* [Dataquest - NumPyチュートリアル: Python を使ったデータ解析](https://www.dataquest.io/blog/numpy-tutorial-python/)
* [Numpy チュートリアル *by Nicolas Rougier*](https://github.com/rougier/numpy-tutorial)
* [スタンフォード大学 CS231 *by Justin Johnson*](http://cs231n.github.io/python-numpy-tutorial/)
* [Numpyユーザーガイド](https://numpy.org/devdocs)

<i class="fas fa-book"></i> **書籍**

* [NumPガイド*by Travelis E. Oliphant*](http://web.mit.edu/dvp/Public/numpybook.pdf) これは2006年の無料版の初版です 最新版(2015年)については、こちら [を参照ください](https://www.barnesandnoble.com/w/guide-to-numpy-travis-e-oliphant-phd/1122853007).
* [PythonからNumPyまで*by Nicolas P. Rougier*](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)
* [エレガントなSciPy](https://www.amazon.com/Elegant-SciPy-Art-Scientific-Python/dp/1491922877) *by Juan Nunez-Iglesias, Stefan van der Walt, and Harriet Dashnow*

また、PythonとSciPyを題材にした [おすすめリスト](https://www.goodreads.com/shelf/show/python-scipy) もチェックしてみてください。 ほとんどの書籍ではNumPyを核とした「SciPyエコシステム」が説明されています。

<i class="far fa-file-video"></i> **動画**

* [Numpy を使った数値計算入門](http://youtu.be/ZB7BZMhfPgk) *by Alex Chabot-Leclerc*

***

## 上級者向け

インデックス処理、分割、スタック、線形代数などのより高度なNumpy の概念を、より深く理解するためには、これらの資料が参考になると思います。

<i class="fas fa-chalkboard"></i> **チュートリアル**

* [NumPy 100演習](http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html) *Nicolas P. Rougier*
* [NumPyとSciPyイントロダクション](https://engineering.ucsb.edu/~shell/che210d/numpy.pdf) *by M. Scott Shell*
* [Numpy救急キット](http://mentat.za.net/numpy/numpy_advanced_slides/) *by Stéfan van der Walt*
* [PythonにおけるNumPy (発展編)](https://www.geeksforgeeks.org/numpy-python-set-2-advanced/)
* [高度なインデックシング](https://www.tutorialspoint.com/numpy/numpy_advanced_indexing.htm)
* [NumPy による機械学習とデータ分析](https://www.machinelearningplus.com/python/numpy-tutorial-python-part2/)

<i class="fas fa-book"></i> **書籍**

* [Pythonデータサイエンスハンドブック](https://www.amazon.com/Python-Data-Science-Handbook-Essential/dp/1491912057) *by Jake Vanderplas*
* [Pythonデータ解析](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662) *by Wes McKinney*
* [数値解析Python: Numpy, SciPy, Matplotlibによる数値計算とデータサイエンスアプリケーション](https://www.amazon.com/Numerical-Python-Scientific-Applications-Matplotlib/dp/1484242459) *by Robert Johansson*

<i class="far fa-file-video"></i> **動画**

* [アドバンスドNumPy -](https://www.youtube.com/watch?v=cYugp9IN1-Q) *ブロードキャストルール、ストライド、および高度なインデックシング* by Fan Nunuz-Iglesias
* [NumPy配列における高度なインデクシング処理](https://www.youtube.com/watch?v=2WTDrSkQBng) *by Amuls Academy*

***

## NumPyに関する講演

* [Numpy Indexing の未来](https://www.youtube.com/watch?v=o0EacbIbf58) *by Jaime Fernadez* (2016)
* [Python における配列計算革命](https://www.youtube.com/watch?v=HVLPJnvInzM&t=10s) *by Ralf Gommers* (2019)
* [Numpy: 何が変わり、そして何が今後変わるのか?](https://www.youtube.com/watch?v=YFLVQFjRmPY) *by Matti Picus* (2019)
* [NumPyの内部](https://www.youtube.com/watch?v=dBTJD_FDVjU) *by Ralf Gommers, Sebastian Berg, Matti Picus, Tyler Reddy, Stefan van der Walt, Charles Harris* (2019)
* [Python における配列計算の概要](https://www.youtube.com/watch?v=f176j2g2eNc) *by Travis Oliphant* (2019)

***

## NumPy を引用する場合

もし、あなたの研究においてNumPyが重要な役割を果たし、あなたの論文でNumPyについて言及したい場合は、こちらの[ページ](/citing-numpy)を参照して下さい。

## このページへの貢献

<a name="add-to-this-list"></a>
このページのリストに新しいリンクを追加するには、[プルリクエスト](https://github.com/numpy/numpy.org/blob/master/content/en/learn.md)を使って提案してみて下さい。 PRでは、あなたが推薦する資料が、なぜこのページで言及に値するのか、そして誰がその資料によって最も利益を得るかを説明して下さい。
