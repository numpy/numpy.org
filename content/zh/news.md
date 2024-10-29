---
title: 社区快讯
sidebar: false
newsHeader: NumPy 2.1 released!
date: 2024-08-18
---

### NumPy 2.1.0 released

_18 Aug, 2024_ -- NumPy 2.1.0 provides support for Python 3.13 and
drops support for Python 3.9. In addition to the usual bug fixes and
updated Python support, it helps get NumPy back to its usual release
cycle after the extended development of 2.0. The highlights for this
release are:

- Support for Python 3.13.
- Preliminary support for free threaded Python 3.13.
- Support for the array-api 2023.12 standard.

Python versions 3.10-3.13 are supported by this release.

### NumPy 2.0.0 released

_16 Jun, 2024_ -- NumPy 2.0.0 is the first major release since 2006. It is the
result of 11 months of development since the last feature release and is the
work of 212 contributors spread over 1078 pull requests. It contains a large
number of exciting new features as well as changes to both the Python and C
APIs.  It includes breaking changes that could not happen in a regular minor
release - including an ABI break, changes to type promotion rules, and API
changes which may not have been emitting deprecation warnings in 1.26.x. Key
documents related to how to adapt to changes in NumPy 2.0 include:

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

The blog post ["NumPy 2.0: an evolutionary milestone"](https://blog.scientific-python.org/numpy/numpy2/)
tells a bit of the story about how this release came together.

### NumPy 2.0 release date: June 16

_23 May, 2024_ -- We are excited to announce that NumPy 2.0 is planned to be
released on June 16, 2024. This release has been over a year in the making, and
is the first major release since 2006. Importantly, in addition to many new
features and performance improvement, it contains **breaking changes** to the
ABI as well as the Python and C APIs. It is likely that downstream packages and
end user code needs to be adapted - if you can, please verify whether your code
works with NumPy `2.0.0rc2`. **Please see the following for more details:**

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

### NumFOCUS end of the year fundraiser

_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount
on first-time PyCharm licenses. All year-one revenue from PyCharm purchases from now
until December 23rd, 2023 will go directly to the NumFOCUS programs.

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/
or a coupon code ISUPPORTDATASCIENCE 

### NumPy 1.26.0 released

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)
is now available. 此次发布的重点是：

- Python 3.12.0 support.
- Cython 3.0.0 compatibility.
- Use of the Meson build system
- Updated SIMD support
- f2py fixes, meson and bind(x) support
- Support for the updated Accelerate BLAS/LAPACK library

The NumPy 1.26.0 release is a continuation of the 1.25.x series that marks the
transition to the Meson build system and provision of support for Cython 3.0.0.
A total of 20 people contributed to this release and 59 pull requests were
merged.

The Python versions supported by this release are 3.9-3.12.

### numpy.org is now available in Japanese and Portuguese

_Aug 2, 2023_ -- numpy.org is now available in 2 additional languages:
Japanese and Portuguese. This wouldn’t be possible without our dedicated volunteers:

_Portuguese:_

- Melissa Weber Mendonça (melissawm)
- Ricardo Prins (ricardoprins)
- Getúlio Silva (getuliosilva)
- Julio Batista Silva (jbsilva)
- Alexandre de Siqueira (alexdesiqueira)
- Alexandre B A Villares (villares)
- Vini Salazar (vinisalazar)

_Japanese:_

- Atsushi Sakai (AtsushiSakai)
- KKunai
- Tom Kelly (TomKellyGenetics)
- Yuji Kanagawa (kngwyu)
- Tetsuo Koyama (tkoyama010)

The work on the translation infrastructure is supported with funding from CZI.

Looking ahead, we’d love to translate the website into more languages.
If you’d like to help, please connect with the NumPy Translations Team on Slack:
https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w.
(Look for the #translations channel.) We are also building a Translations Team who will be
working on localizing documentation and educational content across the Scientific Python
ecosystem. If this piqued your interest, join us on the Scientific Python
Discord: https://discord.gg/khWtqY6RKr. (Look for the #translation channel.)

### NumPy 1.25.0 released

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html)
is now available. 此次发布的重点是：

- Support for MUSL, there are now MUSL wheels.
- Support for the Fujitsu C/C++ compiler.
- Object arrays are now supported in einsum.
- Support for the inplace matrix multiplication (`@=`).

The NumPy 1.25.0 release continues the ongoing work to improve the handling and
promotion of dtypes, increase the execution speed, and clarify the
documentation. There has also been preparatory work for the future NumPy 2.0.0,
resulting in a large number of new and expired deprecations.

A total of 148 people contributed to this release and 530 pull requests were
merged.

The Python versions supported by this release are 3.9-3.11.

### Fostering an Inclusive Culture: Call for Participation

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

