from setuptools import setup, find_packages
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='viessmann-gridbox-connector',
    version='1.3.3',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['requests'],
    install_requires=required,
)
