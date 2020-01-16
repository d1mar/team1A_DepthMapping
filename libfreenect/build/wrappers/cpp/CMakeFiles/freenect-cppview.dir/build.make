# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi1a/workspace/team1A_DepthMapping/libfreenect

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build

# Include any dependencies generated for this target.
include wrappers/cpp/CMakeFiles/freenect-cppview.dir/depend.make

# Include the progress variables for this target.
include wrappers/cpp/CMakeFiles/freenect-cppview.dir/progress.make

# Include the compile flags for this target's objects.
include wrappers/cpp/CMakeFiles/freenect-cppview.dir/flags.make

wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o: wrappers/cpp/CMakeFiles/freenect-cppview.dir/flags.make
wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o: ../wrappers/cpp/cppview.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o"
	cd /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/freenect-cppview.dir/cppview.cpp.o -c /home/pi1a/workspace/team1A_DepthMapping/libfreenect/wrappers/cpp/cppview.cpp

wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/freenect-cppview.dir/cppview.cpp.i"
	cd /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi1a/workspace/team1A_DepthMapping/libfreenect/wrappers/cpp/cppview.cpp > CMakeFiles/freenect-cppview.dir/cppview.cpp.i

wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/freenect-cppview.dir/cppview.cpp.s"
	cd /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi1a/workspace/team1A_DepthMapping/libfreenect/wrappers/cpp/cppview.cpp -o CMakeFiles/freenect-cppview.dir/cppview.cpp.s

wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.requires:

.PHONY : wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.requires

wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.provides: wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.requires
	$(MAKE) -f wrappers/cpp/CMakeFiles/freenect-cppview.dir/build.make wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.provides.build
.PHONY : wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.provides

wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.provides.build: wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o


# Object files for target freenect-cppview
freenect__cppview_OBJECTS = \
"CMakeFiles/freenect-cppview.dir/cppview.cpp.o"

# External object files for target freenect-cppview
freenect__cppview_EXTERNAL_OBJECTS =

bin/freenect-cppview: wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o
bin/freenect-cppview: wrappers/cpp/CMakeFiles/freenect-cppview.dir/build.make
bin/freenect-cppview: lib/libfreenect.so.0.6.0
bin/freenect-cppview: /usr/lib/arm-linux-gnueabihf/libGL.so
bin/freenect-cppview: /usr/lib/arm-linux-gnueabihf/libGLU.so
bin/freenect-cppview: /usr/lib/arm-linux-gnueabihf/libglut.so
bin/freenect-cppview: /usr/lib/arm-linux-gnueabihf/libXmu.so
bin/freenect-cppview: /usr/lib/arm-linux-gnueabihf/libXi.so
bin/freenect-cppview: /usr/lib/arm-linux-gnueabihf/libusb-1.0.so
bin/freenect-cppview: wrappers/cpp/CMakeFiles/freenect-cppview.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/freenect-cppview"
	cd /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/freenect-cppview.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
wrappers/cpp/CMakeFiles/freenect-cppview.dir/build: bin/freenect-cppview

.PHONY : wrappers/cpp/CMakeFiles/freenect-cppview.dir/build

wrappers/cpp/CMakeFiles/freenect-cppview.dir/requires: wrappers/cpp/CMakeFiles/freenect-cppview.dir/cppview.cpp.o.requires

.PHONY : wrappers/cpp/CMakeFiles/freenect-cppview.dir/requires

wrappers/cpp/CMakeFiles/freenect-cppview.dir/clean:
	cd /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp && $(CMAKE_COMMAND) -P CMakeFiles/freenect-cppview.dir/cmake_clean.cmake
.PHONY : wrappers/cpp/CMakeFiles/freenect-cppview.dir/clean

wrappers/cpp/CMakeFiles/freenect-cppview.dir/depend:
	cd /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi1a/workspace/team1A_DepthMapping/libfreenect /home/pi1a/workspace/team1A_DepthMapping/libfreenect/wrappers/cpp /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp /home/pi1a/workspace/team1A_DepthMapping/libfreenect/build/wrappers/cpp/CMakeFiles/freenect-cppview.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : wrappers/cpp/CMakeFiles/freenect-cppview.dir/depend

