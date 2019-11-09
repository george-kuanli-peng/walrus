# walrus

[![PyPI - Downloads](https://pepy.tech/badge/python-walrus)](https://pepy.tech/count/python-walrus)
[![PyPI - Version](https://img.shields.io/pypi/v/python-walrus.svg)](https://pypi.org/project/python-walrus)
[![PyPI - Format](https://img.shields.io/pypi/format/python-walrus.svg)](https://pypi.org/project/python-walrus)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-walrus.svg)](https://pypi.org/project/python-walrus)

[![Travis CI - Status](https://img.shields.io/travis/JarryShaw/walrus.svg)](https://travis-ci.org/JarryShaw/walrus)
[![Codecov - Coverage](https://codecov.io/gh/JarryShaw/walrus/branch/master/graph/badge.svg)](https://codecov.io/gh/JarryShaw/walrus)
![License](https://img.shields.io/github/license/jarryshaw/walrus.svg)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

 > Write *assignment expressions* in Python 3.8 flavour, and let `walrus` worry about back-port issues :beer:

&emsp; Since [PEP 572](https://www.python.org/dev/peps/pep-0572/), Python introduced *assignment expressions*
syntax in version __3.8__. For those who wish to use *assignment expressions* in their codes, `walrus` provides an
intelligent, yet imperfect, solution of a **backport compiler** by replacing *assignment expressions* syntax with
old-fashioned assignment-then-conditional syntax, which guarantees you to always write *assignment expressions* in
Python 3.8 flavour then compile for compatibility later.

**NB**: `walrus` currently can only support *assignment expressions* used in `if` statements.

## Installation

> Note that `walrus` only supports Python versions __since 3.3__ 🐍

&emsp; For macOS users, `walrus` is now available through [Homebrew](https://brew.sh):

```sh
brew tap jarryshaw/tap
brew install walrus
# or simply, a one-liner
brew install jarryshaw/tap/walrus
```

&emsp; Simply run the following to install the current version from PyPI:

```sh
pip install python-walrus
```

&emsp; Or install the latest version from the git repository:

```sh
git clone https://github.com/JarryShaw/walrus.git
cd walrus
pip install -e .
# and to update at any time
git pull
```

## Basic Usage

### CLI

&emsp; It is fairly straightforward to use `walrus`:

 > context in `${...}` changes dynamically according to runtime environment

```man
usage: walrus [options] <python source files and folders...>

Back-port compiler for Python 3.8 assignment expressions.

positional arguments:
  SOURCE                python source files and folders to be converted (${CWD})

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -q, --quiet           run in quiet mode

archive options:
  duplicate original files in case there's any issue

  -n, --no-archive      do not archive original files
  -p PATH, --archive-path PATH
                        path to archive original files (${CWD}/archive)

convert options:
  compatibility configuration for none-unicode files

  -c CODING, --encoding CODING
                        encoding to open source files (${LOCALE_ENCODING})
  -v VERSION, --python VERSION
                        convert against Python version (${LATEST_VERSION})
  -s SEP, --linesep SEP
                        line separator to process source files (${OS_LINESEP})
  -nl, --no-linting     do not lint converted codes
```

&emsp; `walrus` will read then convert all *assignment expressions* syntax in every Python
file under this path. In case there might be some problems with the conversion, `walrus` will
duplicate all original files it is to modify into `archive` directory ahead of the process,
if `-n` not set.

&emsp; Besides, to keep consistency of API to users, `walrus` ships with a *decorator* for
such functions to check assignment expressions at runtime, if `-nl` not set.

## Developer Reference

### Environments

`walrus` currently supports three environment arguments:

- `WALRUS_QUIET` -- run in quiet mode (same as `--quiet` option in CLI)
- `WALRUS_VERSION` -- convert against Python version (same as `--python` option in CLI)
- `WALRUS_ENCODING` -- encoding to open source files (same as `--encoding` option in CLI)
- `WALRUS_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
- `WALRUS_LINTING` -- lint converted codes (same as `--linting` option in CLI)

### APIs

#### `walrus` -- wrapper works for conversion

```python
walrus(filename)
```

Args:

- `filename` -- `str`, file to be converted

Envs:

- `WALRUS_QUIET` -- run in quiet mode (same as `--quiet` option in CLI)
- `WALRUS_ENCODING` -- encoding to open source files (same as `--encoding` option in CLI)
- `WALRUS_VERSION`-- convert against Python version (same as `--python` option in CLI)
- `WALRUS_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
- `WALRUS_LINTING` -- lint converted codes (same as `--linting` option in CLI)

Raises:

- `ConvertError `-- when `parso.ParserSyntaxError` raised

#### `convert` -- the main conversion process

```python
convert(string, source='<unknown>')
```

Args:

- `string` -- `str`, context to be converted
- `source` -- `str`, source of the context

Envs:

- `WALRUS_VERSION`-- convert against Python version (same as `--python` option in CLI)
- `WALRUS_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
- `WALRUS_LINTING` -- lint converted codes (same as `--linting` option in CLI)

Returns:

- `str` -- converted string

Raises:

- `ConvertError `-- when `parso.ParserSyntaxError` raised

#### `ConvertError` -- `walrus` internal exception

```python
class ConvertError(SyntaxError):
    pass
```

## Test

&emsp; See [`test.py`](https://github.com/JarryShaw/walrus/blob/master/scripts/test.py).

## Contribution

&emsp; Contributions are very welcome, especially fixing bugs and providing test cases.
Note that code must remain valid and reasonable.

## See Also

- [`babel`](https://github.com/jarryshaw/babel)
- [`f2format`](https://github.com/jarryshaw/f2format)
- [`poseur`](https://github.com/jarryshaw/poseur)
- [`vermin`](https://github.com/netromdk/vermin)
