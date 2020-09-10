#!/usr/bin/env python

"""setup script for blizzardapy."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author="Drew Frezell",
    author_email='acorn@eldertribu.nl',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Blizzard API python wrapper",
    entry_points={
        'console_scripts': [
            'blizzardapy=blizzardapy.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='blizzardapy',
    name='blizzardapy',
    packages=find_packages(include=['blizzardapy', 'blizzardapy.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eldertribunal/blizzardapy',
    version='0.1.0',
    zip_safe=False,
)