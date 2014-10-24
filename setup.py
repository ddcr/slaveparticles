# -*- coding: utf-8 -*-
"""
@author: Óscar Nájera
Installing packages on Slave Particles Mean Field Theories
"""
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    """Test class to do test coverage analysis"""
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--cov-report', 'term-missing', '--cov', 'slavespins', 'tests/']
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name = "Slave Particles",
    version = "0.2",
    packages = find_packages(),
    author = "Óscar Nájera",
    author_email='najera.oscar@gmail.com',

    install_requires=['numpy', 'scipy', 'Sphinx', 'matplotlib'],

    tests_require=['pytest', 'pytest-cov'],
    cmdclass={'test': PyTest},
)
