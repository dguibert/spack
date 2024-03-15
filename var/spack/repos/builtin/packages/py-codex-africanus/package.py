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
