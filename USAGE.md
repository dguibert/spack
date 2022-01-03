Our fork of SPACK contains our modifications (patches, configuration files) for our use-cases.

    $ git clone -c feature.manyFiles=true https://castle.frec.bull.fr:24443/bguibertd/spack
    $ source spack/share/spack/setup-env.sh

On our clusters, no internet connection, predownloaded archives can be found in a mirror. To add it, run:

    $ spack config --scope site add mirrors:software-mirror:file://software/spack/mirror

PS: if your install requires some additionnal sources, either ask, set http_proxy/https_proxy or set a local proxy on your workstation and synchronise it on the cluster.

That’s it! You’re ready to use Spack.

If you want to use already available installed packages on our cluster, you have to add these upstream locations by:

    $ spack config --scope site add upstreams:spack-base:install_tree:/software/spack/v0.13.2-9600-g5f36801aa7-2925a5e/base/spack/opt/spack
    $ spack config --scope site add upstreams:spack-compilers:install_tree:/software/spack/v0.13.2-9600-g5f36801aa7-2925a5e/compilers/spack/opt/spack
    $ spack config --scope site add upstreams:spack-software:install_tree:/software/spack/v0.13.2-9600-g5f36801aa7-2925a5e/software/spack/opt/spack

PS: They can be removed by

    $ spack config --scope site rm upstreams:spack-base
    $ spack config --scope site rm upstreams:spack-compilers
    $ spack config --scope site rm upstreams:spack-software


# Usage

To install new packages, it is easier to isolate them within an environment. Some environments already exist, they can be listed with

    $ spack env list


You can load/activate one of them with

    $ spack env activate -p $env


To create a new env, use the following steps:

    $ spack env create $new_env
    $ spack env activate -p $new_env
    $ spack config edit
    $ spack external find
    $ $EDITOR ./var/spack/environments/$env


PS: remove python from external packages (problem with /lib, /lib64 PYTHONPATH)

# Recipes
## UCX

    ucx:
      variants:
        - +cm
        - +cma
        - +dc
        - +dm
        - +ib-hw-tm
        - +knem
        - +mlx5-dv
        - +rc
        - +ud
        - +mofed
        - +rocm

## OpenMPI

    openmpi:
      variants:
        - fabrics=knem,ucx # comma not handle
        - +legacylaunchers
        - +pmix
        - schedulers=slurm
        - +thread_multiple




