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

_2020年9月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) 正式发布。 这个最新版本修复了1.19 系列中的几个漏洞，为 [即将发布的Cython3.x](http://docs.cython.org/en/latest/src/changes.html) 和 pins安装工具做好准备，以确保正在进行上游修改时用户仍然可以正常安装运行。 Aarch64架构的安装包是用最新的 manylinux2014 版本构建的，它修复了 linux 发行版之间使用不同大小内存页的问题。

### 首次NumPy调研即将开始！

_2020年7月2日_ - 本次调查旨在指导并确定 关于使用社区方式还是软件方式来开发NumPy的决策。 除英文外，调查还提供了另外8种语言的版本：孟加拉语、印地语、日语、曼达林语、葡萄牙语、俄语、西班牙语和法语。

请帮助我们让 NumPy 变得更好，在[这里](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl)参与调查。


### NumPy 有新logo了!

_2020年7月24日_ -- NumPy 现在有一个新的标志：

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

这是一个更时髦更纯净的标志。 感谢Isabela Presedo-Floryd的设计方案， 同时感谢Travis Vaugh设计的旧图标为我们提供了很好的15年以上服务。


### NumPy 1.19.0 发布

_2020年6月_ -- NumPy 1.19.0 正式发布。 这是第一个不支持Python 2的版本，因此它是一个“清理版本”。 目前支持的最小Python 版本是 Python 3.6。 本版本拥有一个重要的新特性，NumPy 1.17.0引进的随机数字生成基础模块现在可以通过Cython访问。


### 文档整改时间段

_2020年5月11日_ -- NumPy 已成为Google Season 文档项目的mentor组织之一。 我们很高兴看到有机会和技术写作者一起再次改进NumPy的技术文档！ 更多详情，请参考 [GsoD网站的官方赛期](https://developers.google.com/season-of-docs/) 和我们的 [意见页面](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas)。


### NumPy 1.18.0 发布

_2019年12月22日_ -- NumPy 1.18.0 正式发布。 在1.17.0发生重大变化后，这是一个合并版本。 这是最后一个支持 Python 3.5的小版本。 该版本的重要更新包括两个，添加了与64位 BLAS 和 LAPACK 库有关的底层更新， 添加 一个用于`numpy.random`的新C-API更新。

详情请看 [版本说明](https://github.com/numpy/numpy/releases/tag/v1.18.0)。


### NumPy 从Chan Zuckerberg Initiative获得了一笔捐款

_2019年11月15日_ -- 我们高兴地宣布NumPy和 OpenBLAS (Numpy的一个核心依赖库)已经收到一笔19,5000美元的联合赠款。 捐款来自于Chan Zuckerberg Initiative通过的[基础开源科学计算软件项目](https://chanzuckerberg.com/eoss/)，用来支持对科学发展起到关键作用的开源软件的维护、增长、开发和社区参与。

这笔赠款将用来加速改进NumPy文档、网站重构和社区开发，进而更好地为我们庞大和迅速增长的用户基础服务，并确保项目的长期可持续性。 While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

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
