# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyViridian(PythonPackage):
    """Virus assembler from amplicon sequencing reads."""

    homepage = "https://github.com/iqbal-lab-org/viridian"

    url      = "https://github.com/iqbal-lab-org/viridian/archive/refs/tags/v0.1.0.tar.gz"

    version('main', git='https://github.com/iqbal-lab-org/viridian', branch='main', numeric_equivalent='>')
    version('0.1.0', sha256='b319a4dc6d6510a9bd4cb6248c38d38f2d11c02eed7eb5645fe48d683c3c1e9f')

    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    # depends_on('py-foo',        type=('build', 'run'))
    depends_on('racon', type='run')
    depends_on('minimap2', type=('build', 'run'))
    depends_on('py-pysam')
    depends_on('py-fastaq')

