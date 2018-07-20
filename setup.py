from setuptools import setup, find_packages
from os import path


setup(
    name='pyunoservice',
    version='0.1.0'
    description='Python Uno Service wrapper',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().strip().split()
)
