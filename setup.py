#!/usr/bin/env python

from setuptools import setup, find_packages

import os.path

# Evaluate version module without importing parsy, which could have undesirable
# effects.
version_file = os.path.join(os.path.dirname(__file__),
                            "src", "parsy", "version.py")
namespace = {}
exec(compile(open(version_file, "rb").read(), version_file, 'exec'),
     globals(), namespace)
version = namespace['__version__']

setup(
    name="parsy",
    version=version,
    description="easy-to-use parser combinators",
    author="Jeanine Adkisson",
    url="https://github.com/jneen/parsy",
    author_email="jneen at jneen dot net (humans only, please)",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="parser parsing monad combinators",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
