# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install lofar
#
# You can edit this file again by typing:
#
#     spack edit lofar
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Lofar(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://git.astron.nl/ro/lofar"
    git = "https://git.astron.nl/ro/lofar"
    url = "https://git.astron.nl/ro/lofar/-/archive/LOFAR-Release-4_4_71/lofar-LOFAR-Release-4_4_71.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("GNU")

    # FIXME: Add proper versions and checksums here.
    # version("1.2.3", md5="0123456789abcdef0123456789abcdef")
    version("master", branch="master")
    #version("4.4.71")

    build_directory = "gnu_opt" # for gnu variants

    # FIXME: Add dependencies if required.
    depends_on("casacore")
    depends_on("boost+date_time+regex")
    depends_on("py-numpy")
    depends_on("hdf5")
    
    patch("lofar-remove-gcc-full-paths.patch")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
            "-DBUILD_PACKAGES=MSLofar",
            "-DUSE_LOG4CPLUS=OFF",
            "-DBUILD_TESTING=OFF",
        ]
        return args
