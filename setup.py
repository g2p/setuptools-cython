#!/usr/bin/env python
# vim: set fileencoding=utf-8 sw=4 ts=4 et :
from setuptools import setup

"""
Usage:
Use setuptools and put cython_setuptools in your setup_requires.
Also paste the monkey-patch reversal below.

setuptools DWIM monkey-patch madness
http://mail.python.org/pipermail/distutils-sig/2007-September/thread.html#8204

No way but to unpatch, by copying the following code in individual setup scripts:

import sys
if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__

Complete example:

#!/usr/bin/env python

from setuptools import setup
from distutils.extension import Extension

# setuptools DWIM monkey-patch madness
# http://mail.python.org/pipermail/distutils-sig/2007-September/thread.html#8204
import sys
if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__

setup(
        name = "example",
        version = "0.1",
        description="cython_setuptools example",
        setup_requires=[
            'cython_setuptools',
            ],
        ext_modules=[
            Extension('example', ['example.pyx']),
            ],
        )

"""

setup(
        name='cython-setuptools',
        version='0.1',
        author='Gabriel de Perthuis',
        author_email='g2p.code@gmail.com',
        description='Cython setuptools integration',
        license='http://www.gnu.org/licenses/gpl-2.0.html',
        long_description='Allows using Cython in setuptools projects\n'
        +'by putting cython-setuptools in your setup_requires.\n',
        py_modules=['cython_setuptools', ],
        install_requires=[
            'Cython',
            ],
        entry_points={
            # Can't override build_ext with an entry point.
            # This means we can't collide on ext_modules either.
            # So we create a cython_ext_modules to hold pyx files.

            # There's still a problem: our extra command isn't invoked automatically.
            # Even though it appears to be a subcommand of build.

            # The only way out would be an alias, and that means getting rid
            # of our parameter. And it doesn't work either, aliases are only expanded
            # when they are on the command line.

            # This means distutils integration using distutils extension points
            # is an impossibility.
            # But we have our own entry point!
            # Take advantage of the parameter validation.
            # In fact, we can write a 'validation' for the original ext_modules
            # parameter.

            'distutils.commands': [
                #'build_cython = cython_setuptools:build_cython',
                ],
            'distutils.setup_keywords': [
                'ext_modules = cython_setuptools:ext_modules_hack',
                #'cython_ext_modules = cython_setuptools:validate_cython_ext_modules',
                ],

            },
        classifiers=[
            'Framework :: Setuptools Plugin',
            'Topic :: Software Development :: Build Tools',
            ],
        )

