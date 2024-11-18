# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCodexAfricanus(PythonPackage):
    """Radio Astronomy Building Blocks"""

    homepage = "https://github.com/ratt-ru/codex-africanus"
    pypi = "codex-africanus/codex-africanus-0.3.4.tar.gz"

    version("0.3.4", sha256="85cddce9e256ec422d2782fb65fa89b9ab701323df84a319f3b80653b5e4b648")
    version("0.2.10", sha256="99a4c73c5f4e7238146d9ef71206c75474578db7a21d23e65c6353bf6da70d2e")

    depends_on("py-setuptools", type="build")

    depends_on("py-appdirs@1.4.3:")
    depends_on("py-decorator")
    depends_on("py-numpy@1.14.0:2")
    conflicts("^py-numpy@1.15.3")
    depends_on("py-numba@0.53.1:")

    variant("cuda", default=False)
    variant("dask", default=False)
    # extras_require
    with when("+cuda"):
        #"cuda": ["cupy >= 9.0.0", "jinja2 >= 2.10"],
        depends_on("py-cupy@9.0.0:")
        depends_on("py-jinja2@2.10:")

    with when("+dask"):
        #"dask": ["dask[array] >= 2.2.0"],
        depends_on("py-dask+array@2.2.0:")
    #"jax": ["jax >= 0.2.11", "jaxlib >= 0.1.65"],
    #"scipy": ["scipy >= 1.4.0"],
    #"astropy": ["astropy >= 4.0"],
    #"python-casacore": ["python-casacore >= 3.4.0, != 3.5.0"],
    #"ducc0": ["ducc0 >= 0.9.0"],
    #"testing": ["pytest", "flaky"],
