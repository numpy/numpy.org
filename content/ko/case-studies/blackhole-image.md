---
title: "사례 연구: 최초의 블랙홀 사진"
sidebar: false
---

{{< figure >}}
{{< /figure >}}

{{< blockquote
  cite="https://www.youtube.com/watch?v=BIvezCVcsYs"
  by="{{< blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs" by="Katie Bouman, _Assistant Professor, Computing & Mathematical Sciences, Caltech_""
>}}
{{< /blockquote >}}

## 지구 크기의 망원경

[사건의 지평선 망원경(EHT)](https://eventhorizontelescope.org)은 8개의 지상 전파 망원경으로 구성된 지구 크기의 전산 망원경으로, 전례없는 감도와 해상도로 우주를 연구하는 데 쓰입니다.  초장기선 간섭 관측법(VLBI)이라는 기술을 사용하는 거대한 가상 망원경의 각해상도는 [20 마이크로각초][resolution]에 달하며 파리의 길거리 카페에서 뉴욕의 신문을 읽기에 충분한 정도입니다!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### 주요 목표 및 결과

- **우주를 보는 새로운 방식:** EHT라는 획기적인 발상의 토대는 [아서 에딩턴 경][eddington]의 관측으로 아인슈타인의 일반 상대성이론이 최초로 관측적 지지를 받았던 시기인 100년 전에 마련되었습니다.

- **블랙홀:** EHT는 처녀자리 은하단의 Messier 87(M87) 은하의 중심부에 있는 초대질량 블랙홀로 훈련되었으며 이는 지구에서 약 5500만 광년 떨어져 있습니다. 이 천체의 질량은 태양의 65억 배입니다. [100년 넘게](https://www.jpl.nasa.gov/news/news.php?feature=7385) 연구되었으나, 블랙홀을 시각적으로 볼 수 있게 구현한 바는 없었습니다.

- **관찰과 이론의 비교:** 아인슈타인의 일반 상대성이론에 따라 과학자들은 중력의 시공간 왜곡이나 빛 흡수에 의해 어둡게 보이는 영역이 나타날 것으로 예측하였습니다. 과학자들은 이를 블랙홀의 엄청난 질량을 재는 데 이용할 수 있었죠.

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

### 도전

- **계산의 규모**

  EHT는 급격한 대기 위상의 변동, 큰 기록 대역폭, 완전히 다르고 지리적으로 분산된 망원경 등의 문제를 포함한 막대한 데이터를 처리해야 하는 문제를 낳습니다.

- **지나치게 많은 정보**

  EHT는 매일 350 테라바이트의 관측 결과를 생성하며, 이 정보는 헬륨으로 채운 하드 드라이브에 저장됩니다. 이토록 많은 데이터의 양과 복잡성을 줄여나가는 것은 지극히 어려운 일입니다.

- **잘 알지 못함**

  만약 목표가 이전에 본 적이 없는 것을 보는 것이라면, 과학자들은 어떻게 이 사진이 옳다고 입증할 수 있을까요?

{{< figure >}}
{{< /figure >}}

## NumPy의 역할

데이터에 만약 문제가 있다면 어떨까요? 아니면 알고리즘이 특정 가정에 지나치게 의존할 수도 있습니다. 매개변수 하나만 달라져도 사진이 크게 바뀔까요?

EHT는 기존 및 최첨된 이미지 재구성 기술을 모두 사용한 뒤, 개개의 팀이 데이터를 평가하도록 하여 이런 문제를 해결했습니다. 결과가 일관적이라는 것을 검증한 뒤, 이들을 결합해 최초의 블랙홀 이미지를 만들어내었습니다.

그들의 연구는 협업 데이터 분석을 통해 과학을 발전시키는 과학적인 Python 생태계의 역할을 보여줍니다.

{{< figure >}}
{{< /figure >}}

예를 들어, [`eht-imaging`][ehtim] Python 패키지는 VLBI 데이터를 통해 실험이나 이미지 재구성을 수행할 때 필요한 도구를 제공합니다.
NumPy는 아래 소프트웨어 종속성 차트에 나와 있는 것처럼 이 패키지에서 사용되는 배열 데이터 처리의 핵심 역할을 합니다.

{{< figure >}}
{{< /figure >}}

[ehtim]: https://github.com/achael/eht-imaging

NumPy 외에도 [SciPy](https://www.scipy.org)와 [Pandas](https://pandas.io) 등의 다른 많은 패키지가 블랙홀을 시각화하는 데이터 처리 파이프라인의 일부입니다.
표준 천문 파일 형식과 시간/좌표 변환에는 [Astropy][astropy]가 쓰였고 [Matplotlib][mpl]는 분석 과정 전체에서 블랙홀의 최종 사진을 생성하는 등 데이터를 시각화하는 데 쓰였습니다.

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/

## 요약

NumPy의 핵심 기능인 효율적이고 유용한 n차원 배열은 연구자들이 대규모 수치 데이터셋을 다룰 수 있도록 하여 최초의 블랙홀 사진을 만드는 데 토대를 제공했습니다. 이번 관측은 아인슈타인의 이론에 훌륭한 시각적 증거를 준 관측으로, 과학계에 한 획을 그은 순간이었습니다. 기술적 혁신뿐만 아니라 200명 이상의 과학자와 세계 최고의 전파 관측소 간의 국제 협력도 이루어 냈습니다.  기존의 천문학 모델을 개선한 혁신적인 알고리즘과 데이터 처리 기술이 우주의 비밀을 알아내는 데 도움을 주었습니다.

{{< figure >}}
{{< /figure >}}
