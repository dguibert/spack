# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Racon(CMakePackage):
    """Ultrafast consensus module for raw de novo genome assembly of long
    uncorrected reads."""

    homepage = "https://github.com/isovic/racon"
    url = "https://github.com/isovic/racon/releases/download/1.2.1/racon-v1.2.1.tar.gz"

    version('1.5.0', sha256='41e362f71cc03b934f17d6e2c0d626e1b2997258261b14551586de006666424a')
    version('1.4.21', sha256='df99208ebef6a12e1da11a31dade2eafe13a4cd80b4917cce44d44d879b5aee4')
    version('1.4.20', sha256='820a2ef7a6edae624c8f2b2b8e22c5daace47af9dc91bb40ce6fe1f8169d299e')
    version('1.4.13', sha256='4220e98bf84768483bd94eef62a0821cffc74f4e7139c74685c08161909263b0')
    version('1.4.12', sha256='ad8a8c15c4dcbbaa2a67d0739abbb74598ff1cf4bbde2dcfeaee3aea17be0284')
    version('1.4.11', sha256='470efcc4b9985f47ffa1f384940034950ebf20b213a88637f2b79f4eb0b0cb2f')
    version('1.4.10', sha256='016fb3affb977303a5f5ad27339a7044fa3d9b89a6ea3c7734479f864155a0c2')
    version('1.4.9', sha256='ec9af55959339719b9de2f78ab7364c7b040eefe4bf0fb4bfaebf2462fc7354f')
    version('1.4.7', sha256='65cff4c0d12547d7a2ff848f6a992da369ed33d8ca481cc3e942e5a07fc3a0ea')
    version('1.4.6', sha256='56b64bbcdfd670ce8a834ba10aebe96bd3342c668da854b152fc1b7b2e84efd3')
    version('1.4.3', sha256='dfce0bae8234c414ef72b690247701b4299e39a2593bcda548a7a864f51de7f2')
    version('1.4.2', sha256='b36d8b767e0fc9acdd3e9d34c99a8bbc02a3aae7a953c57923d935ebdf332700')
    version('1.4.0', sha256='3e1e97388f428326342dead3f8500e72b1986f292bdfd4d1be4a0d2a21f4cc61')
    version('1.3.3', sha256='174afde420ed2e187e57c1a6e9fc6a414aa26723b4ae83c3904640fc84941e66')
    version('1.3.2', sha256='7c99380a0f1091f5ee138b559e318d7e9463d3145eac026bf236751c2c4b92c7')
    version('1.3.1', sha256='7ce3b1ce6abdb6c6a63d50755b1fc55d5a4d2ab8f86a1df81890d4a7842d9b75')
    version('1.3.0', sha256='f2331fb88eae5c54227dc16651607af6f045ae1ccccc1d117011762927d4606a')
    version('1.2.1', sha256='6e4b752b7cb6ab13b5e8cb9db58188cf1a3a61c4dcc565c8849bf4868b891bf8')

    depends_on("cmake@3.2:", type="build")
    depends_on("python", type="build")
    depends_on("sse2neon", when="target=aarch64:")

    conflicts("%gcc@:4.7,10.1.0:")
    conflicts("%clang@:3.1")

    patch('aarch64.patch', when='@:1.4.99 target=aarch64:')

    def cmake_args(self):
        args = ["-Dracon_build_wrapper=ON"]
        return args
