# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyXarray(PythonPackage):
    """N-D labeled arrays and datasets in Python"""

    homepage = "https://github.com/pydata/xarray"
    pypi = "xarray/xarray-0.9.1.tar.gz"

    # 'xarray.tests' requires 'pytest'. Leave out of 'import_modules' to avoid
    # unnecessary dependency.
    import_modules = [
        "xarray",
        "xarray.core",
        "xarray.plot",
        "xarray.util",
        "xarray.backends",
        "xarray.coding",
    ]

    license("Apache-2.0")

    version("2023.9.0", sha256="271955c05dc626dad37791a7807d920aaf9c64cac71d03b45ec7e402cc646603")
    version("2023.8.0", sha256="825c6d64202a731a4e49321edd1e9dfabf4be06802f1b8c8a3c00a3ebfc8cedf")
    version("2023.7.0", sha256="dace2fdbf1b7ff185d9c1226a24bf83c2ae52f3253dbfe80e17d1162600d055c")
    version("2023.5.0", sha256="318a651f4182b9cecb7d1c57ad0ed9bdaed5f49c43dbb638c0a845b8faf405e8")
    version("2023.4.2", sha256="958ec588220352343b910cbc05e54e7ab54d4e8c1c3a7783d6bfe7549d0bd0d2")
    version("2023.4.1", sha256="f424c5d8ee283a8bfb3d481db4c9d8e006cbe3352489af434d1c110e6b806b39")
    version("2023.4.0", sha256="9f0f7e3402037c6611e802662b4374ddf55985a725bfc18dc2325cebdc06d4e7")
    version("2023.3.0", sha256="f05c74b60b072e6919ef2ae9cf3c67a46173da585ca5912808118ab0c61b2cca")
    version("2023.2.0", sha256="aa760500a2d8f8be8efd8f3b27a94b2af3b0a8c2c037347d595eaf6ff09d8a77")
    version("2023.11.0", sha256="9a45e10741844b5f948d8e1e768b460df7e90696d18e2eff2c1d47f5d9d50252")
    version("2023.1.0", sha256="7bee552751ff1b29dab8b7715726e5ecb56691ac54593cf4881dff41978ce0cd")
    version("2023.10.1", sha256="9eeee170c3fc2f3321eb6ba40c17ffe4d8c98d49d55e4a3fba66a75bdc7dd9e5")
    version("2022.9.0", sha256="a2a5b48ec0a3890b71ef48853fe9d5107d2f75452722f319cb8ed6ff8e72e883")
    version("2022.6.0", sha256="1028d198493f66bb15bd35dcfdd11defd831cbee3af6589fff16f41bddd67e84")
    version("2022.3.0", sha256="398344bf7d170477aaceff70210e11ebd69af6b156fe13978054d25c48729440")
    version("2022.12.0", sha256="083d08e552a7647c7ece136dfa3a4b6a1379256beb55bbed8b8ddf05f1e14ec7")
    version("2022.11.0", sha256="3008a302877f87a0f9043b1f01a4ad4e85b668bbdd38d488764098624632f527")
    version("2022.10.0", sha256="b39ff3475f73eaacdf831b0ab7eb6930e7b5933e46dcf71b9327f4c4bb941793")
    version("0.18.2", sha256="5d2e72a228286fcf60f66e16876bd27629a1a70bf64822c565f16515c4d10284")
    version("0.17.0", sha256="9c2edad2a4e588f9117c666a4249920b9717fb75703b96998cf65fcd4f60551f")
    version("0.16.2", sha256="38e8439d6c91bcd5b7c0fca349daf8e0643ac68850c987262d53526e9d7d01e4")
    version("0.14.0", sha256="a8b93e1b0af27fa7de199a2d36933f1f5acc9854783646b0f1b37fed9b4da091")
    version("0.13.0", sha256="80e5746ffdebb96b997dba0430ff02d98028ef3828e6db6106cbbd6d62e32825")
    version("0.12.0", sha256="856fd062c55208a248ac3784cac8d3524b355585387043efc92a4188eede57f3")
    version("0.11.0", sha256="636964baccfca0e5d69220ac4ecb948d561addc76f47704064dcbe399e03a818")
    version("0.9.1", sha256="89772ed0e23f0e71c3fb8323746374999ecbe79c113e3fadc7ae6374e6dc0525")

    variant("io", default=False, description="Build io backends")
    variant("parallel", default=False, description="Build parallel backend")

    # pyproject.toml
    depends_on("py-setuptools", when="@:0.15", type="build")
    depends_on("py-setuptools@38.4:", when="@0.16:", type="build")
    depends_on("py-setuptools@42:", when="@0.17:", type="build")
    depends_on("py-setuptools-scm", when="@0.15:", type="build")
    depends_on("py-setuptools-scm@7:", when="@2023.7.0:", type="build")
    depends_on("py-setuptools-scm@3.4:+toml", when="@0.17:2022.3.0", type="build")
    depends_on("py-setuptools-scm-git-archive", when="@0.17:2022.3.0", type="build")

    # setup.cfg
    depends_on("python@2.7,3.5:", when="@0.11:", type=("build", "run"))
    depends_on("python@3.5:", when="@0.12", type=("build", "run"))
    depends_on("python@3.5.3:", when="@0.13", type=("build", "run"))
    depends_on("python@3.6:", when="@0.14:", type=("build", "run"))
    depends_on("python@3.7:", when="@0.17:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.21:", type=("build", "run"))
    depends_on("python@3.9:", when="@2023.7.0:", type=("build", "run"))

    depends_on("py-numpy@1.7:", when="@0.9.1", type=("build", "run"))
    depends_on("py-numpy@1.12:", when="@0.11:0.13", type=("build", "run"))
    depends_on("py-numpy@1.14:", when="@0.14.0", type=("build", "run"))
    depends_on("py-numpy@1.15:", when="@0.15:", type=("build", "run"))
    depends_on("py-numpy@1.17:", when="@0.18:", type=("build", "run"))
    depends_on("py-numpy@1.18:", when="@0.20:", type=("build", "run"))
    depends_on("py-numpy@1.21:", when="@2023.7.0:", type=("build", "run"))

    depends_on("py-pandas@0.15.0:", when="@0.9.1", type=("build", "run"))
    depends_on("py-pandas@0.19.2:", when="@0.11:0.13", type=("build", "run"))
    depends_on("py-pandas@0.24:", when="@0.14.0", type=("build", "run"))
    depends_on("py-pandas@0.25:", when="@0.15:", type=("build", "run"))
    depends_on("py-pandas@1:", when="@0.18:", type=("build", "run"))
    depends_on("py-pandas@1.1:", when="@0.20:", type=("build", "run"))
    depends_on("py-pandas@1.4:", when="@2023.7.0:", type=("build", "run"))

    depends_on("py-packaging@20:", when="@0.21:", type=("build", "run"))
    depends_on("py-packaging@21.3:", when="@2023.7.0:", type=("build", "run"))

    depends_on("py-netcdf4", when="+io", type=("build", "run"))
    depends_on("py-h5netcdf", when="+io", type=("build", "run"))
    depends_on("py-scipy", when="+io", type=("build", "run"))
    depends_on("py-pydap", when="+io ^python@:3.9", type=("build", "run"))
    depends_on("py-zarr", when="+io", type=("build", "run"))
    depends_on("py-fsspec", when="+io", type=("build", "run"))
    depends_on("py-cftime", when="+io", type=("build", "run"))
    depends_on("py-rasterio", when="@:2022.3.0 +io", type=("build", "run"))
    depends_on("py-cfgrib", when="@:2022.3.0 +io", type=("build", "run"))
    depends_on("py-pooch", when="+io", type=("build", "run"))
    depends_on(
        "py-dask+array+dataframe+distributed+diagnostics+delayed",
        when="+parallel",
        type=("build", "run"),
    )
