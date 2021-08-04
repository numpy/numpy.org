import time
import math
from typing import List, Dict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_input_data 
from bench import pythran
from bench_numba import numba
from bench_numpy_highlevel_jit import pythran_naive
from bench_numpy_highlevel import numpy_highlevel
from bench_pure_numpy_highlevel import pure_numpy_highlevel


# TODO: Name this function something else
def main(time_step: int, number_of_steps: int, iterations: int, masses: List, positions: List, velocities: List) -> Dict[str, float]:
    """
    This function is used to calculate time for following implementations: NumPy, XYZ, ...

    Parameters
    ==========
    time_step: Interval after which energy of each particle is calculated.
    number_of_steps: Total number of steps taken by particle in the given time.
    masses: mass of each article.
    position: position of particle after each interaction
    velocities: velocites of particle after each interaction

    Returns
    =========
    _time: List[int], Time taken for all types of implementations listed above.
    """
    times = {}

    for loop_function in (pythran, numba, pythran_naive, numpy_highlevel, pure_numpy_highlevel):
        start = time.time()
        for iters in range(iterations):
            energy, energy0 = loop_function(time_step, number_of_steps, masses, positions, velocities)
        end = time.time()
        times[loop_function.__name__] = math.round((end-start)/iterations, 2)

    return times


if __name__ == "__main__":
    masses = []
    positions = []
    velocities = []

    datasets_time = {}
    iterations = 5
    time_end = 10.0
    time_step = 0.001
    number_of_steps = int(time_end/time_step) + 1

    # Iterating over different datasets
    for dataset_name in ["16.txt", "32.txt", "64.txt"]:
        file_path = "input" + dataset_name
        masses, positions, velocities = load_input_data(file_path)
        times_list = main(time_step, number_of_steps, iterations, masses, positions, velocities)
        datasets_time[file_path.strip(".txt")] = times_list

    # Conver tthe output dictionary from datasets_time to a CSV file
    df = pd.DataFrame()
    df = df.append((datasets_time.values()).tolist())
    df.columns = ["Pythran", "Numba", "Pythran Naive", "NumPy", "Pure NumPy"]
    df = df.T
    df.columns =  datasets_time.keys()
    df.to_csv("iter_6-b.csv")
