# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNumba(PythonPackage):
    """NumPy aware dynamic Python compiler using LLVM"""

    homepage = "https://numba.pydata.org/"
    pypi = "numba/numba-0.35.0.tar.gz"
    git = "https://github.com/numba/numba.git"

    skip_modules = ["numba.core.rvsdg_frontend"]

    license("BSD-2-Clause")

    version("0.58.1", sha256="487ded0633efccd9ca3a46364b40006dbdaca0f95e99b8b83e778d1195ebcbaa")
    version("0.57.1", sha256="33c0500170d213e66d90558ad6aca57d3e03e97bb11da82e6d87ab793648cb17")
    version("0.57.0", sha256="2af6d81067a5bdc13960c6d2519dbabbf4d5d597cf75d640c5aeaefd48c6420a")
    version("0.56.4", sha256="32d9fef412c81483d7efe0ceb6cf4d3310fde8b624a9cecca00f790573ac96ee")
    version("0.56.3", sha256="07a2d8a149ecc6eca4ef5c7216e58511d48184854e07b7f59d0c32fab0742e8f")
    version("0.56.2", sha256="3492f0a5d09e257fc521f5377a6c6b907eec1920d14739f0b2458b9d29946a5a")
    version("0.56.0", sha256="87a647dd4b8fce389869ff71f117732de9a519fe07663d9a02d75724eb8e244d")
    version("0.55.2", sha256="e428d9e11d9ba592849ccc9f7a009003eb7d30612007e365afe743ce7118c6f4")
    version("0.55.1", sha256="03e9069a2666d1c84f93b00dbd716fb8fedde8bb2c6efafa2f04842a46442ea3")
    version("0.55.0", sha256="b221ebd997662a1dcb77e4f09140e022fbfe7577ad0781fc2e0214135dba6cbd")
    version("0.54.0", sha256="bad6bd98ab2e41c34aa9c80b8d9737e07d92a53df4f74d3ada1458b0b516ccff")
    version("0.53.1", sha256="9cd4e5216acdc66c4e9dab2dfd22ddb5bef151185c070d4a3cd8e78638aff5b0")
    version("0.53.0", sha256="55c11d7edbba2ba715f2b56f5294cad55cfd87bff98e2627c3047c2d5cc52d16")
    version("0.52.0", sha256="44661c5bd85e3d3619be0a40eedee34e397e9ccb3d4c458b70e10bf95d1ce933")
    version("0.51.2", sha256="16bd59572114adbf5f600ea383880d7b2071ae45477e84a24994e089ea390768")
    version("0.51.1", sha256="1e765b1a41535684bf3b0465c1d0a24dcbbff6af325270c8f4dad924c0940160")
    version("0.51.0", sha256="da57ef00bc814bf54446fb3f8c0374557a7476e40279ceabefd9f12b05cc3c0c")
    version("0.50.1", sha256="89e81b51b880f9b18c82b7095beaccc6856fcf84ba29c4f0ced42e4e5748a3a7")
    version("0.50.0", sha256="c9e5752821530694294db41ee19a4b00e5826c689821907f6c2ece9a02756b29")
    version("0.49.1", sha256="89e1ad8215918036b0ffc53501888d44ed44c1f2cb09a9e047d06af5cd7e7a5a")
    version("0.49.0", sha256="9dbef9c738685a624fb0a4e2ec4cc425bed0e1de830d9bafc629bdb55e8df98f")
    version("0.48.0", sha256="9d21bc77e67006b5723052840c88cc59248e079a907cc68f1a1a264e1eaba017")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    variant("tbb", default=False, description="Build with Intel Threading Building Blocks")

    depends_on("python@3.9:3.13", when="@0.58", type=("build", "run"))
    depends_on("python@3.8:3.11", when="@0.57", type=("build", "run"))
    depends_on("python@3.7:3.10", when="@0.55:0.56", type=("build", "run"))
    depends_on("python@3.7:3.9", when="@0.54", type=("build", "run"))
    depends_on("python@3.6:3.9", when="@0.53", type=("build", "run"))
    depends_on("python@3.6:3.8", when="@0.52", type=("build", "run"))
    depends_on("python@3.6:3.8", when="@0.48:0.51", type=("build", "run"))
    depends_on("py-numpy@1.22:1.26", when="@0.58.1:", type=("build", "run"))
    depends_on("py-numpy@1.21:1.25", when="@0.58.0", type=("build", "run"))
    depends_on("py-numpy@1.21:1.24", when="@0.57", type=("build", "run"))
    depends_on("py-numpy@1.18:1.23", when="@0.56.1:0.56.4", type=("build", "run"))
    depends_on("py-numpy@1.18:1.22", when="@0.55.2:0.56.0", type=("build", "run"))
    depends_on("py-numpy@1.18:1.21", when="@0.55.0:0.55.1", type=("build", "run"))
    depends_on("py-numpy@1.17:1.20", when="@0.54", type=("build", "run"))
    depends_on("py-numpy@1.15:1.20", when="@0.48:0.53", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-llvmlite@0.41", when="@0.58", type=("build", "run"))
    depends_on("py-llvmlite@0.40", when="@0.57", type=("build", "run"))
    depends_on("py-llvmlite@0.39", when="@0.56", type=("build", "run"))
    depends_on("py-llvmlite@0.38", when="@0.55", type=("build", "run"))
    depends_on("py-llvmlite@0.37", when="@0.54.0", type=("build", "run"))
    depends_on("py-llvmlite@0.34", when="@0.51.1", type=("build", "run"))
    depends_on("py-llvmlite@0.33", when="@0.50.1", type=("build", "run"))
    depends_on("py-llvmlite@0.31", when="@0.48", type=("build", "run"))
    depends_on("py-importlib-metadata", when="@0.56:^python@:3.8", type=("build", "run"))

    depends_on("tbb", when="+tbb")
    conflicts("~tbb", when="@:0.50")  # No way to disable TBB
    # Version 6.0.0 of llvm had a hidden symbol which breaks numba at runtime.
    # See https://reviews.llvm.org/D44140
    conflicts("^llvm@6.0.0")

    def setup_build_environment(self, env):
        if self.spec.satisfies("~tbb"):
            env.set("NUMBA_DISABLE_TBB", "yes")
