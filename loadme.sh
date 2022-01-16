#!/usr/bin/env bash

SPACK_ROOT=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# remove existing module vars/functions
unset MODULEPATH MODULEPATH_modshare MODULES_CMD MODULESHOME MODULES_RUN_QUARANTINE
unset -f module module_raw ml

source $SPACK_ROOT/share/spack/setup-env.sh
. $(spack location -i lmod arch=$(uname -p))/lmod/lmod/init/profile
source $SPACK_ROOT/share/spack/setup-env.sh
#module use $SPACK_ROOT/share/spack/lmod/linux-$(spack arch -o)-$(uname -p)/Core

module use $SPACK_ROOT/share/spack/lmod/modules
#os=$(spack arch -o)
#for arch in $(spack arch --list-ancestors | tac); do
#module use $SPACK_ROOT/share/spack/lmod/linux-${os}-${arch}/Core
#done
module av

