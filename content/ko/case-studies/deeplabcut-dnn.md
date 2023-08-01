---
title: "사례 연구: DeepLabCut 3D 포즈 추정"
sidebar: false
---

{{< figure src="/images/content_images/cs/mice-hand.gif" class="fig-center" caption="**DeepLapCut을 활용한 쥐의 손 움직임 분석**" alt="쥐 손 애니메이션" attr="*(출처: www.deeplabcut.org )*" attrlink="http://www.mousemotorlab.org/deeplabcut">}}

<blockquote cite="https://news.harvard.edu/gazette/story/newsplus/harvard-researchers-awarded-czi-open-source-award/">
    <p>오픈 소스 소프트웨어는 생물 의학을 가속화하고 있습니다. DeepLabCut은 딥 러닝을 사용하여 동물 행동에 대한 자동화된 비디오 분석을 가능하게 합니다.</p>
    <footer align="right">—알렉산더 마티스, <cite>조교수, 로잔 연방 공과대학교 <a href="https://www.epfl.ch/en/">(EPFL)</a></cite></footer>
</blockquote>

## DeepLabCut 소개

[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) 은 전 세계 수백 개 기관의 연구원이 인간 수준의 정확도로 매우 적은 훈련 데이터로 실험실 동물의 행동을 추적할 수 있는 오픈 소스 도구 상자입니다. DeepLabCut 기술을 통해 과학자들은 동물 종과 시간 척도에 걸쳐 운동 제어 및 행동에 대한 과학적 이해를 더 깊이 탐구할 수 있습니다.

신경 과학, 의학 및 생체 역학을 포함한 여러 연구 분야에서 동물의 움직임을 추적한 데이터를 사용합니다. DeepLabCut은 필름에 기록된 동작을 구문 분석하여 인간과 다른 동물이 하는 일을 이해하는 데 도움을 줍니다. 심층 신경망 기반 데이터 분석과 함께 태깅 및 모니터링의 힘든 작업에 자동화를 사용하는 DeepLabCut은 영장류, 생쥐, 물고기, 파리 등과 같은 동물 관찰과 관련된 과학적 연구를 훨씬 빠르고 정확하게 만듭니다.

{{< figure src="/images/content_images/cs/race-horse.gif" class="fig-center" caption="**경주마 신체 부위의 위치를 트래킹하는 색 점**" alt="경주마 애니메이션" attr="*(출처: Mackenzie Mathis)*">}}

DeeDeepLabCut의 동물 자세 추출을 통한 동물의 비침습적 행동 추적은 생체 역학, 유전학, 행동학 & 신경 과학과 같은 영역에서 과학적 추구에 매우 중요합니다. 동적으로 변화하는 배경에서 마커 없이 비디오에서 동물 포즈를 비침습적으로 측정하는 것은 기술적으로 뿐만 아니라 필요한 리소스 요구 사항 및 필요한 훈련 데이터 측면에서 계산적으로 어려운 일입니다.

DeepLabCut을 사용하면 연구자가 피험자의 자세를 추정하고 Python 기반 소프트웨어 툴킷을 통해 행동을 정량화할 수 있습니다.  DeepLabCut을 사용하여 연구원은 비디오에서 고유한 프레임을 식별하고 맞춤형 GUI를 사용하여 수십 개의 프레임에서 특정 신체 부위에 디지털 레이블을 지정한 다음 DeepLabCut의 딥 러닝 기반 포즈 추정 아키텍처가 나머지 프레임에서 동일한 기능을 선택하는 방법을 학습할 수 있습니다. 그것은 파리와 생쥐와 같은 일반적인 실험실 동물에서 [치타][cheetah-movement]와 같은 좀 더 특이한 동물에 이르기까지 다양한 동물 종에 걸쳐 작동합니다.

