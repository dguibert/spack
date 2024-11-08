# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAstlib(PythonPackage):
    """A set of python modules for producing simple plots, statistics, common calculations,
    coordinate conversions, and manipulating FITS images with World Coordinate System (WCS) information."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://astlib.readthedocs.io/en/latest/"
    pypi = "astLib/astLib-0.11.8.tar.gz"

    version("0.11.8", sha256="2bb3619a71bada2375d5b10ad364a85a0bc631f6580c48537c192b40f70bc5fd")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
