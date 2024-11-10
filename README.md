[![The pybison logo.](doc/pybison.svg)](https://github.com/lukeparser/pybison)

# PyBison
[![python versions](https://img.shields.io/pypi/pyversions/pybison)](https://pypi.org/project/pybison)
[![wheel](https://img.shields.io/pypi/wheel/pybison)](https://pypi.org/project/pybison/#files)
[![CI build](https://github.com/lukeparser/pybison/actions/workflows/master_trigger.yml/badge.svg)](https://github.com/lukeparser/pybison/actions/workflows/master_trigger.yml)

Welcome to PyBison!  
Bringing **GNU Bison/Flex**'s raw speed and power to Python  

## What is PyBison?
PyBison is a framework which effectively 'wraps' **Bison** and **Flex into** a Python class structure.

You define a parser class, define tokens and precedences as attributes, and parse targets as methods with rules in the docstrings, then instantiate and run.

Black Magick happens in the background, whereupon you get callbacks each time `yyparse()` resolves a parse target.

## Install

Now, **install pybison** with:
```bash
pip install pybison
```

The following command will verify if the installation succeeded:

```bash
python -c "import bison"
```

## There are already parsers for Python. Why re-invent the wheel?

I looked at all the Python-based parsing frameworks.

IMO, the best one was **PLY** - a pure-python *lexx/yacc* implementation (which I have borrowed from heavily in designing PyBison's OO model).

But PLY suffers some major limitations:

- usage of 'named groups' regular expressions in the lexer creates a hard limit of 100 tokens - not enough to comfortably handle major languages
- pure-python implementation is a convenience, but incurs a cruel performance penalty
- the parser engine is SLR, not full LALR(1)

The other frameworks utilise a fiddly script syntax -

## How do I use this?

Refer to the [examples](https://github.com/lukeparser/pybison/tree/master/examples) and the [docs](https://github.com/lukeparser/pybison/tree/master/doc) for usage.

## Development
You will need:

- [Python](https://www.python.org/), with development headers and libraries
- [pip](https://pypi.org/project/pip/)
- [GNU bison](https://www.gnu.org/software/bison/)
- [flex](https://github.com/westes/flex)
- A standard C compiler and linker

We assume that Python, pip and a C compiler is already installed.

### Dependencies
First, install the dependencies `bison` and `flex`.

**Arch Linux**
```bash
sudo pacman -S bison flex
```
**Ubuntu**
```bash
sudo apt-get install bison flex
```

**Windows**

With [Chocolatey](https://community.chocolatey.org/), you can install the packages as follows:
```bash
choco install winflexbison3
```
Additionally, if a C compiler is needed, [mingw](https://osdn.net/projects/mingw/) can be installed with Chocolatey as well.
```bash
choco install mingw
```

### Debugging

See the short introduction into [debugging](debugging/README.md).

## Collaborators
- PyBison was designed and written by [David McNab <david@freenet.org.nz>](http://freenet.mcnabhosting.com/python/pybison/)
- [smvv](https://github.com/smvv)
- [habibutsu](https://github.com/habibutsu)
- [thisiscam](https://github.com/thisiscam)
- [eugeneai](https://github.com/eugenai)
- [csarn](https://github.com/csarn)
- [sbrodehl](https://github.com/sbrodehl)
- [da-h](https://github.com/da-h)
