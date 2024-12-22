---
title: 社区快讯
sidebar: false
newsHeader: "NumPy 2.2.0 released!"
date: 2024-12-8
---

### NumPy 2.2.0 released

_8 Dec, 2024_ -- The NumPy 2.2.0 release is a quick release that brings us back into sync with the usual twice yearly release cycle. There have been a number of small cleanups, improvements to the StringDType, and better support for free threaded Python. Highlights are:

* New functions `matvec` and `vecmat`,
* Many improved annotations,
* Improved support for the new StringDType,
* Improved support for free threaded Python,
* Fixes for f2py.

This release supports Python versions 3.10-3.13.


### NumPy 2.1.0 released

_18 Aug, 2024_ -- NumPy 2.1.0 provides support for Python 3.13 and drops support for Python 3.9. In addition to the usual bug fixes and updated Python support, it helps get NumPy back to its usual release cycle after the extended development of 2.0. The highlights for this release are:

-   Support for Python 3.13.
-   Preliminary support for free threaded Python 3.13.
-   Support for the array-api 2023.12 standard.

Python versions 3.10-3.13 are supported by this release.


### NumPy 2.0.0 released

_16 Jun, 2024_ -- NumPy 2.0.0 is the first major release since 2006. It is the result of 11 months of development since the last feature release and is the work of 212 contributors spread over 1078 pull requests. It contains a large number of exciting new features as well as changes to both the Python and C APIs.  It includes breaking changes that could not happen in a regular minor release - including an ABI break, changes to type promotion rules, and API changes which may not have been emitting deprecation warnings in 1.26.x. Key documents related to how to adapt to changes in NumPy 2.0 include:

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

The blog post ["NumPy 2.0: an evolutionary milestone"](https://blog.scientific-python.org/numpy/numpy2/) tells a bit of the story about how this release came together.


### NumPy 2.0 release date: June 16

_23 May, 2024_ -- We are excited to announce that NumPy 2.0 is planned to be released on June 16, 2024. This release has been over a year in the making, and is the first major release since 2006. Importantly, in addition to many new features and performance improvement, it contains **breaking changes** to the ABI as well as the Python and C APIs. It is likely that downstream packages and end user code needs to be adapted - if you can, please verify whether your code works with NumPy `2.0.0rc2`. **Please see the following for more details:**

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)


### NumFOCUS end of the year fundraiser
_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount on first-time PyCharm licenses. All year-one revenue from PyCharm purchases from now until December 23rd, 2023 will go directly to the NumFOCUS programs.

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/ or a coupon code ISUPPORTDATASCIENCE 

### NumPy 1.26.0 released

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html) is now available. 此次发布的重点是：

* Python 3.12.0 support.
* Cython 3.0.0 compatibility.
* Use of the Meson build system
* Updated SIMD support
* f2py fixes, meson and bind(x) support
* Support for the updated Accelerate BLAS/LAPACK library

The NumPy 1.26.0 release is a continuation of the 1.25.x series that marks the transition to the Meson build system and provision of support for Cython 3.0.0. A total of 20 people contributed to this release and 59 pull requests were merged.

The Python versions supported by this release are 3.9-3.12.

### numpy.org is now available in Japanese and Portuguese

_Aug 2, 2023_ -- numpy.org is now available in 2 additional languages: Japanese and Portuguese. This wouldn’t be possible without our dedicated volunteers:

_Portuguese:_
* Melissa Weber Mendonça (melissawm)
* Ricardo Prins (ricardoprins)
* Getúlio Silva (getuliosilva)
* Julio Batista Silva (jbsilva)
* Alexandre de Siqueira (alexdesiqueira)
* Alexandre B A Villares (villares)
* Vini Salazar (vinisalazar)

_Japanese:_
* Atsushi Sakai (AtsushiSakai)
* KKunai
* Tom Kelly (TomKellyGenetics)
* Yuji Kanagawa (kngwyu)
* Tetsuo Koyama (tkoyama010)

The work on the translation infrastructure is supported with funding from CZI.

Looking ahead, we’d love to translate the website into more languages. If you’d like to help, please connect with the NumPy Translations Team on Slack: https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w. (Look for the #translations channel.) We are also building a Translations Team who will be working on localizing documentation and educational content across the Scientific Python ecosystem. If this piqued your interest, join us on the Scientific Python Discord: https://discord.gg/khWtqY6RKr. (Look for the #translation channel.)

### NumPy 1.25.0 released

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html) is now available. 此次发布的重点是：

