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

The [Event Horizon telescope (EHT)](https://eventhorizontelescope.org), is an array of eight ground-based radio telescopes forming a computational telescope the size of the earth, that are designed to study extreme objects in the universe, with unprecedented sensitivity and resolution.  It is a worldwide network of eight pre-existing telescopes based on a technique called very-long-baseline interferometry (VLBI). This technique is used to synchronize these telescopes deployed across the globe to form one huge, Earth-size telescope capable of observing at a wavelength of 1.3 mm. This means EHT can achieve an angular resolution of [20 micro-arcseconds](https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole) — enough to read a newspaper in New York from a sidewalk café in Paris! 

### Key Imaging Objectives

* To study the most extreme objects in the Universe predicted by Einstein’s theory of general relativity, during the centennial year of the historic experiment that first confirmed the theory (2017).

* Focus on the [black hole](https://solarsystem.nasa.gov/resources/2319/first-image-of-a-black-hole/) at the center of Messier 87 galaxy, located in the Virgo galaxy cluster. This black hole resides approximately 55 million light-years from Earth and has a mass equal  to 6.5 billion times that of the Sun. It has been a subject of astronomical study for [over a 100 years](https://www.jpl.nasa.gov/news/news.php?feature=7385). Black holes have been theoretically predicted and observed but a real image was never created until now.

* Based on Einstein’s general theory of relativity, the scientists expected to see a dark region similar to a shadow, caused by the gravitational bending and capture of light by the event horizon. By studying this shadow scientists could measure the enormous mass of M87’s black hole. 

### The Challenges 

* **Scale**

    The observations from Event Horizon Telescope (EHT) present challenges for existing data processing tools, arising from the rapid atmospheric phase fluctuations, wide recording bandwidth, and highly heterogeneous array.

* **Calibration and Correlation**

    Besides scheduling all of these coordinated observations of EHT, reducing the overall volume and complexity of data to aid analysis is a really hard problem to solve. To put things in perspective, EHT generates over 350 Terabytes worth of observed data per day, stored on high-performance helium filled hard drives.

* **Source Imaging and Model Fitting**

    The sequence of correlation and engineering releases represents a year-long effort of identifying and mitigating data issues, and developing new software and procedures that could reliably choose the most likely image based on actual measurements.

{{< figure src="/images/content_images/cs/dataprocessbh.png" class="fig-center" caption="**EHT Data Processing Pipeline**" alt="data pipeline" align="middle" attr="(Diagram Credits: The Astrophysical Journal, Event Horizon Telescope Collaboration)" attrlink="https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57" >}}

## NumPy’s Role in Black Hole Imaging
	
There are several aspects to black hole imaging besides data collection, noise elimination, data cleanup, reduction and correlation. Imaging is crucial as it can help  to predict not only the black hole mass but also rule out whether a black hole could be a wormhole, a theoretical bridge between distant points in spacetime. But it is also incredibly hard to measure given the astronomical distances involved. As Katie Bouman mentions in her [TED talk](https://www.youtube.com/watch?v=BIvezCVcsYs), ‘It is like taking a picture of an orange on the surface of the moon.’

{{< figure src="/images/content_images/cs/bh_numpy_role.png" class="fig-center" alt="role of numpy" caption="**The role of NumPy in Black Hole imaging**" >}}

Once the key challenges posed by EHT, data collection and reduction are taken care of, the next big challenge in data processing is related to imaging. The imaging algorithms form the core of this task as through imaging, scientists could calculate the shadow of the black hole which forms the crux of several other calculations related to event horizon and nearby objects. One of the key algorithms used in imaging was developed by Katie Bouman – Continuous High-resolution Image Reconstruction using Patch priors, or ‘CHIRP’. It can parse the cumulative telescope data gathered by the Event Horizon Telescope project.For imaging tasks, researchers banked on Python to run the datasets on these algorithms, arraying and plotting data for meaningful insights.  

Besides NumPy, there were other packages such as [SciPy](https://www.scipy.org), [Pandas](https://pandas.io) and [Matplotlib](https://matplotlib.org) that helped in imaging and [data processing for imaging the black hole](https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57). The standard astronomical file formats and time/coordinate transformations were handled by [Astropy](https://www.astropy.org) while Matplotlib was used in visualizing data throughout the analysis pipeline, including the generation of the final image of the black hole.

Andrew Chael and the ehtim project team came up with [eht-imaging](https://github.com/achael/eht-imaging) Python modules for simulating and manipulating VLBI data and producing images with regularized maximum likelihood methods. NumPy is at the core of array data processing used in this software package named ehtim as indicated by the partial software dependency chart below.

{{< figure src="/images/content_images/cs/ehtim_numpy.png" class="fig-center" alt="ehtim dependency map highlighting numpy" caption="**Software dependency chart of ehtim package highlighting NumPy**" >}}

The challenge posed during reconstruction of an image using VLBI measurements is that there can be an infinite number of possible images that explain the data.  The ehtim software addresses this challenge by implementing algorithms that help find a set of most likely reasonable images that respects prior scientific assumptions while still satisfying the observed data.


## Summary

NumPy enabled researchers to manipulate large numerical datasets through its efficient data structures of vectors and matrices leading to imaging and plotting of the first ever image of a black hole. Imaging of M87 black hole is a major scientific feat that was almost presumed impossible a century ago.  In a way, black hole image has helped in a stunning confirmation of Einstein’s general theory of relativity. This is not only a breakthrough in technology, but an example of international scale collaboration that uses connections between the world's best radio observatories, over 200 scientists worked with observations collected over 10 days and analyzed for over a year. They used innovative algorithms and data processing techniques improving upon existing astronomical models to help unfold some of the mysteries of the universe.

{{< figure src="/images/content_images/cs/numpy_bh_benefits.png" class="fig-center" alt="numpy benefits" caption="**Key NumPy Capabilities utilized**" >}}
