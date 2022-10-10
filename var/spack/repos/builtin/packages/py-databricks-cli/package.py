# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDatabricksCli(PythonPackage):
    """The Databricks Command Line Interface (CLI) is an open source tool which provides an easy to use interface to the Databricks platform. The CLI is built on top of the Databricks REST APIs."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/databricks/databricks-cli"
    url = "https://github.com/databricks/databricks-cli/archive/refs/tags/0.17.3.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("0.17.3", sha256="1bbf6e6ad2f1404cb70da1568822ab6a8fa07e563e9529782077011c5640bb9e")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.

    depends_on("py-click", type="run") #>=7.0
    depends_on("py-pyjwt", type="run") #>=1.7.0
    depends_on("py-oauthlib", type="run") #>=3.1.0
    depends_on("py-requests", type="run") #>=2.17.3
    depends_on("py-tabulate", type="run") #>=0.7.7
    depends_on("py-six", type="run") #>=1.10.0
#    depends_on("py-configparser">=0.3.5;python_version < "3.6"
