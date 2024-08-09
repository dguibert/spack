# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySharedarray(PythonPackage):
    """Share numpy arrays between processes"""

    homepage = "https://gitlab.com/tenzing/shared-array"
    pypi = "SharedArray/SharedArray-3.2.2.tar.gz"

    version("3.2.2", sha256="eb1b1ae3953864f0b5ceb30e27cd832d19525ece71176c246cc5d30a82f0f8ed")
    version("3.2.1", sha256="ae7bba4f0ae33e209bbe58e5688d709a707b0390f3160e63fe5be8908b8e3902")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
