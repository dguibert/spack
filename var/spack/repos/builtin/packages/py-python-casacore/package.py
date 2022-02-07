# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import inspect

class PyPythonCasacore(PythonPackage):
    """A wrapper around CASACORE, the radio astronomy library"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://casacore.github.io/python-casacore/"
    pypi     = "python-casacore/python-casacore-3.4.0.tar.gz"

    version('3.4.0', sha256='f654781292308de70c037981f5f7f5aeb02cf980a6f1367d1c294e7b4fca42ce')
    version('3.3.1', sha256='c1f196b87ea34f930da6900eebc0a8f39291352d4def6631a2ec148ef5cf083a')
    version('3.3.0', sha256='e682940c50e6dbeb4e4a3301e3e15cd89774ce6849dfc1b6602b6663c058213b')
    version('3.2.0', sha256='d48e6202831ef22983961aa14c82294325f71b2fd3e108efaa3c1ca99b7505b5')


    depends_on('casacore+python', type=('build', 'link'))
    depends_on('boost+python', type=('build', 'link'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-argparse', type=('build', 'run'), when='^python@:2.6,3.0:3.1')
    depends_on('py-future', type=('build', 'run'))

    # https://github.com/casacore/python-casacore/blob/master/setup.py
    # $ python setup.py build_ext -I/opt/casacore/include:/other/include/path -L/opt/casacore/lib
    def build_args(self):
       library_dirs = []
       include_dirs = []
       for dep in self.spec.dependencies(deptype='link'):
          query = self.spec[dep.name]
          library_dirs.extend([query.prefix + "/lib"])
          include_dirs.extend(query.headers.directories)
       options = []
       options.append('--library-dirs=' + (':'.join(library_dirs)))
       options.append('-I' + (':'.join(include_dirs)))
       print(str(options))
       return options

    def install(self, spec, prefix):
       args = self.build_args()
       python('setup.py', 'build_ext', *args)
       python('setup.py', 'build')
       python('setup.py', 'install', '--prefix={0}'.format(prefix))

