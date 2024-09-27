# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRegions(PythonPackage):
    """Astropy coordinated package for region handling"""

    homepage = "https://github.com/astropy/regions"
    pypi = "regions/regions-0.7.tar.gz"

    version("0.7", sha256="75387ef2dfcca46c7716803a81c68dba3669005e01ddf6d0bf254edb677a9a23")
    version("0.5", sha256="ac89875ac8b52277322a54e952d3bd7d1f48510aaf342354e07df005996459ae")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-extension-helpers", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython@0.29.30:", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-astropy", type=("build", "run"))
