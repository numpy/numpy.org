---
title: Installing NumPy
sidebar: false
---

The only prerequisite for installing NumPy is Python, but -- particularly if you're new to the scene -- it's likely that your bigger goal is to use one of the many Python packages that depend on NumPy.  If so, see the [Anaconda](https://www.anaconda.com/products/individual) distribution, below.

Package installation is Python's dark underside [\[1\]](#just-installing-stuff). If Python is new to you, we again recommend Anaconda.

{{< figure src="/images/content_images/python_environment_xkcd.png"
           alt="Python Environment XKCD image"
           link="https://xkcd.com/1987/"
           width="400"
           attr="_Image credit: xkcd_">}}


If your results must be reproducible, the time to think about it is now; see [Reproducible Installs](#reproducible-installs).


## Anaconda

Installing [Anaconda](https://www.anaconda.com/products/individual) gives you all the biggest Python scientific/numeric
players in one shot, including Python itself, which can coexist with any
Python you already have. Of course, those packages need disk space -- about 3
GB. If space is an issue, [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is the batteries-not-included version,

Packages besides NumPy that you may want to use right away include

- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) notebooks for
exploratory and interactive computing

- [Spyder](https://www.spyder-ide.org/) or [Visual Studio
Code](https://code.visualstudio.com/) for writing scripts and packages. (The
install will ask if you want Visual Studio Code.)

[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) is a
convenient way to start programs and manage packages, but you can use the command line instead.


## Miniconda

[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is the à la carte version of Anaconda; it takes up about 50 MB. If you have Miniconda, NumPy can be installed with

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

Installing NumPy via your OS package manager is a poor choice:
* You're likely to get an older version, which in turn may limit your choices for installing a library that uses  NumPy.
* You'll be vulnerable to the dependency issues in [\[1\]](#just-installing-stuff) if you need to install a library
that's not in the distribution.

If you do use the package manager, use it consistently (to install Python
itself, NumPy, and other libraries). If a package isn't included and you must
resort to `pip`, use the `--user` flag: `pip install somepackage --user`. This
installs into your home directory. Do not omit `--user` and use `sudo`,
because it can break Python dependencies in your OS,


## pip

The package to intall is `numpy`:
```
pip install numpy
```


## pip versus conda

[conda](https://conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) are Python's two most popular package managers.

For high-performance computing (HPC), [Spack](https://github.com/spack/spack) is also
an option; we don't cover it here.




**conda** can install Python as well as
non-Python libraries and tools (e.g. compilers, CUDA, HDF5); **pip** is
installed for a particular Python version on your system and installs packages
to that Python only.

**pip** installs from the Python Packaging Index
(PyPI); **conda** installs from its own channels (typically "defaults" or
"conda-forge"). Though conda's repos include over 1,500 packages, PyPI has over 150,000.
If a package is unavailable through conda, pip can be used in the conda environment to install it.

Both pip and conda try to resolve dependencies, but **conda** has a
_dependency resolver_ -- before starting, it determines how to satisfy the
dependencies of all packages at once -- while **pip** handles dependencies on the fly as it installs, so a
package installed later can break a package installed earlier.

**conda** can create isolated environments, each with different packages and
Python versions; this is how the whack-a-mole dependency hell of
[\[1\]](#just-installing-stuff) can be avoided. **pip** by itself lacks this;
you must install a virtual environment (<a href="https://virtualenv.pypa.io/en/latest/">virtualenv</a> or
<a href="https://docs.python.org/3/library/venv.html">venv</a>) or use a tool that wraps pip and a
virtual environment (<a href="https://poetry.eustace.io/">poetry</a> is the best-maintained of these).


<a name="reproducible-installs"></a>
## Reproducible installs

As libraries get updated, your results can change. It's important to be able to
reconstruct your sets of packages and versions.

Best practice is
1. Put each project in a different environment
2. Snapshot names and versions using your package installer; each
has its own metadata format:
   - Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
   - Pip: [virtual environments](https://docs.python.org/3/tutorial/venv.html) and
     [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
   - Poetry: [virtual environments and pyproject.toml](https://python-poetry.org/docs/basic-usage/)


## NumPy packages & accelerated linear algebra libraries

The C-language underchassis of NumPy gives it an invisible
dependency on an accelerated linear algebra library -- typically
[Intel MKL](https://software.intel.com/en-us/mkl) or
[OpenBLAS](https://www.openblas.net/).

The libraries will already be present on your system. To casual users, they're equivalent;
power users will want to know details of what they're getting:

* The NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS.
The OpenBLAS libraries are included in the wheel. This makes the
wheel larger, and if a user installs (for example) SciPy, they will
have two copies of OpenBLAS on disk.

* In the conda defaults channel, NumPy is built against Intel MKL. MKL is a
separate package that will be installed in the users' environment when they
install NumPy. The MKL package is a lot larger than OpenBLAS, several hundred
MB. MKL is typically a little faster and more robust than OpenBLAS.

* In the conda-forge channel, NumPy is built against a dummy "BLAS" package. When
a user installs NumPy from conda-forge, that BLAS package then gets installed
together with the actual library - this defaults to OpenBLAS, but it can also
be MKL (from the defaults channel), or even
[BLIS](https://github.com/flame/blis) or reference BLAS.

* Intel MKL is not open source. This can be a problem downstream
  if a user needs to redistribute an application built with NumPy,

* Both MKL and OpenBLAS may use every CPU core
  available, possibly interfering with other processes like Dask or scikit-learn that
  are also trying to parallelize. The thread maximum is set at build time and
  can be overridden by an environment variable.

  NumPy itself doesn't auto-parallelize any function calls.

<a name="just-installing-stuff"></a> [1] You're in for trouble if you continue
your non-Python practice of just installing stuff. The package you're
installing may require a different version of library X than an existing
package, so installing the new package breaks the old one and reinstalling the
old one breaks the new one. Operating systems use Python too, so the "package"
you break this way might be your OS. The solution is to install packages into
virtual environments: You run tool A in an environment that satisfies tool A's
dependencies and run tool B (possibly on the same files) in an environment
that satisfies B's.