from conans import CMake, ConanFile, tools


class DConan(ConanFile):
    name = "demod"
    python_requires = "disroopbase/0.1@disroop/development"
    python_requires_extend = "disroopbase.Base"

    requires = "democ/0.1@disroop/development"