DeepLabCut은 [전이 학습](https://arxiv.org/pdf/1909.11229), 이라는 원리를 사용하여 필요한 훈련 데이터의 양을 크게 줄이고 훈련 기간의 수렴 속도를 높입니다.  필요에 따라 사용자는 실시간 실험 피드백과 결합할 수 있는 더 빠른 추론(예: MobileNetV2)을 제공하는 다양한 네트워크 아키텍처를 선택할 수 있습니다. DeepLabCut은 원래 [DeeperCut](https://arxiv.org/abs/1605.03170),이라는 최고 성능의 인간 포즈 추정 아키텍처의 특징 검출기를 사용했습니다. 이 이름에 영감을 받았습니다. 이제 패키지가 추가 아키텍처, 증강 방법 및 전체 프런트 엔드 사용자 경험을 포함하도록 크게 변경되었습니다. 또한 대규모 생물학적 실험을 지원하기 위해 DeepLabCut은 능동적 학습 기능을 제공하므로 사용자는 시간이 지남에 따라 트레이닝 세트를 늘려 엣지 케이스를 다루고 특정 상황 내에서 포즈 추정 알고리즘을 강력하게 만들 수 있습니다.

최근에는, 영장류의 안면 분석부터 개 자세까지 다양한 종과 실험 조건에 대해 사전 훈련된 모델을 제공하는 [DeepLabCut 모델 동물원](http://www.mousemotorlab.org/dlc-modelzoo) 이 도입되었습니다. 예를 들어 새 데이터의 레이블 지정이나 신경망 교육 없이 클라우드에서 실행할 수 있으며 프로그래밍 경험이 필요하지 않습니다.

### 주요 목표 및 결과

* **과학적 연구를 위한 동물 자세 분석 자동화:**

  DeepLabCut 기술의 주요 목표는 다양한 환경에서 동물의 자세를 측정하고 추적하는 것입니다. 예를 들어, 이 데이터는 뇌가 움직임을 제어하는 ​​방법을 이해하거나 동물이 사회적으로 상호 작용하는 방식을 설명하기 위해 신경 과학 연구에서 사용될 수 있습니다. 연구원들은 DeepLabCut으로 [성능이 10배 향상](https://www.biorxiv.org/content/10.1101/457242v1) 되는 것을 관찰했습니다. 포즈는 최대 1200 초당 프레임 수(FPS)로 오프라인에서 추론할 수 있습니다.

* **포즈 추정을 위해 사용하기 쉬운 Python 툴킷 생성:**

  DeepLabCut은 연구자들이 쉽게 채택할 수 있는 사용하기 쉬운 도구 형태로 동물 자세 추정 기술을 공유하고 싶었습니다. 그래서 그들은 프로젝트 관리 기능도 포함된 완전하고 사용하기 쉬운 Python 툴킷을 만들었습니다. 이를 통해 포즈 추정의 자동화는 물론 DeepLabCut Toolkit 사용자가 데이터 세트 수집 단계부터 공유 가능하고 재사용 가능한 분석 파이프라인 생성에 이르기까지 프로젝트 전체를 관리할 수 있습니다.

  [툴킷][DLCToolkit]은 현재 오픈 소스로 제공됩니다.

  일반적인 DeepLabCut 작업 흐름에는 다음이 포함됩니다.

  - 능동적 학습을 통한 훈련 세트 생성 및 정제
  - 특정 동물 및 시나리오를 위한 맞춤형 신경망 생성
  - 동영상에 대한 대규모 추론을 위한 코드
  - 통합 시각화 도구를 사용하여 추론 도출

{{< figure src="/images/content_images/cs/deeplabcut-toolkit-steps.png" class="csfigcaption" caption="**포즈 추정 단계 - DeepLabCut**" alt="DLC 단계" align="middle" attr="(출처: DeepLabCut)" attrlink="https://twitter.com/DeepLabCut/status/1198046918284210176/photo/1" >}}

### 도전

* **속도**

    동물의 행동을 측정하고 동시에 과학 실험을 보다 효율적이고 정확하게 하기 위해 동물 행동 비디오를 빠르게 처리합니다. 동적으로 변화하는 배경에서 마커 없이 실험실 실험을 위해 상세한 동물 포즈를 추출하는 것은 기술적으로 뿐만 아니라 필요한 리소스 요구 사항 및 필요한 교육 데이터 측면에서 어려울 수 있습니다. 컴퓨터 비전 전문 지식과 같은 기술 없이도 사용하기 쉬운 도구를 생각해내어 과학자들이 보다 실제 상황에서 연구를 수행할 수 있도록 하는 것은 해결해야 할 사소한 문제가 아닙니다.

* **조합론**

    조합론은 여러 사지의 움직임을 개별 동물 행동으로 조립하고 통합하는 것을 포함합니다. 키포인트와 연결을 개별 동물 움직임으로 조립하고 시간에 따라 연결하는 것은 특히 실험 비디오에서 여러 동물 움직임을 추적하는 경우 강력한 수치 분석이 필요한 복잡한 프로세스입니다.

* **데이터 처리**

    마지막으로 배열 조작 - 다양한 이미지, 대상 텐서 및 키포인트에 해당하는 대규모 배열 스택을 처리하는 것은 상당히 어렵습니다.

{{< figure src="/images/content_images/cs/pose-estimation.png" class="csfigcaption" caption="**포즈 추정 변수 및 복잡도**" alt="난점 설명" align="middle" attr="(출처: Mackenzie Mathis)" attrlink="https://www.biorxiv.org/content/10.1101/476531v1.full.pdf" >}}

## 포즈 추정 문제를 해결하는 NumPy의 역할

NumPy는 행동 분석을 위한 고속 수치 계산에 대한 DeepLabCut 기술의 핵심 요구 사항을 해결합니다.  NumPy 외에도 DeepLabCut은 [SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org), [matplotlib](https://matplotlib.org), [Tensorpack](https://github.com/tensorpack/tensorpack), [imgaug](https://github.com/aleju/imgaug), [scikit-learn](https://scikit-learn.org/stable/), [scikit-image](https://scikit-image.org) 그리고 [Tensorflow](https://www.tensorflow.org) 와 같이 핵심에서 NumPy를 활용하는 다양한 Python 소프트웨어를 사용합니다.

NumPy의 다음 기능은 이미지 처리, 조합 요구 사항 및 DeepLabCut 포즈 추정 알고리즘의 빠른 계산 요구 사항을 해결하는 데 중요한 역할을 했습니다.

* 벡터화
* 마스킹된 어레이 작업
* 선형 대수학
* 무작위 샘플링
* 큰 배열의 재구성

DeepLabCut은 툴킷에서 제공하는 워크플로 전체에서 NumPy의 어레이 기능을 활용합니다. 특히, NumPy는 사람의 주석 레이블 지정을 위한 개별 프레임 샘플링과 주석 데이터 작성, 편집 및 처리에 사용됩니다.  TensorFlow 내에서 신경망은 DeepLabCut 기술로 수천 번의 반복을 통해 훈련되어 프레임에서 실측 주석을 예측합니다. 이를 위해 이미지 대 이미지 변환 문제로 포즈 추정을 캐스팅하기 위해 목표 밀도(점수 지도)가 생성됩니다. 신경망을 강력하게 만들기 위해 다양한 기하 및 이미지 처리 단계에 따라 대상 스코어맵을 계산해야 하는 데이터 확대가 사용됩니다. 학습을 빠르게 하기 위해 NumPy의 벡터화 기능이 활용됩니다. 추론을 위해 대상 스코어맵에서 가장 가능성이 높은 예측을 추출해야 하며 효율적으로 "개별 동물을 조립하기 위해 예측을 연결"해야 합니다.

{{< figure src="/images/content_images/cs/deeplabcut-workflow.png" class="fig-center" caption="**DeepLabCut 워크플로우**" alt="워크플로우" attr="*(출처: Mackenzie Mathis)*" attrlink="https://www.researchgate.net/figure/DeepLabCut-work-flow-The-diagram-delineates-the-work-flow-as-well-as-the-directory-and_fig1_329185962">}}

## 요약

행동을 관찰하고 효율적으로 설명하는 것은 현대 행동학, 신경과학, 의학 및 기술의 핵심 테넌트입니다. [DeepLabCut](http://orga.cvss.cc/wp-content/uploads/2019/05/NathMathis2019.pdf)을 사용하면 연구자가 피험자의 자세를 추정하여 행동을 정량화할 수 있습니다. DeepLabCut Python 툴킷은 작은 훈련 이미지 세트만으로 인간 수준의 라벨링 정확도 내에서 신경망을 훈련할 수 있습니다. 따라서 실험실에서의 행동 분석뿐만 아니라 잠재적으로 스포츠, 보행 분석, 의학 및 재활 연구에도 응용 분야를 확장합니다. DeepLabCut 알고리즘이 직면한 복잡한 조합, 데이터 처리 문제는 NumPy의 배열 조작 기능을 사용하여 해결됩니다.

{{< figure src="/images/content_images/cs/numpy_dlc_benefits.png" class="fig-center" alt="numpy를 통한 이익" caption="**활용한 주요 NumPy 기능**" >}}

[cheetah-movement]: https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618

[DLCToolkit]: https://github.com/DeepLabCut/DeepLabCut
