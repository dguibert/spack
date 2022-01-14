#!/usr/bin/env bash

SPACK_ROOT=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
LOAD_SPACK=${LOAD_SPACK:-true}

# remove existing module vars/functions
unset MODULEPATH MODULEPATH_modshare MODULES_CMD MODULESHOME MODULES_RUN_QUARANTINE
unset -f module module_raw ml

if ${LOAD_SPACK}; then
  source $SPACK_ROOT/share/spack/setup-env.sh
  export LMOD_PATH=${LMOD_PATH:-$(spack location -i lmod@8.6.5 arch=linux-$(spack arch -o)-$(uname -p))}
  export LMOD_PATH=${LMOD_PATH:-$(spack location -i lmod arch=$(uname -p))}
  source $LMOD_PATH/lmod/lmod/init/profile
  source $SPACK_ROOT/share/spack/setup-env.sh
else
  source $LMOD_PATH/lmod/lmod/init/profile
fi

module use $SPACK_ROOT/share/spack/lmod/modules
#os=$(spack arch -o)
#for arch in $(spack arch --list-ancestors | tac); do
#module use $SPACK_ROOT/share/spack/lmod/linux-${os}-${arch}/Core
#done
module av

