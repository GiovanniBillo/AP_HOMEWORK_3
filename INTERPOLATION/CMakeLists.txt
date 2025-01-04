cmake_minimum_required(VERSION 3.22)
project(main_interpolation LANGUAGES CXX)

# Set CMake build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

# Debug or Release configuration
if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
    message(STATUS "Building DEBUG version")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g -Wall -Wpedantic -Wextra -fPIC")
else()
    message(STATUS "Building RELEASE version (default)")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -fPIC")
endif()

# Set C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Add ALGLIB subdirectory
add_subdirectory(external/alglib-cpp)

# Define ALGLIB include directory
set(ALGLIB_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/external/alglib-cpp")

# Debugging messages
message(STATUS "ALGLIB_INCLUDE_DIR: ${ALGLIB_INCLUDE_DIR}")

# Find pybind11
find_package(pybind11 REQUIRED)

# Add InterpolateWrapper target
pybind11_add_module(InterpolateWrapper src/bindings.cpp)
target_include_directories(InterpolateWrapper PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/include 
    ${ALGLIB_INCLUDE_DIR}
    ${pybind11_INCLUDE_DIRS}
)
target_link_libraries(InterpolateWrapper PRIVATE alglib)

# # Set library output directory
# set_target_properties(InterpolateWrapper PROPERTIES
#     LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}
# )

# Add main_interpolation target
add_executable(main_interpolation src/main.cpp)
target_include_directories(main_interpolation PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/include 
    ${ALGLIB_INCLUDE_DIR}
)
target_link_libraries(main_interpolation PRIVATE alglib)


