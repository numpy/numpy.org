---
title: Notícias
sidebar: false
newsHeader: "Lançado o NumPy 1.25.0"
date: 2023-06-17
---

### Lançado o NumPy 1.25.0

_17 de junho, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html) está disponível agora. The highlights of the release are:

* Support for MUSL, there are now MUSL wheels.
* Support for the Fujitsu C/C++ compiler.
* Object arrays are now supported in einsum.
* Support for the inplace matrix multiplication (`@=`).

The NumPy 1.25.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, and clarify the documentation. There has also been preparatory work for the future NumPy 2.0.0, resulting in a large number of new and expired deprecations.

A total of 148 people contributed to this release and 530 pull requests were merged.

The Python versions supported by this release are 3.9-3.11.

### Promovendo uma cultura inclusiva: Chamada de participação

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

How can we be better when it comes to diversity and inclusion? Read the report and find out how to get involved [here](https://contributor-experience.org/docs/posts/dei-report/).

### Transição de liderança do time de documentação do NumPy

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy documentation team leads replacing Melissa Mendonça. We thank Melissa for all her contributions to the NumPy official documentation and educational materials, and Mukulika and Ross for stepping up.

### NumPy 1.24.0 released

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) is now available. The highlights of the release are:

* Novas palavras-chave "dtype" e "casting" para funções que atuam com stacking.
* Novas funcionalidades e correções do F2PY.
* Muitas depreciações novas, confira.
* Muitas depreciações expiradas.

The NumPy 1.24.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase execution speed, and clarify the documentation. There are a large number of new and expired deprecations due to changes in dtype promotion and cleanups. It is the work of 177 contributors spread over 444 pull requests. The supported Python versions are 3.8-3.11.

### NumPy versão 1.23.0

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) is now available. The highlights of the release are:

* Implementação de `loadtxt` em C, melhorando muito seu desempenho.
* Exposição do DLPack ao nível de Python para facilitar a troca de dados.
* Mudanças na promoção e comparações de dtypes estruturados.
* Melhorias no f2py.

The NumPy 1.23.0 release continues the ongoing work to improve the handling and promotion of dtypes, increase the execution speed, clarify the documentation, and expire old deprecations. It is the work of 151 contributors spread over 494 pull requests. The Python versions supported by this release 3.8-3.10. Python 3.11 will be supported when it reaches the rc stage.

### Pesquisa NumFOCUS DEI: chamada para participação

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a [research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c) funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to understand the barriers to participation that contributors, particularly those from historically underrepresented groups, face in the open-source software community. The research team would like to talk to new contributors, project developers and maintainers, and those who have contributed in the past about their experiences joining and contributing to NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe) which contains additional information on the research goals, privacy, and confidentiality considerations. Your participation will be valuable to the growth and sustainability of diverse and inclusive open-source software communities. Accepted participants will participate in a 30-minute interview with a research team member.

### NumPy versão 1.22.0

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) is now available. The highlights of the release are:

* Anotações de tipo do namespace principal estão praticamente completas. Ainda há trabalho a se fazer no upstream, mas a maior parte do trabalho está feita. Esta é provavelmente a melhoria mais visível para os usuários nesta versão.
* Uma versão preliminar da proposta do [array API Standard](https://data-apis.org/array-api/latest/) está disponível (veja [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)). Este é um passo na criação de uma coleção padrão de funções que podem ser compartilhadas entre bibliotecas como CuPy e JAX.
* NumPy agora tem um backend de DLPack. DLPack fornece um formato comum de compartilhamento para dados de arrays (tensores).
* Novos métodos para `quantile`, `percentile`, e funções relacionadas. Os novos métodos fornecem um conjunto completo dos métodos comumente encontrados na literatura.
* As funções universais foram refatoradas para implementar a maior parte da [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html). Isso também desbloqueia a capacidade de experimentar a futura API DType.
* Um novo alocador de memória configurável para uso pelos projetos downstream.

NumPy 1.22.0 is a big release featuring the work of 153 contributors spread over 609 pull requests. The Python versions supported by this release are 3.8-3.10.

### Avançando em uma cultura inclusiva no ecossistema científico de Python

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has [awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) to support the onboarding, inclusion, and retention of people from historically marginalized groups on scientific Python projects, and to structurally improve the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/), this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) will support the creation of dedicated Contributor Experience Lead positions to identify, document, and implement practices to foster inclusive open-source communities. This project will be led by Melissa Mendonça (NumPy), with additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy), Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that should structurally improve the community dynamics of our projects. By establishing these new cross-project roles, we hope to introduce a new collaboration model to the Scientific Python communities, allowing community-building work within the ecosystem to be done more efficiently and with greater outcomes. We also expect to develop a clearer picture of what works and what doesn't in our projects to engage and retain new contributors, especially from historically underrepresented groups. Finally, we plan on producing detailed reports on the actions executed, explaining how they have impacted our projects in terms of representation and interaction with our communities.

