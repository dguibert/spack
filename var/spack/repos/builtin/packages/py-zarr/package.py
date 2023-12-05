# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyZarr(PythonPackage):
    """Zarr is a Python package providing an implementation of chunked,
    compressed, N-dimensional arrays."""

    homepage = "https://zarr.readthedocs.io"
    pypi = "zarr/zarr-2.3.2.tar.gz"

    license("MIT")

    version("2.17.0", sha256="6390a2b8af31babaab4c963efc45bf1da7f9500c9aafac193f84cf019a7c66b0")
    version("2.16.1", sha256="4276cf4b4a653431042cd53ff2282bc4d292a6842411e88529964504fb073286")
    version("2.16.0", sha256="84e36b695bda0ecea52af9861271984cb22a5c864679907b7b9ba3f79b684f7e")
    version("2.15.0", sha256="3894001c0bb5d68d3d21a0562cc49e6ba14fee7d17ad2be8d088ab301665a4c6")
    version("2.14.2", sha256="68ec59b8ebdfc4fee5e32bd6c0ce273f72f7d4ed017454b45327c673c60907bc")
    version("2.14.1", sha256="1d2b6cd4460f1741deca17df1e9f071b917380cb2a27b6e2e949f067a2054a64")
    version("2.14.0", sha256="ddce409e2bc1a7b962e517346fc002033211bc5c5c73229960763815ff9f1839")
    version("2.13.6", sha256="f079444d5126db7ba5895a682797d86d02813f49b35854ee2d89c7503dc3677e")
    version("2.13.3", sha256="db24b090616c638f65e33a6bc5d956d642221182961515ccbc28b17fb0d0b48c")
    version("2.13.2", sha256="8fc469238ae818e183d68ad6203d77c206ddb0b12563eb4bc8209fcb69b7c2d6")
    version("2.13.1", sha256="b800859c569b15b0d75241b0c36fc70dd8337399fb846c70cb536b0f3192fb62")
    version("2.13.0", sha256="3e76ed6e209578e46d1718bb1e90aa1cea5012cffe8db9a9eb3e59d7e32bee40")
    version("2.12.0", sha256="515a31ee4bad6bb48ae05178c588ae49a02a35defa01dd9a3293306903368165")
    version("2.11.3", sha256="6ee84547aec60fd06fc9356e9194302ebbdb2fd912fd365a0a652ad5c69636f5")
    version("2.11.2", sha256="794d76f6ab4940eaaa51b1b1a5c15422ba22e9063199d1ed946f98483e0ef329")
    version("2.11.1", sha256="11b628f42dec36e0147879e8bd471524b59b238094b9b21e3c35be78399c115e")
    version("2.11.0", sha256="b0873be27af5690738fa158ea7a802eae454904c33995056185acc5a7425b451")
    version("2.10.3", sha256="76932665c2146ebdf15f6dba254f9e0030552fbfcf9322dea822bff96fbce693")
    version("2.10.2", sha256="5c6ae914ab9215631bb95c09e76b9b9b4fffa70fec0c7bca26b68387d858ebe2")
    version("2.10.0", sha256="8ca8e505cadb4f7f97aab4e4193bb302b6338bf54593c98fe7581bf574ed864c")
    version("2.6.1", sha256="fa7eac1e4ff47ff82d09c42bb4679e18e8a05a73ee81ce59cee6a441a210b2fd")
    version("2.5.0", sha256="d54f060739208392494c3dbcbfdf41c8df9fa23d9a32b91aea0549b4c5e2b77f")
    version("2.4.0", sha256="53aa21b989a47ddc5e916eaff6115b824c0864444b1c6f3aaf4f6cf9a51ed608")
    version("2.3.2", sha256="c62d0158fb287151c978904935a177b3d2d318dea3057cfbeac8541915dfa105")

    depends_on("python@3.9:", type=("build", "run"), when="@2.17:")
    depends_on("python@3.7:3", type=("build", "run"), when="@2.10")
    depends_on("py-setuptools@64:", type="build", when="@2.17:")
    depends_on("py-setuptools@38.6.0:", type="build", when="@2.4.0:")
    depends_on("py-setuptools@18.0:", type="build")
    depends_on("py-setuptools-scm@1.5.5:", type="build")
    depends_on("py-asciitree", type=("build", "run"))
    depends_on("py-numpy@1.21.1:", type=("build", "run"), when="@2.17:")
    depends_on("py-numpy@1.7:", type=("build", "run"))
    # https://github.com/zarr-developers/zarr-python/issues/1818
    depends_on("py-numpy@:1", when="@:2.17", type=("build", "run"))
    depends_on("py-fasteners", type=("build", "run"))
    depends_on("py-numcodecs@0.10:", type=("build", "run"), when="@2.17:")
    depends_on("py-numcodecs@0.6.4:", type=("build", "run"), when="@2.4.0:")
    depends_on("py-numcodecs@0.6.2:", type=("build", "run"))

    # Historical dependencies
    depends_on("py-msgpack", type=("build", "run"), when="@:2.3.2")
