#!/usr/bin/env python3
# vim:fileencoding=utf-8 tabstop=4 shiftwidth=4 softtabstop=4

import os
from setuptools import find_packages, setup


ROOT = os.path.abspath(os.path.dirname(__file__))


def get_readme_file_as_string():
    """Read in the README file and return as a string."""
    with open(os.path.join(ROOT, 'README.rst'), encoding='utf-8') as f:
        body = f.read()
    return body


setup(
    name='gnudteith',
    version='0.0.1',
    url='https://odo.stooj.org/goodteith/gnudteith',
    licence='GPL',
    author='Stoo Johnston',
    author_email='stoo@goodteith.scot',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6, <4',
)
