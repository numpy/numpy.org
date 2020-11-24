---
title: "Estudo de Caso: Estimativa de Pose 3D com DeepLabCut"
sidebar: false
---

{{< figure src="/images/content_images/cs/mice-hand.gif" class="fig-center" caption="**Análise de movimentos de mãos de camundongos usando DeepLapCut**" alt="micehandanim" attr="*(Fonte: www.deeplabcut.org )*" attrlink="http://www.mousemotorlab.org/deeplabcut">}}

<blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/">
    <p>Software de código aberto está acelerando a Biomedicina. DeepLabCut permite a análise automática de vídeos de comportamento animal usando Deep Learning.</p>
    <footer align="right">—Alexander Mathis, <cite>Professor Assistente, École polytechnique fédérale de Lausanne <a href="https://www.epfl.ch/en/">(EPFL)</a></cite></footer>
</blockquote>

## Sobre o DeepLabCut

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) é uma toolbox de código aberto que permite que pesquisadores de centenas de instituições em todo o mundo rastreiem o comportamento de animais de laboratório, com muito poucos dados de treinamento, mas com precisão no nível humano. Com a tecnologia DeepLabCut, cientistas podem aprofundar a compreensão científica do controle motor e do comportamento em diversas espécies animais e escalas temporais.

Várias áreas de pesquisa, incluindo a neurociência, a medicina e a biomecânica, utilizam dados de rastreamento da movimentação de animais. A DeepLabCut ajuda a compreender o que os seres humanos e outros animais estão fazendo, analisando ações que foram registradas em vídeo. Ao usar automação para tarefas penosas de monitoramento e marcação, junto com análise de dados baseada em redes neurais profundas, a DeepLabCut garante que estudos científicos envolvendo a observação de animais como primatas, camundongos, peixes, moscas etc. sejam mais rápidos e mais precisos.

{{< figure src="/images/content_images/cs/race-horse.gif" class="fig-center" caption="**Pontos coloridos rastreiam as posições das partes do corpo de um cavalo de corrida**" alt="horserideranim" attr="*(Fonte: Mackenzie Mathis)*">}}

O rastreamento não invasivo dos animais pela DeepLabCut através da extração de poses é crucial para pesquisas científicas em domínios como a biomecânica, genética, etologia e neurociência. Medir as poses dos animais de maneira não invasiva através de vídeo - sem marcadores - com fundos dinamicamente variáveis é computacionalmente desafiador, tanto tecnicamente quanto em termos de recursos necessários e dados de treinamento exigidos.

A DeepLabCut permite que pesquisadores façam estimativas de poses para os sujeitos, permitindo que se possa quantificar de maneira eficiente seus comportamentos através de um conjunto de ferramentas de software baseado em Python.  Com a DeepLabCut, pesquisadores podem identificar quadros (*frames*) distintos em vídeos, rotular digitalmente partes específicas do corpo em alguns quadros com uma GUI específica, e a partir disso a arquitetura de estimação de poses baseada em deep learning na DeepLabCut aprende a selecionar essas mesmas características no resto do vídeo e em outros vídeos similares. A ferramenta funciona para várias espécies de animais, desde animais comuns em laboratórios como moscas e camundongos até os mais incomuns como [guepardos][cheetah-movement].

