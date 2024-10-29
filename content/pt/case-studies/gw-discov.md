---
title: "Estudo de Caso: Descoberta de Ondas Gravitacionais"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/gw_sxs_image.png'
title = 'Gravitational Waves'
alt = 'binary coalesce black hole generating gravitational waves'
attribution = '(Image Credits: The Simulating eXtreme Spacetimes (SXS) Project at LIGO)'
attributionlink = 'https://youtu.be/Zt8Z_uzG71o'
{{< /figure >}}

{{< blockquote
cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
by="David Shoemaker, _LIGO Scientific Collaboration_" >}}
The scientific Python ecosystem is critical infrastructure for the research done at LIGO.
{{< /blockquote >}}

## About [Gravitational Waves](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) and [LIGO](https://www.ligo.caltech.edu)

Ondas gravitacionais são ondulações no tecido espaço-tempo, geradas por eventos cataclísmicos no universo, como a colisão e a fusão de dois buracos negros ou a coalescência de estrelas binárias ou supernovas. A observação de ondas gravitacionais pode ajudar não só no estudo da gravidade, mas também no entendimento de alguns dos fenômenos obscuros existentes no universo distante e seu impacto.

The [Laser Interferometer Gravitational-Wave Observatory (LIGO)](https://www.ligo.caltech.edu)
was designed to open the field of gravitational-wave astrophysics through the
direct detection of gravitational waves predicted by Einstein’s General Theory
of Relativity. O observatório consiste de dois interferômetros amplamente separados dentro dos Estados Unidos - um em Hanford, Washington e o outro em Livingston, Louisiana — operando em uníssono para detectar ondas gravitacionais. Cada um deles tem detectores em escala quilométrica de ondas gravitacionais que usam interferometria laser.  A Colaboração Científica LIGO (LSC), é um grupo de mais de 1000 cientistas de universidades dos Estados Unidos e em 14 outros países apoiados por mais de 90 universidades e institutos de pesquisa; aproximadamente 250 estudantes contribuem ativamente com a colaboração. A nova descoberta do LIGO é a primeira observação de ondas gravitacionais em si, feita medindo os pequenos distúrbios que as ondas fazem ao espaço-tempo enquanto atravessam a Terra.  A descoberta abriu novas fronteiras astrofísicas que exploram o lado "curvado" do universo - objetos e fenômenos que são feitos a partir da curvatura do espaço-tempo.

### Objetivos

- Though its [mission](https://www.ligo.caltech.edu/page/what-is-ligo) is to
  detect gravitational waves from some of the most violent and energetic
  processes in the Universe, the data LIGO collects may have far-reaching
  effects on many areas of physics including gravitation, relativity,
  astrophysics, cosmology, particle physics, and nuclear physics.
- Crunch observed data via numerical relativity computations that involves
  complex maths in order to discern signal from noise, filter out relevant
  signal and statistically estimate significance of observed data
- Data visualization so that the binary / numerical results can be
  comprehended.

### Desafios

- **Computation**

  Gravitational Waves are hard to detect as they produce a very small effect
  and have tiny interaction with matter. Processing and analyzing all of
  LIGO's data requires a vast computing infrastructure.After taking care of
  noise, which is billions of times of the signal, there is still very
  complex relativity equations and huge amounts of data which present a
  computational challenge:
  [O(10^7) CPU hrs needed for binary merger analyses](https://youtu.be/7mcHknWWzNI)
  spread on 6 dedicated LIGO clusters

- **Data Deluge**

  As observational devices become more sensitive and reliable, the challenges
  posed by data deluge and finding a needle in a haystack rise multi-fold.
  O LIGO gera terabytes de dados todos os dias! Making sense of this data
  requires an enormous effort for each and every detection. For example, the
  signals being collected by LIGO must be matched by supercomputers against
  hundreds of thousands of templates of possible gravitational-wave signatures.

- **Visualization**

  Once the obstacles related to understanding Einstein’s equations well
  enough to solve them using supercomputers are taken care of, the next big
  challenge was making data comprehensible to the human brain. Simulation
  modeling as well as  signal detection requires effective visualization
  techniques.  Visualization also plays a role in lending more credibility
  to numerical relativity in the eyes of pure science aficionados, who did
  not give enough importance to numerical relativity until imaging and
  simulations made it easier to comprehend results for a larger audience.
  Speed of complex computations and rendering, re-rendering images and
  simulations using latest experimental inputs and insights can be a time
  consuming activity that challenges researchers in this domain.

{{< figure >}}
src = '/images/content_images/cs/gw_strain_amplitude.png'
alt = 'gravitational waves strain amplitude'
title = 'Estimated gravitational-wave strain amplitude from GW150914'
attribution = '(Graph Credits: Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)'
attributionlink = 'https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger'
{{< /figure >}}

## O papel do NumPy na detecção de ondas gravitacionais

Ondas gravitacionais emitidas da fusão não podem ser calculadas usando nenhuma técnica a não ser relatividade numérica por força bruta usando supercomputadores.
A quantidade de dados que o LIGO coleta é imensa tanto quanto os sinais de ondas gravitacionais são pequenos.

NumPy, o pacote padrão de análise numérica para Python, foi parte do software utilizado para várias tarefas executadas durante o projeto de detecção de ondas gravitacionais no LIGO. O NumPy ajudou a resolver problemas matemáticos e de manipulação de dados complexos em alta velocidade.  Aqui estão alguns exemplos:

- [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch
  detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf)
  (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
- Data retrieval: Deciding which data can be analyzed, figuring out whether it
  contains a signal - needle in a haystack
- Statistical analysis: estimate the statistical significance of observational
  data, estimating the signal parameters (e.g. masses of stars, spin velocity,
  and distance) by comparison with a model.
- Visualização de dados
  - Séries temporais
  - Espectrogramas
- Cálculo de correlações
- Key [Software](https://github.com/lscsoft) developed in GW data analysis
  such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and
  [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for
  providing object based interfaces to utilities, tools, and methods for
  studying data from gravitational-wave detectors.

{{< figure >}}
src = '/images/content_images/cs/gwpy-numpy-dep-graph.png'
alt = 'gwpy-numpy depgraph'
title = 'Dependency graph showing how GwPy package depends on NumPy'
{{< /figure >}}

----

{{< figure >}}
src = '/images/content_images/cs/PyCBC-numpy-dep-graph.png'
alt = 'PyCBC-numpy depgraph'
title = 'Dependency graph showing how PyCBC package depends on NumPy'
{{< /figure >}}

## Resumo

A detecção de ondas gravitacionais permitiu que pesquisadores descobrissem fenômenos totalmente inesperados ao mesmo tempo em que proporcionaram novas idéias sobre muitos dos fenômenos mais profundos conhecidos na astrofísica. O processamento e a visualização de dados é um passo crucial que ajuda cientistas a obter informações coletadas de observações científicas e a entender os resultados. Os cálculos são complexos e não podem ser compreendidos por humanos a não ser que sejam visualizados usando simulações de computador que são alimentadas com dados e análises reais observados.  NumPy
along with other Python packages such as matplotlib, pandas, and scikit-learn
is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to
answer complex questions and discover new horizons in our understanding of the
universe.

{{< figure >}}
src = '/images/content_images/cs/numpy_gw_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
