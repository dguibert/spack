# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyFastaq(PythonPackage):
    """Manipulate FASTA and FASTQ files."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/sanger-pathogens/Fastaq"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    url      = "https://github.com/sanger-pathogens/Fastaq/archive/refs/tags/v3.17.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.17.0',         sha256='bb63c03e4bdde92deb43469f8a93a7f440272e47adc8edb9d94cd5fa107fa746')
    version('3.16.0',         sha256='6a81df61782a69acdaccd57895ed776287c480d606526c9e931a216a92b1e32a')
    version('3.15.0',         sha256='5a31226e8021108ce70f159d28aca32ea1b18ef6c13de6aa269c1ec8e540d7ea')
    version('3.14.0',         sha256='4cdf7e53082217bec7079e6888424708308ee1e53957942fbe6bbc28e8d7ba81')
    version('3.13.0',         sha256='e0652b0d8e169a0a49f7d172b146098f4f87ec95d3e30519a8d99af685e6c0bb')
    version('3.12.1',         sha256='deefb2b2956d9f58b24a079c315099d3576df9cd7c26aaea7f1c9aa9437d02f8')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))
    depends_on('samtools', type='run')
    depends_on('gzip', type='run')

