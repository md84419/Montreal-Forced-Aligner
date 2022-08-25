#import setuptools_scm  # noqa
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="montreal-forced-aligner",
    version="2.0.0rc6",
    description="The Montreal Forced Aligner is a command line utility for performing forced alignment of speech datasets using Kaldi",
    description_content_type="text/markdown",
    author=["roboticaml", "md84419"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=["montreal_forced_aligner"],
)
