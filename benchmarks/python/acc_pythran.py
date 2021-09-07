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

        vectors = position0 - positions[index_p0 + 1: nb_particles]

        distances = np.square(vectors).sum(axis = 1)
        coefs = distances ** 1.5

        _x = np.add(np.sum(
            np.divide(
                np.multiply(
                    masses[index_p0 + 1: nb_particles], -1 * vectors.T
                    ),
                coefs).T, axis = 0),
            accelerations[index_p0]
            )
        accelerations[index_p0] = _x

        _temp = np.add(
                np.divide(
                np.multiply(
                    mass0, vectors.T
                    ),
                coefs).T,
            accelerations[index_p0 + 1: nb_particles]
            )
        accelerations[index_p0 + 1: nb_particles] = _temp

    return accelerations

@jit
def pythran_loop(
        time_step: float,
        nb_steps: int,
        masses: "float[]",
        positions: "float[:,:]",
        velocities: "float[:,:]",
    ):

    accelerations = np.zeros_like(positions)
    accelerations1 = np.zeros_like(positions)

    accelerations = compute_accelerations(accelerations, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(nb_steps):
        positions = sum(np.multiply(velocities, time_step), 0.5 *  np.multiply(accelerations, time_step ** 2)) + positions

        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        accelerations = compute_accelerations(accelerations, masses, positions)

        velocities = 0.5 * np.multiply(time_step, np.add(accelerations, accelerations1)) + velocities

        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            energy_previous = energy

    return energy, energy0

def compute_energies(masses, positions, velocities):

    ke = 0.5 * (np.multiply(masses, np.square(velocities).sum(axis = 1)).sum())

    nb_particles = masses.size

    pe = 0.0
    for index_p0 in range(nb_particles - 1):
        mass0 = masses[index_p0]

        for index_p1 in range(index_p0 + 1, nb_particles):

            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]

            distance = np.sqrt((vector ** 2).sum())

            pe = np.subtract(np.divide(np.multiply(mass0, mass1), np.square(distance)), pe)

    return ke + pe, ke, pe

if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    nb_steps = int(time_end/time_step) + 1

    path_input = sys.argv[1]
    masses, positions, velocities = load_input_data(path_input)

    print('time taken:', timeit.timeit('pythran_loop(time_step, nb_steps, masses, positions, velocities)', globals = globals(), number = 50))
