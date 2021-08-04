# Using Pythran

import sys
import time
import math
from datetime import timedelta

import numpy as np
import pandas as pd

from transonic import boost
from transonic import set_compile_at_import
from pathlib import Path

# transonic def pythran(float, int, float, float[:, :], float[:,:])

def get_ts_mod_display_state(name):
    ts = modules[name]
    print(
        "(is_transpiled, is_compiling, is_compiled) =",
        (ts.is_transpiled, ts.is_compiling, ts.is_compiled),
    )
    return ts

src = """
from transonic import boost
import sys
import time
from datetime import timedelta
import pandas as pd
import numpy as np
import math

def load_input_data(path):
    df = pd.read_csv(
        path, names=["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter=r"\s+"
    )

    # with numpy 1.20.3 and pandas 1.2.4
    masses = np.ascontiguousarray(df["mass"].values)
    positions = np.ascontiguousarray(df.loc[:, ["x", "y", "z"]].values)
    velocities = np.ascontiguousarray(df.loc[:, ["vx", "vy", "vz"]].values)

    return masses, positions, velocities


def advance_positions(positions, velocities, accelerations, time_step):
    positions += time_step * velocities + 0.5 * accelerations * time_step ** 2


def advance_velocities(velocities, accelerations, accelerations1, time_step):
    velocities += 0.5 * time_step * (accelerations + accelerations1)


def compute_distance(vec):
    return math.sqrt(sum(vec ** 2))

def compute_accelerations(accelerations, masses, positions):
    number_of_particles = masses.size
    for particle_1_index in range(number_of_particles - 1):
        position_1 = positions[particle_1_index]
        masses_1 = masses[particle_1_index]
        vector = np.empty(3)
        for particle_2_index in range(particle_1_index +1, number_of_particles):
            masses_2 = masses[particle_2_index]
            position_2 = positions[particle_2_index]
            for i in range(3):
                vector[i] = position_1[i] - position_2[i]

            distance = sum(vector ** 2) * math.sqrt(sum(vector ** 2))
            coef_m1 = masses_1 / distance
            coef_m2 = masses_2 / distance
            for i in range(3):
                accelerations[particle_1_index][i] -= coef_m1 * vector[i]
                accelerations[particle_2_index][i] += coef_m2 * vector[i]
    return accelerations


@boost
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
        advance_positions(positions, velocities, accelerations, time_step)
        # swap acceleration arrays
        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        compute_accelerations(accelerations, masses, positions)
        advance_velocities(velocities, accelerations, accelerations1, time_step)
        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            # f-strings supported by Pythran>=0.9.8
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
    nb_particules = masses.size
    pe = 0.0
    for index_p0 in range(nb_particules - 1):
        mass0 = masses[index_p0]
        for index_p1 in range(index_p0 + 1, nb_particules):
            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]
            distance = compute_distance(vector)
            pe -= (mass0 * mass1) / distance
    return pe


def compute_energies(masses, positions, velocities):
    energy_kin = compute_kinetic_energy(masses, velocities)
    energy_pot = compute_potential_energy(masses, positions)
    return energy_kin + energy_pot, energy_kin, energy_pot


if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    nb_steps = int(time_end / time_step) + 1

    path_input = "/mnt/c/Users/khush/Documents/Quansight-Intern/data/input16.txt"
    masses, positions, velocities = load_input_data(path_input)
    
    start = time.time()
    energy, energy0 = pythran_loop(time_step, nb_steps, masses, positions, velocities)
    end = time.time()

    print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
    print(
        f"{nb_steps} time steps run in {timedelta(seconds=end-start)}"
    )
"""


with open("bench-func.py", "w") as file:
    file.write(src)

paths = Path("__pythran__").glob("bench-func*.*")
for path in paths:
    path.unlink()

set_compile_at_import(True)
