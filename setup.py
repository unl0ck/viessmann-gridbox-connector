from setuptools import setup, find_packages
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='viessmann-gridbox-connector',
    version='1.2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=required,
)
