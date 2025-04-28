---
title: Noticias
sidebar: false
newsHeader: ¡NumPy 2.2.0 ha sido lanzado!
date: 2024-06-17
---

### Lanzamiento de NumPy 2.2.0

_8 Dec, 2024_ -- The NumPy 2.2.0 release is a quick release that brings us back
into sync with the usual twice yearly release cycle. Ha habido varias pequeñas limpiezas, mejoras en el tipo StringDType y un mejor soporte para Python de hilos libres. Los puntos destacados son:

- New functions `matvec` and `vecmat`,
- Muchas anotaciones mejoradas,
- Mejor soporte para el nuevo StringDType,
- Mejor soporte para Python libre de hilos
- Correcciones para f2py.

Esta versión es compatible con versiones de Python 3.10-3.13.

### Lanzamiento de NumPy 2.1.0

_18 Aug, 2024_ -- NumPy 2.1.0 provides support for Python 3.13 and
drops support for Python 3.9. Además de las habituales correcciones de errores y
soporte actualizado de Python, ayuda a que NumPy vuelva a su ciclo de publicación habitual
después del extenso desarrollo de 2.0. Los aspectos más destacados son:

- Soporte para Python 3.13.
- Soporte preliminar para Python 3.13 de hilos libres.
- Compatibilidad con la norma array-api 2023.12.

Esta versión es compatible con las versiones 3.10-3.13 de Python.

### Lanzamiento de NumPy 2.0.0

_16 Jun, 2024_ -- NumPy 2.0.0 is the first major release since 2006. Es el resultado
de 11 meses de desarrollo desde el último lanzamiento de características y es el trabajo
de 212 colaboradores distribuidos entre 1078 solicitudes de incorporación de cambios. Contiene un gran número de nuevas características interesantes, así como cambios en las APIs de Python y C.  Incluye cambios importantes que no podrían producirse en un lanzamiento menor regular, como una ruptura de ABI, cambios en las reglas de promoción de tipos y cambios en la API que podrían no haber estado emitiendo advertencias de obsolescencia en la versión 1.26.x. Los documentos clave
relacionados con cómo adaptarse a los cambios en NumPy 2.0 incluyen:

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

