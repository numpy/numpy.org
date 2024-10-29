---
title: Notícias
sidebar: false
newsHeader: NumPy versão 1.26.0
date: 2023-09-16
---

### Lançado o NumPy versão 1.26.0

_18 Aug, 2024_ -- NumPy 2.1.0 provides support for Python 3.13 and
drops support for Python 3.9. Além das habituais correções de erros e suporte a Python atualizado, esta versão ajuda a trazer o NumPy de volta ao ciclo habitual de lançamento após o longo desenvolvimento da versão 2.0. Os destaques desta versão são:

- Suporte ao Python 3.12.0.
- Suporte preliminar para Python 3.13 free threaded.
- Suporte para array-api 2023.12 standard.

As versões 3.10-3.13 do Python são suportadas por esta versão.

### NumPy 2.0.0 lançada

_16 Jun, 2024_ -- NumPy 2.0.0 is the first major release since 2006. É o resultado de 11 meses de desenvolvimento desde a última feature release e é o trabalho de 212 contribuidores espalhado por 1078 pull requests. Esta versão contém um grande número de novas funcionalidades interessantes, bem como mudanças nas APIs Python e C.  As mudanças incluem quebras de compatibilidade que não puderam acontecer em uma versão regular menor - incluindo uma quebra na ABI, mudanças nas regras de promoção de tipo e mudanças na API
que poderiam não estar emitindo alertas de fim de suporte nas versões 1.26.x. Documentos-chave, relacionados a como se adaptar às mudanças em NumPy 2.0, incluem:

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

The blog post ["NumPy 2.0: an evolutionary milestone"](https://blog.scientific-python.org/numpy/numpy2/)
tells a bit of the story about how this release came together.

### Data de lançamento da NumPy 2.0: 16 de junho

_23 May, 2024_ -- We are excited to announce that NumPy 2.0 is planned to be
released on June 16, 2024. Este lançamento está em desenvolvimento há mais de um ano, e
é o primeiro grande lançamento desde 2006. Importantly, in addition to many new
features and performance improvement, it contains **breaking changes** to the
ABI as well as the Python and C APIs. It is likely that downstream packages and
end user code needs to be adapted - if you can, please verify whether your code
works with NumPy `2.0.0rc2`. **Please see the following for more details:**

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

### Lançado o NumPy versão 1.26.0

_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount
on first-time PyCharm licenses. Todas as receitas do primeiro ano das compras do PyCharm a partir de agora
até 23 de dezembro, 2023 irão diretamente para os programas NumFOCUS.

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/
or a coupon code ISUPPORTDATASCIENCE 

### NumPy versão 1.24.0

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)
is now available. Os destaques desta versão são:

- Suport ao Python 3.12.0.
- Compatibilidade com Cython 3.0.0.
- Utilização do sistema Meson para compilação
- Suport a SIMD atualizado
- Melhorias para f2py, suporte a meson e bind(x)
- Suporte à versão mais recente da biblioteca Accelerate BLAS/LAPACK

A versão 1.26.0 é uma continuação da série de versões 1.25.x que marcam a transição para o sistema de compilação Meson e oferecem suporte preliminar para o Cython 3.0.0.
Um total de 20 pessoas contribuíram para este lançamento e 59 pull requests foram incorporadas.

As versões do Python suportadas por esta versão são 3.9-3.12.

### numpy.org agora está disponível em japonês e português

_Aug 2, 2023_ -- numpy.org is now available in 2 additional languages:
Japanese and Portuguese. Isto não seria possível sem nossos voluntários dedicados:

_Portuguese:_

- Melissa Weber Mendonça (melissawm)
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

O trabalho na infraestrutura de traduções é financiado pela CZI.

No futuro, adoraríamos traduzir o site para mais línguas.
Se você quiser ajudar, por favor entre em contato com o time de traduções do NumPy no Slack:
https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w.
(Procure pelo canal de #translations.) (Procure pelo canal #translations)
Também estamos organizando um time de tradutores que serão responsáveis por trabalhar na localização da documentação e conteúdo educacional para o ecossistema Scientific Python. Se esse trabalho te interessa, junte-se a nós no Discord do projeto Scientific Python: https://discord.gg/khWtqY6RKr. (Procure pelo canal #translation)

### NumPy versão 1.22.0

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html)
is now available. Os destaques desta versão são:

