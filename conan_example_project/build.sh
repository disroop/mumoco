#The traditional build way without mumoco and no usage of export and create later
#Thus the order of the creates must match.
#currently the dependencies match the alphabetical package order, which may
# should be improved to show that this is not important for mumoco
clear
conan remove "demo*" -f
conan create a demoa/0.1@disroop/development
conan create b demob/0.1@disroop/development
conan create c democ/0.1@disroop/development
conan create d demod/0.1@disroop/development