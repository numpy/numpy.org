#include <iostream>
#include <math.h>
#include <numeric>
#include <vector>

typedef double real;
using namespace std;

class Star {
public:
  real m;
  vector<real> r;
  vector<real> v;
  vector<real> a, a0;

  Star() {
    r.assign(3, 0);
    v.assign(3, 0);
    a.assign(3, 0);
    a0.assign(3, 0);
  }

  Star(real mass, vector<real> pos, vector<real> vel) {
    m = mass;
    r = pos;
    v = vel;
  }

  friend ostream &operator<<(ostream &so, const Star &si) {
    so << si.m << " " << si.r[0] << " " << si.r[1] << " " << si.r[2] << " "
       << si.v[0] << " " << si.v[1] << " " << si.v[2] << endl;
    return so;
  }
};

class Cluster : public Star {
protected:
public:
  vector<Star> s;
  Cluster() : Star() {}

  void acceleration() {
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si)
      si->a.assign(3, 0);

    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      vector<real> rij(3);
      real init = 0.0;

      for (vector<Star>::iterator sj = s.begin(); sj != s.end(); ++sj) {
        if (si != sj) {

          for (int i = 0; i != 3; ++i)
            rij[i] = si->r[i] - sj->r[i];

          real RdotR = inner_product(rij.begin(), rij.end(), rij.begin(), init);
          real apre = 1. / sqrt(RdotR * RdotR * RdotR);

          for (int i = 0; i != 3; ++i) {
            si->a[i] = sj->m * -1 * apre * rij[i];
          }
        }
      }
    }
  }

  void updatePositions(real dt) {
    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      si->a0 = si->a;
      for (int i = 0; i != 3; ++i)
        si->r[i] += dt * si->v[i] + 0.5 * dt * dt * si->a0[i];
    }
  }

  void updateVelocities(real dt) {

    for (vector<Star>::iterator si = s.begin(); si != s.end(); ++si) {
      for (int i = 0; i != 3; ++i)
        si->v[i] += 0.5 * dt * (si->a0[i] + si->a[i]);
      si->a0 = si->a;
    }
  }

  vector<real> energies() {
    real init = 0;
    vector<real> E(3), rij(3);
    E.assign(3, 0);

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

  cl.s.pop_back();

  // Compute initial energu of the system
  vector<real> E(3), E0(3);
  E0 = cl.energies();

  // Start time, end time and simulation step
  real t = 0.0;
  real tend;

  if (argc > 1)
    tend = strtod(argv[1], NULL);
  else
    tend = 10.0;

  real dt = 1e-3;
  int k = 0;

  for (int i = 0; i < 50; i++) {
    cl.acceleration();

    while (t < tend) {
      cl.updatePositions(dt);

      cl.acceleration();

      cl.updateVelocities(dt);

      t += dt;
      k += 1;
      if (k % 100 == 0) {
        E = cl.energies();
      }
    }
    t = 0;
  }

  return 0;
}
