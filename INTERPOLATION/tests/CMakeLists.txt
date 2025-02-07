cmake_minimum_required(VERSION 3.22)
project(tests_interpolation LANGUAGES CXX)

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

# Fetch GoogleTest
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.14.0
)
FetchContent_MakeAvailable(googletest)

# Add the executable
add_executable(tests_interpolation test_interpolation.cpp)

# If ALGLIB is header-only or doesn't provide a library target:
target_include_directories(tests PRIVATE 
    ${alglib_SOURCE_DIR}/src
    ${CMAKE_CURRENT_SOURCE_DIR}/../
)

# If ALGLIB provides a CMake target (for example, alglib::alglib), link it
# Uncomment the line below if a proper CMake target is available
# target_link_libraries(main PRIVATE alglib::alglib)

# Manually add the source files if ALGLIB doesn't provide a CMake target
file(GLOB ALGLIB_SRC 
    ${alglib_SOURCE_DIR}/src/*.cpp
)

# Link the source files to your project if ALGLIB doesn't have a CMake target
target_sources(tests_interpolation PRIVATE ${ALGLIB_SRC})

# Message to confirm the source directory of ALGLIB
message(STATUS "ALGLIB source dir: ${alglib_SOURCE_DIR}")

# Print the paths being added to the include directories
message("Include path 1: ${CMAKE_CURRENT_SOURCE_DIR}/../")
message("Include path 2: ${alglib_SOURCE_DIR}/src")

# Link libraries
target_link_libraries(tests PRIVATE
    GTest::gtest_main
    # alglib::alglib
)

enable_testing()
include(GoogleTest)
gtest_discover_tests(tests_interpolation)
