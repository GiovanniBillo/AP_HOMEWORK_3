cmake_minimum_required(VERSION 3.22)
project(main_interpolation LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
endif()

if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
    message(STATUS "building DEBUG version")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g -Wall -Wpedantic -Wextra")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR}) 
else() 
    message(STATUS "building RELEASE version (default)")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -Werror")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR})
endif()

include(FetchContent)

# Fetch the ALGLIB library
FetchContent_Declare(
   alglib 
    GIT_REPOSITORY https://github.com/hjkuijf/ALGLIB
    # GIT_TAG v1.18.0 # Uncomment to use a specific version or tag
)

# Ensure the ALGLIB library is downloaded and built
FetchContent_MakeAvailable(alglib)

# Fetch the pybind11 library
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.11.1  # Specify a stable version; change as needed
)

# Ensure pybind11 is downloaded and available
FetchContent_MakeAvailable(pybind11)

# find_package(pybind11 REQUIRED)
# include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})
# pybind11_add_module(example example.cpp)

add_library(Interpolation STATIC 
    InterpolateWrapper.hpp
    helpers.hpp
    helpers.cpp
)

add_library(InterpolationPython 
    InterpolateWrapper.hpp
    bindings.cpp
    helpers.hpp
    helpers.cpp
)

# Add the executable
add_executable(main_interpolation main.cpp)

# If ALGLIB is header-only or doesn't provide a library target:
# target_include_directories(main_interpolation PRIVATE ${alglib_SOURCE_DIR}/src)
# target_include_directories(InterpolationPython PRIVATE ${alglib_SOURCE_DIR}/src)

# If ALGLIB provides a CMake target (for example, alglib::alglib), link it
# Uncomment the line below if a proper CMake target is available
# target_link_libraries(main PRIVATE alglib::alglib)

# Manually add the source files if ALGLIB doesn't provide a CMake target
file(GLOB ALGLIB_SRC 
    ${alglib_SOURCE_DIR}/src/*.cpp
)

# Link the source files to your project if ALGLIB doesn't have a CMake target
target_sources(main_interpolation PRIVATE ${ALGLIB_SRC})
target_sources(InterpolationPython PRIVATE ${ALGLIB_SRC})

# Message to confirm the source directory of ALGLIB
message(STATUS "ALGLIB source dir: ${alglib_SOURCE_DIR}")

