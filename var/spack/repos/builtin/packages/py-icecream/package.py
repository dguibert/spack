# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIcecream(PythonPackage):
    """Never use print() to debug again; inspect variables, expressions, and program execution with
    a single, simple function call.."""

    homepage = "https://github.com/gruns/icecream"
    pypi     = "icecream/icecream-2.1.1.tar.gz"

    version('2.1.1', sha256='47e00e3f4e8477996e7dc420b6fa8ba53f8ced17de65320fedb5b15997b76589')

    depends_on('py-colorama', type=('build','run'))
    depends_on('py-pygments', type=('build','run'))
    depends_on('py-executing', type=('build','run'))
    depends_on('py-asttokens', type=('build','run'))

