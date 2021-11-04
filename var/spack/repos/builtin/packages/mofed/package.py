# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import re

from spack import *


class Mofed(Package):
    """Mellanox OFED package in order to add dependencies."""

    homepage = "https://www.mellanox.com/products/infiniband-drivers/linux/mlnx_ofed"
    url="https://www.mellanox.com/products/infiniband-drivers/linux/mlnx_ofed"
    manual_download = True
    version('MLNX_OFED_LINUX-5.1-2.5.8.0')

    executables = ['ofed_info']

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)('-s', output=str, error=str)
        match = re.match(r'^(\S*):\s', output)
        return match.group(1) if match else None
