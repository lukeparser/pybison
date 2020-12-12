"""
Builds bison python module
"""
import codecs
import os
import re
import sys
import fnmatch
from os.path import join
from setuptools import find_packages, setup


###################################################################
#                             META DATA                           #
###################################################################

NAME = "pybison"
DESCRIPTION = "Python bindings for bison/flex parser engine"
META_PATH = os.path.join("src", "bison", "__init__.py")
PACKAGES = find_packages(where="src")
KEYWORDS = []
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    'Operating System :: Unix',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: C',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing'
]
INSTALL_REQUIRES = [
    # "Cython",
    "six",
    "setuptools"
]
SETUP_REQUIRES = [
    # 'Cython'
]
PACKAGE_DATA = [
    "src/bison/c/bison_callback.c",
    "src/bison/c/bison_callback.h",
    "src/bison/c/bisondynlib.h"
]
SCRIPTS = ['utils/bison2py']


###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


# package_data depending on system
if sys.platform == 'win32':
    libs = []
    extra_link_args = ['/debug', '/Zi']
    bisondynlibModule = 'src/bison/c/bisondynlib-win32.c'
    extra_compile_args = ['/Od', '/Zi', '-D__builtin_expect(a,b)=(a)', '/DCYTHON_TRACE=1']
    for root, dirs, files in os.walk('src/bison/winflexbison'):
        PACKAGE_DATA.extend(join(root.replace('src/bison/', ''), f) for f in files)

elif sys.platform.startswith('linux'):
    libs = ['dl']
    extra_link_args = []
    extra_compile_args = []  # ['-DCYTHON_TRACE=1']
    bisondynlibModule = 'src/bison/c/bisondynlib-linux.c'

elif sys.platform.startswith('darwin'):
    libs = ['dl']
    extra_link_args = []
    extra_compile_args = []
    bisondynlibModule = 'src/bison/c/bisondynlib-linux.c'
    from distutils import sysconfig
    v = sysconfig.get_config_vars()
    v['LDSHARED'] = v['LDSHARED'].replace('-bundle', '-dynamiclib')

else:
    print('Sorry, your platform is not supported.')
    sys.exit(1)

PACKAGE_DATA.append(bisondynlibModule)

PY_MODULES = set()
for file_root, dir_names, filenames in os.walk('src'):
    for filename in fnmatch.filter(filenames, '*.py'):
        PY_MODULES |= {file_root}
        break

# cython
SOURCES = [
    'src/bison/cython/bison_.pyx',
    'src/bison/c/bison_callback.c',
    bisondynlibModule
]

extra_compile_args = []
extra_link_args = []
define_macros = []

# compile with cython if available
try:
    from Cython.Distutils import build_ext
    from Cython.Distutils.extension import Extension
    cmd_class = {'build_ext': build_ext}
    cython_args = {'cython_compile_time_env': {"PY3": sys.version_info.major >= 3}}
except ImportError:
    from setuptools import Extension
    print('Cython does not appear to be installed.  Attempting to use pre-made cpp file...')
    cmd_class = {}
    cython_args = {}
    SOURCES = [s.replace(".pyx", ".c") for s in SOURCES]


ext_modules = [
    Extension(
        'bison.bison_',
        sources=SOURCES,
        extra_compile_args=extra_compile_args,
        libraries=libs,
        extra_link_args=extra_link_args,
        **cython_args
    )
]


if __name__ == "__main__":
    setup(
        name=NAME,
        description=DESCRIPTION,
        author=find_meta("author"),
        maintainer=find_meta("maintainer"),
        license=find_meta("license"),
        url=find_meta("uri"),
        version=find_meta("version"),
        keywords=KEYWORDS,
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        package_dir={"": "src"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        setup_requires=SETUP_REQUIRES,
        # from old setup
        cmdclass=cmd_class,
        ext_modules=ext_modules,
        py_modules=PY_MODULES,
        scripts=SCRIPTS,
        package_data={'bison': PACKAGE_DATA},
    )
