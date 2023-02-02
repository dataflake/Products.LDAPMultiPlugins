##############################################################################
#
# Copyright (c) 2005-2023 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os

from setuptools import find_packages
from setuptools import setup


def read(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as fp:
        return fp.read()


setup(name='Products.LDAPMultiPlugins',
      version='5.1.dev0',
      description='LDAP-backed plugins for the Zope PluggableAuthService',
      long_description=read('README.rst'),
      classifiers=[
        "Development Status :: 6 - Mature",
        "Framework :: Zope",
        "Framework :: Zope :: 5",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development",
        "Topic :: System :: Systems Administration ::"
        " Authentication/Directory :: LDAP",
        ],
      keywords='web application server zope ldap',
      author="Jens Vagelpohl and contributors",
      author_email="jens@dataflake.org",
      url='https://github.com/dataflake/Products.LDAPMultiPlugins',
      project_urls={
        'Issue Tracker': ('https://github.com/dataflake/'
                          'Products.LDAPMultiPlugins/issues'),
        'Sources': 'https://github.com/dataflake/Products.LDAPMultiPlugins',
      },
      license="ZPL 2.1",
      packages=find_packages('src'),
      include_package_data=True,
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      zip_safe=False,
      python_requires='>=3.7',
      install_requires=[
        'setuptools',
        'Zope >= 5',
        'Products.LDAPUserFolder',
        'Products.PluggableAuthService',
        ],
      extras_require={
        'exportimport': ['Products.GenericSetup >= 2.0b1'],
        'docs': [
          'Sphinx',
          'sphinx_rtd_theme',
          'repoze.sphinx.autointerface',
          'pkginfo'
        ],
      },
      entry_points="""
      [zope2.initialize]
      Products.LDAPMultiPlugins = Products.LDAPMultiPlugins:initialize
      """
      )
