from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'

setup(
    name='lazycode',
    version=VERSION,
    description='Lazily code common tedious code',
    long_description='file: README.md',
    url='https://github.com/ikeman32/lazycode-base',
    author='David H Isakson II',
    author_email='david.isakson.ii@gmail.com',
    packages='',
    install_requires='none',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
