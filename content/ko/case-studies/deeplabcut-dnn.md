---
title: "사례 연구: DeepLabCut 3D 포즈 추정"
sidebar: false
---

{{< figure >}}
src = '/images/content_images/cs/mice-hand.gif'
title = 'Analyzing mice hand-movement using DeepLapCut'
alt = 'micehandanim'
attribution = '(Source: www.deeplabcut.org )'
attributionlink = 'http://www.mousemotorlab.org/deeplabcut'
{{< /figure >}}

{{< blockquote
cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/"
by="Alexander Mathis, _Assistant Professor, École polytechnique fédérale de Lausanne_ ([EPFL](https://www.epfl.ch/en/))"

> }}
> Open Source Software is accelerating Biomedicine. DeepLabCut은 딥 러닝을 사용하여 동물 행동에 대한 자동화된 비디오 분석을 가능하게 합니다.
> {{< /blockquote >}}

## DeepLabCut 소개

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) is an open source toolbox that empowers researchers at hundreds of institutions worldwide to track behaviour of laboratory animals, with very little training data, at human-level accuracy. DeepLabCut 기술을 통해 과학자들은 동물 종과 시간 척도에 걸쳐 운동 제어 및 행동에 대한 과학적 이해를 더 깊이 탐구할 수 있습니다.

신경 과학, 의학 및 생체 역학을 포함한 여러 연구 분야에서 동물의 움직임을 추적한 데이터를 사용합니다. DeepLabCut은 필름에 기록된 동작을 구문 분석하여 인간과 다른 동물이 하는 일을 이해하는 데 도움을 줍니다. 심층 신경망 기반 데이터 분석과 함께 태깅 및 모니터링의 힘든 작업에 자동화를 사용하는 DeepLabCut은 영장류, 생쥐, 물고기, 파리 등과 같은 동물 관찰과 관련된 과학적 연구를 훨씬 빠르고 정확하게 만듭니다.

{{< figure >}}
src = '/images/content_images/cs/race-horse.gif'
title = 'Colored dots track the positions of a racehorse’s body part'
alt = 'horserideranim'
attribution = '(Source: Mackenzie Mathis)'
{{< /figure >}}

DeepLabCut's non-invasive behavioral tracking of animals by extracting the poses of animals is crucial for scientific pursuits in domains such as biomechanics, genetics, ethology & neuroscience. 동적으로 변화하는 배경에서 마커 없이 비디오에서 동물 포즈를 비침습적으로 측정하는 것은 기술적으로 뿐만 아니라 필요한 리소스 요구 사항 및 필요한 훈련 데이터 측면에서 계산적으로 어려운 일입니다.

DeepLabCut을 사용하면 연구자가 피험자의 자세를 추정하고 Python 기반 소프트웨어 툴킷을 통해 행동을 정량화할 수 있습니다.  DeepLabCut을 사용하여 연구원은 비디오에서 고유한 프레임을 식별하고 맞춤형 GUI를 사용하여 수십 개의 프레임에서 특정 신체 부위에 디지털 레이블을 지정한 다음 DeepLabCut의 딥 러닝 기반 포즈 추정 아키텍처가 나머지 프레임에서 동일한 기능을 선택하는 방법을 학습할 수 있습니다. It works across species of animals, from common laboratory animals such as flies and mice to more unusual animals like [cheetahs][cheetah-movement].

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

