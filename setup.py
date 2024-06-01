from setuptools import setup, find_packages

setup(
    name='viessmann-gridbox-connector',
    version='1.3.8',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests'
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