* Support for MUSL, there are now MUSL wheels.
* Support for the Fujitsu C/C++ compiler.
* Object arrays are now supported in einsum.
* Support for the inplace matrix multiplication (`@=`).

The NumPy 1.25.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, and clarify the documentation. There has also been preparatory work for the future NumPy 2.0.0, resulting in a large number of new and expired deprecations.

A total of 148 people contributed to this release and 530 pull requests were merged.

The Python versions supported by this release are 3.9-3.11.

### Fostering an Inclusive Culture: Call for Participation

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

How can we be better when it comes to diversity and inclusion? Read the report and find out how to get involved [here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy documentation team leadership transition

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy documentation team leads replacing Melissa Mendonça. We thank Melissa for all her contributions to the NumPy official documentation and educational materials, and Mukulika and Ross for stepping up.

### NumPy 1.24.0 released

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) is now available. 此次发布的重点是：

* New "dtype" and "casting" keywords for stacking functions.
* New F2PY features and fixes.
* Many new deprecations, check them out.
* Many expired deprecations,

The NumPy 1.24.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase execution speed, and clarify the documentation. There are a large number of new and expired deprecations due to changes in dtype promotion and cleanups. It is the work of 177 contributors spread over 444 pull requests. The supported Python versions are 3.8-3.11.

### Numpy 1.23.0 released

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) is now available. 此次发布的重点是：

* Implementation of `loadtxt` in C, greatly improving its performance.
* Exposure of DLPack at the Python level for easy data exchange.
* Changes to the promotion and comparisons of structured dtypes.
* Improvements to f2py.

The NumPy 1.23.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, clarify the documentation, and expire old deprecations. It is the work of 151 contributors spread over 494 pull requests. The Python versions supported by this release 3.8-3.10. Python 3.11 will be supported when it reaches the rc stage.

### NumFOCUS DEI research study: call for participation

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a [research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c) funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to understand the barriers to participation that contributors, particularly those from historically underrepresented groups, face in the open-source software community. The research team would like to talk to new contributors, project developers and maintainers, and those who have contributed in the past about their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe) which contains additional information on the research goals, privacy, and confidentiality considerations. Your participation will be valuable to the growth and sustainability of diverse and inclusive open-source software communities. Accepted participants will participate in a 30-minute interview with a research team member.

### NumPy 1.22.0 发布

_2021年6月31日_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) 正式发布。 此次发布的重点是：

