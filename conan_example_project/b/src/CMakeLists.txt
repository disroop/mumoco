add_library(demob b.h b.c)
target_include_directories(demob PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(demob CONAN_PKG::demoa)