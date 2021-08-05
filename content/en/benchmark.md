---
title: NumPy Benchmarking
sidebar: false
---

<img src = "/static/images/content_images/benchmark-plot.jpg" alt = "Visualization">

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



N-Body problem is the system of n-particles in space where the task is to evaluate the motion of each individual particles. The task becomes more interesting when there are several other factors to consider while evaluating the motion of those particles.

**General Formulation:** 

<!-- Better idea for heading? -->

* $n$-particles exist in space such that their masses are denoted by $m_1, m_2, m_3, ..., m_n$.
* Force on particle: $F$
* Acceleration: $a$
* Initial velocity of each particle: $v_{i-1}$.
* Velocity after nth second: $v_i$.
* Initial position of particle: $s_{i-1}$.
* Postion after ith second: $s_i$.
* Position vectors: $r_i$, $r_j$


See [Wikipedia](https://en.wikipedia.org/wiki/N-body_problem) for more details.

Mathematically, these factors can be formulated as:

\begin{equation}
 {s_i} = {s_{i-1}} + {u\times t} + \frac{a\times t^2}{2} \tag{i}
\end{equation}

\begin{equation}
 {v_i} = {v_{i-1}} + {a\times t} \tag{ii}
\end{equation}

By the Newton's Law of Gravitation the force felt on particle of mass $m_i$ by the particle of mass $m_j$ is given by:

\begin{equation}
 {F} = \frac{{G\times {m_i}\times {m_j}}\times \mid {r_i}-{r_j} \mid}{{\mid {r_i}-{r_j} \mid}^3} \tag{iii}
\end{equation}

By Newton's second laws of the motion, force of the particle is given by:

\begin{equation}
 {F} = {m\times a} \tag{iv}
\end{equation}

The acceleration can now be formulated as:

\begin{equation}
 {a} = \frac{F}{m} \tag{v}
\end{equation}

Particles in universe mainly possess two types of energy:

**Potential Energy:** Energy due to virtue of position. It's given by:

\begin{equation}
 \textrm{U} = -\frac{{m_i}\times {m_j}}{r^2} \tag{vi}
\end{equation}
 
**Kinetic Energy:** Energy due to virtue of motion. Formula:

\begin{equation}
 \textrm{K.E} = \frac{\sum m\times v^2}{2} \tag{vii}
\end{equation}


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

The decision on choosing libraries for benchmarking was done on the basis of their popularity (in terms of usage in the community) and their relevance.

### Numba

Numba is the Just In Time compiler of the Python functions. It translates codes to machine codes using LLVM compiler infrastructure. NumPy support varity of features in Numba like passing NumPy arrays as arrguments, including structured `dtypes`, ufuncs, generalized ufuncs and many more. They are also capable of using variety of NumPy's function in `nopython` mode which helps functions to generate fully compiled result hence removing mediating Python interpretator calls. It supports variety of decoartors `@jit`, `@vectorize`, `@guvectorize`, `@stencil`, `@jitclass`, `@cfunc`, and `@overload`. 

NumPy and Numba both uses compiled ufuncs, hence they both gives same result in manual looping which is one of the limitation of Numba. Another thing in which Numba lacks behind is that is does not support all functions of NumPy, there are functions in NumPy which does not support some of the optional arrguments in nopython mode. Numba is capable of using linear algebra calls in the compiled functions but does not return any faster implementation.

Same kind of technology is used by Julia for acceleration. Numba is heavily used in community and since it helps saving a lot of time - thus, this was chosen as one of the candidates for benchmarking. NumPy is approximately 10x times slower than Numba. 

Implementation details:

* `jit` decorator from Numba was used to compile the Python functions just-in-time.
* `cache = True`: To avoid repetitive compile time. 
* Used NumPy arrays and loops.
* Implemented `jit` decorated functions to call another `jit` decorated functions to increase the performance of our model.

### Cython


### Pythran


### Transonic

Transonic is a pure python package. It is one of the actively growing libraries which is used to increase the speed of our codes. Here, we are operating with two kinds of accelerators in the backend jit and boost to accelerate our code. Transonic uses four different types of accelerators in the backend Pythran, Cython, Numba, and Python. Presently, we have implemented Jit and boost accelerators, in the next iteration, we will be using Cython, with different types of backends.

#### Transonic - JIT

We used Transonic jit to accelerate our code. To implement this we used Pythran (Ahead-Of-Time) compiler in Just-In-Time mode. 

#### Transonic - Boost: Pythran

Pythran is an Ahead Of Time compiler. This module takes a Python file as an input then converts it into some kind of interface which makes the code faster. Transonic's boost decorator replaces the python function with the pythranized function. 

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
  <td>0.89</td>
  <td>0.05</td>
  <td>0.17</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 </tr>
  <td><b>Transonic: Pythran</b></td>
  <td>10.37</td>
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

## Source Code of Benchmarking

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
  </tr>
  <tr>
   <td>Pure NumPy</td>
   <td><a href = "https://github.com/khushi-411/numpy.org/tree/khushi-411/add-benchmarks/benchmarks/python/bench_numpy_highlevel.py">bench_pure_numpy_highlevel.py</a></td>
  </tr>
 <tr>
  <td>C++</td>
  <td><a href = "https://github.com/khushi-411/numpy.org/blob/khushi-411/add-benchmarks/benchmarks/cpp/main.cpp">main.cpp</a></td>
 </tr>
<tr>
  <td>Numba</td>
  <td> <a href = "https://github.com/khushi-411/numpy.org/tree/khushi-411/add-benchmarks/benchmarks/python/bench_numba.py">bench_numba.py</a></td>
</tr>
<tr>
  <td>Transonic: Pythran</td>
  <td> <a href = "https://github.com/khushi-411/numpy.org/tree/khushi-411/add-benchmarks/benchmarks/python/bench.py">bench.py</a></td>
</tr>
<tr>
  <td>Transonic: Pythran Naive</td>
  <td><a href = "https://github.com/khushi-411/numpy.org/tree/khushi-411/add-benchmarks/benchmarks/python/bench_numpy_highlevel_jit.py">bench_numpy_highlevel_jit.py</a></td>
</tr>
  </table>
</html>


## Conclusion

* NumPy satisfactorily performs better than most of the chosen libraries (....). Numba and Pythran Naive do perform better than NumPy but it's also because of their scope and applications.
