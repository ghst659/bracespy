#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools
setuptools.setup(
    name='bracespy',
    version='0.1',
    description='Brace expander',
    long_description='Brace expander',
    url='https://github.com/ghst659/bracespy.git',
    license='GPLv3',
    keywords='python parse',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: GPLv3'
    ],
    author='ghst659',
    author_email='',
    packages=setuptools.find_packages(),
    include_package_data=True,           # see MANIFEST.in on globs of files to include, e.g. json files
    scripts=[],
    install_requires=[]         # packages from http://pypi.python.org
)
