---
title: NumPy Benchmarks
sidebar: false
---

<img src = "/images/content_images/benchmark-plot.jpg" alt = "Visualization" title = "Performance Benchmark; Number of Iterations: 5">


## Overview

This blog post aims to benchmark NumPy's performance on the widely accepted N-body problem[1]. This work also compares NumPy with other popular libraries and compilers like Numba, Pythran, Transonic and pure Python and C++ implementations.

The objective of benchmarking NumPy revolves around the efficiency of the library in quasi real-life situations, and the N-body problem suits the purpose well. Benchmarking is performed over several iterations for different datasets to ensure the accuracy of the results.

<!--Towards the end of this post, an attempt will be made to make a conclusion on how NumPy can be efficient in solving problems like N-body problem.-->

<!-- The post is organized as: -->

<!-- Can be made like a content section? -->
<!-- 1. Overview: (current section): Discussing the objective of the post. -->
<!-- 2. About N-body Problem: Brief description on N-body problem and why it was chosen. -->
<!-- 3. Dataset Description -->
<!-- 4. Implemented Accelerators -->
<!-- 5. Results -->
<!-- 6. Source Code -->
<!-- 7. References -->


## About N-Body Problem

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

> In physics, the n-body problem is the problem of predicting the individual motions of a group of celestial objects interacting with each other gravitationally.

