from distutils.core import setup, Extension

scryptSquared_module = Extension('scryptSquared',
                               sources = ['scryptmodule.c',
                                          'scrypt.c'],
                               include_dirs=['.'])

setup (name = 'scryptSquared',
       version = '1.0',
	   description = 'Bindings for scrypt proof of work used by Verium',
	   ext_modules = [scryptSquared_module])
