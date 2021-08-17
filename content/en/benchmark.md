---
title: NumPy Benchmarks
sidebar: false
---

<img src = "/images/content_images/benchmarking-numpy.png" alt = "Visualization" title = "Performance Benchmark; Number of Iterations: 5">


## Overview

This blog post aims to benchmark NumPy's performance on the widely accepted N-body problem<a href="#nbody">[2]</a>. This work also compares NumPy with other popular libraries like pure Python and C++ and compilers like Numba and Pythran.

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

<div style="text-align: right">Source: <a href="https://en.wikipedia.org/wiki/N-body_problem">Wikipedia</a></div>

From the definition above, the N-body problem includes the kinematics between the different bodies, which involve various mathematical computations. Solving this problem has been motivated by the desire to understand the motions of the celestial bodies. Thus it serves as a robust entity between real-world applications and the computational world. 

A brief description of computations involved in solving the N-body problem is given below, along with the pseudo-code in the next section:

Consider $n$ bodies of masses $m_1, m_2, m_3, ... , m_n$, moving under the mutual [gravitational force](https://en.wikipedia.org/wiki/Gravity) of attraction between them in an [inertial frame of reference](https://en.wikipedia.org/wiki/Inertial_frame_of_reference) of three dimensions, such that consecutive  positions and velocities of an ${ith}$ body are denoted by ($s_{i-1}$, $s_i$) and ($v_{i-1}$, $v_i$) respectively. The gravitational force felt on the $ith$ body of mass $m_i$ by a single body of mass $m_j$ is denoted as $F_{gravitational}$ and the acceleration of the $ith$ body is represented as $a_i$. Consider the position vectors of these two bodies as $r_i$ and $r_j$.

The final aim is to find time taken to evaluate the total energy of each particle in the celestial space at a given time step. The equations involved in solving the problem are listed below:

\begin{equation} {s_i} = {s_{i-1}} + {u\times t} + \frac{a\times t^2}{2} \tag{i} \end{equation}

\begin{equation}{v_i} = {v_{i-1}} + {a\times t} \tag{ii} \end{equation}

\begin{equation} {F_{gravitational}} = \frac{{G\times {m_i}\times {m_j}}\times \mid {r_i}-{r_j} \mid}{{\mid {r_i}-{r_j} \mid}^3} \tag{iii} \end{equation}

\begin{equation} {a} = \frac{F_{gravitational}}{m} \tag{iv} \end{equation}

\begin{equation} \textrm{Self Potential Energy} = \textrm{U} = -\frac{{m_i}\times {m_j}}{r^2} \tag{v} \end{equation}

\begin{equation} \textrm{Kinetic Energy} = \textrm{K.E} = \frac{\sum m\times v^2}{2} \tag{vi} \end{equation}

\begin{equation} \textrm{Total Energy} = \textrm{Kinetic Energy} + \textrm{Self Potential Energy} \tag{vii} \end{equation}

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
* Dataset<a href="#data">[3]</a> consists of the masses of each particle and information about their initial positions and velocities along the three-dimensional axis.

An example from the dataset<a href="#data">[3]</a> used is given below: (for a single particle, the values are approximated up to four decimal places for readability)

```
# Ordered as: label, mass (grams), position_x, position_y, position_z, velocity_x, velocity_y, velocity_z
-1 0.0625 0.2148  -0.1204  -0.2661 0.7578  0.1576  -0.0715
```

## Compiled Methods

We considered accelerators like [Numba](http://numba.pydata.org/), [Pythran](https://transonic.readthedocs.io/), and [Transonic](https://transonic.readthedocs.io/) for benchmarking. This decision is inspired by [Ralf Gommer's Presentation on SciPy 1.0](https://www.slideshare.net/RalfGommers/scipy-10-and-beyond-a-story-of-community-and-code) (conference [video](https://www.youtube.com/watch?v=oHmm3mPxg6Y)). We give brief details on a few of the accelerators below:

### Numba

> Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code.

<div style="text-align: right">Source: <a href="http://numba.pydata.org/">Numba's Website</a></div>

Since Numba is a compiler focused on accelerating Python and NumPy codes, the user API of the library supports various decorators. The supported decorators are `@jit, @vectorize, @guvectorize, @stencil, @jitclass, @cfunc, @overload`. It also supports `nopython` mode to generate fully compiled results without the need for intermediate Python interpreter calls. Numba's assistance to NumPy arrays and functions also makes it a good candidate for comparison.

<!-- NumPy and Numba both use a similar type of compilation for ufuncs in manual looping resulting in the same speed.  Another thing that Numba lacks behind is that it does not support all functions of NumPy. There are functions in NumPy which does not hold up some of the optional arguments in nopython mode. It can implement linear algebra calls in the compiled functions but does not return any faster implementation. -->

Implementation details for benchmarking:

* `jit` decorator from Numba was used to compile the Python functions just-in-time.
* `cache = True`: To avoid repetitive compile time.
* Uses NumPy arrays and loops.
* Implemented `jit` decorated functions to call another `jit` decorated functions to increase the performance of our model.

### Pythran

> Pythran is an ahead of time compiler for a subset of the Python language, with a focus on scientific computing.

<div style="text-align: right">Source: <a href="https://pythran.readthedocs.io/en/latest/#">Pythran's Website</a></div>

Since the focus of Pythran was on accelerating Python and NumPy codes, its C++ API is the same as that of NumPy. Pythran also supports [Expression Templating](https://en.wikipedia.org/wiki/Expression_templates) and [SIMD](https://en.wikipedia.org/wiki/SIMD) instructions, which are its main advantages. It converts annotated Python modules into native Python modules, which are comparatively faster. But both have the same kind of interface.

<!-- NumPy arrays in Cython should be stored in contiguous memory like C-style or Fortran to use Pythran in the backend. Here, the Pythran lacks behind. Another limitation is that the sequence of bytes of words must be the same as the targeted architecture to make Pythran work.-->

## Results

Table values represent the normalized time taken in seconds by each algorithm to run on the given datasets for $5$ number of iterations.

<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>
<table>
 <tr>
  <td>Input(s) $\rightarrow$</td>
  <td><b>16</b></td>
  <td><b>32</b></td>
  <td><b>64</b></td>
  <td><b>128</b></td>
 </tr>
 <tr>
  <tr>
  <td><b>Python-NumPy</b></td>
  <td>0.1841</td>
  <td>0.1753</td>
  <td>0.1772</td>
  <td>0.2075</td>
 </tr>
 <tr>
  <td><b>Pure-NumPy</b></td>
  <td>0.1667</td>
  <td>0.1638</td>
  <td>0.1850</td>
  <td>0.1952</td>
 </tr>
<tr>
  <td><b>Pure-Python</b></td>
  <td>0.2542</td>
  <td>0.1975</td>
  <td>0.1081</td>
  <td>0.1135</td>
</tr>
 <tr>
  <td><b>C++</b></td>
  <td>0.0014</td>
  <td>0.0015</td>
  <td>0.0013</td>
  <td>0.0013</td>
 <tr>
  <td><b>Numba</b></td>
  <td>0.0029</td>
  <td>0.0010</td>
  <td>0.0004</td>     <!-- Zero division error -->
  <td>0.0002</td>
 </tr>
 <tr>
  <td><b>Pythran-Naive: Transonic</b></td>
  <td>0.0054</td>
  <td>0.0011</td>
  <td>0.0004</td>
  <td>0.0002</td>
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

* The code is highly inspired by <a href = "https://github.com/paugier/nbabel">Pierre Augier's work on N-Body Problem</a>.
* Benchmarking Code: <a href = "/benchmarks/python/benchmark-2.py">here</a>.
* Visualization Code: <a href = "/benchmarks/python/plot.py">here</a>.

<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
 <table>
  <tr>
   <td><b>Algorithms</b></td>
   <td><b>Source Code</b></td>
   <td><b>Implementation Details</b></td>
  </tr>
  <tr>
   <td>Optimized-NumPy</td>
   <td><a href = "/benchmarks/python/bench_numpy_highlevel.py">bench_numpy_highlevel.py</a></td>
   <td>Optimized NumPy</td>
  </tr>
  <tr>
   <td>NumPy</td>
   <td><a href = "/benchmarks/python/bench_numpy_highlevel.py">bench_pure_numpy_highlevel.py</a></td>
   <td>Pure NumPy Implementation</td>
  </tr>
  <tr>
   <td>Pure-Python</td>
   <td><a href = "/benchmarks/python/bench_pure_particle.py">bench_pure_particle.py</a></td>
   <td>Pure Python Implementation</td>
  </tr>
 <tr>
  <td>C++</td>
  <td><a href = "/benchmarks/cpp/main.cpp">main.cpp</a></td>
  <td>Optimized C++</td>
 </tr>
 <tr>
   <td>Numba</td>
   <td><a href = "/benchmarks/python/bench_numba.py">bench_pure_numba.py</a></td>
   <td>Just-In-time Compilation</td>
  </tr>
 <tr>
  <td>Pythran: Transonic Jit</td>
  <td><a href = "/benchmarks/python/bench_numpy_highlevel_jit.py">bench_numpy_highlevel_jit.py</a></td>
  <td>Just-In-Time Compilation</td>
 </tr>
 </table>
</html>


## References

1. [The issue for adding content on performance](https://github.com/numpy/numpy.org/issues/370)
2. <a id="nbody" href="https://en.wikipedia.org/wiki/N-body_problem">Wikipedia's Article on N-Body Problem</a>
3. <a id="data" href="https://github.com/paugier/nbabel/tree/master/data">Dataset used from Pierre Augier's repository</a>
