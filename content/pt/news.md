---
title: Notícias
sidebar: false
---

### NumPy versão 1.20.0

_30 de janeiro de 2021_ -- O [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) está disponível. Este é o maior release do NumPy até agora, graças a mais de 180 contribuidores. As duas novidades mais emocionantes são:
- Anotações de tipos para grandes partes do NumPy, e um novo submódulo `numpy.typing` contendo aliases `ArrayLike` e `DtypeLike` que usuários e bibliotecas downstream podem usar quando quiserem adicionar anotações de tipos em seu próprio código.
- Otimizações de compilação SIMD multi-plataforma, com suporte para instruções x86 (SSE, AVX), ARM64 (Neon) e PowerPC (VSX). Isso rendeu melhorias significativas de desempenho para muitas funções (exemplos: [sen/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### Diversidade no projeto NumPy

_20 de setembro de 2020_ -- Escrevemos uma [declaração sobre o estado da diversidade e inclusão no projeto NumPy e discussões em redes sociais sobre isso.](/diversity_sep2020).


### Primeiro artigo oficial do NumPy publicado na Nature!

_16 de setembro de 2020_ -- Temos o prazer de anunciar a publicação do [primeiro artigo oficial do NumPy](https://www.nature.com/articles/s41586-020-2649-2) como um artigo de revisão na Nature. Isso ocorre 14 anos após o lançamento do NumPy 1.0. O artigo abrange aplicações e conceitos fundamentais da programação de matrizes, o rico ecossistema científico de Python construído em cima do NumPy, e os protocolos de array recentemente adicionados para facilitar a interoperabilidade com bibliotecas externas para computação com matrizes e tensores, como CuPy, Dask e JAX.


### O Python 3.9 está chegando, quando o NumPy vai liberar wheels binárias?

_14 de setembro de 2020_ -- Python 3.9 será lançado em algumas semanas. Se você for quiser usar imediatamente a nova versão do Python, você pode ficar desapontado ao descobrir que o NumPy (e outros pacotes binários como SciPy) não terão wheels no dia do lançamento. É um grande esforço adaptar a infraestrutura de compilação a uma nova versão de Python e normalmente leva algumas semanas para que os pacotes apareçam no PyPI e no conda-forge. Em preparação para este evento, por favor, certifique-se de
- atualizar seu `pip` para a versão 20.1 pelo menos para suportar `manylinux2010` e `manylinux2014`
- usar [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) ou `--only-binary=:all:` para impedir `pip` de tentar compilar a partir do código fonte.


### NumPy versão 1.19.2

_10 de setembro de 2020_ -- O [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) está disponível. Essa última versão da série 1.19 corrige vários bugs, inclui preparações para o lançamento [do Cython 3](http://docs.cython.org/en/latest/src/changes.html) e fixa o setuptools para que o distutils continue funcionando enquanto modificações upstream estão sendo feitas. As wheels para aarch64 são compiladas com manylinux2014 mais recente que conserta um problema com distribuições linux diferentes.

### A primeira pesquisa NumPy está aqui!

_2 de julho de 2020_ -- Esta pesquisa tem como objetivo guiar e definir prioridades para tomada de decisões sobre o desenvolvimento do NumPy como software e como comunidade. A pesquisa está disponível em mais 8 idiomas além do inglês: Bangla, Hindi, Japonês, Mandarim, Português, Russo, Espanhol e Francês.

Ajude-nos a melhorar o NumPy respondendo à pesquisa [aqui](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).


### O NumPy tem um novo logo!

_24 de junho de 2020_ -- NumPy agora tem um novo logo:

<img src="/images/logos/numpy_logo.svg" alt="NumPy logo" title="The new NumPy logo" width=300>

O logo é uma versão moderna do antigo, com um design mais limpo. Obrigado a Isabela Presedo-Floyd por projetar o novo logo, bem como o Travis Vaught pelo o logo antigo que nos serviu bem durante mais de 15 anos.


### NumPy versão 1.19.0

_20 de junho de 2020_ -- O NumPy 1.19.0 está disponível. Esta é a primeira versão sem suporte ao Python 2, portanto foi uma "versão de limpeza". A versão mínima de Python suportada agora é Python 3.6. Uma característica nova importante é que a infraestrutura de geração de números aleatórios que foi introduzida na NumPy 1.17.0 agora está acessível a partir do Cython.


### Aceitação no programa Season of Docs

_11 de maio de 2020_ -- O NumPy foi aceito como uma das organizações mentoras do programa Google Season of Docs. Estamos animados com a oportunidade de trabalhar com um *technical writer* para melhorar a documentação do NumPy mais uma vez! Para mais detalhes, consulte [o site oficial do programa Season of Docs](https://developers.google.com/season-of-docs/) e nossa [página de ideias](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).


### NumPy versão 1.18.0

_22 de dezembro de 2019_ -- O NumPy 1.18.0 está disponível. Após as principais mudanças em 1.17.0, esta é uma versão de consolidação. Esta é a última versão menor que irá suportar Python 3.5. Destaques dessa versão incluem a adição de uma infraestrutura básica para permitir o link com as bibliotecas BLAS e LAPACK em 64 bits durante a compilação, e uma nova C-API para `numpy.random`.

Por favor, veja as [notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.0) para mais detalhes.


### O NumPy recebe financiamento da Chan Zuckerberg Initiative

_15 de novembro de 2019_ -- Estamos felizes em anunciar que o NumPy e a OpenBLAS, uma das dependências-chave da NumPy, receberam um auxílio conjunto de $195,000 da Chan Zuckerberg Initiative através do seu programa [Essential Open Source Software for Science](https://chanzuckerberg.com/eoss/) que apoia a manutenção, crescimento, desenvolvimento e envolvimento com a comunidade de ferramentas de software open source fundamentais para a ciência.

Este auxílio será usado para aumentar os esforços de melhoria da documentação do NumPy, atualização do design do site, e desenvolvimento comunitário para servir melhor a nossa grande e rápida base de usuários, e garantir a sustentabilidade do projeto a longo prazo. Enquanto a equipe OpenBLAS se concentrará em tratar de um conjunto de questões técnicas fundamentais, em particular relacionadas a *thread-safety*, AVX-512, e *thread-local storage* (TLS), bem como melhorias algorítmicas na ReLAPACK (Recursive LAPACK) da qual a OpenBLAS depende.

Mais detalhes sobre nossas propostas e resultados esperados podem ser encontrados na [proposta completa de concessão de auxílio](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). O trabalho está agendado para começar no dia 1 de dezembro de 2019 e continuar pelos próximos 12 meses.


## Lançamentos

Aqui está uma lista de versões do NumPy, com links para notas de lançamento. Todos os lançamentos de bugfix (apenas o `z` muda no formato `x.y.z` do número da versão) não tem novos recursos; versões menores (o `y` aumenta) contém novos recursos.

- NumPy 1.18.4 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 de maio de 2020_.
- NumPy 1.18.3 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.3)) -- _19 de abril de 2020_.
- NumPy 1.18.2 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.2)) -- _17 de março de 2020_.
- NumPy 1.18.1 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.1)) -- _6 de janeiro de 2020_.
- NumPy 1.17.5 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 de janeiro de 2020_.
- NumPy 1.18.0 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 de dezembro de 2019_.
- NumPy 1.17.4 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.17.4)) -- _11 de novembro de 2019_.
- NumPy 1.17.0 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 de julho de 2019_.
- NumPy 1.16.0 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.16.0)) -- _14 de janeiro de 2019_.
- NumPy 1.15.0 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 de julho de 2018_.
- NumPy 1.14.0 ([notas de lançamento](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 de janeiro de 2018_.