- Suporte para MUSL, agora existem rodas MUSL.
- Suporte para o compilador Fujitsu C/C++.
- Arrays de objetos agora são suportados em einsum.
- Support for the inplace matrix multiplication (`@=`).

A versão 1.25.0 do NumPy continua o trabalho de melhorias no suporte e promoção de dtypes, na velocidade e execução, e na documentação. Também tem havido trabalho preparatório para a futura versão 2.0.0, resultando em um grande número de depreciações novas e expiradas.

Um total de 148 pessoas contribuíram para este lançamento e 530 pull requests foram incorporadas.

As versões do Python suportadas por esta versão são 3.9-3.11.

### Promovendo uma cultura inclusiva: Chamada de participação

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

Como podemos ser melhores quando se trata de diversidade e de inclusão?
Read the report and find out how to get involved
[here](https://contributor-experience.org/docs/posts/dei-report/).

### Transição de liderança do time de documentação do NumPy

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy
documentation team leads replacing Melissa Mendonça. Agradecemos a Melissa por todas suas contribuições para a documentação oficial do NumPy e materiais educacionais, e Mukulika e Ross por aceitarem o desafio.

### NumPy versão 1.23.0

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html)
is now available. Os destaques desta versão são:

- Novas palavras-chave "dtype" e "casting" para funções que atuam com stacking.
- Novas funcionalidades e correções do F2PY.
- Muitas depreciações novas, confira.
- Muitas depreciações expiradas.

A versão 1.24.0 do NumPy continua o trabalho de melhorias no suporte e promoção de dtypes, na velocidade e execução, e na documentação.
Há um grande número de depreciações novas e expiradas devido a mudanças na promoção de dtypes e limpezas no código. É o trabalho de 177 contribuidores espalhados em 444 pull requests. As versões suportadas do Python são 3.8-3.11.

### NumPy versão 1.19.0

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html)
is now available. Os destaques desta versão são:

- Implementation of `loadtxt` in C, greatly improving its performance.
- Exposição do DLPack ao nível de Python para facilitar a troca de dados.
- Mudanças na promoção e comparações de dtypes estruturados.
- Melhorias no f2py.

A versão 1.23.0 do NumPy continua o trabalho de melhorias no suporte e promoção de dtypes, na velocidade de execução, na documentação e na expiração de depreciações. É o trabalho de 151 contribuidores espalhados em 494 pull requests. As versões do Python suportadas por esta versão 3.8-3.10.
Python 3.11 será suportado quando chegar na etapa rc.

### Pesquisa NumFOCUS DEI: chamada para participação

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a
[research project](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent\&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c)
funded by the [Gordon & Betty Moore Foundation](https://www.moore.org/) to
understand the barriers to participation that contributors, particularly those
from historically underrepresented groups, face in the open-source software
community. A equipe da pesquisa gostaria de falar com novos colaboradores, desenvolvedores e mantenedores, e aqueles que contribuíram no passado sobre suas experiências contribuindo para o NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe)
which contains additional information on the research goals, privacy, and
confidentiality considerations. Sua participação será valiosa para o crescimento e sustentabilidade de comunidades de software open source diversas e inclusivas. Os participantes aceitos participarão de uma entrevista de 30 minutos com um membro da equipe de pesquisa.

### NumPy versão 1.22.0

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)
is now available. Os destaques desta versão são:

- Anotações de tipo do namespace principal estão praticamente completas. Upstream is
  a moving target, so there will likely be further improvements, but the major
  work is done. This is probably the most user visible enhancement in this
  release.
- A preliminary version of the proposed
  [array API Standard](https://data-apis.org/array-api/latest/) is provided
  (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)).
  This is a step in creating a standard collection of functions that can be
  used across libraries such as CuPy and JAX.
- NumPy agora tem um backend de DLPack. DLPack provides a common interchange format
  for array (tensor) data.
