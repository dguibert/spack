# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPylru(PythonPackage):
    """A least recently used (LRU) cache implementation"""

    homepage = "https://github.com/jlhutch/pylru"
    pypi = "pylru/pylru-1.2.1.tar.gz"

    version("1.2.1", sha256="47ad140a63ab9389648dadfbb4330700e0ffeeb28ec04664ee47d37ed133b0f4")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
