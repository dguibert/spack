# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-ddfacet
#
# You can edit this file again by typing:
#
#     spack edit py-ddfacet
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDdfacet(PythonPackage):
    """A facet-based radio imaging package"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/saopicc/DDFacet"
    pypi = "DDFacet/DDFacet-0.7.2.0.tar.gz"

    version("mpi", git="/home_nfs/bguibertd/work/2020-WW-SKA/code/ddfacet")
    version("0.7.2.0", sha256="09350602ea83814b5acfcbfc677e8efe5a2bcd0687c6da294aa9e3526d42d0c8")

    conflicts("python@3.9:")

    depends_on("py-nose@1.3.7:")            # "nose >= 1.3.7; python_version >= '3'",
    depends_on("py-cython@0.25.2:0.29.30")  # "Cython >= 0.25.2, <= 0.29.30; python_version >= '3'",
    depends_on("py-numpy@1.15.1:1.19.5")    # "numpy >= 1.15.1, <= 1.19.5; python_version >= '3'",
    depends_on("py-sharedarray@3.2.0:3.2.1")# "sharedarray >= 3.2.0, <= 3.2.1; python_version >= '3'",
    depends_on("py-polygon3@3.0.8:3.0.9.1") # "Polygon3 >= 3.0.8, <= 3.0.9.1; python_version >= '3'",
    depends_on("py-pyfftw@0.10.4:0.12.0")   # "pyFFTW >= 0.10.4, <= 0.12.0; python_version >= '3'",
    depends_on("py-astropy@3.0:4.1")        # "astropy >= 3.0, <= 4.1; python_version >= '3'",
    depends_on("py-deap@1.0.1:1.3.1")       # "deap >= 1.0.1, <= 1.3.1; python_version >= '3'",
    depends_on("py-ptyprocess")      # "ptyprocess>=0.5, <= 0.7.0; python_version >= '3'",
    depends_on("py-ipdb")            # "ipdb >= 0.10.3, <=0.13.9; python_version >= '3'",
    depends_on("py-python-casacore") # "python-casacore >= 3.0.0, <=3.4.0; python_version >= '3'",
    depends_on("py-ephem")           # "pyephem >= 3.7.6.0, <=9.99; python_version >= '3'",
    depends_on("py-numexpr")         # "numexpr >= 2.6.2,<=2.8.1; python_version >= '3'",
    depends_on("py-matplotlib")      # "matplotlib >= 2.0.0,<=3.3.4; python_version >= '3'",
    depends_on("py-scipy")           # "scipy >= 1.3.3,<=1.5.4; python_version >= '3'",
    depends_on("py-astlib")          # "astLib >= 0.8.0,<=0.11.7; python_version >= '3'",
    depends_on("py-psutil")          # "psutil >= 5.2.2,<=5.9.1; python_version >= '3'",
    depends_on("py-pycpuinfo")       # "py-cpuinfo >= 3.2.0,<=8.0.0; python_version >= '3'",
    depends_on("py-tables")          # "tables >= 3.6.0,<=3.7.0; python_version >= '3'",
    depends_on("py-prettytable")     # "prettytable >= 0.7.2,<=2.5.0; python_version >= '3'",
    depends_on("py-pybind11")        # "pybind11 >= 2.2.2,<=2.9.2; python_version >= '3'",
    depends_on("py-configparser")    # "configparser >= 3.7.1,<=5.2.0; python_version >= '3'",
    depends_on("py-pandas")          # "pandas >=0.23.3,<=1.1.5; python_version >= '3'",
    depends_on("py-ruamel-yaml")     # "ruamel.yaml >= 0.15.92,<=0.17.21; python_version >= '3'",
    depends_on("py-pylru")           # "pylru >= 1.1.0,<=1.2.1; python_version >= '3'",
    depends_on("py-six")             # "six >= 1.12.0,<=1.16.0; python_version >= '3'",
    depends_on("py-dask@1.1.0:2021.3.0") # "dask[array] >= 1.1.0,<=2021.3.0; python_version >= '3'",
    depends_on("py-codex-africanus@:0.2.10") # "codex-africanus[dask] <= 0.2.10; python_version >= '3'",
    depends_on("py-regions@:0.5")          # "regions <=0.5",
    depends_on("py-pywavelets@:1.1.1")     # "pywavelets <=1.1.1",

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-scikit-build-core+pyproject", type="build")
