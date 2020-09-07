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

    The observations from Event Horizon Telescope (EHT) present challenges for existing data processing tools, arising from the rapid atmospheric phase fluctuations, wide recording bandwidth, and highly heterogeneous array.

* **Calibration and Correlation**

    Besides scheduling all of these coordinated observations of EHT, reducing the overall volume and complexity of data to aid analysis is a really hard problem to solve. To put things in perspective, EHT generates over 350 Terabytes worth of observed data per day, stored on high-performance helium filled hard drives.

* **Image Reconstruction**

    How are the calibrated data processed to produce an image of something that has never before been directly imaged? How can scientists be confident that the image is correct? These are some of the challenges overcome in the analysis to produce the image.

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**EHT Data Processing Pipeline**" alt="data pipeline" align="middle" attr="(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## NumPy’s Role in Black Hole Imaging

While collecting, curating, and processing the data from the EHT facilities represents a monumental challenge, it is only the first step in generating an image from the data. There are many approaches to image reconstruction, each incorporating unique assumptions and constraints in order to solve the ill-posed problem of recovering an image of the black hole from the collected data. But how can anyone be confident that the image that's produced is correct? What if there's a problem with the data? Or perhaps an algorithm relies too heavily on a particular assumption? Will the image change drastically if a single parameter is changed? The EHT collaboration met these challenges by having independent teams evaluate the data using both established and cutting-edge image reconstruction techniques to verify that the resulting images were consistent. Results from these independent teams of researchers were combined to yield the first-of-a-kind image of the black hole. This approach is a powerful example of the importance of reproducibility and collaboration to modern scientific discovery and illustrates the role that the scientific Python ecosystem plays in supporting scientific advancement through collaborative data analysis.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**The role of NumPy in Black Hole imaging**" >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for simulating and performing image reconstruction on VLBI data. NumPy is at the core of array data processing used in this package as illustrated by the partial software dependency chart below.

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
