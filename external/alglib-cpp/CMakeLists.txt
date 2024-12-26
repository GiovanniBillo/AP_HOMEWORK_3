cmake_minimum_required(VERSION 3.22)
project(alglib LANGUAGES CXX)

# Gather all ALGLIB source files
file(GLOB ALGLIB_SOURCES src/*.cpp)
file(GLOB ALGLIB_HEADERS src/*.h)

# Create a static library for ALGLIB
add_library(alglib STATIC ${ALGLIB_SOURCES})

# Expose the ALGLIB headers to consumers
target_include_directories(alglib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

# Optional: Add compile options for ALGLIB (if needed)
target_compile_options(alglib PRIVATE -Wall -Wextra -pedantic -fPIC)

