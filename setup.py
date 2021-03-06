# setup.py
# Copyright (C) 2012 the ColanderAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of ColanderAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import sys
from setuptools import setup, find_packages

version = '0.3.3.dev1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

tests_require = []

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    # In Python < 2.7 use unittest2.
    tests_require.append('unittest2')


setup(name='ColanderAlchemy',
      version=version,
      description="Autogenerate Colander schemas based on SQLAlchemy "
                  "models.",
      long_description=README + '\n\n' + CHANGES,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Topic :: Database'],
      keywords='serialize deserialize validate schema validation '
               'colander sqlalchemy',
      author='Stefano Fontanelli',
      author_email='s.fontanelli@asidev.com',
      url='https://github.com/stefanofontanelli/ColanderAlchemy',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=['colander >= 1.0b1',
                        'SQLAlchemy >= 0.8dev'],
      tests_require=tests_require,
      test_suite='tests',
      )
