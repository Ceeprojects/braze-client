from setuptools import find_packages
from setuptools import setup

NAME = "braze-client"
VERSION = "0.0.6"

REQUIRES = ["requests >=2.21.0, <3.0.0", "tenacity >=8.2.3"]

EXTRAS = {"dev": ["tox"]}

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Braze Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eugene-ydc/braze-client",
    author_email="eugene.druzhynin@you.com",
    keywords=["Appboy", "Braze"],
    install_requires=REQUIRES,
    extras_require=EXTRAS,
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
)
