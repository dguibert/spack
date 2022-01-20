# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyClusterVcfRecords(PythonPackage):
    """Python package to cluster VCF records. Used by gramtools and minos """

    homepage = "https://github.com/iqbal-lab-org/cluster_vcf_records"

    url      = "https://github.com/iqbal-lab-org/cluster_vcf_records/archive/refs/tags/v0.13.2.tar.gz"

    version('0.13.2', sha256='57cb4e41515e85073d612626b210d4eea3b740491e505dd7af2d2d17727e7963')
    version('0.13.1', sha256='5cc8768a8fd28fe20052641d6d83cc7599d709608c7b99297f8ef64547266049')
    version('0.13.0', sha256='f86d87d4941b5c8409bcb653557c9a52086d8e20fd9cc295bd7785a37fc67c6c')
    version('0.12.4', sha256='785942d5dd2ec5c969a9a3af9704717ed5f9354e7e47682d7c89a84999e652f1')
    version('0.12.3', sha256='ab42c5bce13c192a12613383c5fc705e81f21c01050d9c5872fcd9774488af9d')
    version('0.12.2', sha256='f16b643e6a52df88e9d149571fb2560acb0dcf05641cc6d9090ab22285e8713f')
    version('0.12.1', sha256='8b8dfd6a38c29abe22fe7d0fc9a36ac8c57b8ab4782b8d4afb3e1f8a3470400d')
    version('0.12.0', sha256='d3aaf7779f77edef89bd701a73ff9c31525ba60a0807539d64300172bdad2919')
    version('0.11.1', sha256='02d8686150af76a7cb635c7b0149e85381f25b79d225a7052c10f3e9c4c1d601')
    version('0.11.0', sha256='81bb3892f6383d9d82c6bd6a135f263a5c534034f931ef73693d6b434fa0ca6a')

    depends_on('py-bitarray', type=('build', 'run'))
    depends_on('py-fastaq@3.14.0:', type=('build', 'run'))
    depends_on('py-pysam', type=('build', 'run'))
    depends_on('bcftools', type='run')
    depends_on('vt', type='run')

