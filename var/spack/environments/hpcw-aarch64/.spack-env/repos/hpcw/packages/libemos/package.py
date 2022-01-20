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
#     spack install libemos
#
# You can edit this file again by typing:
#
#     spack edit libemos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Libemos(CMakePackage):
    """The Interpolation library (EMOSLIB) includes Interpolation software and BUFR & CREX
    encoding/decoding routines. It is used by the ECMWF meteorological archival and retrieval system
    (MARS) and also by the ECMWF workstation Metview."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://confluence.ecmwf.int/display/EMOS/Emoslib"
    url      = "file://%s/libemos-4.5.5c-Source.tar.gz" % os.environ.get('HPCW_DOWNLOAD_URL')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.5.5c', sha256='baf7144e29bfe17554db27971fc5eef501d133bf38cf56953b10f722e82d664a')

    depends_on('raps-support')
    depends_on('oops')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = [
          '-DENABLE_ECCODES:BOOL=ON',
          '-DENABLE_INSTALL_TABLES:BOOL=OFF',
          '-DENABLE_GRIBEX_ABORT:BOOL=OFF',
          '-DENABLE_SINGLE_PRECISION:BOOL=ON',
          '-DENABLE_FORTRAN90:BOOL=OFF',
          '-DENABLE_FFTW:BOOL=OFF',
          '-DENABLE_REQUIRE_FFTW:BOOL=OFF',
          '-DLIBEMOS_BUILD_SHARED_LIBS:BOOL=ON',
          '-DENABLE_TESTS:BOOL=OFF',
          '-DENABLE_INSTALL_TOOLS:BOOL=OFF',
          '-DECBUILD_TRUST_FLAGS:BOOL=ON',
          ]
        # only gcc@10:
        if self.spec.satisfies('%gcc@10:'):
          args.append(
          '-DCMAKE_Fortran_FLAGS=-fallow-argument-mismatch -ffree-line-length-none'
          )
        return args
