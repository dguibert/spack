# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyPythonCasacore(PythonPackage):
    """A wrapper around CASACORE, the radio astronomy library"""

    homepage = "https://github.com/casacore/python-casacore"
    pypi = "python-casacore/python-casacore-3.5.2.tar.gz"

    version("3.5.2", sha256="ad70c8e08893eec928b3e38c099bda8863f5aa9d099fd00694ad2b0d48eba08f")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")

    depends_on("boost+python", type=("build", "run"))
    depends_on("casacore+python", type=("build", "run"))
    depends_on("wcslib@4.20:+cfitsio")

    def install(self, spec, prefix):
        cflags = []
        cflags.append("-I"+spec["boost"].prefix.include+"/boost")
        cflags.append("-L"+spec["boost"].prefix.lib)

        cflags.append("-I"+spec["casacore"].prefix.include)
        cflags.append("-L"+spec["casacore"].prefix.lib)

        env["CFLAGS"] = f"{' '.join(cflags)}"
        env["LD_LIBRARY_PATH"] = f"{spec['boost'].prefix.lib}:{spec['casacore'].prefix.lib}"
        print(f"CFLAGS={env['CFLAGS']}")
        print(f"LD_LIBRARY_PATH={env['LD_LIBRARY_PATH']}")
        super().install(spec,prefix)
