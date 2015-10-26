
"""A module to manage your deep learning networks.
Build on top of Lasagne 
See:
https://github.com/corentinmarek/
"""
# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name='LasagneEngine',
    version='0.0.1',
    description='A Deep Learning engine to manage training sessions on top of Lasagne',
    url='https://github.com/corentinmarek/LasagneEngine',
    author='corentin marek',
    license='MIT',
    keywords='lasagne',
    packages=['lasagneEngine'],
    install_requires=[
          'theano',
          'lasagne',
    ],
    zip_safe=False
)