# -*- coding: utf-8 -*-

import os
import subprocess  # nosec
import sys

from setuptools import setup

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

module_name = 'walrus'
version = subprocess.check_output([sys.executable,  # nosec
                                   os.path.join('scripts', 'find_version.py')],
                                  universal_newlines=True).strip()

setup(
    name='george-walrus',
    version=version,
    description='Backport compiler for Python 3.8 assignment expressions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/george-kuanli-peng/walrus',
    # author='Jarry Shaw',
    # author_email='jarryshaw@icloud.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    keywords=['walrus operator', 'assignment expression', 'back-port compiler'],
    py_modules=[module_name],
    python_requires='>=3.4',
    install_requires=[
        'parso>=0.6.0',         # universal AST support
        'tbtrim>=0.2.1',        # traceback trim support
        'bpc-f2format',         # bpc-f2format
        'bpc-utils~=0.10.0',    # utility library
        'typing;python_version<"3.5"',
        'typing_extensions',
    ],
    extras_require={
        'lint': [
            'flake8',
            'pylint',
            'mypy',
            'bandit>=1.6.3',
            'vermin>=1.1.0',
            'colorlabels>=0.7.0',
            'parso>=0.8.0',
        ],
        'test': [
            'pytest>=4.5.0',
            'pytest-doctestplus>=0.5.0',
            'coverage',
        ],
        'docs': [
            'Sphinx',
            'sphinx-autodoc-typehints',
            'sphinxemoji',
        ],
    },
    entry_points={
        'console_scripts': [
            'walrus = walrus:main',
        ]
    },
)
