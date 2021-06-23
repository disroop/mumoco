from conans import CMake, ConanFile, tools


class CConan(ConanFile):
    name = "democ"
    python_requires = "disroopbase/0.1@disroop/development"
    python_requires_extend = "disroopbase.Base"

    requires = "demob/0.1@disroop/development"
