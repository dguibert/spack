# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cdi(AutotoolsPackage):
    """CDI is a C and Fortran Interface to access Climate and NWP model Data.
    Supported data formats are GRIB, netCDF, SERVICE, EXTRA and IEG."""

    homepage = "https://code.mpimet.mpg.de/projects/cdi"
    url      = "https://code.mpimet.mpg.de/attachments/download/22867/cdi-1.9.9.tar.gz"
    list_url = 'https://code.mpimet.mpg.de/projects/cdi/files'

    version('1.9.9', sha256='93904f4021e602f1e35bce3c9983879b37395b38842957f24d2766ffabb8f5e2')
    version('1.9.6', url='https://code.mpimet.mpg.de/attachments/download/19298/cdi-1.9.6.tar.gz',
        sha256='cbfbe0711ef1b7305a8f20763fa852452c0ce4e6352f2d6fd9481402fee295ad')
    version('1.9.5', 'fb8315a36708a5cbc898715dbdc3da48',
            url = 'https://code.mpimet.mpg.de/attachments/download/18255/cdi-1.9.5.tar.gz')
    version('1.9.4', 'e5bb0e67367482f23e8e8e05b33950e8',
            url='https://code.mpimet.mpg.de/attachments/download/17327/cdi-1.9.4.tar.gz')
    version('1.9.3', '3702754326319545164576995d419826',
            url='https://code.mpimet.mpg.de/attachments/download/16436/cdi-1.9.3.tar.gz')
    version('1.9.2', 'e494540ea37e4401344e023c67cba112',
            url='https://code.mpimet.mpg.de/attachments/download/16032/cdi-1.9.2.tar.gz')
    version('1.9.1', '17edfb700ca9180cdb273465d0016910',
            url='https://code.mpimet.mpg.de/attachments/download/15646/cdi-1.9.1.tar.gz')
    version('1.8.3', branch='cdi-1.8.x')
    version('1.8.2', 'aa39f7fea8a49845b8cb9409146f803d',
            url='https://code.mpimet.mpg.de/attachments/download/15194/cdi-1.8.2.tar.gz',
            preferred=True)
    version('1.8.1', 'e06c6643f9c042c2b1f1ea8ed7ce8d7d',
            url='https://code.mpimet.mpg.de/attachments/download/14290/cdi-1.8.1.tar.gz')
    version('1.7.3', branch='cdi-1.7.x')
    version('1.7.2', '33a293e089d7f4c0f19bda1d490a20b6',
            url='https://code.mpimet.mpg.de/attachments/download/12690/cdi-1.7.2.tar.gz')

    variant('netcdf', default=True, description='Enable NetCDF support')
    variant('grib2', default='eccodes', values=('eccodes', 'grib-api', 'none'),
            description='Specify GRIB2 backend')
    variant('external-grib1', default=False,
            description='Ignore the built-in support and use the external '
                        'GRIB2 backend for GRIB1 files')
    variant('szip-grib1', default=False,
            description='Enable szip compression for GRIB1')
    variant('fortran', default=True, description='Enable Fortran interfaces')
    variant('threads', default=True,
            description='Compile and link for multithreading')

    # YAXT is required
    # variant('mpi', default=True,
    #         description='Enable MPI support')

    patch('cdi_write_f2003_int64.patch', when='@1.9.5:+fortran')
    patch('cdi_f2003.pc.patch', when='@1.9.5:+fortran')
    patch('icon.patch', when='@1.8.0:1.8.2+fortran')

    # The following patches require autoreconf.
    when_not_patched = '@:1.7.2,1.8.0:1.8.2,1.9.0:'
    patch('fortran_interface.patch', when=when_not_patched + '1.9.4+fortran')
    patch('excessive_linking.patch', when='@1.9.3:1.9.4')
    patch('nag_threads.patch', when=when_not_patched + '%nag+fortran+threads')

    depends_on('autoconf', type='build',
               when=when_not_patched + '1.9.4+fortran')
    depends_on('automake', type='build',
               when=when_not_patched + '1.9.4+fortran')
    depends_on('libtool', type='build',
               when=when_not_patched + '1.9.4+fortran')

    depends_on('autoconf', type='build', when='@1.9.3:1.9.4')
    depends_on('automake', type='build', when='@1.9.3:1.9.4')
    depends_on('libtool', type='build', when='@1.9.3:1.9.4')

    depends_on('autoconf', type='build',
               when=when_not_patched + '%nag+fortran+threads')
    depends_on('automake', type='build',
               when=when_not_patched + '%nag+fortran+threads')
    depends_on('libtool', type='build',
               when=when_not_patched + '%nag+fortran+threads')

    depends_on('netcdf-c', when='+netcdf')
    depends_on('grib-api', when='grib2=grib-api')
    depends_on('eccodes', when='grib2=eccodes')

    depends_on('szip', when='+szip-grib1')

    depends_on('libuuid')

    # depends_on('mpi', when='+mpi')

    conflicts('+szip-grib1', when='+external-grib1 grib2=none',
              msg='The configuration does not support GRIB1')

    @property
    def libs(self):
        """Libcdi can be queried for the following parameters:

        - "c": C-only interface (default)
        - "fortran": Fortran interface

        :return: list of matching libraries
        """
        query_parameters = self.spec.last_query.extra_parameters

        query2libraries = {tuple(): ['libcdi'],
                           ('c',): ['libcdi'],
                           ('c', 'fortran'): ['libcdi_f2003', 'libcdi'],
                           ('fortran',): ['libcdi_f2003', 'libcdi']}

        key = tuple(sorted(query_parameters))
        libraries = query2libraries[key]

        return find_libraries(libraries, root=self.prefix,
                              shared=True, recursive=True)

    @property
    def force_autoreconf(self):
        # We need to autoreconf if any of the patches requiring it has been
        # applied.
        return self.spec.satisfies(self.when_not_patched + '1.9.4+fortran') or \
               self.spec.satisfies('@1.9.3:1.9.4') or \
               self.spec.satisfies(self.when_not_patched + '%nag+fortran+threads')

    @when(when_not_patched + '%nag+fortran+threads')
    def autoreconf(self, spec, prefix):
        script = './autogen.sh'
        set_executable(script)
        autogen = Executable(script)
        autogen()

    def configure_args(self):
        config_args = [
            # Use the service library
            '--enable-service',
            # Use the extra library
            '--enable-extra',
            # Use the ieg library
            '--enable-ieg',
            # Disable HIRLAM extensions
            '--disable-hirlam-extensions',
            # Disable MPI support (due to a bug in the configure script we
            # can't explicitly disable MPI support)
            # '--disable-mpi',
            # Disable extra bindings
            '--disable-swig',
            # Disable Ruby language bindings
            '--disable-ruby',
            # Disable Python language bindings
            '--disable-python']

        config_args += self.with_or_without('netcdf',
                                            activation_value='prefix')
        config_args += self.with_or_without('threads')

        if self.spec.variants['grib2'].value == 'eccodes':
            if self.spec.satisfies('@1.9:'):
                config_args.append('--with-eccodes=' +
                                   self.spec['eccodes'].prefix)
                config_args.append('--without-grib_api')
            else:
                config_args.append('LIBS=' +
                                   self.spec['eccodes'].libs.link_flags)
                config_args.append('--with-grib_api')
        elif self.spec.variants['grib2'].value == 'grib-api':
            config_args.append('--with-grib_api=' +
                               self.spec['grib-api'].prefix)
            if self.spec.satisfies('@1.9:'):
                config_args.append('--without-eccodes')
        else:
            config_args.append('--without-grib_api')
            if self.spec.satisfies('@1.9:'):
                config_args.append('--without-eccodes')

        if '+external-grib1' in self.spec:
            config_args.append('--disable-cgribex')
        else:
            config_args.append('--enable-cgribex')

        if '+szip-grib1' in self.spec:
            config_args.append('--with-szlib=' + self.spec['szip'].prefix)
        else:
            config_args.append('--without-szlib')

        if '+fortran' in self.spec:
            config_args.extend(['--enable-iso-c-interface',
                                '--enable-cf-interface'])
        else:
            config_args.extend(['--disable-iso-c-interface',
                                '--disable-cf-interface'])

        # if '+mpi' in self.spec:
        #     config_args += ['--enable-mpi',
        #                     'CC=' + self.spec['mpi'].mpicc,
        #                     'FC=' + self.spec['mpi'].mpifc]
