# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyVarifier(PythonPackage):
    """Variant call verification"""

    homepage = "https://github.com/iqbal-lab-org/varifier"
    url      = "https://github.com/iqbal-lab-org/varifier/archive/refs/tags/v0.3.1.tar.gz"

    version('master', git='https://github.com/iqbal-lab-org/varifier', branch='master', numeric_equivalent='>')
    version('0.3.1', sha256='119f49d985f694ef0452dd70d2c53134b09a82a95d356913f7d729617c8cc7c1')
    version('0.3.0', sha256='d318db2ef96eebc9682db9e0b11178f9ebee891afb584ff6aa32de3728d56f36')
    version('0.2.0', sha256='9ac7ad3eacd21261ca7a5b4a214152cb55e51cfb8c0cb3ffa3538ebfebc8e359')
    version('0.1.0', sha256='1f58fbb5d38f8427df0521eda5e92d916283e14ffffc0008ff49cc9fcf009707')

    depends_on('bcftools', type='run')
    depends_on('vt', type='run')
    depends_on('py-biopython', type=('build', 'run'))
    depends_on('py-cluster-vcf-records@0.13.2:', type=('build', 'run'))
    #mappy >= 2.17 provided by minimap2
    depends_on('minimap2@2.17:', type=('build', 'run'))
    depends_on('k8', type='run')
    depends_on('py-pandas')
    depends_on('py-fastaq@3.14.0:')
    depends_on('py-pymummer')
    depends_on('py-pysam', type='run')
    depends_on('py-seaborn', type=('build', 'run'))

