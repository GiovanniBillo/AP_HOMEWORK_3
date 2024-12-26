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
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -FPIC")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_PROJECT_DIR})
endif()
# Set C++ Standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)


# # Include ALGLIB source files manually
# add_subdirectory(external/alglib-cpp) # Include ALGLIB directory
# Add ALGLIB include directory
include_directories(${ALGLIB_INCLUDE_DIR})


find_package(pybind11 REQUIRED)
include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})

pybind11_add_module(InterpolateWrapper src/bindings.cpp)
target_link_libraries(InterpolateWrapper PRIVATE alglib)
target_include_directories(InterpolateWrapper PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include) # explicitly add the include directory for the target library as well

# # always place python library in the main directory ( to avoid having to set PYTHONPATH everytime)
# set_target_properties(InterpolateWrapper PROPERTIES
#     LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}
# )

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
# Add the main executable
add_executable(main_interpolation src/main.cpp)

# Include ALGLIB headers in the include path
target_include_directories(main_interpolation PRIVATE external/alglib/src)

# Link ALGLIB sources to the main executable
target_link_libraries(main_interpolation PRIVATE alglib)
target_link_libraries(InterpolateWrapper PRIVATE alglib)

# Debugging messages
message(STATUS "ALGLIB directory: ${CMAKE_CURRENT_SOURCE_DIR}/external/alglib")

