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
#     spack install nemo
#
# You can edit this file again by typing:
#
#     spack edit nemo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Nemo(Package):
    """NEMO (Nucleus for European Modelling of the Ocean) is a state-of-the-art modelling framework
    of ocean related engines for oceanographic research, operational oceanography, seasonal forecast
    and [paleo]climate studies"""

    homepage = "https://forge.ipsl.jussieu.fr/nemo/wiki/Users"
    svn = "https://forge.ipsl.jussieu.fr/nemo/svn/NEMO"

    # FIXME: Add proper versions and checksums here.
    version('4.0.14480', svn='http://forge.ipsl.jussieu.fr/nemo/svn/NEMO/releases/release-4.0',
        revision=14480)
    version('4.0.5', svn='https://forge.ipsl.jussieu.fr/nemo/svn/NEMO/releases/r4.0/r4.0.5/',
        revision=14450)

    depends_on('xios')
    depends_on('mpi')
    depends_on('perl', type='build')
    depends_on('perl-uri', type='build')
    depends_on('gmake', type='build')

    # as of version 4.0.5
    # The reference configuration ('-r'), demonstration case ('-a') or
    # remote configuration ('-u') selected is not available!!!
    # Check the option used and the available items in .txt files
    # ¤ Reference configurations with default sub-components (can be updated by a new set)
    ref_cfgs=(
      'AGRIF_DEMO'         , #  OCE ICE NST
      'AMM12'              , #  OCE
      'C1D_PAPA'           , #  OCE
      'GYRE_BFM'           , #  OCE TOP
      'GYRE_PISCES'        , #  OCE TOP
      'ORCA2_OFF_PISCES'   , #  OCE TOP OFF
      'ORCA2_OFF_TRC'      , #  OCE TOP OFF
      'ORCA2_SAS_ICE'      , #  OCE ICE NST SAS
      'ORCA2_ICE_PISCES'   , #  OCE TOP ICE NST
      'SPITZ12'            , #  OCE ICE
      )
    # ¤ Demonstrations cases (see https://github.com/sflavoni/NEMO-test-cases for more)
    demo_cases=(
      'CANAL'              , #  OCE
      'ISOMIP'             , #  OCE
      'LOCK_EXCHANGE'      , #  OCE
      'OVERFLOW'           , #  OCE
      'ICE_AGRIF'          , #  OCE NST SAS ICE
      'ICE_ADV1D'          , #  OCE SAS ICE
      'ICE_ADV2D'          , #  OCE SAS ICE
      'VORTEX'             , #  OCE NST
      'WAD'                , #  OCE
      'BENCH'              , #  OCE ICE TOP
    )
    variant(
      'cfg', default='ORCA2_ICE_PISCES', description='Configuration name',
             values=ref_cfgs + demo_cases, multi=False
    )

    cpp_keys=(
        'key_top',
        'key_si3',
        'key_iomput',
        'key_mpp_mpi',
        'key_mpi2',
        )
    #-n MY_ORCA25 -r ORCA2_ICE_PISCES  del_key "key_top" add_key "key_si3  key_iomput key_mpp_mpi key_mpi2"
    variant('add_keys', default=None, values=any_combination_of(*cpp_keys), description="FCM add keys")
    variant('del_keys', default=None, values=any_combination_of(*cpp_keys), description="FCM del keys")

    def nemo_env(self):
        file = join_path('arch', 'arch-SPACK.env')
        touch(file)

    def nemo_path(self):
        file = join_path('arch', 'arch-SPACK.path')
        touch(file)

    def nemo_fcm(self):
        file = join_path('arch', 'arch-SPACK.fcm')
        spec = self.spec
        param = dict()
        param = {
          'MPICC':  spec['mpi'].mpicc,
          'MPIFC':  spec['mpi'].mpifc,
          'NEMO_USER_INC': '',
          'NEMO_USER_LIB': '-lnetcdff -lnetcdf -lxios',
          'NETCDFF_INC_DIR': spec['netcdf-fortran'].prefix.include,
          'NETCDFF_LIB_DIR': spec['netcdf-fortran'].prefix.lib
        }

        if spec.satisfies('%gcc'):
          param['NEMO_COMPILE_OPTIONS']='-g -fdefault-real-8 -O3 -funroll-all-loops -fcray-pointer -ffree-line-length-none'
        if spec.satisfies('%intel'):
          param['NEMO_COMPILE_OPTIONS']='-g -xHost  -align array64byte -traceback -i4 -r8 -O3 -fp-model precise -fno-alias'

        if any(map(spec.satisfies,
                   ('%gcc', '%intel'))):
            text = r"""
%CPP	               cpp
%FC                  {MPIFC} -c -cpp
%FCFLAGS             {NEMO_COMPILE_OPTIONS} -fallow-argument-mismatch
%FFLAGS              %FCFLAGS
%LD                  {MPIFC}
%LDFLAGS             -lstdc++
%FPPFLAGS            -P -C -traditional -std=c99 -Dkey_nosignedzero
%AR                  ar
%ARFLAGS             rs
%MK                  make
%USER_INC            {NEMO_USER_INC} -I{NETCDFF_INC_DIR}
%USER_LIB            {NEMO_USER_LIB} -L{NETCDFF_LIB_DIR}

%CC                  {MPICC}
%CFLAGS              -O3
""".format(**param)
        else:
            raise InstallError('Unsupported compiler.')

        with open(file, 'w') as f:
            f.write(text)

    def install(self, spec, prefix):
        env['CC'] = spec['mpi'].mpicc
        env['CXX'] = spec['mpi'].mpicxx
        env['F77'] = spec['mpi'].mpif77
        env['FC'] = spec['mpi'].mpifc

        cfg = spec.variants['cfg'].value

        cfg_flags=[]
        if cfg in self.ref_cfgs:
            cfg_flags.append('-r')
            cfg_flags.append(spec.variants['cfg'].value)
        if cfg in self.demo_cases:
            cfg_flags.append('-a')
            cfg_flags.append(spec.variants['cfg'].value)

        used_add_keys=[]
        for add_key in spec.variants['add_keys'].value:
            used_add_keys.append(add_key)
        if used_add_keys:
            cfg_flags.append('add_key="' + " ".join(used_add_keys) + '"')

        used_del_keys=[]
        for del_key in spec.variants['del_keys'].value:
            used_del_keys.append(del_key)
        if used_del_keys:
            cfg_flags.append('del_key="' + " ".join(used_del_keys) + '"')

        options = [
                   '-m', 'SPACK',
                   '-j', str(make_jobs)
                  ] + cfg_flags

        self.nemo_env()
        self.nemo_path()
        self.nemo_fcm()

        make_nemo = Executable('./makenemo')
        make_nemo(*options)

        mkdirp(spec.prefix)

        mkdirp(prefix.bin)
        if cfg in self.ref_cfgs:
            install('cfgs/%s/BLD/bin/nemo.exe' % spec.variants['cfg'].value, spec.prefix.bin)
        if cfg in self.demo_cases:
            install('tests/%s/BLD/bin/nemo.exe' % spec.variants['cfg'].value, spec.prefix.bin)
