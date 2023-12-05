# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDaskMs(PythonPackage):
    """xarray Dataset from CASA Tables."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ska-sa/dask-ms"
    pypi = "dask_ms/dask_ms-0.2.19.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("BSD-3-CLAUSE")
    
    version("0.2.19", sha256="892712e68df7a4f98daf4f2a0be406baad3ca92d301d38a00fac1d53ee6ca7a2")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.9:3.12", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    depends_on("py-setuptools", type="build")

    #[tool.poetry.dependencies]
    # python = "^3.9, < 3.13"
    # appdirs = "^1.4.4"
    depends_on("py-appdirs@1.4.4", type=("build", "run"))
    # dask = {extras = ["array"], version = "^2023.1.0"}
    depends_on("py-appdirs@1.4.4", type=("build", "run"))
    # donfig = "^0.7.0"
    depends_on("py-donfig@0.7.0", type=("build", "run"))
    # python-casacore = "^3.5.1"
    depends_on("py-python-casacore@3.5.1:", type=("build", "run"))
    # pyarrow = {version = "^14.0.1", optional = true}
    depends_on("py-pyarrow@14.0.1", type=("build", "run"))
    # zarr = {version = "^2.12.0", optional=true}
    depends_on("py-zarr@2.12.0:", type=("build", "run"), when="+zarr")
    # xarray = {version = "^2023.01.0", optional=true}
    depends_on("py-xarray@2023.1.0:", type=("build", "run"), when="+xarray")
    # s3fs = {version = "^2023.1.0", optional=true}
    depends_on("py-s3fs@2023.1.0:", type=("build", "run"), when="+s3")
    # minio = {version = "^7.2.0", optional = true}
    depends_on("py-minio@7.2.0", type=("build", "run"), when="+testing")
    # pytest = {version = "^7.1.3", optional=true}
    depends_on("py-pytest@7.1.3", type=("build", "run"), when="+testing")
    # pandas = {version = "^2.1.2", optional = true}
    depends_on("py-pandas@2.1.2:", type=("build", "run"), when="+arrow")
    depends_on("py-pyarrow", type=("build", "run"), when="+arrow")
    
    # [tool.poetry.extras]
    # arrow = ["pandas", "pyarrow"]
    variant("arrow", default=True)
    # xarray = ["xarray"]
    variant("xarray", default=True)
    # zarr = ["zarr"]
    variant("zarr", default=True)
    # s3 = ["s3fs"]
    variant("s3", default=False)
    # testing = ["minio", "pytest"]
    variant("testing", default=False)

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
