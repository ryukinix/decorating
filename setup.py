#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
from warnings import warn
import decorating

here = path.abspath(path.dirname(__file__))
readme = path.join(here, 'README.md')

try:
    import pypandoc
    long_description = pypandoc.convert(readme, 'rst', format='markdown')
except ImportError:
    warn("Only-for-developers: you need pypandoc for upload "
         "correct reStructuredText into PyPI home page")
    # Get the long description from the relevant file
    with open(readme, encoding='utf-8') as f:
        long_description = f.read()


with open('requirements.txt') as f:
    install_requires = list(map(str.strip, f.readlines()))

with open('requirements-dev.txt') as f:
    develop_requires = list(map(str.strip, f.readlines()))


setup(
    name=decorating.__name__,
    version=decorating.__version__,
    description="A useful collection of decorators (focused in animation)",
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='decorating animation decorators decorator',
    author=decorating.__author__,
    author_email=decorating.__email__,
    url=decorating.__url__,
    download_url="{u}/archive/v{v}.tar.gz".format(u=decorating.__url__,
                                                  v=decorating.__version__),
    zip_safe=False,
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples',
                                    'tests', 'docs', '__pycache__']),
    platforms='unix',
    install_requires=install_requires,
    extras_require={
        'develop': develop_requires,
        "Requires-Dist": ["pypandoc"]
    },

    entry_points={  # no entry-points yet
        # 'console_scripts': [
        #     'decorating = decorating.cli:main'
        # ]
    },
)
