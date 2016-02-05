#!/usr/bin/env python

from setuptools import setup, find_packages
import lifecellapi

setup(name='pylifecellapi',
      version=lifecellapi.__version__,
      description='Python Lifecell API library',
      author='Alexander R',
      author_email='work@myrfid.pp.ua',
      url='https://github.com/sash13/pylifecellapi',
      license='MIT',
      packages=find_packages(),
      classifiers=[
      		"Development Status :: 2 - Pre-Alpha",
      		"Environment :: Plugins",
      		"Intended Audience :: Developers",
      		"Programming Language :: Python",
      		"Programming Language :: Python :: 2",
      		"Programming Language :: Python :: 2.5",
      		"Programming Language :: Python :: 2.6",
      		"Programming Language :: Python :: 2.7",
      		"Programming Language :: Python :: 3",
      		"Topic :: Software Development :: Libraries :: Python Modules"
      ],
      install_requires=[
      	'requests',
      	'xmltodict'
      ]
     )