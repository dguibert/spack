# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIcecream(PythonPackage):
    """Never use print() to debug again; inspect variables, expressions, and program execution with
    a single, simple function call.."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/gruns/icecream"
    pypi     = "icecream/icecream-2.1.1.tar.gz"

    version('2.1.1', sha256='47e00e3f4e8477996e7dc420b6fa8ba53f8ced17de65320fedb5b15997b76589')

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-pip@X.Y:', type='build')
    # depends_on('py-wheel@X.Y:', type='build')

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on('py-setuptools', type='build')
    # depends_on('py-flit-core', type='build')
    # depends_on('py-poetry-core', type='build')

    # FIXME: Add additional dependencies if required.
    # depends_on('py-foo', type=('build', 'run'))

