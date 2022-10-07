#!/usr/bin/env bash
# https://www.starkandwayne.com/blog/bashing-your-yaml/

set -eu -o pipefail
${VERBOSE:-false} && set -x

cluster=$(hostname)
case "${cluster}" in
	l0|c[0-9][0-9][0-9]|g[0-9][0-9][0-9]|o[0-9][0-9][0-9])
		cluster=spartan;;
esac
arch=$(uname -m)
package_yaml_file=packages-$cluster-$arch.yaml

# define variable to be used inside yaml file
declare -a pkgs
declare -A specs
pkgs+=(autoconf)
pkgs+=(automake)
pkgs+=(bash)
# pkgs+=(berkeley-db)
pkgs+=(bzip2)
pkgs+=(cpio)
pkgs+=(curl)
pkgs+=(diffutils)
# pkgs+=(doxygen)
pkgs+=(file)
pkgs+=(findutils)
pkgs+=(flex)
pkgs+=(gawk)
pkgs+=(gcc) # languages=c,c++,fortran + extra_attributes
pkgs+=(git) # ~tcltk
pkgs+=(make)
specs[make]='gmake/$version'
#pkgs+=(groff)
#pkgs+=(krb5)
#kgs+=(libfuse)
pkgs+=(libtool)
#pkgs+=(lustre) # not installed on l0
pkgs+=(m4)
pkgs+=(ncurses) # +termlib abi=5
pkgs+=(openssh)
pkgs+=(openssl)
pkgs+=(perl)
pkgs+=(pkgconf)
pkgs+=(rsync)
pkgs+=(sed)
pkgs+=(tar)
pkgs+=(xz)
pkgs+=(zip)
pkgs+=(ucx) # specs?

export pkgs
export specs

rm -f $package_yaml_file
. <( echo "cat <<EOF >$package_yaml_file";
  echo "packages:"
  for pkg in ${pkgs[@]}; do
      version=$(rpm -q --queryformat=%{VERSION} $pkg)
      prefix=$(rpm -q --queryformat=%{instprefixes} $pkg)
      prefix=${prefix%%(none)} # remove: '(none)'
      prefix=${prefix:-/usr}   # if empty set to /usr
      spec=$(eval "echo ${specs["$pkg"]:-$pkg@$version}")
      echo "  $pkg:"
      echo "    externals:"
      echo "    - spec: $spec"
      echo "      prefix: $prefix"
      echo "    buildable: False"
  done
  echo "EOF";
)
cat $package_yaml_file