- New methods for `quantile`, `percentile`, and related functions. The new
  methods provide a complete set of the methods commonly found in the
  literature.
- The universal functions have been refactored to implement most of
  [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html).
  Isso também desbloqueia a capacidade de experimentar a futura API DType.
- Um novo alocador de memória configurável para uso pelos projetos downstream.

NumPy 1.22.0 é uma versão importante com o trabalho de 153 contribuidores espalhados por
mais de 609 pull requests. As versões do Python suportadas por esta versão são 3.8-3.10.

### Promovendo uma cultura inclusiva no ecossistema científico de Python

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has
[awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)
to support the onboarding, inclusion, and retention of people from historically
marginalized groups on scientific Python projects, and to structurally improve
the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/),
this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)
will support the creation of dedicated Contributor Experience Lead positions to
identify, document, and implement practices to foster inclusive open-source
communities. Este projeto será liderado por Melissa Mendonça (NumPy), com apoio adicional de Ralf Gommers (NumPy, SciPy), Hannah Aizenman e Thomas Caswell (Matplotlib), Matt Haberland (SciPy), e
Joris Van den Bossche (Pandas).

Esse é um projeto ambicioso que visa descobrir e implementar atividades que
devem estruturalmente melhorar a dinâmica da comunidade de nossos projetos. Ao
criar essas novas funções entre projetos, esperamos introduzir um novo
modelo de colaboração às comunidades de Python científico, permitir que
o trabalho de construção da comunidade no ecossistema seja feito de forma mais eficiente e
com maiores resultados. Também esperamos desenvolver uma imagem mais clara do que
funciona e o que não funciona em nossos projetos para engajar e reter novos colaboradores,
especialmente de grupos historicamente sub-representados. Finalmente, planejamos
produzir relatórios detalhados sobre as ações executadas, explicando como eles
afetaram nossos projetos em termos de representação e interação com nossas
comunidades.

O projeto de dois anos deverá começar em novembro de 2021 e estamos animados
para ver os resultados deste trabalho!
[You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### Pesquisa NumPy 2021

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 usuários do NumPy de 75 países participaram da nossa primeira pesquisa ano passado.
Os resultados da pesquisa nos ajudaram a compreender muito bem o que devemos fazer pelos 12 meses seguintes.

Chegou a hora de fazer outra pesquisa e estamos contando com você novamente. Vai levar cerca de 15 minutos do seu tempo. Além de Inglês, o questionário de pesquisa está disponível em 8 idiomas adicionais: Bangla, Francês, Hindi, Japonês, Mandarim, Português, Russo e Espanhol.

Siga o link para começar: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.

### NumPy versão 1.21.0

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)
is now available. Os destaques desta versão são:

- a continuação do trabalho com SIMD para suportar mais funções e plataformas,
- trabalho inicial na infraestrutura e conversão de novos dtypes,
- wheels universal2 para Python 3.8 e Python 3.9 no Mac,
- melhorias na documentação,
- melhorias nas anotações de tipos,
- new `PCG64DXSM` bitgenerator for random numbers.

Esta versão do NumPy é o resultado de 581 pull requests aceitos, a partir das contribuições de 175 pessoas.  As versões do Python suportadas por esta versão são 3.7-3.9; o suporte para o Python 3.10 será adicionado após o lançamento do Python 3.10.

### Resultados da pesquisa NumPy 2020

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students
and faculty from the University of Michigan and the University of Maryland
conducted the first official NumPy community survey. Encontre os resultados da pesquisa aqui: https://numpy.org/user-survey-2020/.

### NumPy versão 1.20.0

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)
is now available. Este é o maior lançamento do NumPy até hoje, graças a mais de 180 colaboradores. As duas novidades mais emocionantes são:

- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule
  containing `ArrayLike` and `DtypeLike` aliases that users and downstream
  libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE,
  AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant
  performance improvements for many functions (examples:
  [sin/cos](https://github.com/numpy/numpy/pull/17587),
  [einsum](https://github.com/numpy/numpy/pull/18194)).

### Diversidade no projeto NumPy

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).

### Primeiro artigo oficial do NumPy publicado na Nature!

_Sep 16, 2020_ -- We are pleased to announce the publication of
[the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2)
as a review article in Nature. Isso ocorre 14 anos após o lançamento do NumPy 1.0.
O artigo abrange aplicações e conceitos fundamentais da programação de matrizes, o rico ecossistema científico de Python construído em cima do NumPy, e os protocolos de array recentemente adicionados para facilitar a interoperabilidade com bibliotecas externas para computação com matrizes e tensores, como CuPy, Dask e JAX.

### O Python 3.9 está chegando, quando o NumPy vai liberar wheels binárias?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. Se você for quiser usar imediatamente a nova versão do Python, você pode ficar desapontado ao descobrir que o NumPy (e outros pacotes binários como SciPy) não terão wheels no dia do lançamento. É um grande esforço adaptar a infraestrutura de compilação a uma nova versão de Python e normalmente leva algumas semanas para que os pacotes apareçam no PyPI e no conda-forge. Em preparação para este evento, por favor, certifique-se de

- update your `pip` to version 20.1 at least to support `manylinux2010` and
  `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from
  trying to build from source.

### NumPy versão 1.19.2

_Sep 10, 2020_ -- NumPy
1.19.2 is now available.
This latest release in the 1.19 series fixes several bugs, prepares for the
upcoming Cython 3.x
release and pins
setuptools to keep distutils working while upstream modifications are ongoing.
As wheels para aarch64 são compiladas com manylinux2014 mais recente que conserta um problema com distribuições linux diferentes.

### A primeira pesquisa NumPy está aqui!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for
decision-making about the development of NumPy as software and as a community.
A pesquisa está disponível em mais 8 idiomas além do inglês: Bangla, Hindi, Japonês, Mandarim, Português, Russo, Espanhol e Francês.

Please help us make NumPy better and take the survey
[here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).

### O NumPy tem um novo logo!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img
src="/images/logos/numpy_logo.svg"
alt="NumPy logo"
title="The new NumPy logo"
width=300>

O logotipo é uma versão moderna do antigo, com um design mais limpo. Obrigado à Isabela Presedo-Floyd por projetar o novo logotipo, bem como ao Travis Vaught pelo o logotipo antigo que nos serviu bem durante mais de 15 anos.

### NumPy versão 1.19.0

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. Esta é a primeira versão sem suporte ao Python 2, portanto foi uma "versão de limpeza". A versão mínima de Python suportada agora é Python 3.6. Uma característica nova importante é que a infraestrutura de geração de números aleatórios que foi introduzida na NumPy 1.17.0 agora está acessível a partir do Cython.

### Aceitação no programa Season of Docs

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for
the Google Season of Docs program. Estamos animados com a oportunidade de trabalhar com um <em x-id="3">technical writer</em> para melhorar a documentação do NumPy mais uma vez! For more
details, please see
[the official Season of Docs site](https://developers.google.com/season-of-docs/) and our
[ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).

### NumPy versão 1.18.0

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. Após as principais mudanças em 1.17.0, esta é uma versão de consolidação. É a última versão menor que suportará Python 3.5. Highlights of the release includes the addition of basic
infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.

### O NumPy recebe financiamento da Chan Zuckerberg Initiative

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

Este auxílio será usado para aumentar os esforços de melhoria da documentação do NumPy, reformulação do site, desenvolvimento comunitário para melhor servir a nossa grande, e rapidamente crescente, base de usuários, assim como para garantir a sustentabilidade do projeto a longo prazo. Enquanto a equipe OpenBLAS se concentrará em tratar de um conjunto de questões técnicas fundamentais, em particular relacionadas a <em x-id="3">thread-safety</em>, AVX-512, e <em x-id="3">thread-local storage</em> (TLS), bem como melhorias algorítmicas na ReLAPACK (Recursive LAPACK) da qual a OpenBLAS depende.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). O trabalho está agendado para começar no dia 1 de dezembro de 2019 e continuar pelos próximos 12 meses.

<a name="releases"></a>

## Lançamentos

Aqui está uma lista de versões do NumPy, com links para notas de lançamento. Bugfix
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
