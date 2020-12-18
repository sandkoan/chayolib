SOURCES := $(shell find -name '*.cpp')
shared:
	g++ -c -Wall -Werror -fpic $(SOURCES)
	g++ -shared -o ./projektileMotion/shared/program.so *.o
	rm *.o