The blog post ["NumPy 2.0: an evolutionary milestone"](https://blog.scientific-python.org/numpy/numpy2/)
tells a bit of the story about how this release came together.

### Fecha de lanzamiento de NumPy 2.0: 16 de junio

_23 May, 2024_ -- We are excited to announce that NumPy 2.0 is planned to be
released on June 16, 2024. Esta publicación lleva más de un año en proceso y
es el primer lanzamiento importante desde 2006. Importantly, in addition to many new
features and performance improvement, it contains **breaking changes** to the
ABI as well as the Python and C APIs. It is likely that downstream packages and
end user code needs to be adapted - if you can, please verify whether your code
works with NumPy `2.0.0rc2`. **Please see the following for more details:**

- The [NumPy 2.0 migration guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- The [2.0.0 release notes](https://numpy.org/devdocs/release/2.0.0-notes.html)
- Announcement issue for status updates: [numpy#24300](https://github.com/numpy/numpy/issues/24300)

### Recaudación de fondos de fin de año de NumFOCUS

_Dec 19, 2023_ -- NumFOCUS has teamed up with PyCharm during their EOY campaign to offer a 30% discount
on first-time PyCharm licenses. Todos los ingresos del primer año de las compras de PyCharm desde ahora hasta el 23 de diciembre de 2023 se destinarán directamente a los programas de NumFOCUS.

Use unique URL that will allow to track purchases https://lp.jetbrains.com/support-data-science/
or a coupon code ISUPPORTDATASCIENCE

### NumPy 1.26.0 ha sido lanzado

_Sep 16, 2023_ -- [NumPy 1.26.0](https://numpy.org/doc/stable/release/1.26.0-notes.html)
is now available. Los aspectos más destacados del lanzamiento son:

- Soporte de Python 3.12.0.
- Compatibilidad con Cython 3.0.0.
- Utilización del sistema de compilación Meson
- Actualización del soporte de SIMD
- Correcciones de f2py, meson y soporte de bind(x)
- Soporte para la librería actualizada Accelerate BLAS/LAPACK

La versión 1.26.0 de NumPy es la continuación de la serie 1.25.x que marca la transición al sistema de compilación Meson y que provee soporte para Cython 3.0.0.
Un total de 20 personas contribuyeron a esta versión y 59 solicitudes de cambios fueron fusionadas.

Las versiones de Python compatibles con esta versión son 3.9-3.12.

### numpy.org ya está disponible en japonés y portugués

_Aug 2, 2023_ -- numpy.org is now available in 2 additional languages:
Japanese and Portuguese. Esto no sería posible sin nuestros dedicados voluntarios:

_Portuguese:_

- Melissa Weber Mendonça (melissawm)
- Precios Ricardo (ricardoprins)
- Getúlio Silva (getuliosilva)
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

El trabajo sobre la infraestructura de traducción se apoya con fondos de CZI.

De cara al futuro, nos encantaría traducir el sitio web a más idiomas.
Si quieres ayudar, por favor pone en contacto con el equipo de traducciones de NumPy en Slack:
https://join.slack.com/t/numpy-team/shared_invite/zt-1gokbq56s-bvEpo10Ef7aHbVtVFeZv2w.
(Busca el canal #translations) También estamos formando un equipo de traducciones que estará trabajando en la localización de la documentación y el contenido educativo a través de todo el ecosistema de Python científico. Si esto ha despertado tu interés, únete a nosotros en el Discord de Python científico: https://discord.gg/khWtqY6RKr. (Busca el canal #translations)

### NumPy 1.25.0 ha sido lanzado

_Jun 17, 2023_ -- [NumPy 1.25.0](https://numpy.org/doc/stable/release/1.25.0-notes.html)
is now available. Los aspectos más destacados del lanzamiento son:

- Soporte para MUSL, ahora hay ruedas MUSL.
- Soporte para el compilador de Fujitsu C/C++.
- Los arreglos de objetos ahora están soportadas en einsum.
- Support for the inplace matrix multiplication (`@=`).

NumPy 1.25. continúa el trabajo en curso para mejorar el manejo y
promoción de dtypes, aumentar la velocidad de ejecución y clarificar la documentación. También se ha realizado trabajo preparatorio para el futuro NumPy 2.0.0, resultando en un gran número de nuevas y eliminadas obsolescencias.

Un total de 148 personas contribuyeron a esta versión y 530 solicitudes de incorporación de cambios fueron aceptadas.

Las versiones de Python soportadas por este lanzamiento son
3.9-3.11.

### Fomentar una Cultura Inclusiva: Convocatoria de Participación

_May 10, 2023_ -- Fostering an Inclusive Culture: Call for Participation

¿Cómo podemos ser mejores cuando se trata de diversidad e inclusión?
Read the report and find out how to get involved
[here](https://contributor-experience.org/docs/posts/dei-report/).

### Transición en el liderazgo del equipo de documentación de NumPy

_Jan 6, 2023_ –- Mukulika Pahari and Ross Barnowski are appointed as the new NumPy
documentation team leads replacing Melissa Mendonça. Damos las gracias a Melissa por todas sus
contribuciones a la documentación oficial de NumPy y materiales educativos,
y a Mukulika y Ross por asumir este rol.

### Lanzamiento de NumPy 1.24.0

_Dec 18, 2022_ -- [NumPy 1.24.0](https://numpy.org/doc/stable/release/1.24.0-notes.html)
is now available. Los aspectos más destacados del lanzamiento son:

- Nuevas palabras clave "dtype" y "casting" para las funciones de apilamiento.
- Nuevas características y correcciones de F2PY.
- Muchas nuevas obsolescencias, revísalas.
- Muchas obsolescencias caducadas,

El lanzamiento de NumPy 1.24.0 continúa el trabajo en curso para mejorar el manejo y
promoción de dtypes, aumentar la velocidad de ejecución y clarificar la documentación.
Hay un gran número de obsolescencias nuevas y caducadas debido a los cambios en la limpieza y promoción de tipo dtype. Es el trabajo de 177 colaboradores distribuidos sobre
444 solicitudes de incorporación de cambios. Las versiones Python soportadas son 3.8-3.11.

### NumPy 1.23.0 ha sido lanzado

_Jun 22, 2022_ -- [NumPy 1.23.0](https://numpy.org/doc/stable/release/1.23.0-notes.html)
is now available. Los aspectos más destacados del lanzamiento son:

- Implementation of `loadtxt` in C, greatly improving its performance.
- Exposición de DLPack a nivel Python para facilitar el intercambio de datos.
- Cambios a la promoción y comparación de dtypes estructurados.
- Mejoras a f2py.

El lanzamiento de NumPy 1.23.0 continúa el trabajo en curso para mejorar el manejo y
promoción de dtypes, aumentar la velocidad de ejecución y clarificar la documentación, caducar viejas obsolescencias. Es el trabajo de 151 colaboradores distribuidos sobre
494 solicitudes de incorporación de cambios. Las versiones de Python soportadas por este lanzamiento son
3.8-3.10.
Python 3.11 será soportado cuando alcance la etapa rc.

### Estudio de investigación NumFOCUS DEI: llamado a participar

_Apr 13, 2022_ -- NumPy is working with [NumFOCUS](http://numfocus.org/) on a
research project
funded by the Gordon & Betty Moore Foundation to
understand the barriers to participation that contributors, particularly those
from historically underrepresented groups, face in the open-source software
community. El equipo de investigación quisiera hablar con nuevos colaboradores, desarrolladores y mantenedores del proyecto, y con aquellos que han contribuido en el pasado acerca de
sus experiencias uniéndose y contribuyendo a NumPy.

**Interested in sharing your experiences?**

Please complete this brief [“Participant Interest” form](https://numfocus.typeform.com/to/WBWVJSqe)
which contains additional information on the research goals, privacy, and
confidentiality considerations. Tu participación será valiosa para el crecimiento
y la sostenibilidad de comunidades de software de código abierto diversas e inclusivas. Los participantes aceptados participarán en una entrevista de 30 minutos con un miembro del equipo de investigación.

### Lanzamiento de NumPy 1.22.0

_Dec 31, 2021_ -- [NumPy 1.22.0](https://numpy.org/doc/stable/release/1.22.0-notes.html)
is now available. Los aspectos más destacados del lanzamiento son:

- Las anotaciones de tipo del espacio de nombres principal están esencialmente completas. Upstream is
  a moving target, so there will likely be further improvements, but the major
  work is done. This is probably the most user visible enhancement in this
  release.
- A preliminary version of the proposed
  [array API Standard](https://data-apis.org/array-api/latest/) is provided
  (see [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html)).
  This is a step in creating a standard collection of functions that can be
  used across libraries such as CuPy and JAX.
- NumPy ahora tiene un backend de DLPack. DLPack provides a common interchange format
  for array (tensor) data.
- New methods for `quantile`, `percentile`, and related functions. The new
  methods provide a complete set of the methods commonly found in the
  literature.
- The universal functions have been refactored to implement most of
  [NEP 43](https://numpy.org/neps/nep-0043-extensible-ufuncs.html).
  Esto también desbloquea la capacidad de experimentar con la futura API DType.
- Un nuevo asignador de memoria configurable para el uso de proyectos dependientes o downstream.

NumPy 1.22.0 es un gran lanzamiento que contó con el trabajo de 153 colaboradores distribuidos
sobre 609 solicitudes de incorporación de cambios. Las versiones de Python soportadas por este lanzamiento son
3.8-3.10.

### Promoviendo una cultura inclusiva en el ecosistema científico de Python

_August 31, 2021_ -- We are happy to announce the Chan Zuckerberg Initiative has
[awarded a grant](https://chanzuckerberg.com/newsroom/czi-awards-16-million-for-foundational-open-source-software-tools-essential-to-biomedicine/)
to support the onboarding, inclusion, and retention of people from historically
marginalized groups on scientific Python projects, and to structurally improve
the community dynamics for NumPy, SciPy, Matplotlib, and Pandas.

As a part of [CZI's Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/),
this [Diversity & Inclusion supplemental grant](https://cziscience.medium.com/advancing-diversity-and-inclusion-in-scientific-open-source-eaabe6a5488b)
will support the creation of dedicated Contributor Experience Lead positions to
identify, document, and implement practices to foster inclusive open-source
communities. Este proyecto será liderado por Melissa Mendonça (NumPy), con mentoría y orientación adicionales por parte de Ralf Gommers (NumPy, SciPy),
Hannah Aizenman y Thomas Caswell (Matplotlib), Matt Haberland (SciPy), y
Joris Van den Bossche (Pandas).

Este es un proyecto ambicioso destinado a descubrir e implementar actividades que
deberían mejorar estructuralmente la dinámica comunitaria de nuestros proyectos. Al establecer estos nuevos roles entre proyectos, esperamos introducir un nuevo
modelo de colaboración para las comunidades de Python Científico, permitiendo que el trabajo de construcción de comunidades dentro del ecosistema se realice de manera más eficiente y con mejores resultados. También esperamos desarrollar una idea más clara tanto de lo que funciona y lo que no en nuestros proyectos, para atraer y retener nuevos colaboradores, especialmente de grupos históricamente subrepresentados. Finalmente, planeamos producir informes detallados sobre las acciones ejecutadas, explicando cómo éstas han impactado nuestros proyectos en términos de representación e interacción con nuestras comunidades.

Se espera que este proyecto, de dos años de duración, comience en noviembre de 2021, y estamos emocionados por ver los resultados de este trabajo!
[You can read the full proposal here](https://figshare.com/articles/online_resource/Advancing_an_inclusive_culture_in_the_scientific_Python_ecosystem/16548063).

### Encuesta de NumPy de 2021

_July 12, 2021_ -- At NumPy, we believe in the power of our community. 1,236 usuarios de NumPy de 75 países participaron en nuestra encuesta inaugural el año pasado.
Los resultados de la encuesta nos dieron una muy buena comprensión acerca de lo que debería ser nuestro enfoque durante los próximos 12 meses.

Es hora de otra encuesta, y contamos contigo una vez más. Te tomará alrededor de 15 minutos de tu tiempo. Además de inglés, el cuestionario de la encuesta está disponible en 8 idiomas adicionales: Bangla, Francés, Hindi, Japonés, Mandarín, Portugués, Ruso y Español.

Sigue el enlace para comenzar: https://berkeley.qualtrics.com/jfe/form/SV_aaOONjgcBXDSl4q.

### Lanzamiento de NumPy 1.21.0

_Jun 23, 2021_ -- [NumPy 1.21.0](https://numpy.org/doc/stable/release/1.21.0-notes.html)
is now available. Los aspectos más destacados del lanzamiento son:

- trabajo SIMD continuo que cubre más funciones y plataformas,
- trabajo inicial sobre la nueva infraestructura dtype y conversiones de tipo,
- universal2 wheels para Python 3.8 y Python 3.9 en Mac,
- documentación mejorada,
- anotaciones mejoradas,
- new `PCG64DXSM` bitgenerator for random numbers.

Esta versión de NumPy es el resultado de 581 solicitudes de incorporación de cambios contribuidas por 175 personas.  Las versiones de Python soportadas por este lanzamiento son las 3.7-3.9, se añadirá soporte para Python 3.10 después del lanzamiento de Python 3.10.

### Resultados de la encuesta de NumPy de 2020

_Jun 22, 2021_ -- In 2020, the NumPy survey team in partnership with students
and faculty from the University of Michigan and the University of Maryland
conducted the first official NumPy community survey. Encuentra los resultados de la encuesta
aquí: https://numpy.org/user-survey-2020/.

### Lanzamiento de NumPy 1.20.0

_Jan 30, 2021_ -- [NumPy 1.20.0](https://numpy.org/doc/stable/release/1.20.0-notes.html)
is now available. Este es el lanzamiento de NumPy más grande hasta la fecha, gracias a los más de 180 colaboradores. Las dos nuevas características más importantes son:

- Type annotations for large parts of NumPy, and a new `numpy.typing` submodule
  containing `ArrayLike` and `DtypeLike` aliases that users and downstream
  libraries can use when adding type annotations in their own code.
- Multi-platform SIMD compiler optimizations, with support for x86 (SSE,
  AVX), ARM64 (Neon), and PowerPC (VSX) instructions. This yielded significant
  performance improvements for many functions (examples:
  [sin/cos](https://github.com/numpy/numpy/pull/17587),
  [einsum](https://github.com/numpy/numpy/pull/18194)).

### Diversidad en el proyecto NumPy

_Sep 20, 2020_ -- We wrote a [statement on the state of, and discussion on social media around, diversity and inclusion in the NumPy project](/diversity_sep2020).

### Primer artículo oficial de NumPy publicado en Nature!

_Sep 16, 2020_ -- We are pleased to announce the publication of
[the first official paper on NumPy](https://www.nature.com/articles/s41586-020-2649-2)
as a review article in Nature. Esto llega 14 años después de la publicación de NumPy 1.0.
El documento cubre aplicaciones y conceptos fundamentales de programación de arreglos, el rico ecosistema científico de Python construido sobre NumPy, y los recientemente añadidos protocolos de arreglos que facilitan la interoperabilidad con librerías de arreglos y tensores externas, tales como CuPy, Dask y JAX.

### Python 3.9 está por llegar, ¿cuándo lanzará NumPy ruedas binarias?

_Sept 14, 2020_ -- Python 3.9 will be released in a few weeks. Si eres uno de los primeros en adoptar las más recientes versiones de Python, es posible que te sientas decepcionado al descubrir que NumPy (y otros paquetes binarios como SciPy) no tendrán ruedas binarias listas para el
día del lanzamiento. Es un esfuerzo importante el adaptar la infraestructura de compilación a una versión
nueva de Python y normalmente tarda unas cuantas semanas para que los paquetes aparezcan
en PyPI y conda-forge. En preparación para este evento, por favor asegúrese de

- update your `pip` to version 20.1 at least to support `manylinux2010` and
  `manylinux2014`
- use [`--only-binary=numpy`](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-only-binary) or `--only-binary=:all:` to prevent `pip` from
  trying to build from source.

### Lanzamiento de NumPy 1.19.2

_Sep 10, 2020_ -- NumPy
1.19.2 is now available.
This latest release in the 1.19 series fixes several bugs, prepares for the
upcoming Cython 3.x
release and pins
setuptools to keep distutils working while upstream modifications are ongoing.
Las wheels para aarch64 están construidas con la última versión de manylinux2014 que corrige
el problema de diferentes tamaños de página utilizados por diferentes distribuciones de linux.

### La encuesta inaugural de NumPy ya está disponible!

_Jul 2, 2020_ -- This survey is meant to guide and set priorities for
decision-making about the development of NumPy as software and as a community.
La encuesta está disponible en 8 idiomas adicionales además del Inglés:
Bangla, Hindi, Japonés, Mandarín, Portugués, Ruso, Español y Francés.

Please help us make NumPy better and take the survey
[here](https://umdsurvey.umd.edu/jfe/form/SV_8bJrXjbhXf7saAl).

### ¡NumPy tiene un nuevo logo!

_Jun 24, 2020_ -- NumPy now has a new logo:

<img
src="/images/logos/numpy_logo.svg"
alt="NumPy logo"
title="The new NumPy logo"
width=300>

El logo es una versión moderna del anterior, con un diseño más limpio. Gracias a
Isabela Presedo-Floyd por diseñar el nuevo logo, así como a Travis Vaught
por el viejo logo que nos sirvió tanto durante más de 15 años.

### Lanzamiento de NumPy 1.19.0

_Jun 20, 2020_ -- NumPy 1.19.0 is now available. Esta es el primer lanzamiento
sin soporte para Python 2, por lo que fue una "versión de limpieza". La versión mínima
soportada de Python es ahora Python 3.6. Una nueva característica importante es que
la infraestructura de generación de números aleatorios que fue introducida en NumPy 1.17.0 es ahora accesible desde Cython.

### Aceptación a Season of Docs

_May 11, 2020_ -- NumPy has been accepted as one of the mentor organizations for
the Google Season of Docs program. ¡Estamos entusiasmados de tener la oportunidad de trabajar con un redactor técnico para mejorar la documentación de NumPy una vez más! For more
details, please see
[the official Season of Docs site](https://developers.google.com/season-of-docs/) and our
[ideas page](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2020-Project-Ideas).

### Lanzamiento de NumPy 1.18.0

_Dec 22, 2019_ -- NumPy 1.18.0 is now available. Después de los grandes cambios en
1.17.0, este es un lanzamiento de consolidación. Es el último lanzamiento menor que
soportará Python 3.5. Highlights of the release includes the addition of basic
infrastructure for linking with 64-bit BLAS and LAPACK libraries, and a new C-API for `numpy.random`.

Please see the [release notes](https://github.com/numpy/numpy/releases/tag/v1.18.0) for more details.

### NumPy recibe una subvención de la Iniciativa Chan Zuckerberg

_Nov 15, 2019_ -- We are pleased to announce that NumPy and OpenBLAS, one of NumPy's key dependencies, have received a joint grant for $195,000 from the Chan Zuckerberg Initiative through their [Essential Open Source Software for Science program](https://chanzuckerberg.com/eoss/) that supports software maintenance, growth, development, and community engagement for open source tools critical to science.

Esta subvención se utilizará para acelerar los esfuerzos en la mejora de la documentación de NumPy, rediseño del sitio web y desarrollo de la comunidad para servir mejor a nuestra amplia y creciente base de usuarios, y asegurar la sostenibilidad a largo plazo del proyecto. Mientras que el equipo de OpenBLAS se enfocará en abordar conjuntos de problemas técnicos clave, en particular la seguridad de los hilos, AVX-512, y problemas de almacenamiento local de hilos (TLS), así como mejoras algorítmicas en ReLAPACK (Recursive LAPACK) de las que depende OpenBLAS.

More details on our proposed initiatives and deliverables can be found in the [full grant proposal](https://figshare.com/articles/Proposal_NumPy_OpenBLAS_for_Chan_Zuckerberg_Initiative_EOSS_2019_round_1/10302167). Está previsto que el trabajo comience el 1 de diciembre de 2019 y continúe durante los siguientes 12 meses.

<a name="releases"></a>

## Lanzamientos

Esta es una lista de lanzamientos NumPy, con enlaces a notas de lanzamiento. Bugfix
releases (only the `z` changes in the `x.y.z` version number) have no new
features; minor releases (the `y` increases) do.

- NumPy 2.2.5 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.5)) -- _19 Apr 2025_.
- NumPy 2.2.4 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.4)) -- _16 Mar 2025_.
- NumPy 2.2.3 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.3)) -- _13 Feb 2025_.
- NumPy 2.2.2 ([release notes](https://github.com/numpy/numpy/releases/tag/v2.2.2)) -- _18 Jan 2025_.
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
