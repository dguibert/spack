# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPymummer(PythonPackage):
    """Python3 module for running MUMmer and reading the output """

    homepage = "https://github.com/sanger-pathogens/pymummer"

    url      = "https://github.com/sanger-pathogens/pymummer/archive/refs/tags/v0.11.0.tar.gz"

    version('0.11.0', sha256='960b7e29603f6126e8df89ded62e15399c10d9e62b501336971ee272923967ac')
    version('0.10.3', sha256='cabae6ff65cdafc0d52c3a824c0e8456423f740260c6f91e1853554a6b13d42f')
    version('0.10.2', sha256='3c0c7308b88fcef7e43589992e31d1384165095acee253680b5844f9e2feb7b1')
    version('0.10.1', sha256='8c358227b842a61477889db50af0918ea3e793fddc56f6a9900e6820f2712b20')
    version('0.10.0', sha256='381927a3dfee34727da173bfc747b34a9ddecb1647c2d36c3df4ceb297f85309')
    version('0.9.0',  sha256='e0c8bead3dacd1ecb29cdb1bdd60d7b52f13073dfbb152eefcfe08a147b9b3a1')
    version('0.8.1',  sha256='b7b137ac1e96fdaa24a18a56dc35db26c276b70615b511303518d3771631e189')
    version('0.8.0',  sha256='45d33f9aaa92a1ad06732456d3b8539cf09a81aac5bbfb3f61dd571b85c74116')
    version('0.7.1',  sha256='33ab7aeb4f09a4e00ca32c237d3f6eca0050127663ad445b139debf7137a4e57')
    version('0.7.0',  sha256='bd329946f67d3c7ebb783038077cbd831a63d65353e24f9454404150e5217876')

    depends_on('mummer', type=('build', 'run'))
    depends_on('py-fastaq@3.10.0:', type=('build', 'run'))

