---
title: 社区快讯
sidebar: false
---

### 2021 Numpy调查

_2021年7月12日_ -- 我们相信NumPy社区的力量。 来自75个国家的1236 名用户参加了我们去年的首次调查。 调查结果使我们对今后12个月应该集中注意的问题有了很好的了解。

现在是时候进行另一次调查了，我们将再度尋求您的合作。 这份调查将耗费您大约15分钟的时间。 除英文外，调查问卷还提供另外8种语文：孟加拉语、法语、印地语、日语、普通话、葡萄牙语、俄语和西班牙语。

点击链接开始：https://berkeley.qualtrics.com/jfe/form/SV_aOONjgcBXDSl4q。


### NumPy 1.21.0 发布

_2021年6月23日_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) 正式发布。 此次发布的重点是：

- 继续开展SIMD工作，涵盖更多的功能和平台
- 新dtype的基础和型态转换初步工作
- 适用于Mac平台的Python 3.8和Python 3.9的universal2 wheels
- 改进文档
- 改进注释
- 新的 `PCG64DXSM` 位元生成器，用于生成随机数字

这个NumPy版本包含175人所贡献的581个合并请求。 此发布版本支持Python 3.7-3.9，将在Python 3.10发布后添加Python 3.10支持。


### 2020 Numpy调研结果出炉

_2021年6月22日_ -- 在2020年, NumPy调研小组与密歇根大学和马里兰大学的学生和教职员工合作，进行了第一次官方NumPy社区调查。 在这里可以查看调研结果：https://numpy.org/user-survey-2020/。


### NumPy 1.20.0 发布

_2021年1月30日_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) 正式发布。 这是 NumPy到目前为止最大的一次版本更新，感谢180+位贡献者。 最令人振奋的两个特点是：
- 为大部分Numpy代码做了类型注解，並添加了一个全新的`numpy.typing` 子模块，其中包含 `ArrayLike` 和 `DtypeLike`别名 ，使得用户和下游依赖库可以为自己的代码添加类型注解。
- 为多个架构进行SIMD编译优化，其支持X86(SSE、AVX)、ARM64(Neon) 和PowerPC(VSX) 指令集。 大幅提高许多函数的性能(例如： [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194))。

### NumPy项目的多样性

_2020年9月20日_ -- 我们就NumPy项目的社交媒体、多样性和包容性的现状以及相关的讨论撰写了一份[声明](/diversity_sep2020)。


### NumPy官方第一次在Nature发表论文！

_2020年9月16日_ - 我们高兴地宣布 [Numpy的第一篇官方论文](https://www.nature.com/articles/s41586-020-2649-2)刊登在Nature的评论文章。 这离NumPy 1.0发布已经过去了整整14年。 该论文涵盖数组编程的应用和基本概念，丰富的Python科学计算生态系统建立在NumPy之上，包括最近添加的数组标准协议，大大提高了与外部数组和张量库(如CuPy, Dask 和 JAX) 的互操作性 。


### Python 3.9 即将来临，新版本的NumPy 将在何时发布？

_2020年9月14日_ -- Python 3.9 将在几周后发布。 如果您是这个Python版本的早期采用者， 您可能会失望的发现NumPy(以及其他二进制软件包，如SciPy) 在Python新版发布当天还不会发布相应的版本。 构建兼容新的 Python 版本的基础设施需要付出重大努力，通常需要几周时间才能让新版本出现在 PyPI 和 conda-forge 上。 为了这次版本升级得以顺利进行，请确保：
- 将您的 `pip` 升级到 20.1 版本，至少要支持`manylinux2010` 和 `manylinux2014`
- 使用 [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) 或 `--only-binary=:all:` 选项来防止 `pip` 尝试从源码构建。


### NumPy 1.19.2 发布

_2020年9月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) 正式发布。 这个最新版本修复了1.19 系列中的几个漏洞，为 [即将发布的Cython3.x](http://docs.cython.org/en/latest/src/changes.html) 做准备，並固定设置工具以在上游修改正在进行时保持 distutils 工作。 Aarch64架构的安装包是用最新的 manylinux2014 版本构建的，它修复了 linux 发行版之间使用不同大小内存页的问题。

### The inaugural NumPy survey is live!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. The survey is available in 8 additional languages besides English: Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey [here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### NumPy has a new logo!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught for the old logo that served us well for 15+ years.


### NumPy 1.19.0 release

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### Season of Docs acceptance

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy 1.18.0 release

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.


### NumPy receives a grant from the Chan Zuckerberg Initiative

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## 版本发布

Here is a list of NumPy releases, with links to release notes. Bugfix releases (only the `z` changes in the `x.y.z` version number) have no new features; minor releases (the `y` increases) do.

- NumPy 1.21.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 Jun 2021_.
- NumPy 1.20.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 May 2021_.
- NumPy 1.20.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 Jan 2021_.
- NumPy 1.19.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 Jan 2021_.
- NumPy 1.19.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _20 Jun 2020_.
- NumPy 1.18.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 May 2020_.
- NumPy 1.17.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 Jan 2020_.
- NumPy 1.18.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 Dec 2019_.
- NumPy 1.17.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 Jul 2019_.
- NumPy 1.16.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 Jan 2019_.
- NumPy 1.15.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 Jul 2018_.
- NumPy 1.14.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 Jan 2018_.
