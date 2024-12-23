cmake_minimum_required(VERSION 3.22)
project(main_interpolation LANGUAGES CXX)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
endif()

if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
    message(STATUS "building DEBUG version")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g -Wall -Wpedantic -Wextra -fPIC")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR}) 
else() 
    message(STATUS "building RELEASE version (default)")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -Werror -FPIC")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR})
endif()
# Set C++ Standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include ALGLIB source files manually
add_subdirectory(external/alglib-cpp) # Include ALGLIB directory

find_package(pybind11 REQUIRED)
include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})

pybind11_add_module(InterpolateWrapper src/bindings.cpp)
target_link_libraries(InterpolateWrapper PRIVATE alglib)
target_include_directories(InterpolateWrapper PRIVATE ${CMAKE_SOURCE_DIR}/include) # explicitly add the include directory for the target library as well

# always place python library in the main directory ( to avoid having to set PYTHONPATH everytime)
set_target_properties(InterpolateWrapper PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}
)

include_directories(${CMAKE_SOURCE_DIR}/include)
# Add the main executable
add_executable(main_interpolation src/main.cpp)

# Include ALGLIB headers in the include path
target_include_directories(main_interpolation PRIVATE external/alglib/src)

# Link ALGLIB sources to the main executable
target_link_libraries(main_interpolation PRIVATE alglib)

# Debugging messages
message(STATUS "ALGLIB directory: ${CMAKE_SOURCE_DIR}/external/alglib")

# cmake_minimum_required(VERSION 3.22)
# project(main_interpolation LANGUAGES CXX)

# set(CMAKE_CXX_STANDARD 23)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)

# if(NOT CMAKE_BUILD_TYPE)
#     set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
# endif()

# if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
#     message(STATUS "building DEBUG version")
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g -Wall -Wpedantic -Wextra")
#     set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR}) 
# else() 
#     message(STATUS "building RELEASE version (default)")
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -Werror")
#     set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR})
# endif()

# include(FetchContent)

# # Fetch the ALGLIB library
# FetchContent_Declare(
#    alglib 
#     GIT_REPOSITORY https://github.com/hjkuijf/ALGLIB
#     # GIT_TAG v1.18.0 # Uncomment to use a specific version or tag
# )

# # Ensure the ALGLIB library is downloaded and built
# FetchContent_MakeAvailable(alglib)

# # Add the executable
# add_executable(main_interpolation src/main.cpp)
# include_directories(${CMAKE_SOURCE_DIR}/include)
# # Manually add the source files if ALGLIB doesn't provide a CMake target
# file(GLOB ALGLIB_SRC 
#     ${alglib_SOURCE_DIR}/src/*.cpp
# )

# # Link the source files to your project if ALGLIB doesn't have a CMake target
# target_sources(main_interpolation PRIVATE ${alglib_SOURCE_DIR})

# find_package(pybind11 REQUIRED)
# # find_package(alglib REQUIRED)
# include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})
# pybind11_add_module(InterpolateWrapper src/bindings.cpp)
# # target_link_libraries(InterpolateWrapper PRIVATE alglib::alglib)
# target_include_directories(InterpolateWrapper PRIVATE ${CMAKE_SOURCE_DIR}/include) # explicitly add the include directory for the target library as well


# # Message to confirm the source directory of ALGLIB
# message(STATUS "ALGLIB source dir: ${alglib_SOURCE_DIR}")

# cmake_minimum_required(VERSION 3.22)
# project(main_interpolation LANGUAGES CXX)

# # C++ Standard
# set(CMAKE_CXX_STANDARD 23)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)

# # Build Type
# if(NOT CMAKE_BUILD_TYPE)
#     set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
# endif()

# if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
#     message(STATUS "Building DEBUG version")
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g -Wall -Wpedantic -Wextra")
# else() 
#     message(STATUS "Building RELEASE version (default)")
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -Werror")
# endif()

# # Include FetchContent for ALGLIB
# include(FetchContent)

# # Fetch the ALGLIB library
# FetchContent_Declare(
#     alglib 
#     GIT_REPOSITORY https://github.com/hjkuijf/ALGLIB
# )

# # Ensure ALGLIB is downloaded
# FetchContent_MakeAvailable(alglib)

# # Include ALGLIB headers
# include_directories(${alglib_SOURCE_DIR}/src)

# # Find pybind11
# find_package(pybind11 REQUIRED)

# # Include directories for your project
# include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})
# include_directories(${CMAKE_SOURCE_DIR}/include)

# # Add ALGLIB sources manually if needed
# file(GLOB ALGLIB_SOURCES ${alglib_SOURCE_DIR}/src/*.cpp)

# # Add the executable
# add_executable(main_interpolation src/main.cpp)
# target_sources(main_interpolation PRIVATE ${ALGLIB_SOURCES})
# # target_link_libraries(main_interpolation PRIVATE alglib)

# # Add the pybind11 module
# pybind11_add_module(InterpolateWrapper src/bindings.cpp)
# target_sources(InterpolateWrapper PRIVATE ${ALGLIB_SOURCES})
# target_include_directories(InterpolateWrapper PRIVATE ${CMAKE_SOURCE_DIR}/include)
# # target_link_libraries(InterpolateWrapper PRIVATE alglib)

# # Debugging message
# message(STATUS "ALGLIB source dir: ${alglib_SOURCE_DIR}")

