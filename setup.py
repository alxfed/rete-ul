# -*- coding: utf-8 -*-
"""Setup with C99
"""
try:
    from setuptools import setup, Extension
    from setuptools.command import install_lib as _install_lib
except ImportError:
    print('Error. This Setup requires Setuptools')
from codecs import open
from os import path
from os import environ

environ['CFLAGS'] = '-std=c99 -D_GNU_SOURCE'

class install_lib(_install_lib.install_lib):
  def build(self):
    if not self.skip_build:
      if self.distribution.has_pure_modules():
        self.run_command('build_py')
        if self.distribution.has_c_libraries():
          self.run_command('build_clib')
        if self.distribution.has_ext_modules():
          self.run_command('build_ext')

rules_lib = ('rete_ul_engine_py', {'sources': ['src/rules/%s.c' % src for src in ('json', 'rete', 'state', 'events', 'regex')]})

rules = Extension('rules_ul_engine_py',
                  sources = ['src/rulespy/rules.c'],
                  include_dirs=['src/rules'])

this_dir = path.abspath(path.dirname(__file__)) + '/docs/py'
with open(path.join(this_dir, 'readme.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup (
    name = 'rete-ul',
    version = '0.0.1',
    description = 'C/Python RETE/UL Rules Engine',
    long_description=long_description,
    url='https://github.com/alxfed/rete-ul',
    author='Alex Fedotov',
    author_email='alex.fedotov@aol.com',
    license='MIT',
    classifiers=[
        'Operating System :: Linux',
        'Development Status :: Beta',
        'Intended Audience :: Humans',
        'Topic :: Software Development :: Libraries',
        'License :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='rules engine rete/ul with forward chaining and backward chaining',
    packages = ['rete-ul'],
    libraries = [rules_lib],
    ext_modules = [rules],
    # Override 'install_lib' command
    cmdclass={'install_lib': install_lib},
)