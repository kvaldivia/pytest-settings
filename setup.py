#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


requires = [
    'pytest>=5.3.5',
    'plaster_pastedeploy',
]

setup(
    name='pytest-settings',
    version='0.1.0',
    author='Kenny Valdivia',
    author_email='k_valdivia@gmx.com',
    maintainer='Kenny Valdivia',
    maintainer_email='k_valdivia@gmx.com',
    license='BSD-3',
    url='https://github.com/kvaldivia/pytest-settings',
    description="Access your configuration file's parsed settings from your tests",
    long_description=read('README.rst'),
    py_modules=['pytest_settings'],
    python_requires='>=3.6.9',
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'pytest11': [
            'settings = pytest_settings',
        ],
    },
)
