from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="FuncPy",
    version="0.0.1",
    author="GitNov66 company",
    author_email="kivy156@gmail.com",
    description='''s library is a collection of activation functions for a neural network.
This library contains the following functions
binary_step
sigmoid
tanf
ReLU
softplus
leaky_ReLU''',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/FuncPy/homepage",
    packages=find_packages(),
    install_requires=requirements_dev,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD 3-Clause License",
    ],
)
