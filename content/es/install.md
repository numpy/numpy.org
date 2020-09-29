---
title: Installing NumPy
sidebar: false
---

The only prerequisite for NumPy is Python itself. If you don't have Python yet and want the simplest way to get started, we recommend you use the [Anaconda Distribution](https://www.anaconda.com/distribution) - it includes Python, NumPy, and other commonly used packages for scientific computing and data science.

NumPy can be installed with `conda`, with `pip`, or with a package manager on macOS and Linux. For more detailed instructions, consult our [Python and NumPy installation guide](#python-numpy-install-guide) below.

## conda

If you use `conda`, you can install it with:

```bash
conda install numpy
```

## pip

If you use `pip`, you can install it with:

```bash
pip install numpy
```

<a name="python-numpy-install-guide"></a>

# Python and NumPy installation guide

Installing and managing packages in Python is complicated, there are a number of alternative solutions for most tasks. This guide tries to give the reader a sense of the best (or most popular) solutions, and give clear recommendations. It focuses on users of Python, NumPy, and the PyData (or numerical computing) stack on common operating systems and hardware.

## Recommendations

We'll start with recommendations based on the user's experience level and operating system of interest. If you're in between "beginning" and "advanced", please go with "beginning" if you want to keep things simple, and with "advanced" if you want to work according to best practices that go a longer way in the future.

### Beginning users

On all of Windows, macOS, and Linux:

- Install [Anaconda](https://www.anaconda.com/distribution/) (it installs all packages you need and all other tools mentioned below).
- For writing and executing code, use notebooks in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) for exploratory and interactive computing, and [Spyder](https://www.spyder-ide.org/) or [Visual Studio Code](https://code.visualstudio.com/) for writing scripts and packages.
- Use [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) to manage your packages and start JupyterLab, Spyder, or Visual Studio Code.


### Advanced users

#### Windows or macOS

- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Keep the `base` conda environment minimal, and use one or more [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) to install the package you need for the task or project you're working on.
- Unless you're fine with only the packages in the `defaults` channel, make `conda-forge` your default channel via [setting the channel priority](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge).


#### Linux

If you're fine with slightly outdated packages and prefer stability over being able to use the latest versions of libraries:
- Use your OS package manager for as much as possible (Python itself, NumPy, and other libraries).
- Install packages not provided by your package manager with `pip install somepackage --user`.

If you use a GPU:
- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Keep the `base` conda environment minimal, and use one or more [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) to install the package you need for the task or project you're working on.
- Use the `defaults` conda channel (`conda-forge` doesn't have good support for GPU packages yet).

Otherwise:
- Install [Miniforge](https://github.com/conda-forge/miniforge).
- Keep the `base` conda environment minimal, and use one or more [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) to install the package you need for the task or project you're working on.


#### Alternative if you prefer pip/PyPI

For users who know, from personal preference or reading about the main differences between conda and pip below, they prefer a pip/PyPI-based solution, we recommend:
- Install Python from, for example, [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/), or your Linux package manager.
- Use [Poetry](https://python-poetry.org/) as the most well-maintained tool that provides a dependency resolver and environment management capabilities in a similar fashion as conda does.


## Troubleshooting ImportError

If your installation fails with the message below, see [Troubleshooting ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```

## Building from source

See [Building from source](https://numpy.org/devdocs/user/building.html).


## Python package management

Managing packages is a challenging problem, and, as a result, there are lots of tools. For web and general purpose Python development there's a whole [host of tools](https://packaging.python.org/guides/tool-recommendations/) complementary with pip. For high-performance computing (HPC), [Spack](https://github.com/spack/spack) is worth considering. For most NumPy users though, [conda](https://conda.io/en/latest/) and [pip](https://pip.pypa.io/en/stable/) are the two most popular tools.


### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their functionality partially overlaps (e.g. both can install `numpy`), however, they can also work together. We'll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can't.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically "defaults" or "conda-forge"). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

The third difference is that pip does not have a _dependency resolver_ (this is expected to change in the near future), while conda does. For simple cases (e.g. you just want NumPy, SciPy, Matplotlib, Pandas, Scikit-learn, and a few other packages) that doesn't matter, however, for complicated cases conda can be expected to do a better job keeping everything working well together. The flip side of that coin is that installing with pip is typically a _lot_ faster than installing with conda.

The fourth difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.


### Reproducible installs

Making the installation of all the packages your analysis, library or application depends on reproducible is important. Sounds obvious, yet most users don't think about doing this (at least until it's too late).

The problem with Python packaging is that sooner or later, something will break. It's not often this bad,

{{< figure src="/images/content_images/python_environment_xkcd.png" alt="Python Environment XKCD image" link="https://xkcd.com/1987/" width="400" attr="_XKCD illustration - Python environment degradation_">}}

but it does degrade over time. Hence, it's important to be able to delete and reconstruct the set of packages you have installed.

Best practice is to use a different environment per project you're working on, and record at least the names (and preferably versions) of the packages you directly depend on in a static metadata file. Each packaging tool has its own metadata format for this:
- Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
- Pip: [virtual environments](https://docs.python.org/3/tutorial/venv.html) and [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
- Poetry: [virtual environments and pyproject.toml](https://python-poetry.org/docs/basic-usage/)

Sometimes it's too much overhead to create and switch between new environments for small tasks. In that case we encourage you to not install too many packages into your base environment, and keep track of versions of packages some other way (e.g. comments inside files, or printing `numpy.__version__` after importing it in notebooks).


## NumPy packages & accelerated linear algebra libraries

NumPy doesn't depend on any other Python packages, however, it does depend on an accelerated linear algebra library - typically [Intel MKL](https://software.intel.com/en-us/mkl) or [OpenBLAS](https://www.openblas.net/). Users don't have to worry about installing those, but it may still be important to understand how the packaging is done and how it affects performance and behavior users see.

The NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS. The OpenBLAS libraries are shipped within the wheels itself. This makes those wheels larger, and if a user installs (for example) SciPy as well, they will now have two copies of OpenBLAS on disk.

In the conda defaults channel, NumPy is built against Intel MKL. MKL is a separate package that will be installed in the users' environment when they install NumPy. That MKL package is a lot larger than OpenBLAS, several hundred MB. MKL is typically a little faster and more robust than OpenBLAS.

In the conda-forge channel, NumPy is built against a dummy "BLAS" package. When a user installs NumPy from conda-forge, that BLAS package then gets installed together with the actual library - this defaults to OpenBLAS, but it can also be MKL (from the defaults channel), or even [BLIS](https://github.com/flame/blis) or reference BLAS.

Besides install sizes, performance and robustness, there are two more things to consider:
- Intel MKL is not open source. For normal use this is not a problem, but if a user needs to redistribute an application built with NumPy, this could be an issue.
- Both MKL and OpenBLAS will use multi-threading for function calls like `np.dot`, with the number of threads being determined by both a build-time option and an environment variable. Often all CPU cores will be used. This is sometimes unexpected for users; NumPy itself doesn't auto-parallelize any function calls. It can also be harmful for performance, for example when using another level of parallelization manually or with, e.g. Dask or scikit-learn functionality.

