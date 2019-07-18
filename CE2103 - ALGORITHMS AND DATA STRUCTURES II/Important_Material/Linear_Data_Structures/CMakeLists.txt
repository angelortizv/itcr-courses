cmake_minimum_required(VERSION 3.13)
project(Linear_Data_Structures)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_CXX_STANDARD 14)


set(SOURCE_FILES
        main.cpp

        linkedList/LinkedListInterface.cpp
        linkedList/List.cpp

        queue/QueueInterface.cpp
        queue/Queue.cpp
        queue/QueueItem.cpp

        )

add_executable(Linear_Data_Structures ${SOURCE_FILES})