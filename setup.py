from setuptools import setup, find_packages


setup(
    name='example_module',
    version='1.0.0',
    description="Example of issues with numpydoc attributes and properties",
    author="Rob Brackett",
    python_requires='>=3.11.0',
    packages=find_packages(exclude=['docs']),
    install_requires=[
        'sphinx ~=9.1.0',
        'numpydoc ~=1.10.0'
    ],
    license="BSD (3-clause)",
)
