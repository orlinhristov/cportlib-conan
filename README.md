# Conan Package for cportlib
cport library package for conan.io

### Basic Setup

```sh
$ conan install cportlib/1.0@batoro/stable
```

### Project Setup
If you handle multiple dependencies in your project is better to add a *conanfile.txt*

```
[requires]
cportlib/1.0@batoro/stable

[generators]
txt
cmake
```

Complete the installation of requirements for your project running:

```sh
$ conan install .
```

Project setup installs the library and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.
