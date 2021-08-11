import sys
import math
import time
from itertools import combinations
from datetime import timedelta


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def _zero(cls):
        return cls(0.0, 0.0, 0.0)

    def norm(self):
        return math.sqrt(self.norm2())

    def norm_cube(self):
        norm2 = self.norm2()
        return norm2 * math.sqrt(norm2)

    def norm2(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def __repr__(self):
        return f"[{self.x:.10f}, {self.y:.10f}, {self.z:.10f}]"

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(other * self.x, other * self.y, other * self.z)

    __rmul__ = __mul__

    def reset_to_0(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0


def make_inlined_point(name):
    x = f"_{name}_x"
    y = f"_{name}_y"
    z = f"_{name}_z"

    def get(self):
        return Point3D(getattr(self, x), getattr(self, y), getattr(self, z))

    def set(self, value):
        setattr(self, x, value.x)
        setattr(self, y, value.y)
        setattr(self, z, value.z)

    return property(get, set)


class Particle:
    """
    A Particle has mass, position, velocity and acceleration.
    """

    position = make_inlined_point("position")
    velocity = make_inlined_point("velocity")
    acceleration = make_inlined_point("acceleration")
    acceleration1 = make_inlined_point("acceleration1")

    def __init__(self, mass, x, y, z, vx, vy, vz):
        self.mass = mass
        self.position = Point3D(x, y, z)
        self.velocity = Point3D(vx, vy, vz)
        self.acceleration = Point3D(0.0, 0.0, 0.0)
        self.acceleration1 = Point3D(0.0, 0.0, 0.0)

    @property
    def ke(self):
        return 0.5 * self.mass * self.velocity.norm2()


class Cluster(list):
    """
    A Cluster is just a list of particles with methods to accelerate and
    advance them.
    """

    @property
    def ke(self):
        return sum(particle.ke for particle in self)

    @property
    def pe(self):
        pe = 0.0
        for p1, p2 in combinations(self, 2):
            vector = p1.position - p2.position
            distance = math.sqrt(vector.norm2())
            pe -= (p1.mass * p2.mass) / distance
        return pe

    @property
    def energy(self):
        return self.ke + self.pe

    def step(self, dt):
        self.__advance_positions(dt)
        self.accelerate()
        self.__advance_velocities(dt)

    def accelerate(self):
        for particle in self:
            particle.acceleration1 = particle.acceleration
            particle.acceleration = Point3D(0.0, 0.0, 0.0)

        nb_particules = len(self)
        for i0 in range(nb_particules - 1):
            p0 = self[i0]
            for i1 in range(i0 + 1, nb_particules):
                p1 = self[i1]
                delta = p0.position - p1.position
                distance_cube = delta.norm_cube()
                p0.acceleration -= p1.mass / distance_cube * delta
                p1.acceleration += p0.mass / distance_cube * delta

    def __advance_positions(self, dt):
        for p in self:
            p.position += dt * p.velocity + 0.5 * dt ** 2 * p.acceleration

    def __advance_velocities(self, dt):
        for p in self:
            p.velocity += 0.5 * dt * (p.acceleration + p.acceleration1)


if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.

    time_step = 0.001

    start = time.time()
    for i in range(5):  
        cluster = Cluster()
        with open(sys.argv[1]) as input_file:
            for line in input_file:
                try:
                    cluster.append(Particle(*[float(x) for x in line.split()[1:]]))
                except TypeError:
                    pass

        old_energy = energy0 = energy = -0.25
        cluster.accelerate()
        for step in range(1, int(time_end / time_step + 1)):
            cluster.step(time_step)
            if not step % 100:
                energy = cluster.energy
                #print(
                #    f"t = {time_step * step:.2f}, E = {energy:.10f}, "
                #    f"dE/E = {(energy - old_energy) / old_energy:.10f}"
                #)
                old_energy = energy
    
    end = time.time()

    print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
    print(f"run in {timedelta(seconds=end - start)}")
