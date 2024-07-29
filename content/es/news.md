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

### Promoviendo una cultura inclusiva en el ecosistema científico de Python

_31 de agosto de 2021_ -- Nos complace anunciar que la Iniciativa Chan Zuckerberg ha [otorgado una subvención](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/) para apoyar la incorporación, inclusión, y retención de personas de grupos históricamente marginados en proyectos científicos de Python y para mejorar estructuralmente la dinámica de la comunidad para NumPy, SciPy, Matplotlib y Pandas.

Como parte del [Programa de Software Esencial de Código Abierto para la Ciencia de CZI](https://chanzuckerberg.com/eoss/), esta subvención suplementaria de [Diversidad &e Inclusión](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b) apoyará la creación de posiciones dedicadas de Líder de Experiencia del Colaborador para identificar, documentar e implementar prácticas para fomentar comunidades inclusivas de código abierto. Este proyecto será liderado por Melissa Mendonça (NumPy), con mentoría y orientación adicionales por parte de Ralf Gommers (NumPy, SciPy), Hannah Aizenman y Thomas Caswell (Matplotlib), Matt Haberland (SciPy), y Joris Van den Bossche (Pandas).

Este es un proyecto ambicioso destinado a descubrir e implementar actividades que deberían mejorar estructuralmente la dinámica comunitaria de nuestros proyectos. Al establecer estos nuevos roles entre proyectos, esperamos introducir un nuevo modelo de colaboración para las comunidades de Python Científico, permitiendo que el trabajo de construcción de comunidades dentro del ecosistema se realice de manera más eficiente y con mejores resultados. También esperamos desarrollar una imagen más clara tanto de lo que sí y como de lo que no funciona en nuestros proyectos, para atraer y retener nuevos colaboradores, especialmente de grupos históricamente subrepresentados. Finalmente, planeamos producir informes detallados sobre las acciones ejecutadas, explicando cómo éstas han impactado nuestros proyectos en términos de representación e interacción con nuestras comunidades.

Se espera que este proyecto, de dos años de duración, comience en noviembre de 2021, y estamos emocionados por ver los resultados de este trabajo! [Puede leer la propuesta completa aquí](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### Encuesta de NumPy de 2021

_12 de julio de 2021_ -- En NumPy creemos en el poder de nuestra comunidad. 1,236 usuarios de NumPy de 75 países participaron en nuestra encuesta inaugural el año pasado. Los resultados de la encuesta nos dieron una muy buena comprensión acerca de lo que debería ser nuestro enfoque durante los próximos 12 meses.

Es hora de otra encuesta, y contamos contigo una vez más. Te tomará alrededor de 15 minutos de tu tiempo. Además de inglés, el cuestionario de la encuesta está disponible en 8 idiomas adicionales: Bangla, Francés, Hindi, Japonés, Mandarín, Portugués, Ruso y Español.

Sigue el enlace para comenzar: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.


### Lanzamiento de NumPy 1.21.0

_23 de junio de 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html) ya está disponible. Los aspectos más destacados de esta versión son:

- trabajo SIMD continuo que cubre más funciones y plataformas,
- trabajo inicial sobre la nueva infraestructura dtype y conversiones de tipo,
- ruedas universal2 para Python 3.8 y Python 3.9 en Mac,
- documentación mejorada,
- anotaciones mejoradas,
- nuevo `PCG64DXSM` generador de bits para números aleatorios.

Esta versión de NumPy es el resultado de 581 solicitudes de incorporación de cambios contribuidas por 175 personas.  Las versiones de Python soportadas por este lanzamiento son las 3.7-3.9, se añadirá soporte para Python 3.10 después del lanzamiento de Python 3.10.


### Resultados de la encuesta de NumPy de 2020

_22 de junio de 2021_ -- En 2020, el equipo de encuestas de NumPy, en asociación con los estudiantes y profesores de la Universidad de Michigan y la Universidad de Maryland, realizó la primera encuesta oficial de la comunidad NumPy. Encuentra los resultados de la encuesta aquí: https://numpy.org/user-survey-2020/.


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


### NumPy recibe una subvención de la Iniciativa Chan Zuckerberg

_15 de noviembre de 2019_ -- Nos complace anunciar que NumPy y OpenBLAS, una de las dependencias clave de NumPy, han recibido una subvención conjunta por $195,000 de la Iniciativa Chan Zuckerberg a través de su [programa Esencial de Software Abierto para la Ciencia](https://chanzuckerberg.com/eoss/) que apoya el mantenimiento de software, crecimiento, desarrollo y compromiso comunitario para herramientas de código abierto críticas para la ciencia.

Esta subvención se utilizará para acelerar los esfuerzos en la mejora de la documentación de NumPy, rediseño del sitio web y desarrollo de la comunidad para servir mejor a nuestra amplia y creciente base de usuarios, y asegurar la sostenibilidad a largo plazo del proyecto. Mientras que el equipo de OpenBLAS se enfocará en abordar conjuntos de problemas técnicos clave, en particular la seguridad de los hilos, AVX-512, y problemas de almacenamiento local de hilos (TLS), así como mejoras algorítmicas en ReLAPACK (Recursive LAPACK) de las que depende OpenBLAS.

Puede encontrar más detalles sobre nuestras iniciativas y entregables propuestos en la [propuesta completa de subvención](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). Está previsto que el trabajo comience el 1 de diciembre de 2019 y continúe durante los siguientes 12 meses.


<a name="releases"></a>

## Lanzamientos

Esta es una lista de lanzamientos NumPy, con enlaces a notas de lanzamiento. Los lanzamientos de corrección de errores (solo cambia la `z` en el número de versión `x.y.z`) no tienen nuevas características; las versiones menores (aumenta la `y`) sí las tienen.

- NumPy 2.0.1 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v2.0.1)) -- _21 de julio de 2024_.
- NumPy 2.0.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v2.0.0)) -- _16 de junio de 2024_.
- NumPy 1.26.4 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.26.4)) -- _5 de febrero de 2024_.
- NumPy 1.26.3 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.26.3)) -- _2 de enero de 2024_.
- NumPy 1.26.2 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _12 de noviembre de 2023_.
- NumPy 1.26.1 ([notas de publicación](https://github.com/numpy/numpy/releases/tag/v1.26.1)) -- _14 Oct 2023_.
- NumPy 1.26.0 ([notas de publicación](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _16 Sep 2023_.
- NumPy 1.25.2 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.25.2)) -- _31 de julio de 2023_.
- NumPy 1.25.1 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.25.1)) -- _8 de julio de 2023_.
- NumPy 1.24.4 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.24.4)) -- _26 de junio de 2023_.
- NumPy 1.25.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.25.0)) -- _17 de junio de 2023_.
- NumPy 1.24.3 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.24.3)) -- _22 de abril de 2023_.
- NumPy 1.24.2 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.24.2)) -- _5 de febrero de 2023_.
- NumPy 1.24.1 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.24.1)) -- _26 de diciembre de 2022_.
- NumPy 1.24.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.24.0)) -- _18 de diciembre de 2022_.
- NumPy 1.23.5 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.26.0)) -- _19 de noviembre de 2022_.
- NumPy 1.23.4 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.23.4)) -- _12 de octubre de 2022_.
- NumPy 1.23.3 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.23.3)) -- _9 de septiembre de 2022_.
- NumPy 1.23.2 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.23.2)) -- _14 de agosto de 2022_.
- NumPy 1.23.1 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.23.1)) -- _8 de julio de 2022_.
- NumPy 1.23.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.23.0)) -- _22 de junio de 2022_.
- NumPy 1.22.4 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.22.4)) -- _20 de mayo de 2022_.
- NumPy 1.21.6 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.21.6)) -- _12 de abril de 2022_.
- NumPy 1.22.3 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.22.3)) -- _7 de marzo de 2022_.
- NumPy 1.22.2 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.22.2)) -- _3 de febrero de 2022_.
- NumPy 1.22.1 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.22.1)) -- _14 de enero de 2022_.
- NumPy 1.22.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.22.0)) -- _31 de diciembre de 2021_.
- NumPy 1.21.5 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.21.5)) -- _19 de diciembre de 2021_.
- NumPy 1.21.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.21.0)) -- _22 de junio de 2021_.
- NumPy 1.20.3 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.20.3)) -- _10 de mayo de 2021_.
- NumPy 1.20.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.20.0)) -- _30 de enero de 2021_.
- NumPy 1.19.5 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.19.5)) -- _5 de enero de 2021_.
- NumPy 1.19.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.19.0)) -- _20 de junio de 2020_.
- NumPy 1.18.4 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.18.4)) -- _3 de mayo de 2020_.
- NumPy 1.17.5 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.17.5)) -- _1 de enero de 2020_.
- NumPy 1.18.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.18.0)) -- _22 de diciembre de 2019_.
- NumPy 1.17.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.17.0)) -- _26 de julio de 2019_.
- .
- NumPy 1.15.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.15.0)) -- _23 de julio de 2018_.
- NumPy 1.14.0 ([notas del lanzamiento](https://github.com/numpy/numpy/releases/tag/v1.14.0)) -- _7 de enero de 2018_.
