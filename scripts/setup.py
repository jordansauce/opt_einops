"""
This is a fake script, it is not used.
Seems github does not count contributions unless you have a setup.py
"""
__author__ = "Alex Rogozhnikov"

from setuptools import setup

setup(
    name="opt_einops",
    version="0.7.0",
    description="Optimized convenient tensor manipulations and contractions (combining einiops with opt_einsum)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jordansauce/opt_einops/tree/master",
    author="Jordan Taylor",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="deep learning, neural networks, tensor manipulation, machine learning, "
    "scientific computations, opt_einops",
    install_requires=[
        "opt_einsum"
    ],
)
