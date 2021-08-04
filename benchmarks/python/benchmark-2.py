# Benchmarks

# Importing required libraries
import time
import math
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from data_loader import load_input_data 
from bench import pythran
from bench_numba import numba
from bench_numpy_highlevel_jit import pythran_naive
from bench_numpy_highlevel import numpy_highlevel
from bench_pure_numpy_highlevel import pure_numpy_highlevel


def main(_time_step, _number_of_steps, _iterations, _masses, _positions, _velocities):
    
    """Function to calculate time.

    Parameters
    ----------
    _time_step : int
                 Interval after which energy of each particle is calculated
    
    _number_of_steps : int
                       total number of steps taken by particle in the given time

    _masses : numpy.ndarray
              mass of each particle 

    _position : numpy.ndarray
                position of particle after each interaction

    _velocities : numpy.ndarray
                  velocites of particle after each interaction

    Returns
    -------
    _time : 
            Time taken for different types of implementations

    """

    _time = []

    for loop in (pythran, numba, pythran_naive, numpy_highlevel, pure_numpy_highlevel):
    #for loop in (pythran, numba, numpy_highlevel, pure_numpy_highlevel, transonic_boost):
        t = 0
        for iters in range(_iterations):
            start = time.time()
            energy, energy0 = loop(_time_step, _number_of_steps, _masses, _positions, _velocities)
            t += time.time() - start
        _time.append(math.floor(100 * (t / _iterations)) / 100)

    print(_time)
    return _time


if __name__ == "__main__":
    
    _masses = []
    _positions = []
    _velocities = []
    _diff_time = []

    _iterations = 5
    _time_end = 10.0
    _time_step = 0.001
    _number_of_steps = int(_time_end / _time_step) + 1

    # Iterating over different datasets
    for i in ("16.txt", "32.txt", "64.txt"):#, "128.txt", "256.txt", "512.txt", "1k.txt"):
        _file_path = "input"+str(i)
        _masses, _positions, _velocities = load_input_data(_file_path)
        _time = main(_time_step, _number_of_steps, _iterations, _masses, _positions, _velocities)
        _diff_time.append(_time)
    
    #_file_path = "input16.txt"
    #_masses, _positions, _velocities = load_input_data(_file_path)
    #for _iterations in (1, 5, 10, 20, 50, 100, 200):
    #    _time = main(_time_step, _number_of_steps, _iterations, _masses, _positions, _velocities)
    #    _diff_time.append(_time)

    #labels = ["Pythran", "Numba", "Pythran\nNaive", "NumPy", "Pure\nNumPy", "Pythran Opti"] 
    #x = np.arange(len(labels))

    #_data_labels = ["input16.txt", "input32.txt", "input64.txt", "input128.txt", "input256.txt", "input512.txt", "input1k.txt"]
    #_iter_labels = [1, 5, 10, 20, 50, 100, 200]

    df = pd.DataFrame()
    df = df.append((np.array(_diff_time)).tolist())
    df.columns = ["Pythran", "Numba", "Pythran Naive", "NumPy", "Pure NumPy"]
    df = df.T
    #df = df.append((np.array(_diff_time).T).tolist())
    df.columns =  ["input16", "input32", "input64"] #, "input128", "input256", "input512", "input1k"]
    #df.columns = ["Pythran", "Numba", "Pythran Naive", "NumPy", "Pure NumPy", "Pythran Opti"]
    #df.columns = ["Pythran", "Numba", "NumPy", "Pure NumPy", "Pythran Opti"]
    df.to_csv("iter_6-b.csv")