* 主命名空间的注释类型基本上已完成。 上游是个移动目标，所以很可能会有进一步的改进，但是主要的 项工作已经完成。 这可能是本次发布中用户最可见的增强功能。
* A preliminary version of the proposed [array API Standard](https://data-apis.org/array-api/latest/) is provided (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)). 这是创建一个可以在 CuPy 和 JAX 等库中使用的函数的标准收藏的一个步骤。
* NumPy 现在有一个 DLPack 后端。 DLPack提供了一个数组 (tensor) 数据的通用交换格式。
* `量化`, `百分比`以及相关函数的新方法。 新的 方法提供了一整套常见于 文献中的方法。
* 通用函数已被重新考虑，以实现大多数的 [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html) 这也会解锁实验未来DType API的能力。
* 一个新的可配置内存分配器，供下游项目使用。

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread over 609 pull requests. 此版本支持的 Python 版本是 3.8-3.10。

### 促进Python科学生态系统中的包容性文化

_8月31日， 2021_ — 我们很高兴宣布Chan Zuckerberg倡议 [授予赠款](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) 以支持历史上被边缘化群体的人在科学Python项目中的融入、包容和留存，并为NumPy、SciPy、Matplotlib和Pandas的社区动态进行结构性改善。

作为 [CZI 基本开放源码科学程序](https://chanzuckerberg.com/eoss/)的一部分， 这 个[多样性 & 包容性补充赠款](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) 将支持创建专门的负责人职位，以确定、记录和实施促进包容性开源社区的实践。 这个项目将由Melissa Mendoncstima (NumPy) 领导，由Ralf Gommers (NumPy, SciPy) Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas)， 提供 额外的辅导和指导

这是一个雄心勃勃的项目，旨在发现和执行 应该从结构上改善我们项目的社区动态的活动。 通过 建立这些新的跨项目角色，我们希望在Scientific Python社区引进一个新的 协作模型。 使生态系统中的 社区建设工作能够更有效地开展， 取得更大的成果。 我们还希望在项目中了解什么有效，什么无效，以吸引和留住来自历史上未被代表的群体的新贡献者，建立更清晰的认知。 最后，我们计划制作详细的报告，说明我们采取的措施如何在代表性和与社区互动方面对我们的项目产生影响。

这个为期两年的项目预计将于2021年11月开始，我们很期待看到这项工作的成果! [您可以在这里阅读完整的提案](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063)。

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

这个NumPy版本包含175人所贡献的581个合并请求。  此发布版本支持Python 3.7-3.9，将在Python 3.10发布后添加Python 3.10支持。


### 2020 Numpy调研结果结果

_2021年6月22日_ -- 在2020年, NumPy调研小组与密歇根大学和马里兰大学的学生和教职员工合作，进行了第一次官方NumPy社区调查。 在这里可以查看调研结果：https://numpy.org/user-survey-2020/。


### NumPy 1.20.0 发布

_2021年1月30日_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) 正式发布。 这是 NumPy到目前为止最大的一次版本更新，感谢180+位贡献者。 最令人振奋的两个特点是：
- 为大部分Numpy代码做了类型注解，並添加了一个全新的`numpy.typing` 子模块，其中包含 `ArrayLike` 和 `DtypeLike`别名 ，使得用户和下游依赖库可以为自己的代码添加类型注解。
- 为多个架构进行SIMD编译优化，其支持X86(SSE、AVX)、ARM64(Neon) 和PowerPC(VSX) 指令集。 大幅提高许多函数的性能(例如： [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194))。

### NumPy项目的多样性

_2020年9月20日_ -- 我们就NumPy项目的社交媒体、多样性和包容性的现状以及相关的讨论撰写了一份[声明](/diversity_sep2020)。


### NumPy官方第一次在Nature发表论文！

_2020年9月16日_ - 我们高兴地宣布 [Numpy的第一篇官方论文](https://www.nature.com/articles/s41586-020-2649-2)刊登在Nature的评论文章。 这离NumPy 1.0发布已经过去了整整14年。 这篇论文涵盖了数组编程的应用和基本概念，基于NumPy构建的丰富科学Python生态系统，以及最近添加的数组协议，以促进与外部数组和张量库（如CuPy、Dask和JAX）的互操作性。


### Python 3.9 即将来临，新版本的NumPy 将在何时发布？

_2020年9月14日_ -- Python 3.9 将在几周后发布。 如果您是这个Python版本的早期采用者， 您可能会失望的发现NumPy(以及其他二进制软件包，如SciPy) 在Python新版发布当天还不会发布相应的版本。 构建兼容新的 Python 版本的基础设施需要付出重大努力，通常需要几周时间才能让新版本出现在 PyPI 和 conda-forge 上。 为了这次版本升级得以顺利进行，请确保：
- 将您的 `pip` 升级到 20.1 版本，至少要支持`manylinux2010` 和 `manylinux2014`
- 使用 [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) 或 `--only-binary=:all:` 选项来防止 `pip` 尝试从源码构建。


### NumPy 1.19.2 发布

_2020年9月10日_ -- [NumPy 19.2.0](https://numpy.org/devdocs/release/1.19.2-notes.html) 正式发布。 这个最新版本修复了1.19 系列中的几个漏洞，为 [即将发布的Cython3.x](http://docs.cython.org/en/latest/src/changes.html) 做准备，並固定设置工具以在上游修改正在进行时保持 distutils 工作。 Aarch64架构的安装包是用最新的 manylinux2014 版本构建的，它修复了 linux 发行版之间使用不同大小内存页的问题。

### 首次NumPy调研即将开始！

_Jul 2, 2020_ - 本次调查旨在指导并确定 关于开发NumPy 作为软件和社区的决策重点。 除英文外，调查还提供了另外8种语言的版本：孟加拉语、印地语、日语、普通话、葡萄牙语、俄语、西班牙语和法语。

请帮助我们让 NumPy 变得更好，在[这里](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl)参与调查。


### NumPy 有新标志了!

_2020年7月24日_ -- NumPy 现在有一个新的标志：

<img src="/images/logos/numpy_logo.svg" alt="NumPy 标志" title="新的 NumPy 标志" width=300>

这个标志是对旧标志的现代化演绎，采用更加简洁的设计。 感谢Isabela Presedo-Floryd的设计方案， 同时感谢Travis Vaugh设计的旧图标为我们服务了15年以上。


### NumPy 1.19.0 发布

_2020年6月20日_ -- NumPy 1.19.0 正式发布。 这是第一个不支持Python 2的版本，因此它是一个“清理版本”。 目前支持的最低Python 版本是 Python 3.6。 本版本拥有一个重要的新特性，NumPy 1.17.0引进的随机数字生成基础模块现在可以通过Cython访问。


### 文档整改时段

_2020年5月11日_ -- NumPy 已成为Google Season 文档项目之一。 我们很高兴看到有机会和技术写作者一起再次改进NumPy的技术文档！ 更多详情，请参考 [文档整改时段官方网站](https://developers.google.com/season-of-docs/) 和我们的 [意见页面](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas)。


### NumPy 1.18.0 发布

_2019年12月22日_ -- NumPy 1.18.0 正式发布。 在1.17.0发生重大变化后，这是一个合并版本。 这是最后一个支持 Python 3.5的小版本。 该版本的重要更新包括两个，添加了与64位 BLAS 和 LAPACK 库有关的底层更新， 添加 一个用于`numpy.random`的新C-API更新。

详情请看 [版本说明](https://github.com/numpy/numpy/releases/tag/v1.18.0)。


### NumPy 从Chan Zuckerberg Initiative获得了一笔捐款

_2019年11月15日_ -- 我们高兴地宣布NumPy和 OpenBLAS (Numpy的一个核心依赖库)已经收到一笔19,5000美元的联合赠款。 捐款来自于Chan Zuckerberg Initiative通过的[基础开源科学计算软件项目](https://chanzuckerberg.com/eoss/)，用来支持对科学发展起到关键作用的开源软件的维护、增长、开发和社区参与。

这笔赠款将用来加速改进NumPy文档、网站重构和社区开发，进而更好地为我们庞大和迅速增长的用户基础服务，并确保项目的长期可持续性。 OpenBLAS 团队将侧重于处理几个关键技术问题，特别是线程安全问题、AVX-512和 thread-local 存储(TLS) 问题，以及OpenBLAS 依赖的 ReLAPACK (递归的LAPACK) 算法改进。

若想查看更多关于捐款的倡议和交付件的详情，可在 [全额赠款提案](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167) 中找到。 项目开始于2019年12月1日，今后12个月将持续运作下去。


<a name="releases"></a>

## 版本发布

这是NumPy 版本列表，包含了对应版本发布说明的链接。 所有的 bug修复版本(即在 `x.y.z`格式版本号中只有 `z`改变)没有新功能；小版本更新(`y` 改变)有新功能。

- NumPy 2.2.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.1)) -- _21 Dec 2024_.
- NumPy 2.2.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.0)) -- _8 Dec 2024_.
- NumPy 2.1.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.3)) -- _2 Nov 2024_.
- NumPy 2.1.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.2)) -- _5 Oct 2024_.
- NumPy 2.1.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.1)) -- _3 Sep 2024_.
- NumPy 2.0.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.2)) -- _26 Aug 2024_.
- NumPy 2.1.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.1.0)) -- _18 Aug 2024_.
- NumPy 2.0.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.1)) -- _21 Jul 2024_.
- NumPy 2.0.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.0)) -- _16 Jun 2024_.
- NumPy 1.26.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.4)) -- _5 Feb 2024_.
- NumPy 1.26.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _2 Jan 2024_.
- NumPy 1.26.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _12 Nov 2023_.
- NumPy 1.26.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _14 Oct 2023_.
- NumPy 1.26.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _16 Sep 2023_.
- NumPy 1.25.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.2)) -- _31 Jul 2023_.
- NumPy 1.25.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _8 Jul 2023_.
- NumPy 1.24.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _26 Jun 2023_.
- NumPy 1.25.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _17 Jun 2023_.
- NumPy 1.24.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 Apr 2023_.
- NumPy 1.24.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 Feb 2023_.
- NumPy 1.24.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 Dec 2022_.
- NumPy 1.24.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.24.0)) -- _18 Dec 2022_.
- NumPy 1.23.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _19 Nov 2022_.
- NumPy 1.23.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _12 Oct 2022_.
- NumPy 1.23.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 Sep 2022_.
- NumPy 1.23.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 Aug 2022_.
- NumPy 1.23.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 Jul 2022_.
- NumPy 1.23.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 Jun 2022_.
- NumPy 1.22.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 May 2022_.
- NumPy 1.21.6 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 Apr 2022_.
- NumPy 1.22.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.3)) -- _7 Mar 2022_.
- NumPy 1.22.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 Feb 2022_.
- NumPy 1.22.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 Jan 2022_.
- NumPy1.22.0 (<a>发行说明</a>) -- _2021年12月31日_.
- NumPy1.21.5 (<a>发行说明</a>) -- _2021年12月19日_.
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
