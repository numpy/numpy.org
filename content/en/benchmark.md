---
title: NumPy Benchmarking
sidebar: false
---

<img src = "/static/images/content_images/benchmark-plot.jpg" alt = "Visualization" title = "Performance Benchmark">

**Note:**

* These benchmarks are run with an Intel(R) Core(TM) i7-10870H CPU @ 2.20GHz.
* 

<!-- TODO: Add analysis of graph -->

## Introduction

## Objective

- Why did you choose to benchmark? 
- Important to understand how NumPy performs with other relevant and commonly used libraries in the community.

## What makes the N-Body problem a good benchmark?

The scope of N-body problem takes us to scientific computations involving many processes in a single problem. The aim of this benchmarking is to understand how different libraries perform compared to NumPy and while there can be several problems which can be picked up, but N-body problem is one of the problems which are universally accepted in the community and easy to understand (comparatively).

As mentioned above, N-Body problem comprises of several numerical computations which are helpful in benchmarking tasks, for an example: computing distances, velocities and accelerations involve various arithmetical operations.

## About N-Body Problem

Let us consider $n$ bodies of masses $m_1, m_2, m_3, ..., m_n$, moving under the mutual [gravitational force](https://en.wikipedia.org/wiki/Gravity) of attraction between them in an [inertial frame of reference](https://en.wikipedia.org/wiki/Inertial_frame_of_reference) of three dimension. Such that consequetive positions and velocities of the bodies are denoted by $s_{i-1}$, $s_i$ and $v_{i-1}$, $v_i$. The force gravitational force felt on body of mass $m_i$ by a single mass $m_j$ is denoted as $F$ and the acceleration  of the body $m_i$ is represented as $a$. Consider the position vectors of these particles as $r_i$ and $r_j$. 

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

The dataset consists of nine different text files consisting datas of 16, 32, 64, 128, 256, 512, 1k, 2k and 16k number of particles. It contains the masses of particles and information regarding their positions and velocities along the x-axis, y-axis and z-axis respectively. The datasets have varrying number of rows depending on the datasets but the number of columns are fixed. They have 8 columns in which 1st column shows an entry of data, the next column tells about the mass of particle. The other 3 of them shows the positions of the particle along the x, y and z-axis and the next 3 columns represents velocities of the particle along the 3-dimentional axis.

## Implemented Accelerators

The decision on choosing libraries for benchmarking is taken from the [presentation by Ralf Gommers](https://www.slideshare.net/RalfGommers/scipy-10-and-beyond-a-story-of-community-and-code) (conference [video](https://www.youtube.com/watch?v=oHmm3mPxg6Y)) on Scipy 1.0.

### Numba

Numba is the Just In Time compiler of the Python functions. It translates codes to machine codes using LLVM compiler infrastructure. NumPy support varity of features in Numba like passing NumPy arrays as arrguments, including structured `dtypes`, ufuncs, generalized ufuncs and many more. They are also capable of using variety of NumPy's function in `nopython` mode which helps functions to generate fully compiled result hence removing mediating Python interpretator calls. It's user API supports variety of decoartors like `@jit`, `@vectorize`, `@guvectorize`, `@stencil`, `@jitclass`, `@cfunc`, and `@overload` which make it easier to use. 

NumPy and Numba both uses compiled ufuncs, hence they both gives same result in manual looping which is one of the limitation of Numba. Another thing in which Numba lacks behind is that is does not support all functions of NumPy, there are functions in NumPy which does not support some of the optional arrguments in nopython mode. Numba is capable of using linear algebra calls in the compiled functions but does not return any faster implementation.

Same kind of technology is used by Julia for acceleration. Numba is heavily used in community and since it helps saving a lot of time - thus, this was chosen as one of the candidates for benchmarking. NumPy is approximately 10x times slower than Numba. 

Visit [here](https://numba.pydata.org/) to know more about Numba.

Implementation details:

* `jit` decorator from Numba was used to compile the Python functions just-in-time.
* `cache = True`: To avoid repetitive compile time. 
* Used NumPy arrays and loops.
* Implemented `jit` decorated functions to call another `jit` decorated functions to increase the performance of our model.

### Pythran

Pythran is a Python-specific Ahead Of Time compiler. It's primary focus was on scientific computing. It has the same C++ API implementation as in NumPy which was originally designed for the purpose of scientific computing. In Pythran, annotated Python modules are converted into native Python modules which have the same interface, but (hopefully) are faster to load. Pythran's biggest benefit is that it uses [Expression Templating](https://en.wikipedia.org/wiki/Expression_templates) and [SIMD](https://en.wikipedia.org/wiki/SIMD) instructions. Pythran was designed with an aim to use it as a backend for NumPy arrays in Cython when possible.  

To use Pythran in the model it needs to be stored in contiguous memory like C-style or like Fortran, this is where Pythran lacks behind. Another limitation is that the order of sequence of bytes of works must be same as the targeted architecture to make Pythran work.

Pythran GitHub repository is available [here](https://github.com/serge-sans-paille/pythran)

Implementation details:

* 

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
  <td><b>NumPy</b></td>
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
  <td><b>Pure NumPy</b></td>
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
  <td><b>Transonic: Pythran</b></td>
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
  <td><b>Transonic: Pythran Naive</b></td>
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
   <td>NumPy</td>
   <td><a href = "/benchmarks/python/bench_numpy_highlevel.py">bench_numpy_highlevel.py</a></td>
   <td>Optimized NumPy</td>
  </tr>
  <tr>
   <td>Pure NumPy</td>
   <td><a href = "/benchmarks/python/bench_numpy_highlevel.py">bench_pure_numpy_highlevel.py</a></td>
   <td>Only NumPy Functions</td>
  </tr>
 <tr>
  <td>C++</td>
  <td><a href = "/benchmarks/cpp/main.cpp">main.cpp</a></td>
  <td></td>
 </tr>
<tr>
  <td>Numba</td>
  <td> <a href = "/benchmarks/python/bench_numba.py">bench_numba.py</a></td>
  <td>Just-In-Time Compilation</td>
</tr>
<tr>
  <td>Transonic: Pythran</td>
  <td> <a href = "/benchmarks/python/bench.py">bench.py</a></td>
  <td>Ahead-Of-Time Compilation</td>
</tr>
<tr>
  <td>Transonic: Pythran Naive</td>
  <td><a href = "/benchmarks/python/bench_numpy_highlevel_jit.py">bench_numpy_highlevel_jit.py</a></td>
  <td>Just-In-Time Compilation</td>
</tr>
  </table>
</html>


## Conclusion

* NumPy satisfactorily performs better than most of the chosen libraries (....). Numba and Pythran Naive do perform better than NumPy but it's also because of their scope and applications.
