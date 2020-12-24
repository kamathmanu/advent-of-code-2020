cmake_minimum_required(VERSION 3.15)

project(solution CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(${PROJECT_NAME} solution.cpp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

target_link_libraries(${PROJECT_NAME} CONAN_PKG::fmt)
target_link_libraries(${PROJECT_NAME} CONAN_PKG::range-v3)
