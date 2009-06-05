# vim: set fileencoding=utf-8 sw=4 ts=4 et :
import Cython.Distutils.build_ext

def validate_cython_ext_modules(dist, attr, value):
    build_cython(dist).check_extensions_list(value)

class build_cython(Cython.Distutils.build_ext, object):
    def initialize_options(self):
        super(build_cython, self).initialize_options()

    def finalize_options(self):
        super(build_cython, self).finalize_options()
        self.extensions = self.distribution.cython_ext_modules

