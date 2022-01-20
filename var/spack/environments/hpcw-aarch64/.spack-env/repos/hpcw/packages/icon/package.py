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
#     spack install icon
#
# You can edit this file again by typing:
#
#     spack edit icon
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

# CREDIT https://gitlab.dkrz.de/m300488/icon-bootstrap/-/blob/master/repo/packages/icon/package.py
class Icon(AutotoolsPackage):
    """Icosahedral Nonhydrostatic Weather and Climate Model"""

    homepage = 'https://code.mpimet.mpg.de/projects/iconpublic'
    git = 'git@gitlab.dkrz.de:icon/icon-dkrz.git'

    # version('master', commit='ad0a0b1b82db3892b65bef5c618cf13654e91d52')
    version('hpcw', git = 'file:///home_nfs_robin_ib/bguibertd/work/hpcw',
        branch = 'master')

    variant('mpi', default=True,
            description='Enable MPI (parallelization) support')

    # https://gitlab.dkrz.de/m300488/icon-bootstrap/-/blob/master/repo/packages/icon/overlong_filename.patch
    #patch('overlong_filename.patch')

    depends_on('python', type='build')
    depends_on('perl', type='build')

    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('blas')
    depends_on('lapack')
    depends_on('libxml2')
    depends_on('mpi', when='+mpi')

    #depends_on('libmtime')
    #depends_on('libself@0.1')
    #depends_on('libcdi+fortran')

    #: Phases of a GNU Autotools package
    phases = ['configure', 'build', 'install']

    @property
    def build_directory(self):
        return 'icon'

    def configure_args(self):
        libs = self.spec['lapack:fortran'].libs + \
               self.spec['blas:fortran'].libs + \
               self.spec['netcdf-c'].libs + \
               self.spec['netcdf-fortran'].libs + \
               self.spec['libxml2'].libs
        args = ['LIBS=' + libs.link_flags,
                'PYTHON=' + self.spec['python'].command.path,
                'CC=' + self.spec['mpi'].mpicc,
                'CXX=' + self.spec['mpi'].mpicxx,
                'F77=' + self.spec['mpi'].mpif77,
                'FC=' + self.spec['mpi'].mpifc,
                # FIXMe only gfortran 10
                'FCFLAGS=-fallow-argument-mismatch',
                'ICON_FCFLAGS=-fallow-argument-mismatch',
                # configure: error: unable to find sources of the land component JSBACH
                # (src/base/mo_jsb_base.f90) in './externals/jsbach': disable the component
                # (--disable-jsbach)
                '--enable-openmp',
                # configure: error: unable to find sources of the bundled version of YAXT library
                # (src/xt_idxlist.c) in './externals/yaxt': either disable the YAXT data exchange
                # (--disable-yaxt) or provide an external version of YAXT library (--
                #           with-external-yaxt) by setting FCFLAGS, LDFLAGS and LIBS accordingly
                #'--enable-yaxt',
                '--enable-intel-consistency',
                # Omit optimizations for now
                'FCFLAGS=-g']

        if self.spec.satisfies('+mpi'):
            args.extend(['--enable-mpi', 'FC=' + self.spec['mpi'].mpifc])
        else:
            args.append('--disable-mpi')
        return args
