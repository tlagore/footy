# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(  
    name='foot_scraper',
    version='0.1.0',
    description='stat scraper for football statistics',
    long_description=readme,
    author='Tyrone Lagore, Johnny Simmonds',
    author_email='SimmondsJohnny@gmail.com,tyronelagore@gmail.com',
    url='https://github.com/tlagore/foot_scraper',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)