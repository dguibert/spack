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
#     spack install ifs
#
# You can edit this file again by typing:
#
#     spack edit ifs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import subprocess
import os, stat

class Ifs(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "file://%s/RAPS18u2.1.tgz" % os.environ.get('HPCW_DOWNLOAD_URL')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('18u2.1', sha256='f7fdbc59bd8a51d362c9e18cd17769c304ef6f506a85db299c7f0a92b97b2698')

    variant('single', default='no', values=('yes', 'no'))
    variant('nemo', default='yes', values=('yes', 'no'))
    variant('raps_support', default='yes', values=('yes', 'no'))
    variant('oops', default='no', values=('yes', 'no'))

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('hdf5+fortran+hl')
    depends_on('fftw')
    depends_on('blas')
    depends_on('lapack')
    depends_on('parmetis')

    depends_on('raps-support')
#    depends_on('oops')
    depends_on('libemos')
#    depends_on('pgen')

    patch('ifs-flexbuild-rsync_files.patch')
    ## :configure_file(${CMAKE_SOURCE_DIR}/projects/ifs-nemo_fcmconfig_bld_hpcw_nemo.cfg.in
    ## :               ${CMAKE_BINARY_DIR}/ifs-nemo_fcmconfig_bld_hpcw_nemo.cfg
    ## :               @ONLY)
    ## :if(CMAKE_Fortran_COMPILER_ID MATCHES "GNU")
    ## :  configure_file(${CMAKE_SOURCE_DIR}/projects/ifs-flexbuild_make.gnu.hpcw.in
    ## :                 ${CMAKE_BINARY_DIR}/ifs-flexbuild_make.hpcw
    ## :                 @ONLY)
    ## :endif()
    ## :if(CMAKE_Fortran_COMPILER_ID MATCHES "Intel")
    ## :  configure_file(${CMAKE_SOURCE_DIR}/projects/ifs-flexbuild_make.intel.hpcw.in
    ## :                 ${CMAKE_BINARY_DIR}/ifs-flexbuild_make.hpcw
    ## :                 @ONLY)
    ## :endif()
    def ifs_build_all(self):
        mkdirp('flexbuild/external/hpcw')
        file = join_path('flexbuild', 'external', 'hpcw', 'build_all')
        text = r"""
#!/bin/sh

echo "HPCW: all dependencies already compiled"
"""
        with open(file, 'w') as f:
            f.write(text)
            mode = os.fstat(f.fileno()).st_mode
            mode |= stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
            os.fchmod(f.fileno(), stat.S_IMODE(mode))


    def ifs_nemo_fcmconfig_bld_hpcw_nemo(self):
        mkdirp('nemo/fcmconfig/bld/hpcw')
        file = join_path('nemo', 'fcmconfig', 'bld', 'hpcw', 'nemo.cfg')
        spec = self.spec
        param = dict()
        param = {
          'MPICC':  spec['mpi'].mpicc,
          'MPIFC':  spec['mpi'].mpifc,
        }

        if spec.satisfies('%gcc'):
          param['NEMO_COMPILE_OPTIONS']='-fdefault-real-8 -O3 -funroll-all-loops -fcray-pointer -ffree-line-length-none -fallow(argument-mismatch'
          param['NEMO_FC_ARGS']='-g -fbacktrace -fconvert=big-endian'
        if spec.satisfies('%intel'):
          param['NEMO_COMPILE_OPTIONS']='-xHost  -align array64byte -traceback -i4 -r8 -O3 -fp-model precise -fno-alias'
          param['NEMO_FC_ARGS']='-g -traceback'

        if any(map(spec.satisfies, ('%gcc', '%intel'))):
            text = r"""
#---------------------------------------------------------------------
# Configuration File:  nemo.cfg
#---------------------------------------------------------------------
# Purpose: Build configuration file for an linux build of Nemo.
# File header
cfg::type                                   ext
cfg::version                                1.0
bld::tool::fc      {MPIFC} {NEMO_FC_ARGS} $(OMP)
bld::tool::fflags  {NEMO_COMPILE_OPTIONS}
bld::tool::cc      {MPICC}
%fppkeys_bufr      HAS_BUFR
%fppkeys_arch      LINUX REAL8 key_mpp key_mpp_mpi key_mpi_isend key_has_lapack key_dr_hook
bld::tool::ld      %bld::tool::fc
bld::tool::ldflags  -lz -lcurl -lm -lrt -ldl
bld::tool::ar      ar

########################################################################
# NetCDF
bld::tool::ldflags      %bld::tool::ldflags -lnetcdf -lnetcdff

########################################################################
# GRIB_API
bld::tool::ldflags      %bld::tool::ldflags $(ECCODES_LIB)

########################################################################
# DrHook
bld::tool::ldflags      %bld::tool::ldflags $(IFSAUXLIB)
bld::tool::fflags       %bld::tool::fflags $(IFSAUXINC)
""".format(**param)
        else:
            raise InstallError('Unsupported compiler.')

        with open(file, 'w') as f:
            f.write(text)


    def ifs_flexbuild_config_hpcw(self):
        file = join_path('flexbuild', 'config.hpcw')
        touch(file)

    def ifs_flexbuild_make_hpcw(self):
        file = join_path('flexbuild', 'make.hpcw')
        spec = self.spec
        libs = spec['parmetis'].libs + \
               spec['netcdf-c'].libs + \
               spec['netcdf-fortran'].libs + \
               spec['lapack:fortran'].libs + \
               spec['blas:fortran'].libs
        param = dict()
        param = {
          'MPICC':  spec['mpi'].mpicc,
          'MPICXX':  spec['mpi'].mpicxx,
          'MPIFC':  spec['mpi'].mpifc,
          'NETCDF_INC_DIR': spec['netcdf-c'].prefix.include,
          'NETCDFF_INC_DIR': spec['netcdf-fortran'].prefix.include,
          'EXTLIBS': libs.link_flags
        }

        if spec.satisfies('%gcc'):
          param['FC_ARGS']='-g -fbacktrace -fconvert=big-endian'
          param['FC_FLAGS']='-fallow-argument-mismatch -fallow-invalid-boz'
        if spec.satisfies('%intel'):
          param['FC_ARGS']='-g -traceback'
          param['FC_FLAGS']=''

        param['OMP']= self.compiler.openmp_flag

        if spec.satisfies('%gcc'):
            text = r"""
COMPSYS = hpcw
OMP = {OMP}
export OMP

AVXMODE = -mavx

INSTALL_DIR = $(PREFIX)

BMPATH = $(INSTALL_DIR)/bin:$(PATH)

FC = {MPIFC} $(OMP) {FC_ARGS}
FCFLAGS += -J $(DOT_MODULE) # place modules in $(DOT_MODULE) -dir
FCFLAGS += -cpp -fno-second-underscore
FCFLAGS += -fno-range-check
FCFLAGS += -std=gnu
FCFLAGS += -I{NETCDF_INC_DIR}
FCFLAGS += -I{NETCDFF_INC_DIR}

ifneq ($(CHECKB),)
FCOPTS += -O0
FCOPTS += $(CHECKB)
else
#FCOPTS += -O0
#FCOPTS += -O1
FCOPTS += -O2
FCOPTS += $(AVXMODE)
endif

FCFREE  = -ffree-form -ffree-line-length-0
FCFIXED = -ffixed-form

LD = $(FC)
LDFLAGS = -Wl,--as-needed -Wl,-export-dynamic
LDFLAGS += -ffast-math

CC = {MPICC} -g
COPTS += -O2
COPTS += $(AVXMODE)

CXX = {MPICXX} -pthread -g
CXXFLAGS += -std=c++11
CXXOPTS += -O2
CXXOPTS += $(AVXMODE)
CXXLD = $(CXX) $(OMP)
CXXLDFLAGS = {FC_FLAGS} # need in fact export GFORTRAN_CONVERT_UNIT=big_endian -- now in bin/model .. hardwired

OOPSLD = $(CXXLD)
OOPSLDFLAGS = $(CXXLDFLAGS)
OOPSLDLIBS = $(OOPSLDLIBS_EXTRA)

AUTODBL_OPTS = -fdefault-real-8 -fdefault-double-8

EXTLIBS=
ifeq ($(SINGLE),no)
  EXTLIBS+=-lfftw3
else
  EXTLIBS+=-lfftw3f
endif

EXTLIBS += {EXTLIBS} -lrt -ldl

#%/ec_meminfo.o: FCFLAGS += -O0 -g -fcheck=bounds

ifneq ($(CHECKB),)
# Exclude these from array bound checks ("superfluos")
# Run with nundefld=1
ifs/adiab/cpg_drv.o: private CHECKB =
ifs/phys_radi/radintg.o: private CHECKB =
ifs/adiab/call_sl.o: private CHECKB =
ifs/phys_ec/ec_phys_drv.o: private CHECKB =
ifs/phys_ec/ec_phys.o: private CHECKB =
surf/module/surfexcdriver_ctl_mod.o: private CHECKB =
endif

%/drhook.o: private CFLAGS += -fstack-check
%/env.o: private CFLAGS += -fstack-check
""".format(**param)

        elif spec.satisfies('%intel'):
            text = r"""
COMPSYS = hpcw
OMP = {OMP}
export OMP

AVXMODE=-g -march=core-avx2 -fimf-use-svml=false
AVXMODE2=-g -march=core-avx2 -fimf-use-svml=false

INSTALL_DIR = $(PREFIX)

BMPATH = $(INSTALL_DIR)/bin:$(PATH)

FC = {MPIFC} $(OMP) {FC_ARGS}
FCFLAGS += -module $(DOT_MODULE)
FCFLAGS += -Wp,-w0 # no fpp warnings about -Undefs
FCFLAGS += -diag-disable=7713 # no messages about "This statement function has not been used"
#FCFLAGS += -I{NETCDF_INC_DIR}
#FCFLAGS += -I{NETCDFF_INC_DIR}

FCOPTS += -O2
FCOPTS += $(AVXMODE)
FCOPTS += -assume byterecl -align array64byte,all
FCOPTS += -fpe0 -fp-model source -fp-model precise   -ftz
FCOPTS += -fp-speculation safe
FCOPTS += -finline-functions -finline-limit=1500 -Winline

FCFREE  = -free
FCFIXED = -nofree

LD = $(FC)
LDFLAGS = -Wl,--as-needed -Wl,-export-dynamic
LDFLAGS += -Wl,--cref

CC = {MPICC} -g
COPTS += -O2
COPTS += $(AVXMODE)

CXX = {MPICXX} -pthread -g -std=gnu++14
CXXFLAGS += -std=c++11
CXXOPTS += -O2
CXXOPTS += $(AVXMODE)
CXXLD = $(CXX) $(OMP)
CXXLDFLAGS =-Wl,--copy-dt-needed-entries

OOPSLD = $(CXXLD)
OOPSLDFLAGS = $(CXXLDFLAGS)
OOPSLDLIBS = $(OOPSLDLIBS_EXTRA)

AUTODBL_OPTS = -real-size 64 -double-size 64

DEFS += -DINTEL

EXTLIBS=
ifeq ($(SINGLE),no)
  EXTLIBS+=-lfftw3
else
  EXTLIBS+=-lfftw3f
endif

EXTLIBS += {EXTLIBS} -lrt -ldl

#=== from Mikko (meant for RAPS16+mods originally)

%/fcgeneralized_gamma.o: private FCFLAGS += -O0 $(AVXMODE2) # Removes NaNs ?
%/surfseb_ctl_mod.o: private FCFLAGS += $(AVXMODE2) # Removes NaNs ?

%/mwave_cpfrac.o: private FCFLAGS += -no-fma # Removes internal compiler error ?
%/radinatl.o: private FCFLAGS += -no-fma  # Removes internal compiler error ?
%/rttov_integrate_tl.o: private FCFLAGS += -no-fma  # Removes internal compiler error ?
%/waven.o: private FCFLAGS += -no-fma  # Removes internal compiler error ?

# 2018 Beta U1 workarounds
%/srfsn_lwexp_mod.o: private FCFLAGS += $(AVXMODE2)
%/srfsn_lwimpsad_mod.o: private FCFLAGS += -O0 $(AVXMODE2)
%/asre1ad_mod.o: private FCFLAGS += $(AVXMODE2)
%/yownodepool.F90: private FCFLAGS += $(AVXMODE2)
%/sdissip_jan.o: private FCFLAGS += $(AVXMODE2)
%/mpl_read_mod.o: private FCFLAGS += $(AVXMODE2)
%/incli1.o: private FCFLAGS += $(AVXMODE2)
%/mpbcastsarin.o: private FCFLAGS += $(AVXMODE2)
%/mpexchng.o: private FCFLAGS += $(AVXMODE2)
%/inirp.o: private FCFLAGS += -O0

# Compile optimizations
#%/cloudsc.o: private FCFLAGS += -O3 -qno-openmp-simd
%/cloudsc.o: private FCFLAGS += -O3
%/laitli.o: private FCFLAGS += -O3 -qopt-prefetch=0
%/laitri.o: private FCFLAGS += -O3
%/cloudvar.o: private FCFLAGS += -O3
%/radiation_mcica_sw.o: private FCFLAGS += -O2 -vecabi=cmdtarget
%/radiation_cloud_generator.o: private FCFLAGS += -O2 -vecabi=cmdtarget
%/radintg.o: private FCFLAGS += -O3
%/radiation_aerosol_optics.o: private FCFLAGS += -O3
%/larmes.o: private FCFLAGS += -O3

#%.o: private FCFLAGS += -O1

#ifeq ($(RAPS_SUPPORT),yes)
#-- Intel v18 with RAPS-support HAD issues

#%/fv_gradient.o: private UNDEFS += -UWITH_ATLAS
##	touch $@

%/gp_derivatives.o: private UNDEFS += -UWITH_ATLAS
#	touch $@

#%/suorog.o: private UNDEFS += -UWITH_ATLAS

#%/master.o: private DEFS += -DONT_REGISTER_FCKIT_HANDLER
#endif


%/supert.o: private FCFLAGS += -heap-arrays
%/spectral_fields_mod.o: private FCFLAGS += -heap-arrays
%/control_vectors_oper_mod.o: private FCFLAGS += -heap-arrays



# Migrated from R17 - still seams a problem uin 18u1
%/radiation_cloud_generator.o: private FCFLAGS += -O2 $(AVXMODE2)
%/rebind.o: private COPTS += -std=gnu99
%/lwcad.o: private FCFLAGS += -O3 -qopt-prefetch=0
%/laitriad.o: private FCFLAGS += -O3 -qopt-prefetch=0
%/lwvdr.o: private FCFLAGS += -O3 -qopt-prefetch=0
%/lwvdrad.o: private FCFLAGS += -O3 -qopt-prefetch=0
%/lwctl.o: private FCFLAGS += -O3 -qopt-prefetch=0
%/lwvdrtl.o: private FCFLAGS += -O3 -qopt-prefetch=0
""".format(**param)
        else:
            raise InstallError('Unsupported compiler.')

        with open(file, 'w') as f:
            f.write(text)




    def install(self, spec, prefix):
        self.ifs_nemo_fcmconfig_bld_hpcw_nemo()
        self.ifs_flexbuild_config_hpcw()
        self.ifs_flexbuild_make_hpcw()
        self.ifs_build_all()

        param = {
          'PREFIX':  prefix,
          'SINGLE': spec.variants['single'].value,
          'NEMO': spec.variants['nemo'].value,
          'RAPS_SUPPORT': spec.variants['raps_support'].value,
          'OOPS': spec.variants['oops'].value,
        }

        subprocess.run(
            '(cd flexbuild;'
            ' source ./initbm hpcw'
            ' SINGLE={SINGLE} NEMO={NEMO} NCPUS=$(nproc) RAPS_SUPPORT={RAPS_SUPPORT} OOPS={OOPS} PREFIX={PREFIX}'
            ') && make -C flexbuild VERBOSE=1 PREFIX={PREFIX}'.format(**param)
            , shell=True, check=True)

