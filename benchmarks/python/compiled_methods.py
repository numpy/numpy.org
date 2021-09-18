import sys
import math
import timeit

import numpy as np
import pandas as pd

from transonic import jit

def load_input_data(path):

    df = pd.read_csv(
        path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter=r"\s+"
    )

    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()

    return masses, positions, velocities

def compute_accelerations(accelerations, masses, positions):
    nb_particles = masses.size

    for index_p0 in range(nb_particles - 1):
        position0 = positions[index_p0]
        mass0 = masses[index_p0]
        
        # TODO: Use compiled methods like Numba & Pythran in vectorized approach.
        # Issue: https://github.com/khushi-411/numpy-benchmarks/issues/4
        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]

            vectors = position0 - positions[index_p1]

            distances = (vectors**2).sum()
            coefs = 1./distances**1.5

            accelerations[index_p0] += mass1 * -1 * vectors * coefs
            accelerations[index_p1] += mass0 * vectors * coefs

    return accelerations

@jit
def loop(
        time_step, nb_steps, masses, positions,
        velocities):

    accelerations = np.zeros_like(positions)
    accelerations1 = np.zeros_like(positions)

    accelerations = compute_accelerations(accelerations, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(nb_steps):
        positions += time_step*velocities + 0.5*accelerations*time_step**2

        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        accelerations = compute_accelerations(accelerations, masses, positions)

        velocities += 0.5*time_step*(accelerations+accelerations1)

        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            energy_previous = energy

    return energy, energy0

def compute_energies(masses, positions, velocities):

    ke = 0.5 * masses @ np.sum(velocities**2, axis=1)

    nb_particles = masses.size
    pe = 0.0
    for index_p0 in range(nb_particles - 1):

        mass0 = masses[index_p0]
        for index_p1 in range(index_p0 + 1, nb_particles):

            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]

            distance = math.sqrt((vector**2).sum())

            pe -= (mass0*mass1) / distance**2

    return ke+pe, ke, pe

if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    nb_steps = int(time_end/time_step) + 1

    path_input = sys.argv[1]
    masses, positions, velocities = load_input_data(path_input)

    print('time taken:', timeit.timeit('loop(time_step, nb_steps, masses, positions, velocities)', globals=globals(), number=50))
