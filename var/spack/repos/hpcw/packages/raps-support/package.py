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
#     spack install raps-support
#
# You can edit this file again by typing:
#
#     spack edit raps-support
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class RapsSupport(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "file://%s/raps-support-18.4.1-Source.tar.gz" % os.environ.get('HPCW_DOWNLOAD_URL')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('18.4.1', sha256='4e0428dbe57e636d93750736a1ee55075b5a89a05c9405ef920f9f9eed0c13e6')

    #depends_on('eccodes+fortran')
    depends_on('mpi')
    depends_on('curl')
    depends_on('python@:2')

    def cmake_args(self):
        args = [
          '-DENABLE_ECCODES:BOOL=ON',
          '-DENABLE_TESTS:BOOL=OFF',
          '-DENABLE_ODB:BOOL=OFF',
          '-DENABLE_EXAMPLES:BOOL=OFF',
          '-DENABLE_PYTHON:BOOL=OFF',
          '-DENABLE_JPG:BOOL=OFF',
        ]
        # only gcc@10:
        if self.spec.satisfies('%gcc@10:'):
          args.append(
          '-DCMAKE_Fortran_FLAGS=-fallow-argument-mismatch -ffree-line-length-none'
          )
        return args
