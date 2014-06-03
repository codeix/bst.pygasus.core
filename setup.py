from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='bb.extjs.core',
      version=version,
      description="Python Framework for ExtJs",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bb', 'bb.extjs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'bb.extjs.wsgi',
          'bb.extjs.resources',
          'bb.extjs.scaffolding',
          'js.extjs',
          'martian',
          'grokcore.component',
          'zope.interface',
          'zope.schema',
          'Genshi'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )