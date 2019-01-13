cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup()

add_definitions(-DCPORT_HEADER_ONLY_LIB)

add_executable(example example.cpp)
