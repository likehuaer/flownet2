if("v2.1.2" STREQUAL "")
  message(FATAL_ERROR "Tag for git checkout should not be empty.")
endif()

set(run 0)

if("C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags-stamp/gflags-gitinfo.txt" IS_NEWER_THAN "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags-stamp/gflags-gitclone-lastrun.txt")
  set(run 1)
endif()

if(NOT run)
  message(STATUS "Avoiding repeated git clone, stamp file is up to date: 'C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags-stamp/gflags-gitclone-lastrun.txt'")
  return()
endif()

execute_process(
  COMMAND ${CMAKE_COMMAND} -E remove_directory "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to remove directory: 'C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags'")
endif()

# try the clone 3 times incase there is an odd git clone issue
set(error_code 1)
set(number_of_tries 0)
while(error_code AND number_of_tries LESS 3)
  execute_process(
    COMMAND "C:/Program Files (x86)/Git/cmd/git.exe" clone --origin "origin" "https://github.com/gflags/gflags.git" "gflags"
    WORKING_DIRECTORY "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src"
    RESULT_VARIABLE error_code
    )
  math(EXPR number_of_tries "${number_of_tries} + 1")
endwhile()
if(number_of_tries GREATER 1)
  message(STATUS "Had to git clone more than once:
          ${number_of_tries} times.")
endif()
if(error_code)
  message(FATAL_ERROR "Failed to clone repository: 'https://github.com/gflags/gflags.git'")
endif()

execute_process(
  COMMAND "C:/Program Files (x86)/Git/cmd/git.exe" checkout v2.1.2
  WORKING_DIRECTORY "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to checkout tag: 'v2.1.2'")
endif()

execute_process(
  COMMAND "C:/Program Files (x86)/Git/cmd/git.exe" submodule init 
  WORKING_DIRECTORY "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to init submodules in: 'C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags'")
endif()

execute_process(
  COMMAND "C:/Program Files (x86)/Git/cmd/git.exe" submodule update --recursive 
  WORKING_DIRECTORY "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to update submodules in: 'C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags'")
endif()

# Complete success, update the script-last-run stamp file:
#
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy
    "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags-stamp/gflags-gitinfo.txt"
    "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags-stamp/gflags-gitclone-lastrun.txt"
  WORKING_DIRECTORY "C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to copy script-last-run stamp file: 'C:/Users/10008777.IS/mLearn/flownet-release/windows/external/gflags-prefix/src/gflags-stamp/gflags-gitclone-lastrun.txt'")
endif()

