cmake_minimum_required(VERSION 3.16)

project(solution CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(${PROJECT_NAME} solution.cpp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS) # introduce targets that conan generates

target_link_libraries(${PROJECT_NAME} CONAN_PKG::fmt)
target_link_libraries(${PROJECT_NAME} CONAN_PKG::range-v3)
