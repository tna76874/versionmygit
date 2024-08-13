#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

from versionmygit.version import *
package_version = GitVersion('.', minor=0, major=0, minor_commit = '174e2e64a1e1dbff53dae333fbb1697f79d78a03')

setup(
    name='versionmygit',
    version=package_version._get_semantic_version(),
    description='versionmygit',
    url='https://github.com/tna76874/versionmygit',
    author='lmh',
    author_email='',
    license='BSD 2-clause',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyYAML",
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires = ">=3.6",
    entry_points={
        "console_scripts": [
            "versionmygit = versionmygit.cli:main",
        ],
    },
    )
