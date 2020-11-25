---
title: "Estudo de Caso: Descoberta de Ondas Gravitacionais"
sidebar: false
---

{{< figure src="/images/content_images/cs/gw_sxs_image.png" class="fig-center" caption="**Ondas gravitacionais**" alt="binary coalesce black hole generating gravitational waves" attr="*(Créditos de imagem: O projeto Simulating eXtreme Spacetimes (SXS) no LIGO)*" attrlink="https://youtu.be/Zt8Z_uzG71o" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>O ecossistema científico Python é uma infraestrutura crítica para a pesquisa feita no LIGO.</p>
    <footer align="right">David Shoemaker, <cite>Colaborador Científico no LIGO</cite></footer>
</blockquote>

## Sobre [Ondas Gravitacionais](https://www.nationalgeographic.com/news/2017/10/what-are-gravitational-waves-ligo-astronomy-science/) e o [LIGO](https://www.ligo.caltech.edu)

Ondas gravitacionais são ondulações no tecido espaço-tempo, gerado por eventos cataclísmicos no universo, como colisão e fusão de dois buracos negros ou a coalescência de estrelas binárias ou supernovas. A observação de ondas gravitacionais pode ajudar não só no estudo da gravidade, mas também no entendimento de alguns dos fenômenos obscuros existentes no universo distante e seu impacto.

O [Observatório Interferômetro Laser de Ondas Gravitacionais (LIGO)](https://www.ligo.caltech.edu) foi projetado para abrir o campo da astrofísica das ondas gravitacionais através da detecção direta de ondas gravitacionais previstas pela Teoria Geral da Relatividade de Einstein. O observatório consiste de dois interferômetros amplamente separados dentro dos Estados Unidos - um em Hanford, Washington e o outro em Livingston, Louisiana — operando em uníssono para detectar ondas gravitacionais. Cada um deles tem detectores em escala quilométrica de ondas gravitacionais que usam interferometria laser.  A Colaboração Científica LIGO (LSC), é um grupo de mais de 1000 cientistas de universidades dos Estados Unidos e em 14 outros países apoiados por mais de 90 universidades e institutos de pesquisa; aproximadamente 250 estudantes contribuem ativamente com a colaboração. A nova descoberta do LIGO é a primeira observação de ondas gravitacionais em si, feita medindo os pequenos distúrbios que as ondas fazem ao espaço-tempo enquanto atravessam a terra.  A descoberta abriu novas fronteiras astrofísicas que exploram o lado "curvado" do universo - objetos e fenômenos que são feitos a partir da curvatura do espaço-tempo.


### Objetivos

* Embora sua [missão](https://www.ligo.caltech.edu/page/what-is-ligo) seja detectar ondas gravitacionais de alguns dos processos mais violentos e enérgicos no Universo, os dados que o LIGO coleta podem ter efeitos de grande alcance em muitas áreas da física, incluindo gravitação, relatividade, astrofísica, cosmologia, física de partículas e física nuclear.
* Processar dados observados através de cálculos numéricos de relatividade que envolvem matemática complexa para identificar o sinal e o ruído, filtrar o sinal relevante e estimar estatisticamente o significado dos dados observados.
* Visualização de dados para que os resultados binários/numéricos possam ser compreendidos.



### Desafios

* **Computação**

    As ondas gravitacionais são difíceis de detectar pois produzem um efeito muito pequeno e têm uma pequena interação com a matéria. Processar e analisar todos os dados do LIGO requer uma vasta infraestrutura de computação. Depois de cuidar do ruído, que é bilhões de vezes maior que o sinal, ainda há equações de relatividade complexas e enormes quantidades de dados que apresentam um desafio computacional: [O(10^7) horas de CPU necessárias para análises de fusão binária](https://youtu.be/7mcHknWWzNI) espalhado em 6 clusters LIGO dedicados.

* **Sobrecarga de dados**

    À medida que os dispositivos observacionais se tornam mais sensíveis e confiáveis, os desafios criados pela sobrecarga de dados e a procura por uma agulha em um palheiro se tornam muito maiores. O LIGO gera terabytes de dados todos os dias! Entender esses dados requer um enorme esforço para cada detecção. Por exemplo, os sinais sendo coletados pelo LIGO devem ser combinados por supercomputadores e comparados a centenas de milhares de modelos de possíveis assinaturas de ondas gravitacionais.

* **Visualização**

    Uma vez que os obstáculos relacionados a compreender as equações de Einstein bem o suficiente para resolvê-las usando supercomputadores foram ultrapassados, o próximo grande desafio era tornar os dados compreensíveis para o cérebro humano. A modelagem de simulações, assim como a detecção de sinais, exigem técnicas de visualização efetiva.  A visualização também desempenha um papel de fornecer mais credibilidade à relatividade numérica aos olhos dos aficionados pela ciência pura, que não dão importância suficiente à relatividade numérica até que a imagem e as simulações tornem mais fácil a compreensão dos resultados para um público maior. A velocidade da computação complexa, e da renderização, re-renderização de imagens e simulações usando as últimas entradas e informações experimentais pode ser uma atividade demorada que desafia pesquisadores neste domínio.

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="gravitational waves strain amplitude" caption="**Estimated gravitational-wave strain amplitude from GW150914**" attr="(**Graph Credits:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## NumPy’s Role in the Detection of Gravitational Waves

Gravitational waves emitted from the merger cannot be computed using any technique except brute force numerical relativity using supercomputers. The amount of data LIGO collects is as incomprehensibly large as gravitational wave signals are small.

NumPy, the standard numerical analysis package for Python,  was utilized by the software used for various tasks performed during the GW detection project at LIGO. NumPy helped in solving complex maths and data manipulation at high speed.  Here are some examples:

* [Signal Processing](https://www.uv.es/virgogroup/Denoising_ROF.html): Glitch detection,  [Noise identification and Data Characterization](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, pyCharm)
* Data retrieval: Deciding which data can be analyzed, figuring out whether it contains a signal - needle in a haystack
* Statistical analysis: estimate the statistical significance of observational data, estimating the signal parameters (e.g. masses of stars, spin velocity, and distance) by comparison with a model.
* Visualization of data
  - Time series
  - Spectrograms
* Compute Correlations
* Key [Software](https://github.com/lscsoft) developed in GW data analysis such as [GwPy](https://gwpy.github.io/docs/stable/overview.html) and [PyCBC](https://pycbc.org) uses NumPy and AstroPy under the hood for providing object based interfaces to utilities, tools, and methods for studying data from gravitational-wave detectors.

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy depgraph" caption="**Dependency graph showing how GwPy package depends on NumPy**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy depgraph" caption="**Dependency graph showing how PyCBC package depends on NumPy**" >}}

## Summary

GW detection has enabled researchers to discover entirely unexpected phenomena while providing new insight into many of the most profound astrophysical phenomena known. Number crunching and data visualization is a crucial step that helps scientists gain insights into data gathered from the scientific observations and understand the results. The computations are complex and cannot be comprehended by humans unless it is visualized using computer simulations that are fed with the real observed data and analysis.  NumPy along with other Python packages such as matplotlib, pandas, and scikit-learn is [enabling researchers](https://www.gw-openscience.org/events/GW150914/) to answer complex questions and discover new horizons in our understanding of the universe.

{{< figure src="/images/content_images/cs/numpy_gw_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}
