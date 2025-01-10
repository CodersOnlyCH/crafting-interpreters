cmake_minimum_required(VERSION 3.28)
project(C_Code C)

if(CMAKE_SYSTEM MATCHES Windows)
    set(CMAKE_SYSTEM_NAME Windows)
    message(STATUS "Target system is Windows")
endif()

if(CMAKE_HOST_SYSTEM MATCHES Linux)
    set(CMAKE_SYSTEM_NAME Linux)
    message(STATUS "Build host runs Linux")
endif()

if(CMAKE_HOST_SYSTEM MATCHES Apple)
    set(CMAKE_SYSTEM_NAME Apple)
    message(STATUS "Build host runs Apple")
endif()

set(CMAKE_C_COMPILER "gcc")
set(CMAKE_C_STANDARD 23)

add_executable(C_Code main.c)
set_property(TARGET C_Code PROPERTY VERSION "0.0.1")

# Set default build type to Release if not specified
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Define build types
set(CMAKE_C_FLAGS_DEBUG "-g")
set(CMAKE_C_FLAGS_RELEASE "-O3")

# Set output directories for different build types
set_target_properties(C_Code PROPERTIES
                      RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_BINARY_DIR}/bin/Debug
                      RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_BINARY_DIR}/bin/Release
)

# Print the build type
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
