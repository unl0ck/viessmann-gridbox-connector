from setuptools import setup, find_packages

setup(
    name='viessmann-gridbox-connector',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
