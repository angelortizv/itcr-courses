# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/clion-2018.3.4/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /opt/clion-2018.3.4/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Linear_Data_Structures.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Linear_Data_Structures.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Linear_Data_Structures.dir/flags.make

CMakeFiles/Linear_Data_Structures.dir/main.cpp.o: CMakeFiles/Linear_Data_Structures.dir/flags.make
CMakeFiles/Linear_Data_Structures.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Linear_Data_Structures.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Linear_Data_Structures.dir/main.cpp.o -c "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/main.cpp"

CMakeFiles/Linear_Data_Structures.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Linear_Data_Structures.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/main.cpp" > CMakeFiles/Linear_Data_Structures.dir/main.cpp.i

CMakeFiles/Linear_Data_Structures.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Linear_Data_Structures.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/main.cpp" -o CMakeFiles/Linear_Data_Structures.dir/main.cpp.s

CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.o: CMakeFiles/Linear_Data_Structures.dir/flags.make
CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.o: ../linkedList/LinkedListInterface.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.o -c "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/linkedList/LinkedListInterface.cpp"

CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/linkedList/LinkedListInterface.cpp" > CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.i

CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/linkedList/LinkedListInterface.cpp" -o CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.s

CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.o: CMakeFiles/Linear_Data_Structures.dir/flags.make
CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.o: ../linkedList/List.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.o -c "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/linkedList/List.cpp"

CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/linkedList/List.cpp" > CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.i

CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/linkedList/List.cpp" -o CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.s

CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.o: CMakeFiles/Linear_Data_Structures.dir/flags.make
CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.o: ../queue/QueueInterface.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.o -c "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/QueueInterface.cpp"

CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/QueueInterface.cpp" > CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.i

CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/QueueInterface.cpp" -o CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.s

CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.o: CMakeFiles/Linear_Data_Structures.dir/flags.make
CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.o: ../queue/Queue.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.o -c "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/Queue.cpp"

CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/Queue.cpp" > CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.i

CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/Queue.cpp" -o CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.s

CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.o: CMakeFiles/Linear_Data_Structures.dir/flags.make
CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.o: ../queue/QueueItem.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.o -c "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/QueueItem.cpp"

CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/QueueItem.cpp" > CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.i

CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/queue/QueueItem.cpp" -o CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.s

# Object files for target Linear_Data_Structures
Linear_Data_Structures_OBJECTS = \
"CMakeFiles/Linear_Data_Structures.dir/main.cpp.o" \
"CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.o" \
"CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.o" \
"CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.o" \
"CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.o" \
"CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.o"

# External object files for target Linear_Data_Structures
Linear_Data_Structures_EXTERNAL_OBJECTS =

Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/main.cpp.o
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/linkedList/LinkedListInterface.cpp.o
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/linkedList/List.cpp.o
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/queue/QueueInterface.cpp.o
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/queue/Queue.cpp.o
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/queue/QueueItem.cpp.o
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/build.make
Linear_Data_Structures: CMakeFiles/Linear_Data_Structures.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable Linear_Data_Structures"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Linear_Data_Structures.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Linear_Data_Structures.dir/build: Linear_Data_Structures

.PHONY : CMakeFiles/Linear_Data_Structures.dir/build

CMakeFiles/Linear_Data_Structures.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Linear_Data_Structures.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Linear_Data_Structures.dir/clean

CMakeFiles/Linear_Data_Structures.dir/depend:
	cd "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures" "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures" "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug" "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug" "/home/angelortizv/Documents/Projects/itcr-courses/CE2103 - ALGORITHMS AND DATA STRUCTURES II/Important_Material/Linear_Data_Structures/cmake-build-debug/CMakeFiles/Linear_Data_Structures.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Linear_Data_Structures.dir/depend
