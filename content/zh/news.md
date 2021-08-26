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

### 首次NumPy调研即将开始！

_2020年7月2日_ - 本次调查旨在指导并确定将NumPy以社区方式还是软件方式来开发。 除英文外，调查还提供了另外8种语言的版本：孟加拉语、印地语、日语、普通话、葡萄牙语、俄语、西班牙语和法语。

请帮助我们让 NumPy 变得更好，在[这里](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl)参与调查。


### NumPy 有新标志了!

_2020年7月24日_ -- NumPy 现在有一个新的标志：

<img src="/images/logos/numpy_logo.svg" alt="NumPy 标志" title="新的 NumPy 标志" width=300>

这是一个更时髦、纯净的标志。 感谢Isabela Presedo-Floryd的设计方案， 同时感谢Travis Vaugh设计的旧图标为我们服务了15年以上。


### NumPy 1.19.0 发布

_2020年6月20日_ -- NumPy 1.19.0 正式发布。 这是第一个不支持Python 2的版本，因此它是一个“清理版本”。 目前支持的最低Python 版本是 Python 3.6。 本版本拥有一个重要的新特性，NumPy 1.17.0引进的随机数字生成基础模块现在可以通过Cython访问。


### 文档整改时段

_2020年5月11日_ -- NumPy 已成为Google Season 文档项目之一。 我们很高兴看到有机会和技术写作者一起再次改进NumPy的技术文档！ 更多详情，请参考 [文档整改时段官方网站](https://developers.google.com/season-of-docs/) 和我们的 [意见页面](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas)。


### NumPy 1.18.0 发布

_2019年12月22日_ -- NumPy 1.18.0 正式发布。 在1.17.0发生重大变化后，这是一个合并版本。 这是最后一个支持 Python 3.5的小版本。 该版本的重要更新包括两个，添加了与64位 BLAS 和 LAPACK 库有关的底层更新， 添加 一个用于`numpy.random`的新C-API更新。

详情请看 [版本说明](https://github.com/numpy/numpy/releases/tag/v1.18.0)。


### NumPy 从Chan Zuckerberg Initiative获得了一笔捐款

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

This grant will be used to ramp up the efforts in improving NumPy documentation, website redesign, and community development to better serve our large and rapidly growing user base, and ensure the long-term sustainability of the project. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## 版本发布

Here is a list of NumPy releases, with links to release notes. Bugfix releases (only the `z` changes in the `x.y.z` version number) have no new features; minor releases (the `y` increases) do.

- NumPy1.21.0 ([发行说明](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _2021年6月22日_.
- NumPy1.23.0 ([发行说明](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _2021年5月10日_.
- NumPy1.20.0 ([发行说明](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _2021年1月30日_.
- NumPy1.19.5 ([发行说明](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _2021年1月5日_.
- NumPy1.19.0 ([发行说明](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _2020年6月20日_.
- NumPy1.18.4 (<a>发行说明</a>) -- _2020年5月3日_.
- NumPy1.17.5 (<a>发行说明</a>) -- _2020年1月1日_.
- NumPy1.18.0 (<a>发行说明</a>) -- _2019年12月22日_.
- NumPy1.17.0 (<a>发行说明</a>) -- _2019年7月26日_.
- NumPy1.16.0 (<a>发行说明</a>) -- _2019年1月14日_.
- NumPy1.15.0 (<a>发行说明</a>) -- _2018年7月23日_.
- NumPy1.14.0 (<a>发行说明</a>) -- _2018年1月7日_.
