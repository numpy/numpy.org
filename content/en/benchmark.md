---
title: NumPy Benchmarks
sidebar: false
---

<img src = "/images/content_images/benchmark-plot.jpg" alt = "Visualization" title = "Performance Benchmark">

**Note:**

* Machine Configurations:
    * **Machine:** Intel(R) Core(TM) i7-10870H CPU @ 2.20GHz, 16GB RAM
    * **Operating System:** Ubuntu 20.04.2 LTS
    * **Library Versions:** Python: 3.8.10, NumPy: 1.21.1, Numba: 0.53.1, Transonic: 0.4.10
    * **Methodology:**  

<!-- TODO: Add analysis of graph -->

## Overview

Benchmarking is the process of estimating and appraising the best among all the existing practices. This benchmark aims to understand how Python, NumPy, and their various subsets stand and to improve their performance and procedures of libraries accordingly. The aim is to present the current positions and help the end-users select the best existing practices.

We selected the N-Body problem as a reference algorithm for benchmarking. The aim is to examine the efficiency of NumPy in quasi-real-life situations. The task is to show that how Python-NumPy can be efficient even for computationally intensive tasks. 
The scope of the N-body problem takes us to scientific computations involving many processes in a single problem statement. N-body problem is one of the most famous universally accepted problems in the community and is easy to understand (comparatively).
All these reasons make the N-Body problem a good problem benchmarking problem.

## About N-Body Problem

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Let us consider $n$ bodies of masses $m_1, m_2, m_3, ..., m_n$, moving under the mutual [gravitational force](https://en.wikipedia.org/wiki/Gravity) of attraction between them in an [inertial frame of reference](https://en.wikipedia.org/wiki/Inertial_frame_of_reference) of three dimension. Such that consecutive  positions and velocities of the bodies are denoted by $s_{i-1}$, $s_i$ and $v_{i-1}$, $v_i$. The force gravitational force felt on body of mass $m_i$ by a single mass $m_j$ is denoted as $F$ and the acceleration  of the body of mass $m_i$ is represented as $a$. Consider the position vectors of these particles as $r_i$ and $r_j$.
 
For more details visit [Wikipedia](https://en.wikipedia.org/wiki/N-body_problem).

Mathematically,

$$\begin{equation} {s_i} = {s_{i-1}} + {u\times t} + \frac{a\times t^2}{2} \tag{i} \end{equation}$$

$$\begin{equation}{v_i} = {v_{i-1}} + {a\times t} \tag{ii} \end{equation}$$

$$\begin{equation} {F} = \frac{{G\times {m_i}\times {m_j}}\times \mid {r_i}-{r_j} \mid}{{\mid {r_i}-{r_j} \mid}^3} \tag{iii} \end{equation}$$

$$\begin{equation} {F} = {m\times a} \tag{iv} \end{equation}$$

$$\begin{equation} {a} = \frac{F}{m} \tag{v} \end{equation}$$

$$\begin{equation} \textrm{Self Potential Energy} = \textrm{U} = -\frac{{m_i}\times {m_j}}{r^2} \tag{vi} \end{equation}$$

$$\begin{equation} \textrm{Kinetic Energy} = \textrm{K.E} = \frac{\sum m\times v^2}{2} \tag{vii} \end{equation}$$

## Pseudo Code

<!-- TODO: To add subsripts ($a_i$) -->

```bash
Set time to 0, time_step to 0.001 and time_end to 10s
THEN number_of_step is 10/0.001
FOR time is less than or equal to time_end 
    Call compute_accelerations ($a_i$, for given position $r_i$)
    Compute initial_energies:
        Call compute_kinetic_energy
        Call compute_potential_energy
    FOR i less than number_of_steps
        Call advance_positions ($r_{i+1}$)
        Swap accelerations
        Call compute_accelerations
        Call advance_velocities ($v_{i+1}$)
        Increment time
        IF number_of_step % 100 is not 0 THEN
            Call compute_energies
            Print energy
        ENDIF
    END FOR
END FOR
```

## Dataset Description

The dataset consists of nine different text files with 16, 32, 64, 128, 256, 512, 1k, 2k, and 16k particles. It contains the masses of particles, information about their positions, and velocities along the x, y, and z-axis. The number of rows in the datasets varies depending on the dataset. The dataset has 8 columns, the first column consists of a data entry, and the next column tells about the particle's mass. The other three columns represent the particle's positions along the x, y, and z-axes, while the other three represent the particle's velocities along the three-dimensional axis.

## Implemented Accelerators

The decision on choosing libraries for benchmarking is taken from the [presentation by Ralf Gommers](https://www.slideshare.net/RalfGommers/scipy-10-and-beyond-a-story-of-community-and-code) (conference [video](https://www.youtube.com/watch?v=oHmm3mPxg6Y)) on Scipy 1.0.

### Numba

Numba is the Just In Time compiler of the Python functions. It translates codes to machine codes using LLVM compiler infrastructure. NumPy supports diversified features in Numba like passing NumPy arrays as arguments, including structured `dtypes`, ufuncs, generalized ufuncs, and many more. Numba uses nopython mode to generate fully compiled results without the need for intermediate Python interpreter calls. Its user API supports diversified decorators like `@jit`, `@vectorize`, `@guvectorize`, `@stencil`, `@jitclass`, `@cfunc`, and `@overload`; which make it easier to use. Numba is popular in the community since it saves so much time. Numba is approximate 10x times faster than NumPy. 

NumPy and Numba both use a similar type of compilation for ufuncs in manual looping resulting in the same speed.  Another thing that Numba lacks behind is that it does not support all functions of NumPy. There are functions in NumPy which does not hold up some of the optional arguments in nopython mode. It can implement linear algebra calls in the compiled functions but does not return any faster implementation.

Visit [here](https://numba.pydata.org/) to know more about Numba.

Implementation details:

* `jit` decorator from Numba was used to compile the Python functions just-in-time.
* `cache = True`: To avoid repetitive compile time. 
* Used NumPy arrays and loops.
* Implemented `jit` decorated functions to call another `jit` decorated functions to increase the performance of our model.

### Pythran

Pythran is a Python-specific Ahead Of Time compiler. Its primary focus was on scientific computing. It uses the same C++ API as NumPy, which was designed specifically for scientific computing. Pythran converts annotated Python modules into native Python modules. These modules have the same interface but (hopefully) are faster to load. Pythran's main advantage is that it uses [Expression Templating](https://en.wikipedia.org/wiki/Expression_templates) and [SIMD](https://en.wikipedia.org/wiki/SIMD) instructions.  

NumPy arrays in Cython should be stored in contiguous memory like C-style or Fortran to use Pythran in the backend. Here, the Pythran lacks behind. Another limitation is that the sequence of bytes of words must be the same as the targeted architecture to make Pythran work.

Pythran GitHub repository is available [here](https://github.com/serge-sans-paille/pythran)

## Results

Table values represent the time taken by each algorithm to run, in respected datasets for 5 iterations.

<html>
<table>
 <tr>
  <td></td>
  <td><b>Input 16 (s)</b></td>
  <td><b>Input 32 (s)</b></td>
  <td><b>Input 64 (s)</b></td>
  <td><b>Input 128 (s)</b></td>
  <td><b>Input 256 (s)</b></td>
  <td><b>Input 512 (s)</b></td>
  <td><b>Input 1k (s)</b></td>
  <td><b>Input 2k (s)</b></td>
  <td><b>Input 16k (s)</b></td>
 </tr>
 <tr>
  <tr>
  <td><b>Python-NumPy</b></td>
  <td>10.15</td>
  <td>45.2</td>
  <td>161.01</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td><b>Pure-NumPy</b></td>
  <td>10.56</td>
  <td>41.59</td>
  <td>169.4</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td><b>C++</b></td>
  <td>0.04</td>
  <td>0.07</td>
  <td>0.24</td>
  <td> 0.94</td>
  <td>3.90</td>
  <td>15.28</td>
  <td>62.56</td>
  <td>251.27</td>
  <td>19082.54</td>
 <tr>
  <td><b>Numba</b></td>
  <td>0.89/ 0.72/ 0.02</td>
  <td>0.05/ 0.05</td>
  <td>0.17/ 0.17</td>     <!-- Zero division error -->
  <td> 0.61/ 0.60</td>
  <td>2.40/ 2.66/ 2.31</td>          <!-- Zero division error -->
  <td>10.56/ 10.09</td>
  <td>37.39/ 40.17</td>
  <td>160.62/ 145.89</td>
  <td></td>
 </tr>
 </tr>
  <td><b>Pythran: Transonic</b></td>
  <td>10.37/ 9.17</td>
  <td>41.88</td>
  <td>160.15</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td><b>Pythran-Naive: Transonic</b></td>
  <td>0.01</td>
  <td>0.05</td>
  <td>0.17</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
</table>
</html>

## Source Code

* These codes are highly inspired from <a href = "https://github.com/paugier/nbabel">here</a>.
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
  <td>C++</td>
  <td><a href = "/benchmarks/cpp/main.cpp">main.cpp</a></td>
  <td>Optimized C++</td>
 </tr>
<tr>
  <td>Numba</td>
  <td> <a href = "/benchmarks/python/bench_numba.py">bench_numba.py</a></td>
  <td>Just-In-Time Compilation</td>
</tr>
<tr>
  <td>Pythran: Transonic Boost</td>
  <td> <a href = "/benchmarks/python/bench.py">bench.py</a></td>
  <td>Ahead-Of-Time Compilation</td>
</tr>
<tr>
  <td>Pythran-Naive: Transonic Jit</td>
  <td><a href = "/benchmarks/python/bench_numpy_highlevel_jit.py">bench_numpy_highlevel_jit.py</a></td>
  <td>Just-In-Time Compilation</td>
</tr>
  </table>
</html>

