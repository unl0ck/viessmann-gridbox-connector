from setuptools import setup, find_packages

setup(
    name='viessmann-gridbox-connector',
    version='1.5.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests',
        'authlib'
    ],
    package_data={
        'viessmann_gridbox_connector': ['config.json'],
    },
    entry_points={
        'console_scripts': [
            'viessmann=viessmann_gridbox_connector.cli:main',
        ],
    },
)
