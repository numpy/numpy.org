import sys
import math
import timeit

import numpy as np
import pandas as pd

def load_input_data(path):

    df = pd.read_csv(
        path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter=r"\s+"
    )

    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()

    return masses, positions, velocities

def compute_accelerations(accelerations, masses, positions):
    nb_particles = len(masses)

    for index_p0 in range(nb_particles - 1):
        position0 = positions[index_p0]
        mass0 = masses[index_p0]

        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]

            vector = [p0 - p1 for (p0, p1) in zip(position0, positions[index_p1])]

            distance = 0
            for i in vector:
                distance += i**2
            coefs = 1./distance**1.5

            accelerations[index_p0] = [sum(i) for i in zip([vec_val * mass1 * -1 * coefs for vec_val in vector], accelerations[index_p0])]
            accelerations[index_p1] = [sum(i) for i in zip([vec_val * mass0 * coefs for vec_val in vector], accelerations[index_p1])]

    return accelerations

def loop(
    time_step: float,
    nb_steps: int,
    masses: "float[]",
    positions: "float[:,:]",
    velocities: "float[:,:]",
):

    accelerations = [[0.0 for _ in range(3)] for _ in range(len(positions))]
    accelerations1 = [[0.0 for _ in range(3)] for _ in range(len(positions))]

    accelerations = compute_accelerations(accelerations, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(nb_steps):
        pos_val = []
        for (vel, acc) in zip(velocities, accelerations):
            pos = []
            for (v, a) in zip(vel, acc):
                pos.append(v*time_step + 0.5*a*time_step**2)
            pos_val.append(pos)

        positions1 = []
        for (pos_val1, pos1) in zip(pos_val, positions):
            pos_1 = []
            for (pos_val0, pos0) in zip(pos_val1, pos1):
                pos_1.append(pos_val0 + pos0)
            positions1.append(pos_1)
        positions = positions1

        accelerations, accelerations1 = accelerations1, accelerations
        accelerations = [[0.0 for acc0 in acc1] for acc1 in accelerations]
        accelerations = compute_accelerations(accelerations, masses, positions)

        new_accelerations = []
        for (acc, acc1) in zip(accelerations, accelerations1):
            new_acc = []
            for (a, a1) in zip(acc, acc1):
                new_acc.append(a + a1)
            new_accelerations.append(new_acc)

        velocities1 = []
        for (acc, vel) in zip(new_accelerations, velocities):
            vel1 = []
            for (a, v) in zip(acc, vel):
                vel1.append(v + a*time_step)
            velocities1.append(vel1)
        velocities = velocities1

        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            energy_previous = energy

    return energy, energy0

def compute_energies(masses, positions, velocities):

    vel = []
    for ind, val in enumerate(velocities):
        vel.append([j**2 for j in val])
    val = []
    for i in vel:
        k = 0
        for j in i:
            k += j
        val.append(k)
    ke_list = [0.5*i*masses[ind] for ind, i in enumerate(val)]
    ke = 0.0
    for i in ke_list:
        ke += i

    nb_particles = len(masses)
    pe = 0.0
    for index_p0 in range(nb_particles - 1):
        mass0 = masses[index_p0]

        for index_p1 in range(index_p0 + 1, nb_particles):

            mass1 = masses[index_p1]
            vector = [p0 - p1 for (p0, p1) in zip(positions[index_p0], positions[index_p1])]

            dist = 0
            for i in vector:
                dist += i**2
            distance = math.sqrt(dist)

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

    masses = masses.tolist()
    positions = positions.tolist()
    velocities = velocities.tolist()

    print('time taken', timeit.timeit('loop(time_step, nb_steps, masses, positions, velocities)', globals=globals(), number=50))
