# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPolygon3(PythonPackage):
    """Python-3 package that handles polygonal shapes in 2D"""

    homepage = "https://www.j-raedler.de/projects/polygon"
    pypi = "Polygon3/Polygon3-3.0.9.1.tar.gz"

    version("3.0.9.1", sha256="2ddf8d06975f728d5b40786136c82e5b9d38a846bce236b7e6587bbd6a5e9b49")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
