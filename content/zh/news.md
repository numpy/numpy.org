---
title: 社区快讯
sidebar: false
---

### 2020 Numpy调研结果出炉

_22, 2021_ -- 2020, NumPy调研小组与密歇根大学和马里兰大学的学生和教职员工合作，进行了第一次官方NumPy社区调查。 在这里可以查看调查结果：https://numpy.org/user-survey-2020/。


### NumPy 1.20.0 发布

_2021年1月30日_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) 正式发布。 这是 NumPy到目前为止最大的一次版本更新，感谢社区的180+贡献者。 最令人振奋的两个新特性是：
- Numpy的大部分代码都做了类型注解，添加了一个全新的包含 `ArrayLike` 和 `DtypeLike`别名系统的 `numpy.typing` 子模块，使得用户和下游依赖库可以在自己的代码中添加类型注解。
- 新增多架构SIMD编译优化框架，同时支持X86(SSE、AVX)、ARM64(Neon) 和PowerPC(VSX) 指令集。 大大提高了许多函数的性能(例如： [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194))。

### NumPy项目的多样性

_2020年9月20日_ -- 我们就NumPy项目中的多样性和包容性的现状以及社交媒体相关的讨论写了一份[声明](/diversity_sep2020)


### 在Nature中发表的第一篇官方的NumPy论文！

_2020年9月16日_ - 我们高兴地宣布 [Numpy的第一篇官方论文](https://www.nature.com/articles/s41586-020-2649-2)刊登在自然杂志的评论文章。 这距离NumPy 1.0发布已经过去了整整14年。 该论文涵盖数组编程的应用和基本概念，丰富的Python科学计算生态系统建立在NumPy之上，包括最近添加的数组标准协议，大大提高了与外部数组和张量库(如CuPy, Dask 和 JAX) 的互操作性 。


### Python 3.9 即将来临，新版本的NumPy 何时发布？

_2020年9月14日_ -- Python 3.9 将在几周后发布。 如果您是这个Python版本的忠实拥趸， 您可能会失望的发现NumPy(以及其他二进制软件包，如SciPy) 在Python新版发布后数天内不会有版本发布。 使构建基础设施兼容新的 Python 版本需要付出重大努力，通常需要几周时间才能让包出现在 PyPI 和 conda-forge 上。 为了准备这次重大事件得以顺利进行，请确保：
- 将您的 `pip` 升级到 20.1 版本，至少要支持`manylinux2010` 和 `manylinux2014`
- 使用 [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) 或 `--only-binary=:all:` 选项来防止 `pip` 从源码构建的尝试。


### NumPy 1.19.2 发布

_2020年9月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) 正式发布。 这个最新版本修复了1.19 系列中的几个漏洞，为 [即将发布的Cython3.x](http://docs.cython.org/en/latest/src/changes.html) 和 pins安装工具做好准备，以确保正在进行上游修改时用户仍然可以正常安装运行。 The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

### The inaugural NumPy survey is live!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. The survey is available in 8 additional languages besides English: Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey [here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy 有新logo了!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught for the old logo that served us well for 15+ years.


### NumPy 1.19.0 release

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### Season of Docs acceptance

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 发布

_Decc 22, 2019_ -- NumPy 1.18.0 现在可用了。 After the major changes in 1.17.0, this is a consolidation release. 这是最后一个支持 Python 3.5小版本。 该版本的重要更新包括两个，添加了与64位 BLAS 和 LAPACK 库有关的底层更新， 添加 一个用于`numpy.random`的新C-API更新。

详情请看 [版本说明](https://github.com/numpy/numpy/releases/tag/v1.18.0)。


### NumPy receives a grant from the Chan Zuckerberg Initiative

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## 版本发布

这是NumPy 版本列表，包含了对应版本发布说明的链接。 所有的 bug修复版本(即在 `x.y.z`格式版本号中只有 `z`改变)没有新功能；小版本更新(`y` 改变)有新功能。

- NumPy 1.18.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 May 2020_.
- NumPy 1.18.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.3)) -- _19 Apr 2020_.
- NumPy 1.18.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _17 Mar 2020_.
- NumPy 1.18.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _6 Jan 2020_.
- NumPy 1.17.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 Jan 2020_.
- NumPy 1.18.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 Dec 2019_.
- NumPy 1.17.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _11 Nov 2019_.
- NumPy 1.17.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 Jul 2019_.
- NumPy 1.16.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 Jan 2019_.
- NumPy 1.15.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 Jul 2018_.
- NumPy 1.14.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 Jan 2018_.
