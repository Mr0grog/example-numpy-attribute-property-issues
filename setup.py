from setuptools import setup, find_packages


setup(
    name='example_module',
    version='1.0.0',
    description="Example of issues with numpydoc attributes and properties",
    author="Rob Brackett",
    python_requires='>=3.6.0',
    packages=find_packages(exclude=['docs']),
    install_requires=[
        'sphinx ~=3.2.1',
        'numpydoc ~=1.1.0'
    ],
    license="BSD (3-clause)",
)