Source: [Wikipedia](https://en.wikipedia.org/wiki/N-body_problem).

From the definition above, the N-body problem involves computations related to energies, acceleration, velocity, the distance of several particles in the space, which has also allowed it to be one of the widely accepted algorithms in the community. A brief description of computations involved in solving the N-body problem is given below, along with the pseudo-code in the next section:

Consider $n$ bodies of masses $m_1, m_2, m_3, ... , m_n$, moving under the mutual [gravitational force](https://en.wikipedia.org/wiki/Gravity) of attraction between them in an [inertial frame of reference](https://en.wikipedia.org/wiki/Inertial_frame_of_reference) of three dimensions, such that consecutive  positions and velocities of an ${ith}$ body are denoted by ($s_{i-1}$, $s_i$) and ($v_{i-1}$, $v_i$) respectively. The gravitational force felt on the $ith$ body of mass $m_i$ by a single body of mass $m_j$ is denoted as $F$ and the acceleration of the $ith$ body is represented as $a_i$. Consider the position vectors of these two bodies as $r_i$ and $r_j$.

The final aim is to find the total energy of each particle in the celestial space and the equations involved in solving the problem are listed below:

\begin{equation} {s_i} = {s_{i-1}} + {u\times t} + \frac{a\times t^2}{2} \tag{i} \end{equation}

\begin{equation}{v_i} = {v_{i-1}} + {a\times t} \tag{ii} \end{equation}

\begin{equation} {F} = \frac{{G\times {m_i}\times {m_j}}\times \mid {r_i}-{r_j} \mid}{{\mid {r_i}-{r_j} \mid}^3} \tag{iii} \end{equation}

\begin{equation} {F} = {m\times a} \tag{iv} \end{equation}

\begin{equation} {a} = \frac{F}{m} \tag{v} \end{equation}

\begin{equation} \textrm{Self Potential Energy} = \textrm{U} = -\frac{{m_i}\times {m_j}}{r^2} \tag{vi} \end{equation}

\begin{equation} \textrm{Kinetic Energy} = \textrm{K.E} = \frac{\sum m\times v^2}{2} \tag{vii} \end{equation}

\begin{equation} \textrm{Total Energy} = \textrm{Kinetic Energy} + \textrm{Self Potential Energy} \tag{viii} \end{equation}

### Pseudo Code of Solving N-body Problem

```bash
Set time to 0, time_step to 0.001 and time_end to 10s
THEN number_of_step is 10/0.001
FOR time is less than or equal to time_end
    Calculate accelerations (a[i], for given position r[i])
    Calculate total initial energies:
        Calculate kinetic energy
        Calculate potential energy
    FOR i less than number_of_step
        Calculate positions (r[i+1])
        Swap accelerations
        Calculate accelerations
        Calculate velocities (v[i+1])
        Increment time
        IF number_of_step % 100 is not 0 THEN
            Calculate total energy
            Print energy
        ENDIF
    END FOR
END FOR
```

## Dataset Description

* Nine different text files, named as `InputX.txt`, where $X$ is number of particles in the celestial space (for this problem, number of particles are: $16, 32, 64, 128, 256, 512, 1000, 2000$ and $16000$).
* Dataset[2] consists of the masses of each particle and information about their initial positions and velocities along the three-dimensional axis.

An example from the dataset[2] used is given below: (for a single particle)

```
# Ordered as: label, mass (grams), position_x, position_y, position_z, velocity_x, velocity_y, velocity_z
-1 0.0625 0.214835865608654947  -0.120469325327368135  -0.2661811268232539 0.757849421156586822  0.157644506165220161  -0.0715602005208729741
```

## Implemented Accelerators

Accelerators like [Numba](http://numba.pydata.org/), [Pythran](https://transonic.readthedocs.io/), and [Transonic](https://transonic.readthedocs.io/) are considered for also considered for benchmarking. This decision is inspired from [Ralf Gommer's Presentation on SciPy 1.0](https://www.slideshare.net/RalfGommers/scipy-10-and-beyond-a-story-of-community-and-code) (conference [video](https://www.youtube.com/watch?v=oHmm3mPxg6Y)). We give brief details on few of the accelerators below:

### Numba

From official [Numba's website](http://numba.pydata.org/):

> Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code.

Since Numba is a compiler focused on accelerating Python codes, the user API of the library comes with decorators like: `@jit, @vectorize, @guvectorize, @stencil, @jitclass, @cfunc, @overload` to support ease-of-use of the library. Along with the decorators, it has a `nopython` mode to generate fully compiled results without the need of intermediate Python interpreter calls. Numba supporting NumPy arrays and functions also makes it a good candidate for comparison.

<!-- NumPy and Numba both use a similar type of compilation for ufuncs in manual looping resulting in the same speed.  Another thing that Numba lacks behind is that it does not support all functions of NumPy. There are functions in NumPy which does not hold up some of the optional arguments in nopython mode. It can implement linear algebra calls in the compiled functions but does not return any faster implementation. -->

Implementation details for benchmarking:

* `jit` decorator from Numba was used to compile the Python functions just-in-time.
* `cache = True`: To avoid repetitive compile time.
* Uses NumPy arrays and loops.
* Implemented `jit` decorated functions to call another `jit` decorated functions to increase the performance of our model.

### Pythran

Pythran is a Python-specific Ahead Of Time compiler. Its primary focus was on scientific computing. It uses the same C++ API as NumPy, which was designed specifically for scientific computing. Pythran converts annotated Python modules into native Python modules. These modules have the same interface but (hopefully) are faster to load. Pythran's main advantage is that it uses [Expression Templating](https://en.wikipedia.org/wiki/Expression_templates) and [SIMD](https://en.wikipedia.org/wiki/SIMD) instructions.

NumPy arrays in Cython should be stored in contiguous memory like C-style or Fortran to use Pythran in the backend. Here, the Pythran lacks behind. Another limitation is that the sequence of bytes of words must be the same as the targeted architecture to make Pythran work.

Pythran GitHub repository is available [here](https://github.com/serge-sans-paille/pythran)

## Results

Table values represent the time taken by each algorithm to run on the given datasets for $5$ number of iterations.

<html>
<body>
<table rules = "all">
 <tr>
  <td>Input $\rightarrow$</td>
  <td><b>16</b></td>
  <td><b>32</b></td>
  <td><b>64</b></td>
  <td><b>128</b></td>
 </tr>
 <tr>
  <tr>
  <td><b>Python-NumPy</b></td>
  <td>47.14</td>
  <td>179.6</td>
  <td>726</td>
  <td>3399.8</td>
 </tr>
 <tr>
  <td><b>Pure-NumPy</b></td>
  <td>42.7</td>
  <td>167.8</td>
  <td>758</td>
  <td>3198.2</td>
 </tr>
<tr>
  <td><b>Pure-Python</b></td>
  <td>65.1</td>
  <td>202.3</td>
  <td></td>
  <td></td>
</tr>
 <tr>
  <td><b>C++</b></td>
  <td>0.37</td>
  <td>1.58</td>
  <td>5.46</td>
  <td>22.06</td>
 <tr>
  <td><b>Numba</b></td>
  <td>0.75</td>
  <td>1.11</td>
  <td>1.92</td>     <!-- Zero division error -->
  <td>4.27</td>
 </tr>
 <tr>
  <td><b>Pythran-Naive: Transonic</b></td>
  <td>1.39</td>
  <td>1.16</td>
  <td>1.66</td>
  <td>3.62</td>
 </tr>
</table>
</body>
</html>

**Note** on machine configuration used for benchmarking:

* **Machine:** Intel(R) Core(TM) i7-10870H CPU @ 2.20GHz, 16GB RAM
* **Operating System:** Ubuntu 20.04.2 LTS
* **Library Versions:**
    * Python: 3.8.10
    * NumPy: 1.21.1
    * Numba: 0.53.1
    * Transonic: 0.4.10

## Source Code

* These codes are highly inspired from <a href = "https://github.com/paugier/nbabel">Pierre Augier's work on N-Body Problem</a>.
* Benchmarking Code: <a href = "/benchmarks/python/benchmark-2.py">here</a>.
* Visualization Code: <a href = "/benchmarks/python/plot-modified-1.py">here</a>.

<html>
 <table>
  <tr>
   <td><b>Algorithms</b></td>
   <td><b>Source Codes</b></td>
   <td><b>Implementation Details</b></td>
  </tr>
  <tr>
   <td>Python-NumPy</td>
   <td><a href = "/benchmarks/python/bench_numpy_highlevel.py">bench_numpy_highlevel.py</a></td>
   <td>Optimized NumPy</td>
  </tr>
  <tr>
   <td>Pure-NumPy</td>
   <td><a href = "/benchmarks/python/bench_numpy_highlevel.py">bench_pure_numpy_highlevel.py</a></td>
   <td>Only NumPy Functions</td>
  </tr>
  <tr>
   <td>Pure-Python</td>
   <td><a href = "/benchmarks/python/bench_pure_particle.py">bench_pure_particle.py</a></td>
   <td>Only NumPy Functions</td>
  </tr>
 <tr>
  <td>C++</td>
  <td><a href = "/benchmarks/cpp/main.cpp">main.cpp</a></td>
  <td>Optimized C++</td>
 </tr>
 <tr>
   <td>Numba</td>
   <td><a href = "/benchmarks/python/bench_numba.py">bench_pure_numba.py</a></td>
   <td>Standart puntions of Python Functions</td>
  </tr>
 <tr>
  <td>Pythran-Naive: Transonic Jit</td>
  <td><a href = "/benchmarks/python/bench_numpy_highlevel_jit.py">bench_numpy_highlevel_jit.py</a></td>
  <td>Just-In-Time Compilation</td>
 </tr>
 </table>
</html>


## References

* [Wikipedia's Article on N-Body Problem](https://en.wikipedia.org/wiki/N-body_problem)
* [Dataset used from Pierre Augier's repository](https://github.com/paugier/nbabel/tree/master/data)
