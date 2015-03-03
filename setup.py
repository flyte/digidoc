import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="digidoc",
    version="0.0.1",
    author="Ellis Percival",
    author_email="digidoc@failcode.co.uk",
    description="A document digitiser",
    license="UNLICENSE",
    keywords="document digitiser",
    url="https://github.com/flyte/digidoc",
    packages=("digidoc",),
    install_requires=read("requirements.txt"),
    entry_points={
        "console_scripts": (
            "digidoc = digidoc.menu:main",
        )
    }
)
