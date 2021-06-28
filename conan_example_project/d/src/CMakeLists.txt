add_library(demod d.h d.c)
target_include_directories(demod PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(demod PUBLIC CONAN_PKG::democ)
