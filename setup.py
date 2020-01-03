#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='hf-protobuffers',
    version='1.0.0',
    description='Hypefactors protocol buffers for Python',
    author='Magnus Stahl',
    author_email='msta@hypefactors.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test_client.py"]),
    install_requires=['protobuf==3.6.1']
)
