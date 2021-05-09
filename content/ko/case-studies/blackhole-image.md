---
title: "사례 연구: 최초의 블랙홀 사진"
sidebar: false
---

{{< figure src="/images/content_images/cs/blackhole.jpg" caption="**블랙홀 M87**" alt="블랙홀 사진" attr="*(사진 크레딧: Event Horizon Telescope Collaboration)*" attrlink="https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>M87 블랙홀을 시각화하는 것은 정의상 볼 수 없는 것을 보려고 하는 것과도 같다.</p>
    <footer align="right">Katie Bouman, <cite>캘리포니아 공과대학 컴퓨터과학부 겸 수리과학부 연구 조교수</cite></footer>
</blockquote>

## 지구 크기의 망원경

[사건의 지평선 망원경(EHT)](https://eventhorizontelescope.org)은 8개의 지상 전파 망원경으로 구성된 지구 크기의 전산 망원경으로, 전례없는 감도와 해상도로 우주를 연구하는 데 쓰입니다.  초장기선 간섭 관측법(VLBI)이라는 기술을 사용하는 거대한 가상 망원경의 각해상도는 [20 마이크로각초][resolution]에 달하며 파리의 길거리 카페에서 뉴욕의 신문을 읽기에 충분한 정도입니다!

### 주요 목표 및 결과

* **우주를 보는 새로운 방식:** EHT라는 획기적인 발상의 토대는 [아서 에딩턴 경][eddington]의 관측으로 아인슈타인의 일반 상대성이론이 최초로 관측적 지지를 받았던 시기인 100년 전에 마련되었습니다.

* **블랙홀:** EHT는 처녀자리 은하단의 M87 은하의 중심부에 있는 초대질량 블랙홀로 훈련되었으며 이는 지구에서 약 5500만 광년 떨어져 있습니다. 이 천체의 질량은 태양의 65억 배입니다. [100년 넘게](https://www.jpl.nasa.gov/news/news.php?feature=7385) 연구되었으나, 블랙홀을 시각적으로 볼 수 있게 구현한 바는 없었습니다.

* **관찰과 이론의 비교:** 아인슈타인의 일반 상대성이론에 따라 과학자들은 중력의 시공간 왜곡이나 빛 흡수에 의해 어둡게 보이는 영역이 나타날 것으로 예측하였습니다. 과학자들은 이를 블랙홀의 엄청난 질량을 재는 데 이용할 수 있었죠.

### 과제

* **계산의 규모**

    EHT는 급격한 대기 위상의 변동, 큰 기록 대역폭, 완전히 다르고 지리적으로 분산된 망원경 등의 문제를 포함한 막대한 데이터를 처리해야 하는 문제를 낳습니다.

* **지나치게 많은 정보**

    EHT는 매일 350 테라바이트의 관측 결과를 생성하며, 이 정보는 헬륨으로 채운 하드 드라이브에 저장됩니다. 이토록 많은 데이터의 양과 복잡성을 줄여나가는 것은 지극히 어려운 일입니다.

* **잘 알지 못함**

    만약 목표가 이전에 본 적이 없는 것을 보는 것이라면, 과학자들은 어떻게 이 사진이 옳다고 입증할 수 있을까요?

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**EHT 데이터 처리 파이프라인**" alt="데이터 파이프라인" align="middle" attr="(다이어그램 크레딧: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## NumPy의 역할

데이터에 만약 문제가 있다면 어떨까요? 아니면 알고리즘이 특정 가정에 지나치게 의존할 수도 있습니다. 매개변수 하나만 달라져도 사진이 크게 바뀔까요?

The EHT collaboration met these challenges by having independent teams evaluate the data, using both established and cutting-edge image reconstruction techniques. When results proved consistent, they were combined to yield the first-of-a-kind image of the black hole.

Their work illustrates the role the scientific Python ecosystem plays in advancing science through collaborative data analysis.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="numpy의 역할" caption="**블랙홀 시각화에서 NumPy의 역할**" >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for simulating and performing image reconstruction on VLBI data. NumPy is at the core of array data processing used in this package, as illustrated by the partial software dependency chart below.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Software dependency chart of ehtim package highlighting NumPy**" >}}

Besides NumPy, many other packages, such as [SciPy](https://www.scipy.org) and [Pandas](https://pandas.io), are part of the data processing pipeline for imaging the black hole. The standard astronomical file formats and time/coordinate transformations were handled by [Astropy][astropy], while [Matplotlib][mpl] was used in visualizing data throughout the analysis pipeline, including the generation of the final image of the black hole.

## Summary

The efficient and adaptable n-dimensional array that is NumPy's central feature enabled researchers to manipulate large numerical datasets, providing a foundation for the first-ever image of a black hole. A landmark moment in science, it gives stunning visual evidence of Einstein’s theory. The achievement encompasses not only technological breakthroughs but also international collaboration among over 200 scientists and some of the world's best radio observatories.  Innovative algorithms and data processing techniques, improving upon existing astronomical models, helped unfold a mystery of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy를 통한 이익" caption="**활용된 주요 NumPy 기능**" >}}

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

[eddington]: https://ko.wikipedia.org/wiki/%EC%95%84%EC%84%9C_%EC%8A%A4%ED%83%A0%EB%A6%AC_%EC%97%90%EB%94%A9%ED%84%B4#%EC%9D%BC%EB%B0%98%EC%83%81%EB%8C%80%EC%84%B1%EC%9D%B4%EB%A1%A0%EC%9D%98_%EC%8B%A4%ED%97%98%EC%A0%81_%EA%B2%80%EC%A6%9D

[ehtim]: https://github.com/achael/eht-imaging

[astropy]: https://www.astropy.org/
[mpl]: https://matplotlib.org/
