# setup.py
from setuptools import setup, find_packages

setup(
    name='example_pkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # add any dependencies here
    ],
    package_data={
        'example_pkg': ['data/config.json'],
    },
)
