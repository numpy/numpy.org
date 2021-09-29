---
title: NumPy Benchmarks
sidebar: false
---

<img src = "/images/content_images/performance_benchmarking.png" alt = "Visualization" title = "Performance Benchmark; Number of Iterations: 50">

## Overview

This web page aims to benchmark NumPy's performance on the widely accepted N-body problem
<a href="#nbody">[2]</a>. This work also compares NumPy with Python & C++ 
and with compilers like Numba and Pythran.

The objective of benchmarking NumPy revolves around the efficiency of the library in quasi real-life situations, 
and the N-body problem suits the purpose well. 
Benchmarking is performed over several iterations for different datasets to ensure the accuracy of the results.

<!--Towards the end of this post, an attempt will be made to make a conclusion on how NumPy can be efficient in solving problems like N-body problem.-->

<!-- The post is organized as: -->

<!-- Can be made like a content section? -->
<!-- 1. Overview: (current section): Discussing the objective of the post. -->
<!-- 2. About N-body Problem: Brief description on N-body problem and why it was chosen. -->
<!-- 3. Pseudo Code of Solving N-Body Problem. -->
<!-- 4. Dataset Description -->
<!-- 5. Compiled Methods -->
<!-- 6. Source Code -->
<!-- 7. Results -->
<!-- 8. Environment Configuration -->
<!-- 9. Conclusion -->
<!-- 10. References -->

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

From the definition above, the N-body problem includes the kinematics between the different bodies, 
which involve various mathematical computations. 
Solving this problem has been motivated by the desire to understand the motions of the celestial bodies. 
Thus it serves as a robust entity between real-world applications and the computational world. 

A brief description of computations involved in solving the N-body problem is given below, 
along with the pseudo-code in the next section:

Consider $n$ bodies of masses $m_1, m_2, m_3, ... , m_n$, 
moving under the mutual [gravitational force](https://en.wikipedia.org/wiki/Gravity) of attraction 
between them in an [inertial frame of reference](https://en.wikipedia.org/wiki/Inertial_frame_of_reference) of three dimensions, 
such that consecutive  positions and velocities of an ${ith}$ body 
are denoted by ($s_{k-1}$, $s_k$) and ($v_{k-1}$, $v_k$) respectively. 
According to the [Newton's law of gravity](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation), 
the gravitational force felt on the $ith$ body of mass $m_i$ 
by a single body of mass $m_j$ is denoted as $F_{ij}$ 
and the acceleration of the $ith$ body is represented as $a_i$. 
Let $r_i$ and $r_j$ be the position vectors of two body, such that:

\begin{equation} {r_i} = {s_{k}} - {s_{k-1}} \tag{I} \end{equation}

\begin{equation} {r_j} = {s_{k-1}} - {s_{k}} \tag{II} \end{equation} 

The final aim is to find time taken to evaluate the total energy of each particle 
in the celestial space at a given time step. 
The equations involved in solving the problem are listed below:

\begin{equation} {s_k} = {s_{k-1}} + {u\times t} + \frac{a\times t^2}{2} \tag{III} \end{equation}

\begin{equation}{v_k} = {v_{k-1}} + {a\times t} \tag{IV} \end{equation}

\begin{equation} {F_{ij}} = \frac{{G\times {m_i}\times {m_j}}\times \mid {r_j}-{r_i} \mid}{{\mid {r_j}-{r_i} \mid}^3} \tag{V} \end{equation}

\begin{equation} {a_{i}} = \frac{F_{ij}}{m_{j}} \tag{VI} \end{equation}

\begin{equation} \textrm{Self Potential Energy} = \textrm{U} = -\frac{{m_i}\times {m_j}}{r^2} \tag{VII} \end{equation}

\begin{equation} \textrm{Kinetic Energy} = \textrm{K.E} = \frac{\sum m\times v^2}{2} \tag{VIII} \end{equation}

\begin{equation} \textrm{Total Energy} = \textrm{Kinetic Energy} + \textrm{Self Potential Energy} \tag{IX} \end{equation}

### Pseudo Code of Solving N-body Problem

```
Set time to 0, time_step to 0.001 and time_end to 10s
THEN number_of_step is 10/0.001
FOR time is less than or equal to time_end
    Calculate accelerations (a[i], for given position r[i])
    Calculate total initial energies:
        Calculate kinetic energy
        Calculate potential energy
    FOR k less than number_of_step
        Calculate positions (r[k+1])
        Swap accelerations
        Calculate accelerations
        Calculate velocities (v[k+1])
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

An example from the dataset<a href="#data">[3]</a> used is given below: 
(for a single particle, the values are approximated up to four decimal places for readability)

```
# Ordered as: label, mass (grams), position_x, position_y, position_z, velocity_x, velocity_y, velocity_z
-1 0.0625 0.2148  -0.1204  -0.2661 0.7578  0.1576  -0.0715
```

## Compiled Methods

We considered accelerators like [Numba](http://numba.pydata.org/), 
[Pythran](https://transonic.readthedocs.io/), and [Transonic](https://transonic.readthedocs.io/) 
for benchmarking. 
This decision is inspired by [Ralf Gommer's Presentation on SciPy 1.0](https://www.slideshare.net/RalfGommers/scipy-10-and-beyond-a-story-of-community-and-code) 
(conference [video](https://www.youtube.com/watch?v=oHmm3mPxg6Y)). 
We give brief details on a few of the accelerators below:

### Numba

> Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code.

<div style="text-align: right">Source: <a href="http://numba.pydata.org/">Numba's Website</a></div>

Since Numba is a compiler focused on accelerating Python and NumPy codes, 
the user API of the library supports various decorators. 
It uses the industry-standard LLVM compiler library. 
It aims to translate the Python functions to optimized machine code during runtime. 
It supports variety of decorators like `@jit`, `@vectorize`, `@guvectorize`, `@stencil`, `@jitclass`, `@cfunc`, `@overload`. 
We are using `Just-In-Time` compilation in this work. 
It also supports `nopython` mode to generate fully compiled results 
without the need for intermediate Python interpreter calls. 
Numba's assistance to NumPy arrays and functions also makes it a good candidate for comparison.

<!-- NumPy and Numba both use a similar type of compilation for ufuncs in manual looping resulting in the same speed.  Another thing that Numba lacks behind is that it does not support all functions of NumPy. There are functions in NumPy which does not hold up some of the optional arguments in nopython mode. It can implement linear algebra calls in the compiled functions but does not return any faster implementation. -->

### Pythran

> Pythran is an ahead of time compiler for a subset of the Python language, with a focus on scientific computing.

<div style="text-align: right">Source: <a href="https://pythran.readthedocs.io/en/latest/#">Pythran's Website</a></div>

Since the focus of Pythran was on accelerating Python and NumPy codes, 
its C++ API is the same as that of NumPy. 
Pythran also supports [Expression Templating](https://en.wikipedia.org/wiki/Expression_templates) and [SIMD](https://en.wikipedia.org/wiki/SIMD) instructions, which are its main advantages. 
It converts annotated Python modules into native Python modules, which are comparatively faster. 
But both have the same kind of interface.

<!-- NumPy arrays in Cython should be stored in contiguous memory like C-style or Fortran to use Pythran in the backend. Here, the Pythran lacks behind. Another limitation is that the sequence of bytes of words must be the same as the targeted architecture to make Pythran work.-->

## Source Code

* The code is inspired by <a href = "https://github.com/paugier/nbabel">Pierre Augier's work on N-Body Problem</a>.
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
   <td><b>Algorithm & Source Code</b></td>
   <td><b>Implementation Details</b></td>
  </tr>
  <tr>
   <td><a href = "/benchmarks/python/optimized_numpy.py">NumPy</a></td>
   <td>Vectorized Approach, Broadcasting Method, NumPy Arrays</td>
  </tr>
  <tr>
   <td><a href = "/benchmarks/python/pure_python.py">Python</a></td>
   <td>Standard Python Approach, Using List</td>
  </tr>
 <tr>
  <td><a href = "/benchmarks/cpp/main.cpp">C++</a></td>
  <td>C++ Implementation, GNU C++ Compiler</td>
 </tr>
 <tr>
   <td><a href = "/benchmarks/python/compiled_methods.py">Numba</a></td>
   <td>Just-In-time Compilation, Non-Vectorized Approach, Using Numba at the Backend via Transonic, NumPy Arrays</td>
  </tr>
 <tr>
  <td><a href = "/benchmarks/python/compiled_methods.py">Pythran</a></td>
  <td>Just-In-Time Compilation, Non-Vectorized Approach, Pythran at the Backend via Transonic, NumPy Arrays</td>
 </tr>
 </table>
</html>

## Results

Table values represent the normalized time 'time / nParticles` taken in seconds 
by each algorithm to run on the given datasets for $50$ number of iterations. 
The raw timing data can be downloaded from <a href = "benchmarks/data/table.csv">here</a>.

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
  <td><b>32</b></td>
  <td><b>64</b></td>
  <td><b>128</b></td>
  <td><b>256</b></td>
 </tr>
 <tr>
  <tr>
  <td><b>NumPy</b></td>
  <td>13.88</td>
  <td>15.59</td>
  <td>17.90</td>
  <td>18.27</td>
 </tr>
<tr>
  <td><b>Python</b></td>
  <td>26.82</td>
  <td>50.13</td>
  <td>105.01</td>
  <td>178.6</td>
</tr>
 <tr>
  <td><b>C++</b></td>
  <td>3.206</td>
  <td>5.725</td>
  <td>11.44</td>
  <td>19.43</td>
 <tr>
  <td><b>Numba</b></td>
  <td>3.223</td>
  <td>6.521</td>    
  <td>13.64</td>
  <td>26.64</td>
 </tr>
 <tr>
  <td><b>Pythran</b></td>
  <td>0.6591</td>
  <td>1.2811</td>
  <td>2.5082</td>
  <td>5.2042</td>
 </tr>
</table>
</body>
</html>

## Environment configuration

* **CPU Model:** Intel(R) Core(TM) i7-10870H CPU @ 2.20GHz
* **RAM GB:** 16
* **RAM Model:** DDR4
* **Speed:** 3200 MT/s
* **Operating System:** Manjaro Linux 21.1.1, Pahvo
* **Library Versions:**
    * Python: 3.9.6
    * NumPy: 1.20.3
    * Numba: 0.54.0
    * Pythran: 0.9.12.post1
    * Transonic: 0.4.10
    * GCC: 11.1.0
* **Note:** The benchmarking is performed on the $4$ isolated CPU cores for accurate results.

## Conclusion

* NumPy is very efficient, especially for larger datasets. 
NumPy performs $3.2$ times faster than Python for input size $64$, 
$5.8$ times faster for a dataset of size, $128$. 
It gives more than $9.7$ times better performance than Python for input size $256$. 
The performance of NumPy increases drastically as the number of particles in the datasets increases. 
Thanks to the vectorized approach in NumPy. Vectorization makes the code look clean and concise to read. 
It results in better performance without any explicit looping, indexing, etc. 
NumPy's concept of vectorization is handy for the beginner to learn. It is also beneficial for a 
highly skilled developer to debug the errors with fewer lines of code.
* It uses pre-compiled C code, which adds up to the performance of NumPy. 
We can observe from the table the performance of the NumPy approaches to the speed of C++. 
For a dataset of size $64$, NumPy is $2.72$ times slower than C++. For the dataset of size $128$, 
it reaches equivalent to the speed of C++, with a running time of $1.56$ times the time taken by C++. 
NumPy outperforms C++ by $1.06$ times for input size $256$.

**How can we accelerate NumPy?**

NumPy aims to improve itself and to give better performance for the end-users. It performs well in most cases. 
But to fill the gaps where NumPy is not so good various compiled methods 
like Numba, Pythran, etc are used. They play a huge role. In this implementation, 
we used Transonic's JIT Compilation at the backend for NumPy arrays to implement Numba & Pythran. 
To be specific, we want to compare NumPy's vectorized approach with the JIT-compiled non-vectorized approach.

* We observed Numba performs $2.72$ times faster than NumPy for input size $64$ 
and $1.56$ times faster for input size $128$. 
But later, NumPy outperforms Numba by $1.45$ times faster for input size $256$.
* Pythran performs $12.17$ times faster for input size $64$, 
$7.13$ times better for input size $128$, and $3.51$ times faster than NumPy for input size $256$.

We have compared the performance of NumPy with two of the most popular languages 
Python and C++, and with popular compiled methods like Numba and Pythran. 
NumPy achieves better performance for scientific computations 
as well as for solving real-life situations. That's NumPy. 
It stands explicitly well in all kinds of circumstances.

## References

1. [The issue for adding content on performance](https://github.com/numpy/numpy.org/issues/370)
2. <a id="nbody" href="https://en.wikipedia.org/wiki/N-body_problem">Wikipedia's Article on N-Body Problem</a>
3. <a id="data" href="https://github.com/paugier/nbabel/tree/master/data">Dataset used from Pierre Augier's repository</a>
