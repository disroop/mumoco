add_library(democ c.h c.c)
target_include_directories(democ PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(democ PUBLIC CONAN_PKG::demob)
