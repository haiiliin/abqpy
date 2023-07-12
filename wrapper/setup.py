import re

from setuptools import setup


def get_abqpy_version():
    try:
        import setuptools_scm

        version = setuptools_scm.get_version(root="..", version_scheme="post-release")
        major, minor, patch, *rest = re.match(r"(\d+)\.(\d+)\.(\d+)(.*)", version).groups()
        return f"{major}.{minor}.{patch}"
    except (LookupError, ImportError):
        return "2021.*"


setup(install_requires=[f"abqpy=={get_abqpy_version()}"])
