# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyViridianWorkflow(PythonPackage):
    """Viridian Workflow"""

    homepage = "https://github.com/iqbal-lab-org/viridian_workflow"

    url      = "https://github.com/iqbal-lab-org/viridian_workflow/archive/refs/tags/v0.3.1.tar.gz"

    version('master', git='https://github.com/iqbal-lab-org/viridian_workflow', branch='master', numeric_equivalent='>')
    version('0.3.2', sha256='1c5d6bd80c96c2972a5d2988c735f5fb050e7efe187f2f086fa586619dcaeb63')
    version('0.3.1', sha256='5dc55b4b0efc5ed5901e5e6bfc6d29a6e8ebfe76ad21ee39e6457b797e17a843')
    version('0.3.0', sha256='cbfc167678fe6d0c4d275cb683a84d021002ce9b496270548c202b87bf908b10')
    version('0.2.2', sha256='3f83d2080c739fe3f5a8d6d21e9c43324a1c7bc4b75d7817341dc8a31cf53679')
    version('0.2.1', sha256='0c3225d2485f39070faa7bee4eecd0573efdd1b114313db3b5d4b2126038676c')

    depends_on('py-setuptools', type='build')
    depends_on('py-intervaltree', type=('build', 'run'))
    depends_on('py-fastaq', type=('build', 'run'))
    depends_on('py-pysam', type=('build', 'run'))

    depends_on('bcftools', type='run')
    depends_on('vt', type='run')
    depends_on('minimap2', type='run')
    depends_on('racon', type='run')
    depends_on('py-viridian', type='run')
    depends_on('mummer', type='run')
    depends_on('py-varifier', type='run')
    depends_on('py-qcovid', type='run')
