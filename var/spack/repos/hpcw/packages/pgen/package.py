# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install pgen
#
# You can edit this file again by typing:
#
#     spack edit pgen
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Pgen(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "file://%s/pgen-bundle-0.9.2.0-Source.tar.gz" % os.environ.get('HPCW_DOWNLOAD_URL')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.9.2.0', sha256='39534682b696bf15a88f698bcf76585d183b9685c15be7b5c0f202cccd3458a6')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('oops')
    depends_on('raps-support')
    depends_on('fftw')
    depends_on('blas')
    depends_on('lapack')

    # >> 56    CMake Error at /tmp/spack/opt/spack/linux-rhel8-x86_64/gcc-10.2.0/ecbuild-3.4.0-ywaj2s2gps6v2xucljdyjwtbhwmyljxz/share/ecbuild/cmake/ecbuild_log.cmake:190 (message):
    #    57      CRITICAL - Please define a version for pgen-bundle
    #    58
    #    59         project( pgen-bundle VERSION x.x.x LANGUAGES C CXX Fortran )
    #    60    Call Stack (most recent call first):
    #    61      /tmp/spack/opt/spack/linux-rhel8-x86_64/gcc-10.2.0/ecbuild-3.4.0-ywaj2s2gps6v2xucljdyjwtbhwmyljxz/share/ecbuild/cmake/ecbuild_declare_project.cmake:103 (ecbuild_critical)
    #    62      /tmp/spack/opt/spack/linux-rhel8-x86_64/gcc-10.2.0/ecbuild-3.4.0-ywaj2s2gps6v2xucljdyjwtbhwmyljxz/share/ecbuild/cmake/ecbuild_bundle.cmake:41 (ecbuild_declare_project)
    depends_on('ecbuild@:2.10.2')

    # TODO avoid downloading at build time with
    # tar xfv ${CMAKE_SOURCE_DIR}/downloads/mir-lsm.tgz -C <BINARY_DIR>

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
          '-DCMAKE_MODULE_PATH=%s/share/ecbuild/cmake' % self.spec['ecbuild'].prefix,
        ]
        return args
