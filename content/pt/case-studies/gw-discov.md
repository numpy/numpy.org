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

O [Observatório Interferômetro Laser de Ondas Gravitacionais (LIGO)](https://www.ligo.caltech.edu) foi projetado para abrir o campo da astrofísica das ondas gravitacionais através da detecção direta de ondas gravitacionais previstas pela Teoria Geral da Relatividade de Einstein. O observatório consiste de dois interferômetros amplamente separados dentro dos Estados Unidos - um em Hanford, Washington e o outro em Livingston, Louisiana — operando em uníssono para detectar ondas gravitacionais. Cada um deles tem detectores em escala quilométrica de ondas gravitacionais que usam interferometria laser.  A Colaboração Científica LIGO (LSC), é um grupo de mais de 1000 cientistas de universidades dos Estados Unidos e em 14 outros países apoiados por mais de 90 universidades e institutos de pesquisa; aproximadamente 250 estudantes contribuem ativamente com a colaboração. A nova descoberta do LIGO é a primeira observação de ondas gravitacionais em si, feita medindo os pequenos distúrbios que as ondas fazem ao espaço-tempo enquanto atravessam a Terra.  A descoberta abriu novas fronteiras astrofísicas que exploram o lado "curvado" do universo - objetos e fenômenos que são feitos a partir da curvatura do espaço-tempo.


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

{{< figure src="/images/content_images/cs/gw_strain_amplitude.png" class="fig-center" alt="gravitational waves strain amplitude" caption="**Amplitude estimada da deformação das ondas gravitacionais do evento GW150914**" attr="(**Créditos do gráfico:** Observation of Gravitational Waves from a Binary Black Hole Merger, ResearchGate Publication)" attrlink="https://www.researchgate.net/publication/293886905_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger" >}}

## O papel da NumPy na detecção de ondas gravitacionais

Ondas gravitacionais emitidas da fusão não podem ser calculadas usando nenhuma técnica a não ser relatividade numérica por força bruta usando supercomputadores. A quantidade de dados que o LIGO coleta é imensa tanto quanto os sinais de ondas gravitacionais são pequenos.

NumPy, o pacote padrão de análise numérica para Python, foi parte do software utilizado para várias tarefas executadas durante o projeto de detecção de ondas gravitacionais no LIGO. A NumPy ajudou a resolver problemas matemáticos e de manipulação de dados complexos em alta velocidade.  Aqui estão alguns exemplos:

* [Processamento de sinais](https://www.uv.es/virgogroup/Denoising_ROF.html): Detecção de falhas,  [Identificação de ruídos e caracterização de dados](https://ep2016.europython.eu/media/conference/slides/pyhton-in-gravitational-waves-research-communities.pdf) (NumPy, scikit-learn, scipy, matplotlib, pandas, PyCharm)
* Recuperação de dados: Decidir quais dados podem ser analisados, compreender se os dados contém um sinal - como uma agulha em um palheiro
* Análise estatística: estimar o significado estatístico dos dados observados, estimando os parâmetros do sinal (por exemplo, massa de estrelas, velocidade de giro e distância) em comparação com um modelo.
* Visualização de dados
  - Séries temporais
  - Espectrogramas
* Cálculo de correlações
* [Software](https://github.com/lscsoft) fundamental desenvolvido na análise de ondas gravitacionais, como [GwPy](https://gwpy.github.io/docs/stable/overview.html) e [PyCBC](https://pycbc.org) usam NumPy e AstroPy internamente para fornecer interfaces baseadas em objetos para utilidades, ferramentas e métodos para o estudo de dados de detectores de ondas gravitacionais.

{{< figure src="/images/content_images/cs/gwpy-numpy-dep-graph.png" class="fig-center" alt="gwpy-numpy depgraph" caption="**Grafo de dependências mostrando como o pacote GwPy depended da NumPy**" >}}

----

{{< figure src="/images/content_images/cs/PyCBC-numpy-dep-graph.png" class="fig-center" alt="PyCBC-numpy depgraph" caption="**Grafo de dependências mostrando como o pacote PyCBC depended da NumPy**" >}}

## Resumo

A detecção de ondas gravitacionais permitiu que pesquisadores descobrissem fenômenos totalmente inesperados ao mesmo tempo em que proporcionaram novas idéias sobre muitos dos fenômenos mais profundos conhecidos na astrofísica. O processamento e a visualização de dados é um passo crucial que ajuda cientistas a obter informações coletadas de observações científicas e a entender os resultados. Os cálculos são complexos e não podem ser compreendidos por humanos a não ser que sejam visualizados usando simulações de computador que são alimentadas com dados e análises reais observados.  A NumPy, junto com outras bibliotecas Python, como matplotlib, pandas, e scikit-learn [permitem que pesquisadores](https://www.gw-openscience.org/events/GW150914/) respondam perguntas complexas e descubram novos horizontes em nossa compreensão do universo.

{{< figure src="/images/content_images/cs/numpy_gw_benefits.png" class="fig-center" alt="numpy benefits" caption="**Recursos chave da NumPy utilizados**" >}}
