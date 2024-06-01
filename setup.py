from setuptools import setup, find_packages
import os

setup_py_dir = os.path.dirname(os.path.abspath(__file__))
requirements_file = os.path.join(setup_py_dir, 'requirements.txt')

with open(requirements_file) as f:
    requirements = f.read().splitlines()

setup(
    name='viessmann-gridbox-connector',
    version='1.0.3',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        requirements,
    ],
)
