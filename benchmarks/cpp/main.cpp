#include <iostream>
#include <math.h>
#include <numeric>
#include <vector>

typedef double real;
using namespace std;

// Class Star, contains the properties:
// mass (m)
// position (r)
// velocity (v)
// accelerations (a and a0)

class Star {
public:
  real m;
  vector<real> r;
  vector<real> v;
  vector<real> a, a0;
  // Default constructor
  Star() {
    r.assign(3, 0);
    v.assign(3, 0);
    a.assign(3, 0);
    a0.assign(3, 0);
  }
  // Detailed constructor
  Star(real mass, vector<real> pos, vector<real> vel) {
    m = mass;
    r = pos;
    v = vel;
  }
  // Print function (overloaded << operator)
  friend ostream &operator<<(ostream &so, const Star &si) {
    so << si.m << " " << si.r[0] << " " << si.r[1] << " " << si.r[2] << " "
       << si.v[0] << " " << si.v[1] << " " << si.v[2] << endl;
    return so;
  }
};
// Star cluster based on the Star class
// A star cluster contains a number of stars
// stored in the vector S
//
class Cluster : public Star {
protected:
public:
  vector<Star> s;
  Cluster() : Star() {}
  // Computes the acceleration of each star in the cluster
  void acceleration() {
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si)
      si->a.assign(3, 0);
    // For each star
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      vector<real> rij(3);
      real init = 0.0;
      // For each remaining star
      for (vector<Star>::iterator sj = s.begin(); sj != s.end(); ++sj) {
        if (si != sj) {
          // Distance difference between the two stars
          for (int i = 0; i != 3; ++i)
            rij[i] = si->r[i] - sj->r[i];
          // Sum of the dot product
          real RdotR = inner_product(rij.begin(), rij.end(), rij.begin(), init);
          real apre = 1. / sqrt(RdotR * RdotR * RdotR);
          // Update accelerations
          for (int i = 0; i != 3; ++i) {
            si->a[i] -= sj->m * apre * rij[i];
          }
        } // end for
      }   // si != sj
    }     // end for
  }       // end acceleration

  // Update positions
  void updatePositions(real dt) {
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      // Update the positions, based on the calculated accelerations and
      // velocities
      si->a0 = si->a;
      for (int i = 0; i != 3; ++i) // for each axis (x/y/z)
        si->r[i] += dt * si->v[i] + 0.5 * dt * dt * si->a0[i];
    }
  }

  // Update velocities based on previous and new accelerations
  void updateVelocities(real dt) {
    // Update the velocities based on the previous and old accelerations
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      for (int i = 0; i != 3; ++i)
        si->v[i] += 0.5 * dt * (si->a0[i] + si->a[i]);
      si->a0 = si->a;
    }
  }

  // Compute the energy of the system,
  // contains an expensive O(N^2) part which can be moved to the acceleration
  // part where this is already calculated
  vector<real> energies() {
    real init = 0;
    vector<real> E(3), rij(3);
    E.assign(3, 0);

    // Kinetic energy
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si)
      E[1] += 0.5 * si->m *
              inner_product(si->v.begin(), si->v.end(), si->v.begin(), init);

    // Potential energy
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      for (vector<Star>::iterator sj = si + 1; sj != s.end(); ++sj) {
        for (int i = 0; i != 3; ++i)
          rij[i] = si->r[i] - sj->r[i];
        E[2] -= si->m * sj->m /
                sqrt(inner_product(rij.begin(), rij.end(), rij.begin(), init));
      }
    }
    E[0] = E[1] + E[2];
    return E;
  }

  // Print function
  friend ostream &operator<<(ostream &so, Cluster &cl) {
    for (vector<Star>::iterator si = cl.s.begin(); si != cl.s.end(); ++si)
      so << *si;
    return so;
  }
};

int main(int argc, char* argv[]) {

  Cluster cl;
  real m;
  int dummy;
  vector<real> r(3), v(3);

  // Read input data from the command line (makeplummer | dumbp)
  do {
    cin >> dummy;
    cin >> m;
    for (int i = 0; i != 3; ++i)
      cin >> r[i];
    for (int i = 0; i != 3; ++i)
      cin >> v[i];
    cl.s.push_back(Star(m, r, v));
  } while (!cin.eof());

  // Remove the last one
  cl.s.pop_back();

  // Compute initial energu of the system
  vector<real> E(3), E0(3);
  E0 = cl.energies();
  cerr << "Energies: " << E0[0] << " " << E0[1] << " " << E0[2] << endl;

  // Start time, end time and simulation step
  real t = 0.0;
  real tend;

  if (argc > 1)
    tend = strtod(argv[1], NULL);
  else
    tend = 10.0;

  real dt = 1e-3;
  int k = 0;

  // Initialize the accelerations
  cl.acceleration();

  // Start the main loop
  while (t < tend) {
    // Update positions based on velocities and accelerations
    cl.updatePositions(dt);

    // Get new accelerations
    cl.acceleration();

    // Update velocities
    cl.updateVelocities(dt);

    t += dt;
    k += 1;
    if (k % 100 == 0) {
      E = cl.energies();
      cout << "t= " << t << " E= " << E[0] << " " << E[1] << " " << E[2]
           << " dE/E = " << (E[0] - E0[0]) / E0[0] << endl;
    }
  } // end while

  cout << "number time steps: " << k << endl;

  return 0;
} // end program
