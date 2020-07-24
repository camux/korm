#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'asyncpg',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='korm',
    version='0.0.1',
    description="Killer ORM is lightweight ORM for asyncpg",
    long_description=readme + '\n\n' + history,
    author="Oscar Alvarez",
    author_email='gerente@presik.com',
    url='https://github.com/camux/korm',
    packages=find_packages(),
    package_dir={'korm': 'korm'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='korm',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
