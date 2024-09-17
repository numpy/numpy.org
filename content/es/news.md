---
title: Noticias
sidebar: falso
newsHeader: "Lanzamiento de NumPy 2.0!"
date: 2024-06-17
---

### Lanzamiento de NumPy 2.0.0

_16 de junio de 2024_ -- NumPy 2.0.0 es el primer lanzamiento importante desde 2006. Es el resultado de 11 meses de desarrollo desde el último lanzamiento de características y es el trabajo de 212 colaboradores distribuidos entre 1078 solicitudes de incorporación de cambios. Contiene un gran número de nuevas características emocionantes, así como cambios en las APIs de Python y C.  Incluye cambios importantes que no podrían ocurrir en un lanzamiento menor regular, incluyendo una ruptura de ABI, cambios en las reglas de promoción de tipos y cambios en la API que pueden no haber estado emitiendo advertencias de obsolescencia en la versión 1.26.x. Los documentos clave relacionados con cómo adaptarse a los cambios en NumPy 2.0 incluyen:

- La [guía de migración a NumPy 2.0](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- Las [ notas del lanzamiento 2.0.0](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Problema de anuncio para actualizaciones de estado: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

La publicación ["NumPy 2.0: un hito evolutivo"](https://blog.scientific-python.org/numpy/numpy2/) cuenta un poco de la historia sobre cómo se llegó a este lanzamiento.


### Fecha de lanzamiento de NumPy 2.0: 16 de junio

_23 de mayo de 2024_ -- Estamos encantados de anunciar que NumPy 2.0 está previsto que sea lanzado el 16 de junio de 2024. Esta publicación lleva más de un año en proceso y es el primer lanzamiento importante desde 2006. Es importante destacar que, además de muchas nuevas características y mejoras en el rendimiento, contiene **cambios disruptivos** frente al ABI, como también a las APIs de Python y C. Es probable que los paquetes dependientes o downstream y código de usuario final necesiten ser adaptados - si puede, por favor verifique si su código funciona con NumPy `2.0.0rc2`. **Por favor, vea lo siguiente para más detalles:**

- La [guía de migración a NumPy 2.0](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)


### NumFOCUS end of the year fundraiser
_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount on first-time PyCharm licenses. All year-one revenue from PyCharm purchases from now until December 23rd, 2023 will go directly to the NumFOCUS programs.

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/ or a coupon code ISUPPORTDATASCIENCE 

### NumPy 1.26.0 released

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html) ahora está disponible. The highlights of the release are:

* Soporte de Python 3.12.0.
* Compatibilidad con Cython 3.0.0.
* Utilización del sistema de compilación Meson
* Actualización del soporte de SIMD
* Correcciones de f2py, meson y soporte de bind(x)
* Soporte para la librería actualizada Accelerate BLAS/LAPACK

La versión 1.26.0 de NumPy es la continuación de la serie 1.25.x que marca la transición al sistema de compilación Meson y que provee soporte para Cython 3.0.0. Un total de 20 personas contribuyeron a esta versión y 59 solicitudes de cambios fueron fusionadas.

Las versiones de Python compatibles con esta versión son 3.9-3.12.

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

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html) is now available. The highlights of the release are:

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

### Lanzamiento de NumPy 1.24.0

_18 de diciembre de 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html) ya está disponible. Los aspectos más destacados del lanzamiento son:

* Nuevas palabras clave "dtype" y "casting" para las funciones de apilamiento o stacking.
* Nuevas características y correcciones de F2PY.
* Muchas nuevas obsolescencias, revísalas.
* Muchas obsolescencias caducadas,

El lanzamiento de NumPy 1.24.0 continúa el trabajo en curso para mejorar el manejo y promoción de dtypes, aumentar la velocidad de ejecución y clarificar la documentación. Hay un gran número de obsolescencias nuevas y caducadas debido a los cambios en la limpieza y promoción de tipo dtype. Es el trabajo de 177 colaboradores distribuidos sobre 444 solicitudes de incorporación de cambios. Las versiones Python soportadas son 3.8-3.11.

### NumPy 1.23.0 ha sido lanzado

_22 de junio de 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html) ya está disponible. Los aspectos más destacados del lanzamiento son:

