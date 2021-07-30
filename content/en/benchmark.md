# NumPy Benchmarking


![output-modify-2-new](https://user-images.githubusercontent.com/62256509/127653679-5151e22d-d141-4621-abb9-b3e6dd7988b7.jpg)


## Implemented Algorithms

Till this point 5 algorithms are implemented as mentioned bellow:

### NumPy

NumPy is a most fundamental package for scientific computing in Python. The major advantage of using NumPy is these gives same computational speed as C and Fortran. Let's see our inplementation details:

#### NumPy Python

Here, we used optimised code which consists of both type of implementation i.e. via Python and NumPy. This algorithm took 10.15 seconds for datasets with 16 points, 45.2 seconds for datasets with 32 points and 161.01 seconds for datasets with 64 points. 

#### Pure NumPy

This algorithm is purely implemented via NumPy library functions. It takes 10.56 seconds to run a program with datasets of 16 points, 41.59 seconds for datasets with 32 points and 169.4 seconds for datasets with 64 points.

### Transonic

Transonic is a pure python package. It is one of the actively growing libraries which is used to increase the speed of our codes. Here, we are operating with two kinds of accelerators in the backend jit and boost to accelerate our code. Transonic uses four different types of accelerators in the backend Pythran, Cython, Numba, and Python. Presently, we have implemented Jit and boost accelerators, in the next iteration, we will be using Cython, with different types of backends.

#### Transonic - JIT

We used Transonic jit to accelerate our code. To implement this we used Pythran (Ahead-Of-Time) compiler in Just-In-Time mode. This algorithm took 0.01 seconds for input datasets with 16 points, 0.05 seconds for input datasets with 32 points and 0.17 seconds for input datasets with 64 points.
 
#### Transonic - Boost: Pythran

Pythran is an Ahead Of Time compiler. This module takes a Python file as an input then converts it into some kind of interface which makes the code faster. Transonic's boost decorator replaces the python function with the pythranized function. This algorithm took 10.37 seconds for input data of 16 points, 41.88 seconds for input data with 32 points and 160.15 seconds for input data with 64 points.

### Numba

Numba converts the Python files to optimized machine code during runtime. The major advantage is after compiling codes using Numba, the speed of code becomes approachable to C or FORTRAN. Numba caches all the compiled functions into a file system for future use of the same functions. We used the jit decorated functions to call another jit decorated function while implementing our code. It is advisable to add the jit decorated function to other functions too, so as to prevent it from generating slower outputs. This algorithm took 0.89 seconds for input data with 16 points, 0.05 seconds for input data with 32 points and 0.17 seconds for input data with 64 points.

## Results 

Table values represent the time taken by each algorithm to run, in respected datasets for 5 iterations.

<html>
<table>
 <tr>
  <td></td>
  <td><b>Input 16</b></td>
  <td><b>Input 32</b></td>
  <td><b>Input 64</b></td>
 </tr>
 <tr>
  <td><b>Pythran</b></td>
  <td>10.37</td>
  <td>41.88</td>
  <td>160.15</td>
 </td>
 <tr>
  <td><b>Numba</b></td>
  <td>0.89</td>
  <td>0.05</td>
  <td>o.17</td>
 </tr>
 <tr>
  <td><b>Pythran Naive</b></td>
  <td>0.01</td>
  <td>0.05</td>
  <td>0.17</td>
 </tr>
 <tr>
  <td><b>NumPy</b></td>
  <td>10.15</td>
  <td>45.2</td>
  <td>161.01</td>
 </tr>
 <tr>
  <td><b>Pure NumPy</b></td>
  <td>10.56</td>
  <td>41.59</td>
  <td>169.4</td>
 </tr>
</table>
</html>

## Code Folders

* These codes are originally taken from [here](https://github.com/paugier/nbabel)
* Benchmark code: [here](https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/benchmark-2.py)
* Graph: [here](https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/plot-modified-1.py)

<html>
 <table>
<tr> 
  <td><b>Algorithms</b></td>
  <td><b>Source Codes</b></td>
</tr>
<tr>
  <td>Pythran</td>
  <td> <a href = "https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/bench.py">bench.py</a></td>
</tr>
<tr> 
  <td>Numba</td>
  <td> <a href = "https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/bench_numba.py">bench_numba.py</a></td>
</tr>
<tr>
  <td>Pythran Naive</td>
  <td><a href = "https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/bench_numpy_highlevel_jit.py">bench_numpy_highlevel_jit.py</a></td>
</tr>
<tr>
  <td>NumPy</td>
  <td><a href = "https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/bench_numpy_highlevel.py">bench_numpy_highlevel.py</a></td>
</tr>
<tr>
  <td>Pure NumPy</td>
  <td><a href = "https://github.com/khushi-411/numpy-benchmarks/blob/0.3/python/bench_numpy_highlevel.py">bench_pure_numpy_highlevel.py</a></td>
</tr>
  </table>
</html>


## Conclusion

* These benchmarks are run with an Intel Core i7 processor.
* We found that codes that use Numba and Pythran Naive as accelerators give the best results among all.

## Acknowledgement

I would like to thank [Matti Picus](https://github.com/mattip) for helping me and guiding me throughout these days. Thank you so much!

