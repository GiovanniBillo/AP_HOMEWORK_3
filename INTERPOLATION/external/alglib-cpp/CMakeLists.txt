# cmake_minimum_required(VERSION 3.22)
# project(alglib LANGUAGES CXX)

# # Gather all ALGLIB source files
# file(GLOB ALGLIB_SOURCES src/*.cpp)
# file(GLOB ALGLIB_HEADERS src/*.h)

# # Create a static library for ALGLIB
# add_library(alglib STATIC ${ALGLIB_SOURCES})

# # Expose the ALGLIB headers to consumers
# target_include_directories(alglib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

# # Optional: Add compile options for ALGLIB (if needed)
# target_compile_options(alglib PRIVATE -Wall -Wextra -pedantic -fPIC)
cmake_minimum_required(VERSION 3.22)
project(alglib LANGUAGES CXX)

# Define paths
set(ALGLIB_BUILD_DIR "${CMAKE_CURRENT_BINARY_DIR}/build")
set(ALGLIB_OUTPUT_FILE "${ALGLIB_BUILD_DIR}/build/libalglib.a")

# Check if the library is already built
if(EXISTS ${ALGLIB_OUTPUT_FILE})
    message(STATUS "ALGLIB is already built: ${ALGLIB_OUTPUT_FILE}")
else()
    message(STATUS "ALGLIB is not built. Building now...")

    # Gather all ALGLIB source files
    file(GLOB ALGLIB_SOURCES src/*.cpp)
    file(GLOB ALGLIB_HEADERS src/*.h)

    # Create a static library for ALGLIB
    add_library(alglib STATIC ${ALGLIB_SOURCES})

    # Specify the output directory for the library
    set_target_properties(alglib PROPERTIES
        ARCHIVE_OUTPUT_DIRECTORY ${ALGLIB_BUILD_DIR}
    )

    # Expose the ALGLIB headers to consumers
    target_include_directories(alglib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

    # Optional: Add compile options for ALGLIB (if needed)
    target_compile_options(alglib PRIVATE -Wall -Wextra -pedantic -fPIC)
endif()