* Implementación de `loadtxt` en C, mejorando enormemente su rendimiento.
* Exposición de DLPack a nivel Python para facilitar el intercambio de datos.
* Cambios a la promoción y comparación de dtypes estructurados.
* Mejoras a f2py.

El lanzamiento de NumPy 1.23.0 continúa el trabajo en curso para mejorar el manejo y promoción de dtypes, aumentar la velocidad de ejecución y clarificar la documentación, caducar viejas obsolescencias. Es el trabajo de 151 colaboradores distribuidos sobre 494 solicitudes de incorporación de cambios. Las versiones de Python soportadas por este lanzamiento son 3.8-3.10. Python 3.11 será soportado cuando alcance la etapa rc.

### Estudio de investigación NumFOCUS DEI: llamado a participar

_13 de abril de 2022_ -- NumPy está trabajando con [NumFOCUS](http://numfocus.org/) en un [proyecto de investigación](https://numfocus.org/diversity-inclusion-disc/a-pivotal-time-in-numfocuss-project-aimed-dei-efforts?eType=EmailBlastContent&eId=f41a86c3-60d4-4cf9-86cf-58eb49dc968c) financiado por la [Fundación Gordon & Betty Moore](https://www.moore.org/) para entender las barreras de participación que enfrentan los colaboradores, especialmente aquellos de grupos históricamente subrepresentados, en la comunidad de software de código abierto. El equipo de investigación quisiera hablar con nuevos colaboradores, desarrolladores y mantenedores del proyecto, y con aquellos que han contribuido en el pasado acerca de sus experiencias uniéndose y contribuyendo a NumPy.

**¿Estás interesado en compartir tus experiencias?**

Por favor, complete este breve [formulari o de "Interés del Participante"](https://numfocus.typeform.com/to/WBWVJSqe), que contiene información adicional sobre los objetivos de la investigación, la privacidad y las consideraciones de confidencialidad. Su participación será valiosa para el crecimiento y la sostenibilidad de comunidades de software de código abierto diversas e inclusivas. Los participantes aceptados participarán en una entrevista de 30 minutos con un miembro del equipo de investigación.

### Lanzamiento de NumPy 1.22.0

_31 de diciembre de 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html) ya está disponible. Los aspectos más destacados del lanzamiento son:

* Las anotaciones de tipo del espacio de nombres principal están esencialmente completas. Upstream is a moving target, so there will likely be further improvements, but the major work is done. El repositorio principal (upstream) es un objetivo en movimiento, así que probablemente habrán más mejoras, pero el trabajo principal ya está hecho.
* Una versión preliminar del propuesto [Estándar API de Arreglos](https://data-apis.org/array-api/latest/) es suministrada (véase [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)). Este es un paso en la creación de una colección estándar de funciones que pueden ser usadas a través de librerías como CuPy y JAX.
* NumPy ahora tiene un backend de DLPack. DLPack proporciona un formato de intercambio común para datos de arreglos (tensor).
* Nuevos métodos para `cuantil`, `percentil` y funciones relacionadas. Los nuevos métodos proporcionan un conjunto completo de los métodos comúnmente encontrados en la literatura.
* Las funciones universales se han refactorizado para implementar la mayor parte de [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html). Esto también desbloquea la capacidad de experimentar con la futura API DType.
* Un nuevo asignador de memoria configurable para el uso de proyectos dependientes o downstream.

NumPy 1.22.0 es un gran lanzamiento que contó con el trabajo de 153 colaboradores distribuidos sobre 609 solicitudes de incorporación de cambios. Las versiones de Python soportadas por este lanzamiento son 3.8-3.10.

### Advancing an inclusive culture in the scientific Python ecosystem

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has [awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) to support the onboarding, inclusion, and retention of people from historically marginalized groups on scientific Python projects, and to structurally improve the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/), this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) will support the creation of dedicated Contributor Experience Lead positions to identify, document, and implement practices to foster inclusive open-source communities. This project will be led by Melissa Mendonça (NumPy), with additional mentorship and guidance provided by Ralf Gommers (NumPy, SciPy), Hannah Aizenman and Thomas Caswell (Matplotlib), Matt Haberland (SciPy), and Joris Van den Bossche (Pandas).

