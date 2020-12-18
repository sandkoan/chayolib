# SOURCES := $(shell find -name '*.cpp')
shared:
	g++ -c -Wall -Werror -fpic src\quadratic.cpp
	g++ -shared -o ./projektileMotion/shared/program.dll *.o
	rm *.o