import sys
import math
import time
from datetime import timedelta

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

def advance_positions(positions, velocities, accelerations, time_step):
    positions += velocities * time_step + 0.5 * accelerations * time_step ** 2

def advance_velocities(velocities, accelerations, accelerations1, time_step):
    velocities += 0.5 * time_step * (accelerations + accelerations1)


def compute_accelerations(accelerations, masses, positions):
    nb_particles = masses.size
    for index_p0 in range(nb_particles - 1):
        position0 = positions[index_p0]
        mass0 = masses[index_p0]
        vector = np.empty(3)
        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]
            position1 = positions[index_p1]
            for i in range(3):
                vector[i] = position0[i] - position1[i]
            
            distance = sum(vector ** 2) * math.sqrt(sum(vector ** 2))
        
            coef_m1 = mass0 / distance 
            coef_m2 = mass1 / distance
           
            for i in range(3):
                accelerations[index_p0][i] -= coef_m1 * vector[i]
                accelerations[index_p1][i] += coef_m2 * vector[i]

    return accelerations

def numpy_highlevel(
        time_step: float, 
        number_of_steps: int, 
        masses: "float[]", 
        positions: "float[:,:]", 
        velocities: "float[:,:]",
    ):
    accelerations = np.zeros_like(positions)
    accelerations1 = np.zeros_like(positions)

    # Initial Acceleration
    accelerations = compute_accelerations(accelerations, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(number_of_steps):
        advance_positions(positions, velocities, accelerations, time_step)
        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        compute_accelerations(accelerations, masses, positions)
        advance_velocities(velocities, accelerations, accelerations1, time_step)
        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            #print(
            #    f"t = {time_step * step:5.2f}, E = {energy:.7f}, "
            #    f"dE/E = {(energy - energy_previous) / energy_previous:+.7f}"
            #)
            energy_previous = energy

    return math.floor((10000000*energy)/10000000), math.floor((10000000*energy0)/10000000)
    #return energy, energy0

def compute_kinetic_energy(masses, velocities):
    return 0.5 * np.sum(masses * np.sum(velocities ** 2, 1))


def compute_potential_energy(masses, positions):
    number_of_particles = masses.size
    pe = 0.0              
    for index_p0 in range(number_of_particles - 1):
        mass = masses[index_p0]
        for index_p1 in range(index_p0 + 1, number_of_particles):
            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]
            distance = math.sqrt(sum(vector ** 2))
            pe -= (mass * mass1) / distance
    return pe

def compute_energies(masses, positions, velocities):
    ke = compute_kinetic_energy(masses, velocities)
    pe = compute_potential_energy(masses, positions)
    return ke+pe, ke, pe

if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    number_of_steps = int(time_end/time_step) + 1

    path_input = sys.argv[1]
    
    masses, positions, velocities = load_input_data(path_input)
    
    start = time.time()
    energy, energy0 = numpy_highlevel(time_step, number_of_steps, masses, positions, velocities)
    end = time.time()

    print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
    print(
            f"{number_of_steps} time steps run in {timedelta(seconds=end-start)}"
    )

