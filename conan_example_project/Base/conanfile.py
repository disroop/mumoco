from conans import CMake, ConanFile, tools


class Base(object):
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt", "test/*"

    def source(self):
        self.output.info("Disroop Base run: source")

    def build(self):
        self.output.info("Disroop Base run: build")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        self.output.info("Disroop Base run: package")
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.output.info("Disroop Base run: package_info")
        self.cpp_info.libs = tools.collect_libs(self)

    def build_requirements(self):
        self.output.info("Disroop Base run: requirements")
        self.build_requires("gtest/1.10.0", force_host_context=True)
        self.build_requires("cpputest/4.0", force_host_context=True)

    def package_info(self):
        self.output.info("Disroop Base run: package_info")
        self.output.info("Disroop Base run: package_info")
        collect_libs = tools.collect_libs(self)
        self.output.info(f"Disroop Base run: collect_libs {collect_libs}")
        self.cpp_info.libs = collect_libs


class DisroopBase(ConanFile):
    name = "disroopbase"
    version = "0.1"
