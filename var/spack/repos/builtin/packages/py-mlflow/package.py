# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMlflow(PythonPackage):
    """An open source platform for the machine learning lifecycle"""

    homepage = "https://mlflow.org"
    url = "https://files.pythonhosted.org/packages/6d/c2/2d1027bc6d3f4ff82dc9a4745ce411ebb86cf967d154ea99595d29a11cc4/mlflow-1.29.0-py3-none-any.whl"

    version("1.29.0", sha256="24d95c6a19eccef5abfe5430680d96e9ab27c67f01cd4cde0f7384cb67a5c69a", expand=False)

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))
    ## core-requirements.txt
    #alembic<2
    #docker<7,>=4.0.0
    #Flask<3
    #numpy<2
    #scipy<2
    #pandas<2
    #prometheus-flask-exporter<1
    #querystring_parser<2
    #sqlalchemy<2,>=1.4.0
    #gunicorn<21; platform_system != 'Windows'
    #waitress<3; platform_system == 'Windows'
    #
    ## skinny-requirements.txt
    depends_on("py-click", type="run") # click<9,>=7.0
    depends_on("py-cloudpickle", type="run") # cloudpickle<3
    depends_on("py-databricks-cli", type="run") # databricks-cli<1,>=0.8.7
    depends_on("py-entrypoints", type="run") # entrypoints<1
    depends_on("py-gitpython", type="run") # gitpython<4,>=2.1.0
    depends_on("py-pyyaml", type="run") #pyyaml<7,>=5.1
    depends_on("py-protobuf", type="run") #protobuf<5,>=3.12.0
    depends_on("py-pyts", type="run") #pytz<2023
    depends_on("py-requests", type="run") #requests<3,>=2.17.3
    depends_on("py-packaging", type="run") # packaging<22
    depends_on("py-importlib-metadata", type="run") # importlib_metadata<5,>=3.7.0,!=4.7.0
    depends_on("py-sqlparse", type="run") # sqlparse<1,>=0.4.0
    #
    #"extras": [
    #            "scikit-learn",
    #            # Required to log artifacts and models to HDFS artifact locations
    #            "pyarrow",
    #            # Required to log artifacts and models to AWS S3 artifact locations
    #            "boto3",
    #            # Required to log artifacts and models to GCS artifact locations
    #            "google-cloud-storage>=1.30.0",
    #            "azureml-core>=1.2.0",
    #            # Required to log artifacts to SFTP artifact locations
    #            "pysftp",
    #            # Required by the mlflow.projects module, when running projects against
    #            # a remote Kubernetes cluster
    #            "kubernetes",
    #            # Required to serve models through MLServer
    #            "mlserver>=0.5.3",
    #            "mlserver-mlflow>=0.5.3",
    #            "virtualenv",
    #        ],
    #        "pipelines": [
    #            "scikit-learn>=1.0",
    #            "pyarrow>=7.0",
    #            "shap>=0.40",
    #            "pandas-profiling>=3.1",
    #            "ipython>=7.0",
    #            "markdown>=3.3",
    #            "Jinja2>=3.0",
    #        ],
    #        "sqlserver": ["mlflow-dbstore"],
    #        "aliyun-oss": ["aliyunstoreplugin"],


    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