This is an ambitious project aiming to discover and implement activities that should structurally improve the community dynamics of our projects. By establishing these new cross-project roles, we hope to introduce a new collaboration model to the Scientific Python communities, allowing community-building work within the ecosystem to be done more efficiently and with greater outcomes. We also expect to develop a clearer picture of what works and what doesn't in our projects to engage and retain new contributors, especially from historically underrepresented groups. Finally, we plan on producing detailed reports on the actions executed, explaining how they have impacted our projects in terms of representation and interaction with our communities.

The two-year project is expected to start by November 2021, and we are excited to see the results from this work! [You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### 2021 NumPy survey

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 NumPy users from 75 countries participated in our inaugural survey last year. The survey findings gave us a very good understanding of what we should focus on for the next 12 months.

It’s time for another survey, and we are counting on you once again. It will take about 15 minutes of your time. Besides English, the survey questionnaire is available in 8 additional languages: Bangla, French, Hindi, Japanese, Mandarin, Portuguese, Russian, and Spanish.

Follow the link to get started: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### Numpy 1.21.0 release

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) is now available. Los aspectos más destacados de esta versión son:

- continued SIMD work covering more functions and platforms,
- initial work on the new dtype infrastructure and casting,
- universal2 wheels for Python 3.8 and Python 3.9 on Mac,
- improved documentation,
- improved annotations,
- new `PCG64DXSM` bitgenerator for random numbers.

This NumPy release is the result of 581 merged pull requests contributed by 175 people.  The Python versions supported for this release are 3.7-3.9, support for Python 3.10 will be added after Python 3.10 is released.


### 2020 NumPy survey results

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students and faculty from the University of Michigan and the University of Maryland conducted the first official NumPy community survey. Find the survey results here: https://numpy.org/user-survey-2020/.


### Numpy 1.20.0 release

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html) is now available. This is the largest NumPy release to date, thanks to 180+ contributors. The two most exciting new features are:
- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule containing `ArrayLike` and `DtypeLike` aliases that users and downstream libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE, AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant performance improvements for many functions (examples: [sin/cos](https://github.com/numpy/numpy/pull/17587), [einsum](https://github.com/numpy/numpy/pull/18194)).

### Diversity in the NumPy project

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).


### First official NumPy paper published in Nature!

_Sep 16, 2020_ -- We are pleased to announce the publication of [the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2) as a review article in Nature. This comes 14 years after the release of NumPy 1.0. The paper covers applications and fundamental concepts of array programming, the rich scientific Python ecosystem built on top of NumPy, and the recently added array protocols to facilitate interoperability with external array and tensor libraries like CuPy, Dask, and JAX.


### Python 3.9 is coming, when will NumPy release binary wheels?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. If you are an early adopter of Python versions, you may be dissapointed to find that NumPy (and other binary packages like SciPy) will not have binary wheels ready on the day of the release. It is a major effort to adapt the build infrastructure to a new Python version and it typically takes a few weeks for the packages to appear on PyPI and conda-forge. In preparation for this event, please make sure to
- update your `pip` to version 20.1 at least to support `manylinux2010` and `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from trying to build from source.


### Numpy 1.19.2 release

_Sep 10, 2020_ -- [NumPy 1.19.2](https://numpy.org/devdocs/release/1.19.2-notes.html) is now available. This latest release in the 1.19 series fixes several bugs, prepares for the [upcoming Cython 3.x release](http://docs.cython.org/en/latest/src/changes.html) and pins setuptools to keep distutils working while upstream modifications are ongoing. The aarch64 wheels are built with the latest manylinux2014 release that fixes the problem of differing page sizes used by different linux distros.

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


<a name="releases"></a>

## Releases

Here is a list of NumPy releases, with links to release notes. Bugfix releases (only the `z` changes in the `x.y.z` version number) have no new features; minor releases (the `y` increases) do.

- NumPy 2.0.1 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.1)) -- _21 Jul 2024_.
- NumPy 2.0.0 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.0.0)) -- _16 Jun 2024_.
- NumPy 1.26.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.4)) -- _5 Feb 2024_.
- NumPy 1.26.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _2 Jan 2024_.
- NumPy 1.26.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v1.26.2)) -- _12 Nov 2023_.
- NumPy 1.26.1 ([notas de publicación](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _14 Oct 2023_.
- NumPy 1.26.0 ([notas de publicación](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _16 Sep 2023_.
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
