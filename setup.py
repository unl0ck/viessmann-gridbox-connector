from setuptools import setup, find_packages

setup(
    name='viessmann-gridbox-connector',
    version='1.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
