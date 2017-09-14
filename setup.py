import os

from setuptools import find_packages, setup

setup(name='cutandpaste',
      version='0.3.0',
      description=("Supercharged split and join operations, inspired on the eponymous R functions."),
      #long_description=open('README.rst').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                    ],
      keywords='',
      author='Stijn Debrouwere',
      author_email='stijn@debrouwere.org',
      download_url='http://www.github.com/debrouwere/python-paste/tarball/master',
      license='ISC',
      #test_suite='paste.tests',
      packages=find_packages(),
      )