DeepLabCut uses a principle called [transfer learning](https://arxiv.org/pdf/1909.11229), which greatly reduces the amount of training data required and speeds up the convergence of the training period.  필요에 따라 사용자는 실시간 실험 피드백과 결합할 수 있는 더 빠른 추론(예: MobileNetV2)을 제공하는 다양한 네트워크 아키텍처를 선택할 수 있습니다. DeepLabCut originally used the feature detectors from a top-performing human pose estimation architecture, called [DeeperCut](https://arxiv.org/abs/1605.03170), which inspired the name. 이제 패키지가 추가 아키텍처, 증강 방법 및 전체 프런트 엔드 사용자 경험을 포함하도록 크게 변경되었습니다. 또한 대규모 생물학적 실험을 지원하기 위해 DeepLabCut은 능동적 학습 기능을 제공하므로 사용자는 시간이 지남에 따라 트레이닝 세트를 늘려 엣지 케이스를 다루고 특정 상황 내에서 포즈 추정 알고리즘을 강력하게 만들 수 있습니다.

Recently, the [DeepLabCut model zoo](http://www.mousemotorlab.org/dlc-modelzoo) was introduced, which provides pre-trained models for various species and experimental conditions from facial analysis in primates to dog posture. 예를 들어 새 데이터의 레이블 지정이나 신경망 교육 없이 클라우드에서 실행할 수 있으며 프로그래밍 경험이 필요하지 않습니다.

### 주요 목표 및 결과

- **Automation of animal pose analysis for scientific studies:**

  The primary objective of DeepLabCut technology is to measure and track posture
  of animals in a diverse settings. This data can be used, for example, in
  neuroscience studies to understand how the brain controls movement, or to
  elucidate how animals socially interact. Researchers have observed a
  [tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1)
  with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second
  (FPS).

- **Creation of an easy-to-use Python toolkit for pose estimation:**

  DeepLabCut wanted to share their animal pose-estimation technology in the form
  of an easy to use tool that can be adopted by researchers easily. So they have
  created a complete, easy-to-use Python toolbox with project management features
  as well. These enable not only automation of pose-estimation but also
  managing the project end-to-end by helping the DeepLabCut Toolkit user right
  from the dataset collection stage to creating shareable and reusable analysis
  pipelines.

  Their [toolkit][DLCToolkit] is now available as open source.

  일반적인 DeepLabCut 작업 흐름에는 다음이 포함됩니다.

  - 능동적 학습을 통한 훈련 세트 생성 및 정제
  - 특정 동물 및 시나리오를 위한 맞춤형 신경망 생성
  - 비디오에 대한 대규모 추론을 위한 코드
  - 통합 시각화 도구를 사용하여 추론 도출

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-toolkit-steps.png'
title = 'Pose estimation steps with DeepLabCut'
alt = 'dlcsteps'
align = 'center'
attribution = '(Source: DeepLabCut)'
attributionlink = 'https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1'
{{< /figure >}}

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut

### 과제

- **Speed**

  Fast processing of animal behavior videos in order to measure their behavior
  and at the same time make scientific experiments more efficient, accurate.
  Extracting detailed animal poses for laboratory experiments, without
  markers, in dynamically changing backgrounds, can be challenging, both
  technically as well as in terms of resource needs and training data required.
  Coming up with a tool that is easy to use without the need for skills such
  as computer vision expertise that enables scientists to do research in more
  real-world contexts, is a non-trivial problem to solve.

- **Combinatorics**

  Combinatorics involves assembly and integration of movement of multiple
  limbs into individual animal behavior. Assembling keypoints and their
  connections into individual animal movements and linking them across time
  is a complex process that requires heavy-duty numerical analysis, especially
  in case of multi-animal movement tracking in experiment videos.

- **Data Processing**

  Last but not the least, array manipulation - processing large stacks of
  arrays corresponding to various images, target tensors and keypoints is
  fairly challenging.

{{< figure >}}
src = '/images/content_images/cs/pose-estimation.png'
title = 'Pose estimation variety and complexity'
alt = 'challengesfig'
align = 'center'
attribution = '(Source: Mackenzie Mathis)'
attributionlink = 'https://www.biorxiv.org/content/10.1101/476531v1.full.pdf'
{{< /figure >}}

## 포즈 추정 문제를 해결하는 NumPy의 역할

NumPy는 행동 분석을 위한 고속 수치 계산에 대한 DeepLabCut 기술의 핵심 요구 사항을 해결합니다.  Besides NumPy, DeepLabCut employs
various Python software that utilize NumPy at their core, such as
[SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org),
[matplotlib](https://matplotlib.org),
[Tensorpack](https://github.com/tensorpack/tensorpack),
[imgaug](https://github.com/aleju/imgaug),
[scikit-learn](https://scikit-learn.org/stable/),
[scikit-image](https://scikit-image.org) and
[Tensorflow](https://www.tensorflow.org).

NumPy의 다음 기능은 이미지 처리, 조합 요구 사항 및 DeepLabCut 포즈 추정 알고리즘의 빠른 계산 요구 사항을 해결하는 데 중요한 역할을 했습니다.

- 벡터화
- 마스킹된 어레이 작업
- 선형 대수학
- 무작위 샘플링
- 큰 배열의 재구성

DeepLabCut은 툴킷에서 제공하는 워크플로 전체에서 NumPy의 어레이 기능을 활용합니다. 특히, NumPy는 사람의 주석 레이블 지정을 위한 개별 프레임 샘플링과 주석 데이터 작성, 편집 및 처리에 사용됩니다.  TensorFlow 내에서 신경망은 DeepLabCut 기술로 수천 번의 반복을 통해 훈련되어 프레임에서 실측 주석을 예측합니다. 이를 위해 이미지 대 이미지 변환 문제로 포즈 추정을 캐스팅하기 위해 목표 밀도(점수 지도) 가 생성됩니다. 신경망을 강력하게 만들기 위해 다양한 기하 및 이미지 처리 단계에 따라 대상 스코어맵을 계산해야 하는 데이터 확대가 사용됩니다. 학습을 빠르게 하기 위해 NumPy의 벡터화 기능이 활용됩니다. 추론을 위해 대상 스코어맵에서 가장 가능성이 높은 예측을 추출해야 하며 효율적으로 "개별 동물을 조립하기 위해 예측을 연결"해야 합니다.

{{< figure >}}
src = '/images/content_images/cs/deeplabcut-workflow.png'
title = 'DeepLabCut Workflow'
alt = 'workflow'
attribution = '(Source: Mackenzie Mathis)'
attributionlink = 'https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962'
{{< /figure >}}

## 요약

행동을 관찰하고 효율적으로 설명하는 것은 현대 행동학, 신경과학, 의학 및 기술의 핵심 테넌트입니다.
[DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf)
allows researchers to estimate the pose of the subject, efficiently enabling
them to quantify the behavior. DeepLabCut Python 도구 상자는 작은 훈련 이미지 세트만으로 인간 수준의 라벨링 정확도 내에서 신경망을 훈련할 수 있습니다. 따라서 실험실에서의 행동 분석뿐만 아니라 잠재적으로 스포츠, 보행 분석, 의학 및 재활 연구에도 응용 분야를 확장합니다. DeepLabCut 알고리즘이 직면한 복잡한 조합, 데이터 처리 문제는 NumPy의 배열 조작 기능을 사용하여 해결됩니다.

{{< figure >}}
src = '/images/content_images/cs/numpy_dlc_benefits.png'
alt = 'numpy benefits'
title = 'Key NumPy Capabilities utilized'
{{< /figure >}}
