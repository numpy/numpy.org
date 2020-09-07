---
title: "Estudo de Caso: A Primeira Imagem de um Buraco Negro"
sidebar: false
---

{{< figure src="/images/content_images/cs/blackhole.jpg" caption="**Black Hole M87**" alt="black hole image" attr="*(Créditos: Event Horizon Telescope Collaboration)*" attrlink="https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>Criar uma imagem do Buraco Negro M87 é como tentar ver algo que, por definição, é impossível de se ver.</p>
    <footer align="right">—Katie Bouman, <cite>Professora Assistente, Ciências da Computação e Matemática, Caltech</cite></footer>
</blockquote>

## Sobre o Telescópio Event Horizon

O [telescópio Event Horizon(EHT)](https://eventhorizontelescope.org), é um conjunto de oito telescópios em solo formando um telescópio computacional do tamanho da Terra, projetado para estudar objetos extremos no universo com sensibilidade e resolução sem precedentes.  A rede mundial de telescópios de rádio compreende um telescópio virtual baseado em uma técnica chamada "interferometria de base muito longa" (*very-long-baseline interferometry* — VLBI). Usando essa técnica, o EHT é capaz de alcançar uma resolução angular de [20 micro arco-segundos][resolution] — o suficiente para ler um jornal em Nova York de uma cafeteira em Paris!

### Principais Objetivos e Resultados

* **Uma nova visão do universo:** O EHT é uma ferramenta nova empolgante para estudar os objetos mais extremos no universo. A imagem inovadora do EHT foi publicada 100 anos após [o experimento de Sir Arthur Eddington][eddington] ter produzido as primeiras evidências observacionais apoiando a teoria da relatividade geral de Einstein.

* **Investigando os Buracos Negros:** A primeira imagem do EHT foca no buraco negro supermassivo no centro da galáxia Messier 87 (M87), localizado no aglomerado de Virgem. Esse buraco negro reside a aproximadamente 55 milhões de anos-luz da Terra e tem uma massa igual a 6,5 bilhões de vezes a do Sol. Tem sido um tema de estudo astronômico há [mais de 100 anos](https://www.jpl.nasa.gov/news/news.php?feature=7385). Buracos negros são objeto de estudo intenso há muito tempo, mas o EHT fornece a primeira evidência visual direta desses fenômenos extremos.

* **Comparando observações com teoria:** Baseado na teoria geral da relatividade de Einstein, cientistas esperavam ver uma região sombria semelhante a uma sombra, causada pela curvatura gravitacional e captura de luz pelo horizonte de eventos. Ao estudar esta sombra cientistas poderiam medir a enorme massa do buraco negro supermassivo central da M87.

### Desafios

* **Escala**

    As observações do telescópio Event Horizon (EHT) apresentam desafios para ferramentas de processamento de dados existentes, decorrentes das flutuações de fase atmosférica rápidas, largura de banda ampla para gravação e um conjunto de telescópios altamente heterogêneos.

* **Calibração e Correlação**

    Além de agendar todas essas observações coordenadas do EHT, reduzir o volume geral e a complexidade dos dados para ajudar na análise é um problema difícil de ser resolvido. Para colocar as coisas em perspectiva, o EHT gera mais de 350 Terabytes de dados observados por dia, armazenados em discos rígidos de alto desempenho preenchidos com hélio.

* **Reconstrução de imagem**

    Como os dados calibrados são processados para produzir uma imagem de algo que nunca foi diretamente visto? Como os cientistas podem ter confiança de que a imagem está correta? Esses são alguns dos desafios que precisaram ser superados na análise realizada para produzir a imagem.

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**Etapas de Processamento de Dados do EHT**" alt="data pipeline" align="middle" attr="(Créditos do diagrama: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## Papel do NumPy na criação da imagem do Buraco Negro

Ainda que coletar, selecionar e processar os dados das instalações do EHT represente um desafio monumental, é apenas o primeiro passo para gerar uma imagem a partir dos dados. Há muitas abordagens para a reconstrução de imagens, cada uma incorporando suposições e restrições únicas para resolver o problema mal-posto de recuperar uma imagem do buraco negro a partir dos dados coletados. Mas como alguém pode ter certeza de que a imagem que foi produzida está correta? E se houver um problema com os dados? Ou talvez um algoritmo seja muito dependente de uma hipótese em particular? A imagem será alterada drasticamente se um único parâmetro for alterado? A colaboração do EHT venceu esses desafios ao estabelecer equipes independentes que avaliaram os dados usando técnicas de reconstrução de imagem estabelecidas e de ponta para verificar se as imagens resultantes eram consistentes. Resultados destas equipes independentes de pesquisadores foram combinados para proporcionar a imagem sem precedentes do buraco negro. Essa abordagem é um poderoso exemplo da importância da reprodutibilidade e da colaboração para a descoberta científica moderna e ilustra o papel que o ecossistema científico Python desempenha no apoio ao progresso científico através da análise de dados colaborativos.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**O papel do NumPy na criação da imagem do Buraco Negro**" >}}

Por exemplo, o pacote Python [`eht-imaging`][ehtim] fornece ferramentas para simular e realizar reconstrução de imagem nos dados do VLBI. NumPy is at the core of array data processing used in this package as illustrated by the partial software dependency chart below.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Software dependency chart of ehtim package highlighting NumPy**" >}}

Besides NumPy, many other packages such as [SciPy](https://www.scipy.org) and [Pandas](https://pandas.io) were used in the data processing pipeline for imaging the black hole. The standard astronomical file formats and time/coordinate transformations were handled by [Astropy][astropy] while [Matplotlib][mpl] was used in visualizing data throughout the analysis pipeline, including the generation of the final image of the black hole.

## Summary

NumPy enabled researchers to manipulate large numerical datasets through its efficient and generic n-dimensional array, providing a foundation for the software used to generate the first ever image of a black hole. The direct imaging of a black hole is a major scientific accomplishment providing stunning, visual evidence of Einstein’s general theory of relativity. This achievement encompasses not only technological breakthroughs, but international-scale scientific collaboration between over 200 scientists and some of the world's best radio observatories. They used innovative algorithms and data processing techniques improving upon existing astronomical models to help unfold some of the mysteries of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
