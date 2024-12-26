cmake_minimum_required(VERSION 3.10)

# Set the project name
project(ToolBox)

# Add ALGLIB directory to a global include path
set(ALGLIB_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external/alglib-cpp)

# Add subdirectories
add_subdirectory(STATISTICS)
add_subdirectory(INTERPOLATION)
add_subdirectory(external/alglib-cpp) # Include ALGLIB directory

