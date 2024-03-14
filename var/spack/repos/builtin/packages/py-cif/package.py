# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCif(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git = "https://castle.frec.bull.fr:24443/cepp/apps/cif/cif"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    #license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions and checksums here.
    # version("1.2.3", md5="0123456789abcdef0123456789abcdef")
    version("devel", branch="devel")
    version("LSCE", branch="LSCE")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("py-setuptools", type="build")
    
    depends_on("gdal") #GDAL_with_version(),
    depends_on("py-numpy") #NUMPY,
    depends_on("py-cftime@1.1.1") #CFTIME,
    depends_on("py-scipy") #'scipy',
    depends_on("py-matplotlib@:3.4") #'matplotlib<3.4',
    depends_on("py-pandas") #'pandas',
    depends_on("py-netcdf4") #'netCDF4',
    depends_on("py-pytz") #'pytz',
    depends_on("py-python-dateutil") #'python-dateutil',
    depends_on("py-xarray") #'xarray',
    depends_on("py-pyyaml") #'pyyaml',
    depends_on("py-pyproj") #'pyproj',
    depends_on("py-psutil")#'psutil',
    depends_on("py-pillow") #'Pillow',
    depends_on("py-f90nml")#'f90nml',
    depends_on("py-cfgrib")#'cfgrib',
    #'future',
    depends_on("py-bottleneck") #'bottleneck',
    depends_on("py-h5py")#'h5py'