How can we be better when it comes to diversity and inclusion?
Read the report and find out how to get involved
[here](https://contributor-experience.org/docs/posts/dei-report/).

### NumPy documentation team leadership transition

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy
documentation team leads replacing Melissa Mendonça. We thank Melissa for all her
contributions to the NumPy official documentation and educational materials,
and Mukulika and Ross for stepping up.

### NumPy 1.24.0 released

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html)
is now available. 此次发布的重点是：

- New "dtype" and "casting" keywords for stacking functions.
- New F2PY features and fixes.
- Many new deprecations, check them out.
- Many expired deprecations,

The NumPy 1.24.0 release continues the ongoing work to improve the handling and
promotion of dtypes, increase execution speed, and clarify the documentation.
There are a large number of new and expired deprecations due to changes in
dtype promotion and cleanups. It is the work of 177 contributors spread over
444 pull requests. The supported Python versions are 3.8-3.11.

### Numpy 1.23.0 released

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html)
is now available. 此次发布的重点是：

- Implementation of `loadtxt` in C, greatly improving its performance.
- Exposure of DLPack at the Python level for easy data exchange.
- Changes to the promotion and comparisons of structured dtypes.
- Improvements to f2py.

The NumPy 1.23.0 release continues the ongoing work to improve the handling and
promotion of dtypes, increase the execution speed, clarify the documentation,
and expire old deprecations. It is the work of 151 contributors spread over
494 pull requests. The Python versions supported by this release 3.8-3.10.
Python 3.11 will be supported when it reaches the rc stage.

### NumFOCUS DEI research study: call for participation

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a
[research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent\&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c)
funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to
understand the barriers to participation that contributors, particularly those
from historically underrepresented groups, face in the open-source software
community. The research team would like to talk to new contributors, project
developers and maintainers, and those who have contributed in the past about
their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe)
which contains additional information on the research goals, privacy, and
confidentiality considerations. Your participation will be valuable to the
growth and sustainability of diverse and inclusive open-source software
communities. Accepted participants will participate in a 30-minute interview
with a research team member.

### NumPy 1.22.0 发布

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)
is now available. 此次发布的重点是：

- 主命名空间的注释类型基本上已完成。 Upstream is
  a moving target, so there will likely be further improvements, but the major
  work is done. This is probably the most user visible enhancement in this
  release.
- A preliminary version of the proposed
  [array API Standard](https://data-apis.org/array-api/latest/) is provided
  (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)).
  This is a step in creating a standard collection of functions that can be
  used across libraries such as CuPy and JAX.
- NumPy 现在有一个 DLPack 后端。 DLPack provides a common interchange format
  for array (tensor) data.
- New methods for `quantile`, `percentile`, and related functions. The new
  methods provide a complete set of the methods commonly found in the
  literature.
- The universal functions have been refactored to implement most of
  [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html).
  这也会解锁实验未来DType API的能力。
- 一个新的可配置内存分配器，供下游项目使用。

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread
over 609 pull requests. 此版本支持的 Python 版本是
3.8-3.10。

### 促进Python科学生态系统中的包容性文化

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has
[awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)
to support the onboarding, inclusion, and retention of people from historically
marginalized groups on scientific Python projects, and to structurally improve
the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/),
this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)
will support the creation of dedicated Contributor Experience Lead positions to
identify, document, and implement practices to foster inclusive open-source
communities. 这个项目将由Melissa Mendoncstima (NumPy) 领导，由Ralf Gommers (NumPy, SciPy)
Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and
Joris Van den Bossche (Pandas)， 提供
额外的辅导和指导

这是一个雄心勃勃的项目，旨在发现和执行
应该从结构上改善我们项目的社区动态的活动。 通过
建立这些新的跨项目角色，我们希望在Scientific Python社区引进一个新的
协作模型。 使生态系统中的
社区建设工作能够更有效地开展，
取得更大的成果。 我们还希望在项目中了解什么有效，什么无效，以吸引和留住来自历史上未被代表的群体的新贡献者，建立更清晰的认知。 最后，我们计划制作详细的报告，说明我们采取的措施如何在代表性和与社区互动方面对我们的项目产生影响。

这个为期两年的项目预计将于2021年11月开始，我们很期待看到这项工作的成果!
[You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021 Numpy调查

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 来自75个国家的1236 名用户参加了我们去年的首次调查。
调查结果使我们对今后12个月应该集中注意的问题有了很好的了解。

现在是时候进行另一次调查了，我们将再度尋求您的合作。 这份调查将耗费您大约15分钟的时间。 除英文外，调查问卷还提供另外8种语文：孟加拉语、法语、印地语、日语、普通话、葡萄牙语、俄语和西班牙语。

点击链接开始：https://berkeley.qualtrics.com/jfe/form/SV_aOONjgcBXDSl4q。

### NumPy 1.21.0 发布

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)
is now available. 此次发布的重点是：

