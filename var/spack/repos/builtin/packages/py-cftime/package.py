# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCftime(PythonPackage):
    """Python library for decoding time units and variable values in a
    netCDF file conforming to the Climate and Forecasting (CF)
    netCDF conventions"""

    homepage = "https://unidata.github.io/cftime/"
    url = "https://github.com/Unidata/cftime/archive/v1.0.3.4rel.tar.gz"

    version("1.6.3", sha256="38a20e2c088abe814a5e5ccf365d994dac925f29b7b4b9b57ee4f55e13a017a2")
    version("1.6.2", sha256="b9da5ec5b3abb5aff806d40f84580896ef566821806c8f28e6cb21284f8c377b")
    version("1.6.1", sha256="5440954b446eedc27253a8d437603ca273ca8e59551d016ccf7e9da783a62758")
    version("1.5.1", sha256="b42acd1017242e2885377ed39be7c16100ddcde35dfab88d5db8bd79cb78aa0f")
    version("1.5.0", sha256="9cefc1bdcb3d2dd19a5fb5d142057024d6aabdd3577d912b68696f1155b41691")
    version("1.4.0", sha256="b96814d48ed1a946f04aea67cf372fdb51e2a1f039e87956e4cc707983245f8b")
    version("1.3.1", sha256="c26751e23bdad045ad805a8e2276f9d0c670dc4e743a77f5b6b93de9c26bde9b")
    version("1.3.0", sha256="eceb5154374d165b3c7f5106194ea31f22f34910bd7f3878286f2b704f19252f")
    version("1.2.1", sha256="e174523551625599a5f4c6d76c145af70518bdff833b8797a667d536ad737360")
    version("1.2.0", sha256="23ed6ea1f29ce604a3947693d5bc53fd622c82dd06434163f317db303ce765ce")
    version("1.1.1", sha256="dffad3da7c915752b164eab38296e8eee56cd59d8067d0b4bf7d4b7a4b929ba2")
    version("1.0.3.4", sha256="f261ff8c65ceef4799784cd999b256d608c177d4c90b083553aceec3b6c23fd3")

    depends_on("py-setuptools@18.0:", type="build")
    depends_on("py-cython@0.19:", type="build")
    depends_on("py-numpy", type=("build", "run"))
