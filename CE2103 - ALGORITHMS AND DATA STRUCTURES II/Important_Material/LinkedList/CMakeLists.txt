cmake_minimum_required(VERSION 3.7 )
project(LinkedList)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${Qt5Widgets_EXECUTABLE_COMPILE_FLAGS}")
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
        List.cpp
        Node.cpp)

add_executable(LinkedList ${SOURCE_FILES})
