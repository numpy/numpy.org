---
title: "Case Study: The First Image of a Black Hole"
sidebar: false
---

{{< figure src="/images/content_images/cs/blackhole.jpg" caption="**Black Hole M87**" alt="black hole image" attr="(**Image Credits:** Event Horizon Telescope Collaboration)" attrlink="https://www.jpl.nasa.gov/images/universe/20190410/blackhole20190410.jpg" >}}

<blockquote cite="https://www.youtube.com/watch?v=BIvezCVcsYs">
    <p>Imaging the M87 Black Hole is like trying to see something that is by definition impossible to see.</p>
    <footer align="right">—Katie Bouman, <cite>Assistant Professor, Computing & Mathematical Sciences, Caltech</cite></footer>
</blockquote>

## About Event Horizon Telescope

The [Event Horizon telescope (EHT)](https://eventhorizontelescope.org), is an
array of eight ground-based radio telescopes forming a computational telescope
the size of the earth, designed to study extreme objects in the
universe with unprecedented sensitivity and resolution.  The worldwide
network of radio-telescopes comprises a virtual telescope based on a technique
called very-long-baseline interferometry (VLBI).
Using this technique, the EHT is able to achieve an angular resolution of
[20 micro-arcseconds][resolution] — enough to read a newspaper in New York
from a sidewalk café in Paris!

[resolution]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole

### Key Goals and Results

* The EHT is an exciting new tool for studying the most extreme objects in the
  universe. The EHT's groundbreaking first result was published 100 years
  after [Sir Arthur Eddington's expidition][eddington] yielded the first 
  observational evidence in support of Einstein's theory of general relativity.

* The EHT's first image focuses on the supermassive black hole at the center
  of the galaxy Messier 87 (M87), located in the Virgo galaxy cluster.
  This black hole resides approximately 55 million light-years from Earth and
  has a mass equal  to 6.5 billion times that of the Sun. It has been a
  subject of astronomical study for
  [over a 100 years](https://www.jpl.nasa.gov/news/news.php?feature=7385).
  Black holes have long been the object of intense study but the EHT provides
  the first direct visual evidence of one of these extreme objects.

* Based on Einstein’s general theory of relativity, scientists expected 
  see a dark region similar to a shadow, caused by the gravitational bending
  and capture of light by the event horizon. By studying this shadow
  scientists could measure the enormous mass of M87’s central supermassive
  black hole.

[eddington]: https://en.wikipedia.org/wiki/Eddington_experiment

### The Challenges

* **Scale**

    The observations from Event Horizon Telescope (EHT) present challenges for
    existing data processing tools, arising from the rapid atmospheric phase
    fluctuations, wide recording bandwidth, and highly heterogeneous array.

* **Calibration and Correlation**

    Besides scheduling all of these coordinated observations of EHT, reducing
    the overall volume and complexity of data to aid analysis is a really hard
    problem to solve. To put things in perspective, EHT generates over 350
    Terabytes worth of observed data per day, stored on high-performance
    helium filled hard drives.

* **Image Reconstruction**

    How are the calibrated data processed to produce an image of something that
    has never before been directly imaged? How can scientists be confident
    that the image is correct?

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="csfigcaption" caption="**EHT Data Processing Pipeline**" alt="data pipeline" align="middle" attr="(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## NumPy’s Role in Black Hole Imaging

While collecting, curating, and processing the data from the EHT facilities 
represents a monumental challenge, it is only the first step in generating
an image from the data.
There are many approaches to image reconstruction, each incorporating unique
assumptions and constraints in order to solve the ill-posed problem of 
recovering an image of the black hole from the collected data.
But how can anyone be confident that the image that's produced is correct?
What if there's a problem with the data? Or perhaps an algorithm relies too
heavily on a particular assumption? Will the image change drastically if a
single parameter is changed?
The EHT collaboration met these challenges by having independent teams 
evaluate the data using both established and cutting-edge image reconstruction
techniques to verify that the resulting images were consistent.
Results from these independent teams of researchers were combined to yield the
first-of-a-kind image of the black hole.
This approach is a powerful example of the importance of reproducibility and
collaboration to modern scientific discovery --- and illustrates the role that
the scientific Python ecosystem plays in supporting scientific advancement
through collaborative data analysis.

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**The role of NumPy in Black Hole imaging**" >}}

For example, the [`eht-imaging`][ehtim] Python package provides tools for
simulating and performing image reconstruction on VLBI data. 
NumPy is at the core of array data processing used
in this software package as indicated by the partial software
dependency chart below.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Software dependency chart of ehtim package highlighting NumPy**" >}}


Besides NumPy, there were other packages such as
[SciPy](https://www.scipy.org), [Pandas](https://pandas.io) and
[Matplotlib](https://matplotlib.org) that helped in imaging and
[data processing for imaging the black hole](https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57).
The standard astronomical file formats and time/coordinate transformations
were handled by [Astropy](https://www.astropy.org) while Matplotlib was used
in visualizing data throughout the analysis pipeline, including the generation
of the final image of the black hole.

## Summary

NumPy enabled researchers to manipulate large numerical datasets through its
efficient and generic n-dimensional array, leading to the first ever image of
a black hole. The direct imaging of a black hole is
a major scientific accomplishment providing stunning, visual evidence ofEinstein’s
general theory of relativity. This achievement encompasses not only a
breakthrough in technology, but international-scale scientific collaboration
connections between the world's best radio observatories, and among over 200
scientists. They used
innovative algorithms and data processing techniques improving upon existing
astronomical models to help unfold some of the mysteries of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}
