from conans import ConanFile, CMake, tools


class CPortLibConan(ConanFile):
    name = "cportlib"
    version = "1.0"
    author = "Orlin Hristov, orlin dot hristov at gmail dot com"
    url = "https://github.com/orlinhristov/cportlib-conan"
    description = "A header-only C++ library that manages parallel task processing in concurrent environment. It " \
                  "provides mechanism for asynchronous execution of multiple task handlers and invocation " \
                  "of callback handlers after task completion. "
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"

    def source(self):
        self.run("git clone https://github.com/orlinhristov/cportlib.git")
        self.run("cd cportlib && git checkout v1.0")

    def package(self):
        self.copy("cport*", dst="include", src="cportlib")

    def package_id(self):
        self.info.header_only()

