cmake_minimum_required(VERSION 3.22)
project(main_stats LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(DEFINED DATA_DIR)
  message(STATUS "Using user-specified data directory: ${DATA_DIR}")
else()
  set(DATA_DIR ${CMAKE_CURRENT_SOURCE_DIR}/data)
  message(STATUS "Using default data directory: ${DATA_DIR}")
endif()

add_definitions(-DDATA_DIR=\"${DATA_DIR}\")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)


# # Add the debugging flag
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -fPIC") # !!!TODO: modify with optimizations when releasing

# Debug or Release configuration
if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
    message(STATUS "Building DEBUG version")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -pg -Wall -Wpedantic -Wextra -fPIC")
else()
    message(STATUS "Building RELEASE version (default)")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g0 -O2 -DNDEBUG -Wall -fPIC")
endif()

include(FetchContent)

# Fetch the DataFrame library
FetchContent_Declare(
    DataFrame
    GIT_REPOSITORY https://github.com/hosseinmoein/DataFrame.git
    # GIT_TAG v1.18.0 # Replace with the desired stable version tag
)

# Ensure the DataFrame library is downloaded and built
FetchContent_MakeAvailable(DataFrame)

find_package(pybind11 REQUIRED)
include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})

pybind11_add_module(DataFrameWrapper src/bindings.cpp)
target_link_libraries(DataFrameWrapper PRIVATE DataFrame::DataFrame)
target_include_directories(DataFrameWrapper PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include) # explicitly add the include directory for the target library as well

# # always place python library in the main directory ( to avoid having to set PYTHONPATH everytime)
# set_target_properties(DataFrameWrapper PROPERTIES
#     LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}
# )
# Add the executable
add_executable(main_stats src/main.cpp)

# Link the DataFrame library
target_link_libraries(main_stats PRIVATE DataFrame::DataFrame)

 # Define a flag
 option(INTERPOLATION_MODULE "Include the InterpolationWrapper and Interpolate custom visitor" OFF)

# Conditionally include a library and headers
if(INTERPOLATION_MODULE)
    message(STATUS "Include the InterpolationWrapper and Interpolate custom visitor")
    add_compile_definitions(INTERPOLATION_MODULE)
    target_compile_definitions(main_stats PRIVATE INTERPOLATION_MODULE)

    # Add ALGLIB include directory
    include_directories(${ALGLIB_INCLUDE_DIR})
    
    # # Add custom library
    # add_library(CustomLib STATIC custom_library.cpp)

    # Fetch the ALGLIB library
    FetchContent_Declare(
       alglib 
        GIT_REPOSITORY https://github.com/hjkuijf/ALGLIB
        # GIT_TAG v1.18.0 # Uncomment to use a specific version or tag
    )

    # Ensure the ALGLIB library is downloaded and built
    FetchContent_MakeAvailable(alglib)

    # If ALGLIB is header-only or doesn't provide a library target:
    target_include_directories(main_stats PRIVATE ${alglib_SOURCE_DIR}/src)


    # If ALGLIB provides a CMake target (for example, alglib::alglib), link it
    # Uncomment the line below if a proper CMake target is available
    # target_link_libraries(main PRIVATE alglib::alglib)

    # Manually add the source files if ALGLIB doesn't provide a CMake target
    file(GLOB ALGLIB_SRC 
        ${alglib_SOURCE_DIR}/src/*.cpp
    )


    # Link the source files to your project if ALGLIB doesn't have a CMake target
    target_sources(main_stats PRIVATE ${ALGLIB_SRC})

else()
    message(STATUS "Interpolation module is not included")
endif()

