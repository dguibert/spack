# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install oops
#
# You can edit this file again by typing:
#
#     spack edit oops
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Oops(CMakePackage):
    """OOPS as a common framework for research and Operations."""

    homepage = "https://www.ecmwf.int/en/elibrary/13852-oops-common-framework-research-and-operations"
    url      = "file://%s/oops_cy45b.tar.gz" % os.environ.get('HPCW_DOWNLOAD_URL')

    version('45b', sha256='82bbb17a8e3a04c1ae61ca3c4c85b874e0c9c68ba5bcbd3710e7547f54e1d74e')

    depends_on('raps-support')

