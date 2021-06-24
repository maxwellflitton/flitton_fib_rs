#!/usr/bin/env python

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rust_messaging",
    version="0.1",
    rust_extensions=[RustExtension(".flitton_fib_rs.flitton_fib_rs", binding=Binding.PyO3)],
    packages=["flitton_fib_rs"],
    # rust extensions are not zip safe, just like C-extensions.
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
        ],
    zip_safe=False,
)
