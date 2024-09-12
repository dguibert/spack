# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDonfig(PythonPackage):
    """Python package for configuring a python package."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/pytroll/donfig"
    pypi = "donfig/donfig-0.8.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("0.8.1", sha256="d1773b550e5f1e0930dee03565ce610d1c53a9f9af95fcc46f587cc70e9d39ff")
    version("0.8.0", sha256="c3759f9500acda430775666e2dae0146f25b1e37acf12c57e55344118a089c71")
    version("0.7.0", sha256="7e3993981b7312edb16098989e4cb084ff58c1b1d8e9878c7c0107eabf18dbfa")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    depends_on("py-pyyaml", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
