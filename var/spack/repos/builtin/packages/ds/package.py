# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from os import symlink

from spack.package import *


class Ds(AutotoolsPackage):
    """SAOImage DS9 is an astronomical imaging and data visualization
    application."""

    homepage = "https://ds9.si.edu/"
    #url = "http://ds9.si.edu/download/source/ds9.8.0.tar.gz"
    url = "http://ds9.si.edu/archive/source/ds9.8.0.tar.gz"

    version("9.8.5", sha256="eae537a3354db2b38c88edf5267b27e6ede03ce8aa63a5d7b70f683af194f0f7")
    version("9.8.4.1", sha256="1f3fe21355fb9c1614c90e398a2c980a72e809a96a865244c0b63c4b6655ab90")
    version("9.8.4", sha256="4f15464a87c0a743601b71a0c1ee65baf4e739418e662a6edef7a036f4bc8042")
    version("9.8.3", sha256="cc5952d7ea85239a159ddfb7b5917c137f1bcb633d0668bc76c622c893c9d0f9")
    version("9.8.2.1", sha256="6389badfe01f9d4cc456d6c7614e46e15ff8d30ee8ef051a96109b3d3aa3d3f7")
    version("9.8.2", sha256="06950ea4af803f2bcde1cd6a0f950117728927455b204b0a5ae71093c7979022")
    version("9.8.1", sha256="ee1cbc8325eb3edd20fd4eaf94083156561681d9c322e751515f5a36ed724575")
    version("9.8.0.1", sha256="a84d9b0e6e2520d8ebd57160903228f99a1f5ef33d2a542cea9b4cb72a12f496")
    version("9.8.0", sha256="f3bdb46c1653997202f98c6f76632a4eb444707f4b64c14f8b96863d9c890304")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("m4", type="build")
    depends_on("libtool", type="build")

    depends_on("libx11")
    depends_on("libxml2")
    depends_on("libxslt")
    depends_on("openssl")
    depends_on("tcl")
    depends_on("tcl-tclxml")
    depends_on("tk")

    def patch(self):
        # the package provides it's own Tcl utilities
        # compiling and manually setting paths for all of them is contrived
        # (most of the utilities are small and not included in spack)

        # inject libxml, libxslt prefixes into configure search paths
        filter_file(
            "/usr/bin/xml2-config",
            join_path(self.spec["libxml2"].prefix, "bin/xml2-config"),
            "tclxml/configure",
            string=True,
        )

        filter_file(
            "/usr/bin/xslt-config",
            join_path(self.spec["libxslt"].prefix, "bin/xslt-config"),
            "tclxml/configure",
            string=True,
        )

        # symlink the master configure script into the source directory
        symlink("unix/configure", "configure")

    def configure_args(self):
        srcdir = join_path(self.stage.source_path, "unix")
        return ["--srcdir={0}".format(srcdir)]

    def install(self, spec, prefix):
        # no install target provided in Makefile, install manually

        install_tree("bin", prefix.bin)
        install_tree("share", prefix.share)
        install_tree("lib", prefix.lib)