A DeepLabCut usa um princípio chamado [aprendizado por transferência (*transfer learning*)](https://arxiv.org/pdf/1909.11229), o que reduz enormemente a quantidade de dados de treinamento necessários e acelera a convergência do período de treinamento.  Dependendo das suas necessidades, usuários podem escolher diferentes arquiteturas de rede que forneçam inferência mais rápida (por exemplo, MobileNetV2), que também podem ser combinadas com feedback experimental em tempo real. A DeepLabCut usou originalmente os detectores de features de uma arquitetura de estimativa de poses humanas de alto desempenho, chamada [DeeperCut](https://arxiv.org/abs/1605.03170), que inspirou seu nome. O pacote agora foi significativamente alterado para incluir mais arquiteturas, métodos de ampliação e uma experiência de usuário completa no front-end. Além de possibilitar experiências biológicas em grande escala, DeepLabCut fornece capacidades ativas de aprendizado para que os usuários possam aumentar o conjunto de treinamento ao longo do tempo para incluir casos particulares e tornar seu algoritmo de estimativa de poses robusto no seu contexto específico.

Recentemente, foi introduzido o [modelo DeepLabCut zoo](http://www.mousemotorlab.org/dlc-modelzoo), que proporciona modelos pré-treinados para várias espécies e condições experimentais, desde a análise facial em primatas até à posição de cães. Isso pode ser executado na nuvem, por exemplo, sem qualquer rotulagem de novos dados ou treinamento em rede neural, e não é necessária nenhuma experiência em programação.

### Principais Objetivos e Resultados

* **Automação da análise de poses animais para estudos científicos:**

  O objetivo principal da tecnologia DeepLabCut é medir e rastrear a postura dos animais em várias configurações. Esses dados podem ser usados, por exemplo, em estudos de neurociência para entender como o cérebro controla o movimento, ou para elucidar como os animais interagem socialmente. Pesquisadores observaram que [desempenho é 10 vezes melhor](https://www.biorxiv.org/content/10.1101/457242v1) com o DeepLabCut. Poses podem ser inferidas off-line em até 1200 quadros por segundo (FPS).

* **Criação de um kit de ferramentas Python fácil de usar para estimativa de poses:**

  DeepLabCut queria compartilhar sua tecnologia de estimativa de poses animal na forma de uma ferramenta simples de usar que pudesse ser adotada pelos pesquisadores facilmente. Assim, criaram um conjunto de ferramentas em Python completo e fácil de usar, também com recursos de gerenciamento de projeto. Isso permite não apenas a automação de estimação de poses, mas também o gerenciamento do projeto de ponta a ponta, ajudando o usuário do DeepLabCut Toolkit desde a fase de coleta para criar fluxos de dados compartilháveis e reutilizáveis.

  Seu [conjunto de ferramentas][DLCToolkit] agora está disponível como software de código aberto.

  Um fluxo de trabalho típico na DeepLabCut inclui:

  - criação e refinamento de conjuntos de treinamento por meio de aprendizagem ativa
  - criação de redes neurais personalizadas para animais e cenários específicos
  - código para inferência em larga escala em vídeos
  - inferências de desenho usando ferramentas integradas de visualização

{{< figure src="/images/content_images/cs/deeplabcut-toolkit-steps.png" class="csfigcaption" caption="**Passos na estimação de poses com DeepLabCut**" alt="dlcsteps" align="middle" attr="(Fonte: DeepLabCut)" attrlink="https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1" >}}

### Desafios

* **Velocidade**

    Processamento rápido de vídeos de animais para medir seu comportamento e, ao mesmo tempo, tornar os experimentos científicos mais eficientes e precisos. Extrair poses animais detalhadas para experimentos em laboratório, sem marcadores, sobre fundos dinâmicos, pode ser desafiador tanto tecnicamente quanto em termos de recursos e dados de treinamento necessários. Criar uma ferramenta que seja fácil de usar sem necessidade de habilidades como expertise em visão computacional que permita aos cientistas fazerem pesquisa em contextos mais próximos do mundo real é um problema não-trivial a ser solucionado.

* **Combinatória**

    Combinatória envolve a junção e integração de movimentos de múltiplos membros em um comportamento animal único. Reunir pontos-chave e suas conexões em movimentos animais individuais e encadeá-los em função do tempo é um processo complexo que exige análise numérica intensa, especialmente nos casos de rastreio de múltiplos animais em vídeos experimentais.

* **Processamento de dados**

    Por último, mas não menos importante, manipulação de matrizes - processar grandes conjuntos de matrizes correspondentes a várias imagens, tensores alvo e pontos-chave é bastante desafiador.

{{< figure src="/images/content_images/cs/pose-estimation.png" class="csfigcaption" caption="**Estimação de poses e complexidade**" alt="challengesfig" align="middle" attr="(Fonte: Mackenzie Mathis)" attrlink="https://www.biorxiv.org/content/10.1101/476531v1.full.pdf" >}}

## O papel da NumPy nos desafios da estimação de poses

NumPy supre a principal necessidade da tecnologia DeepLabCut de cálculos numéricos de alta velocidade para análises comportamentais.  Além da NumPy, DeepLabCut emprega várias bibliotecas Python que usam a NumPy como sua base, tais como [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) e [Tensorflow](https://www.tensorflow.org).

The following features of NumPy played a key role in addressing the image processing, combinatorics requirements and need for fast computation in DeepLabCut pose estimation algorithms:

* Vectorization
* Masked Array Operations
* Linear Algebra
* Random Sampling
* Reshaping of large arrays

DeepLabCut utilizes NumPy’s array capabilities throughout the workflow offered by the toolkit. In particular, NumPy is used for sampling distinct frames for human annotation labeling, and for writing, editing and processing annotation data.  Within TensorFlow the neural network is trained by DeepLabCut technology over thousands of iterations to predict the ground truth annotations from frames. For this purpose, target densities (scoremaps) are created to cast pose estimation as a image-to-image translation problem. To make the neural networks robust, data augmentation is employed, which requires the calculation of target scoremaps subject to various geometric and image processing steps. To make training fast, NumPy’s vectorization capabilities are leveraged. For inference, the most likely predictions from target scoremaps need to extracted and one needs to efficiently “link predictions to assemble individual animals”.

{{< figure src="/images/content_images/cs/deeplabcut-workflow.png" class="fig-center" caption="**DeepLabCut Workflow**" alt="workflow" attr="*(Source: Mackenzie Mathis)*" attrlink="https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962">}}

## Summary

Observing and efficiently describing behavior is a core tenant of modern ethology, neuroscience, medicine, and technology. [DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf) allows researchers to estimate the pose of the subject, efficiently enabling them to quantify the behavior. With only a small set of training images, the DeepLabCut Python toolbox allows training a neural network to within human level labeling accuracy, thus expanding its application to not only behavior analysis in the laboratory, but to potentially also in sports, gait analysis, medicine and rehabilitation studies. Complex combinatorics, data processing challenges faced by DeepLabCut algorithms are addressed through the use of NumPy's array manipulation capabilities.

{{< figure src="/images/content_images/cs/numpy_dlc_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