- 继续开展SIMD工作，涵盖更多的功能和平台
- 新dtype的基础和型态转换初步工作
- 适用于Mac平台的Python 3.8和Python 3.9的universal2 wheels
- 改进文档
- 改进注释
- new `PCG64DXSM` bitgenerator for random numbers.

这个NumPy版本包含175人所贡献的581个合并请求。  此发布版本支持Python 3.7-3.9，将在Python 3.10发布后添加Python 3.10支持。

### 2020 Numpy调研结果结果

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students
and faculty from the University of Michigan and the University of Maryland
conducted the first official NumPy community survey. 在这里可以查看调研结果：https://numpy.org/user-survey-2020/。

### NumPy 1.20.0 发布

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)
is now available. 这是 NumPy到目前为止最大的一次版本更新，感谢180+位贡献者。 最令人振奋的两个特点是：

- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule
  containing `ArrayLike` and `DtypeLike` aliases that users and downstream
  libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE,
  AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant
  performance improvements for many functions (examples:
  [sin/cos](https://github.com/numpy/numpy/pull/17587),
  [einsum](https://github.com/numpy/numpy/pull/18194)).

### NumPy项目的多样性

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).

### NumPy官方第一次在Nature发表论文！

_Sep 16, 2020_ -- We are pleased to announce the publication of
[the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2)
as a review article in Nature. 这离NumPy 1.0发布已经过去了整整14年。
这篇论文涵盖了数组编程的应用和基本概念，基于NumPy构建的丰富科学Python生态系统，以及最近添加的数组协议，以促进与外部数组和张量库（如CuPy、Dask和JAX）的互操作性。

### Python 3.9 即将来临，新版本的NumPy 将在何时发布？

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. 如果您是这个Python版本的早期采用者， 您可能会失望的发现NumPy(以及其他二进制软件包，如SciPy) 在Python新版发布当天还不会发布相应的版本。 构建兼容新的 Python 版本的基础设施需要付出重大努力，通常需要几周时间才能让新版本出现在 PyPI 和 conda-forge 上。 为了这次版本升级得以顺利进行，请确保：

- update your `pip` to version 20.1 at least to support `manylinux2010` and
  `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from
  trying to build from source.

### NumPy 1.19.2 发布

_Sep 10, 2020_ -- NumPy
1.19.2 is now available.
This latest release in the 1.19 series fixes several bugs, prepares for the
upcoming Cython 3.x
release and pins
setuptools to keep distutils working while upstream modifications are ongoing.
Aarch64架构的安装包是用最新的 manylinux2014 版本构建的，它修复了
linux 发行版之间使用不同大小内存页的问题。

### 首次NumPy调研即将开始！

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for
decision-making about the development of NumPy as software and as a community.
除英文外，调查还提供了另外8种语言的版本：孟加拉语、印地语、日语、普通话、葡萄牙语、俄语、西班牙语和法语。

Please help us make NumPy better and take the survey
[here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).

### NumPy 有新标志了!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img
src="/images/logos/numpy_logo.svg"
alt="NumPy logo"
title="The new NumPy logo"
width=300>

这个标志是对旧标志的现代化演绎，采用更加简洁的设计。 感谢Isabela Presedo-Floryd的设计方案， 同时感谢Travis Vaugh设计的旧图标为我们服务了15年以上。

### NumPy 1.19.0 发布

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. 这是第一个不支持Python 2的版本，因此它是一个“清理版本”。 目前支持的最低Python 版本是 Python 3.6。 本版本拥有一个重要的新特性，NumPy 1.17.0引进的随机数字生成基础模块现在可以通过Cython访问。

### 文档整改时段

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for
the Google Season of Docs program. 我们很高兴看到有机会和技术写作者一起再次改进NumPy的技术文档！ For more
details, please see
[the official Season of Docs site](https://developers.google.com/season-of-docs/) and our
[ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).

### NumPy 1.18.0 发布

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. 在1.17.0发生重大变化后，这是一个合并版本。 这是最后一个支持 Python 3.5的小版本。 Highlights of the release includes the addition of basic
infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.

### NumPy 从Chan Zuckerberg Initiative获得了一笔捐款

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

这笔赠款将用来加速改进NumPy文档、网站重构和社区开发，进而更好地为我们庞大和迅速增长的用户基础服务，并确保项目的长期可持续性。 OpenBLAS 团队将侧重于处理几个关键技术问题，特别是线程安全问题、AVX-512和 thread-local 存储(TLS) 问题，以及OpenBLAS 依赖的 ReLAPACK (递归的LAPACK) 算法改进。

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). 项目开始于2019年12月1日，今后12个月将持续运作下去。

<a name="releases"></a>

## 版本发布

这是NumPy 版本列表，包含了对应版本发布说明的链接。 Bugfix
releases (only the `z` changes in the `x.y.z` version number) have no new
features; minor releases (the `y` increases) do.

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
- NumPy 1.22.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 Dec 2021_.
- NumPy 1.21.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 Dec 2021_.
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
