cmake_minimum_required(VERSION 3.10)

# Set the project name
project(ToolBox)

# Add subdirectories
add_subdirectory(STATISTICS)
add_subdirectory(INTERPOLATION)

target_include_directories(main_stats PRIVATE ${CMAKE_SOURCE_DIR}/STATISTICS/include)
