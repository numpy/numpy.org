---
title: Installing NumPy
sidebar: false
---

The only prerequisite for installing NumPy is Python, but -- particularly if you're new to the scene -- it's likely that your bigger goal is to use one of the many Python packages that depend on NumPy.  If so, see the Anaconda distribution, below.

Package installation is Python's dark underside [\[1\]](#just-installing-stuff). If Python is new to you, we again recommend Anaconda.

{{< figure src="/images/content_images/python_environment_xkcd.png"
           alt="Python Environment XKCD image"
           link="https://xkcd.com/1987/"
           width="400"
           attr="_XKCD illustration - Python environment degradation_">}}


If your results must be reproducible, the time to think about it is now; see [Reproducible Installs](#reproducible-installs).


## Anaconda

Installing Anaconda gives you all the biggest Python scientific/numeric
players in one shot, including Python itself, which can coexist with any
Python you already have. Of course, those packages need disk space -- about 3
GB. If space is an issue, Miniconda is the batteries-not-included version,

Packages besides NumPy that you may want to use right away include

- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) notebooks for
exploratory and interactive computing

- [Spyder](https://www.spyder-ide.org/) or [Visual Studio
Code](https://code.visualstudio.com/) for writing scripts and packages. (The
install asks if you want Visual Studio Code.)

The most convenient way to start programs and manage packages is via [Anaconda
Navigator](https://docs.anaconda.com/anaconda/navigator/), but it's not
required.


## Miniconda

Miniconda is the à la carte version of Anaconda; it takes up about 50 MB. If you have Miniconda, NumPy can be installed with

```bash
conda install numpy
```

OS-specific advice:

#### Windows or macOS

- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Keep the `base` conda environment minimal, and use one or more
  [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
  to install the package you need for the task or project you're working on.
- Unless you're fine with only the packages in the `defaults` channel, make `conda-forge`
  your default channel via [setting the channel priority](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge).

##### Linux with GPU
<li>Install <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a>.</li>
<li>Keep the <code>base</code> conda environment minimal, and use one or more
<a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#">conda environments</a>
to install the package you need for the task or project you’re working on.</li>
<li>Use the <code>defaults</code> conda channel (<code>conda-forge</code> doesn’t have good support for
GPU packages yet).</li>

##### Linux with no GPU
- Install [Miniforge](https://github.com/conda-forge/miniforge).
- Keep the `base` conda environment minimal, and use one or more
  [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
  to install the package you need for the task or project you're working on.

## Package managers

Installing NumPy via your Linux distribution's package manager is not your
best option; you're likely to get an older version, which in turn may limit
your choices for installing libraries using  NumPy.

If you do use the package manager, use it consistently (to install
Python itself, NumPy, and other libraries). If a package isn't included, use `pip`
with the `--user` flag: `pip install somepackage --user`.
This installs the version in your home directory to avoid disturbing the OS.
Do not omit `--user` and use `sudo`, because you may indeed break the OS.
`--user` still doesn't get you off the hook for the whack-a-mole dependency issues in [\[1\]](#just-installing-stuff).

- [Poetry](https://python-poetry.org/) is the best-maintained tool
  for handling dependencies and environment as conda does.


## Deep dive on Python package management

Managing packages is a challenging problem, and, as a result, there are lots of
tools. For web and general purpose Python development there's a whole
[host of tools](https://packaging.python.org/guides/tool-recommendations/)
complementary with pip. For high-performance computing (HPC),
[Spack](https://github.com/spack/spack) is worth considering. For most NumPy
users though, [conda](https://conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) are the two most popular tools.


### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their
functionality partially overlaps (e.g. both can install `numpy`), however, they
can also work together. We'll discuss the major differences between pip and
conda here - this is important to understand if you want to manage packages
effectively.

The first difference is that conda is cross-language and it can install Python,
while pip is installed for a particular Python on your system and installs other
packages to that same Python install only. This also means conda can install
non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while
pip can't.

The second difference is that pip installs from the Python Packaging Index
(PyPI), while conda installs from its own channels (typically "defaults" or
"conda-forge"). PyPI is the largest collection of packages by far, however, all
popular packages are available for conda as well.

The third difference is that pip does not have a _dependency resolver_ (this is
expected to change in the near future), while conda does. For simple cases (e.g.
you just want NumPy, SciPy, Matplotlib, Pandas, Scikit-learn, and a few other
packages) that doesn't matter, however, for complicated cases conda can be
expected to do a better job keeping everything working well together. The flip
side of that coin is that installing with pip is typically a _lot_ faster than
installing with conda.

The fourth difference is that conda is an integrated solution for managing
packages, dependencies and environments, while with pip you may need another
tool (there are many!) for dealing with environments or complex dependencies.

## pip

For those using `pip` knowingly [1], the package to intall is `numpy`
```
pip install numpy
```

<a name="reproducible-installs"></a>
### Reproducible installs

A library update can change your results. It's important to be able to delete and
reconstruct the set of packages you have installed.

Best practice is
1. Use a different environment per project
2. Record at least the names (and preferably versions) of the packages you
directly depend on in a static metadata file. Each packaging tool has its own
format:
- Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
- Pip: [virtual environments](https://docs.python.org/3/tutorial/venv.html) and
  [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
- Poetry: [virtual environments and pyproject.toml](https://python-poetry.org/docs/basic-usage/)

Sometimes it's too much overhead to create and switch between new environments
for small tasks. In that case we encourage you to not install too many packages
into your base environment, and track versions some other
way (e.g. comments inside files, or printing `numpy.__version__` after
importing it in notebooks).


## NumPy packages & accelerated linear algebra libraries

The C-langugage underchassis of NumPy gives it an invisible
dependency on an accelerated linear algebra library -- typically
[Intel MKL](https://software.intel.com/en-us/mkl) or
[OpenBLAS](https://www.openblas.net/).

These will already be present, and to casual users are equivalent.
Power users familiar with these libraries will want to know what they're getting.

* The NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS.
The OpenBLAS libraries are shipped within the wheels itself. This makes those
wheels larger, and if a user installs (for example) SciPy as well, they will
now have two copies of OpenBLAS on disk.

* In the conda defaults channel, NumPy is built against Intel MKL. MKL is a
separate package that will be installed in the users' environment when they
install NumPy. That MKL package is a lot larger than OpenBLAS, several hundred
MB. MKL is typically a little faster and more robust than OpenBLAS.

* In the conda-forge channel, NumPy is built against a dummy "BLAS" package. When
a user installs NumPy from conda-forge, that BLAS package then gets installed
together with the actual library - this defaults to OpenBLAS, but it can also
be MKL (from the defaults channel), or even
[BLIS](https://github.com/flame/blis) or reference BLAS.

Two more things to consider:

- Intel MKL is not open source. This can be a problem downstream
  if a user needs to redistribute an application built with NumPy,

- Both MKL and OpenBLAS do multithreading and may use every CPU core
  available, possibly interfering with other processes like Dask or scikit-learn that
  are also trying to parallelize. The thread maximum is set at build time and
  can be overridden by an environment variable.

  NumPy itself doesn't auto-parallelize any
  function calls.

<a name="just-installing-stuff"></a>
[1] You're in for trouble if you continue your accustomed practice of just installing stuff. Your new package may require a different library version than an existing package, so installing the new package breaks the old one and reinstalling the old one breaks the new one. Operating systems use Python too, so the "package" you break this way might be your OS. Of course solutions exist; your options are to learn them [Deep dive on Python package management][#Deep dive on Python package management] or to use a package (again, like Anaconda) where it's built in.
