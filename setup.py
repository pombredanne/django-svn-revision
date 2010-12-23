from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='svn-revision',
    version=version,
    description="Adds a template tag to get the current svn revision.",
    author='Sean Auriti, David Napolitan and Alexander Interactive, Inc.',
    url='http://github.com/ff0000/django-svn-revision',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    keywords='django, svn, subversion',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
	]
)