The two-year project is expected to start by November 2021, and we are excited to see the results from this work! [You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### Pesquisa NumPy 2021

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 NumPy users from 75 countries participated in our inaugural survey last year. The survey findings gave us a very good understanding of what we should focus on for the next 12 months.

It’s time for another survey, and we are counting on you once again. It will take about 15 minutes of your time. Besides English, the survey questionnaire is available in 8 additional languages: Bangla, French, Hindi, Japanese, Mandarin, Portuguese, Russian, and Spanish.

Siga o link para começar: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### NumPy versão 1.19.0

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) is now available. The highlights of the release are:

- a continuação do trabalho com SIMD para suportar mais funções e plataformas,
- trabalho inicial na infraestrutura e conversão de novos dtypes,
- wheels universal2 para Python 3.8 e Python 3.9 no Mac,
- melhorias na documentação,
- melhorias nas anotações de tipos,
- novo bitgenerator `PCG64DXSM` para números aleatórios.

This NumPy release is the result of 581 merged pull requests contributed by 175 people.  The Python versions supported for this release are 3.7-3.9, support for Python 3.10 will be added after Python 3.10 is released.


### Resultados da pesquisa NumPy 2020

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students and faculty from the University of Michigan and the University of Maryland conducted the first official NumPy community survey. Find the survey results here: https://numpy.org/user-survey-2020/.


### NumPy versão 1.18.0

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) is now available. This is the largest NumPy release to date, thanks to 180+ contributors. The two most exciting new features are:
- Anotações de tipos para grandes partes do NumPy, e um novo submódulo `numpy.typing` contendo aliases `ArrayLike` e `DtypeLike` que usuários e bibliotecas downstream podem usar quando quiserem adicionar anotações de tipos em seu próprio código.
- Otimizações de compilação SIMD multi-plataforma, com suporte para instruções x86 (SSE, AVX), ARM64 (Neon) e PowerPC (VSX). Isso rendeu melhorias significativas de desempenho para muitas funções (exemplos: [sen/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### Diversidade no projeto NumPy

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).


### Primeiro artigo oficial do NumPy publicado na Nature!

_Sep 16, 2020_ -- We are pleased to announce the publication of [the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2) as a review article in Nature. This comes 14 years after the release of NumPy 1.0. The paper covers applications and fundamental concepts of array programming, the rich scientific Python ecosystem built on top of NumPy, and the recently added array protocols to facilitate interoperability with external array and tensor libraries like CuPy, Dask, and JAX.


### O Python 3.9 está chegando, quando o NumPy vai liberar wheels binárias?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. If you are an early adopter of Python versions, you may be dissapointed to find that NumPy (and other binary packages like SciPy) will not have binary wheels ready on the day of the release. It is a major effort to adapt the build infrastructure to a new Python version and it typically takes a few weeks for the packages to appear on PyPI and conda-forge. In preparation for this event, please make sure to
- atualizar seu `pip` para a versão 20.1 pelo menos para suportar `manylinux2010` e `manylinux2014`
- usar [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) ou `--only-binary=:all:` para impedir `pip` de tentar compilar a partir do código fonte.


### NumPy versão 1.19.2

_Sep 10, 2020_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) is now available. This latest release in the 1.19 series fixes several bugs, prepares for the [upcoming Cython 3.x release](http://docs.cython.org/en/latest/src/changes.html) and pins setuptools to keep distutils working while upstream modifications are ongoing. The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

### A primeira pesquisa NumPy está aqui!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for decision-making about the development of NumPy as software and as a community. The survey is available in 8 additional languages besides English: Bangla, Hindi, Japanese, Mandarin, Portuguese, Russian, Spanish and French.

Please help us make NumPy better and take the survey [here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### O NumPy tem um novo logo!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

The logo is a modern take on the old one, with a cleaner design. Thanks to Isabela Presedo-Floyd for designing the new logo, as well as to Travis Vaught for the old logo that served us well for 15+ years.


### NumPy versão 1.20.0

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. This is the first release without Python 2 support, hence it was a "clean-up release". The minimum supported Python version is now Python 3.6. An important new feature is that the random number generation infrastructure that was introduced in NumPy 1.17.0 is now accessible from Cython.


### Aceitação no programa Season of Docs

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for the Google Season of Docs program. We are excited about the opportunity to work with a technical writer to improve NumPy's documentation once again! For more details, please see [the official Season of Docs site](https://developers.google.com/season-of-docs/) and our [ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy versão 1.18.0

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. After the major changes in 1.17.0, this is a consolidation release. It is the last minor release that will support Python 3.5. Highlights of the release includes the addition of basic infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Por favor, veja as [notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.0) para mais detalhes.


### O NumPy recebe financiamento da Chan Zuckerberg Initiative

_15 de novembro de 2019_ -- Estamos felizes em anunciar que o NumPy e a OpenBLAS, uma das dependências-chave do NumPy, receberam um auxílio conjunto de $195,000 da Chan Zuckerberg Initiative através do seu programa [Essential Open Source Software for Science](https://chanzuckerberg.com/eoss/) que apoia a manutenção, crescimento, desenvolvimento e envolvimento da comunidade em ferramentas de código aberto fundamentais para a ciência.

Este auxílio será usado para aumentar os esforços de melhoria da documentação do NumPy, reformulação do site, desenvolvimento comunitário para melhor servir a nossa grande, e rapidamente crescente, base de usuários, assim como para garantir a sustentabilidade do projeto a longo prazo. While the OpenBLAS team will focus on addressing sets of key technical issues, in particular thread-safety, AVX-512, and thread-local storage (TLS) issues, as well as algorithmic improvements in ReLAPACK (Recursive LAPACK) on which OpenBLAS depends.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). The work is scheduled to start on Dec 1st, 2019 and continue for the next 12 months.


## Lançamentos

Aqui está uma lista de versões do NumPy, com links para notas de lançamento. Bugfix releases (only the `z` changes in the `x.y.z` version number) have no new features; minor releases (the `y` increases) do.

- NumPy 1.25.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _8 Jul 2023_.
- NumPy 1.24.4 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _26 de junho de 2023_.
- NumPy 1.25.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _17 Jun 2023_.
- NumPy 1.24.3 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 de abril de 2023_.
- NumPy 1.24.2 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 de fevereiro de 2023_.
- NumPy 1.24.1 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 de dezembro de 2022_.
- NumPy 1.24.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.24.0)) -- _18 de dezembro de 2022_.
- NumPy 1.23.5 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.23.5)) -- _19 de novembro de 2022_.
- NumPy 1.23.4 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _12 de outubro de 2022_.
- NumPy 1.23.3 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 de setembro de 2022_.
- NumPy 1.23.2 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 de agosto de 2022_.
- NumPy 1.23.1 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 de julho de 2022_.
- NumPy 1.23.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 de junho de 2022_.
- NumPy 1.22.4 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 de maio de 2022_.
- NumPy 1.21.6 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 de abril de 2022_.
- NumPy 1.22.3 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.22.3)) -- _7 de março de 2022_.
- NumPy 1.22.2 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 de fevereiro de 2022_.
- NumPy 1.22.1 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 de janeiro de 2022_.
- NumPy 1.22.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 de dezembro de 2021_.
- NumPy 1.21.5 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 de dezembro de 2021_.
- NumPy 1.21.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 de junho de 2021_.
- NumPy 1.20.3 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 de maio de 2021_.
- NumPy 1.20.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 de janeiro de 2021_.
- NumPy 1.19.5 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 de janeiro de 2021_.
- NumPy 1.19.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _20 de junho de 2020_.
- NumPy 1.18.4 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 de maio de 2020_.
- NumPy 1.17.5 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 de janeiro de 2020_.
- NumPy 1.18.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 de dezembro de 2019_.
- NumPy 1.17.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 de julho de 2019_.
- NumPy 1.16.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 de janeiro de 2019_.
- NumPy 1.15.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 de julho de 2018_.
- NumPy 1.14.0 ([notas de versão](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 de janeiro de 2018_.
