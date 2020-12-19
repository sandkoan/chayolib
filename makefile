# SOURCES := $(shell find -name '*.cpp')
shared:
	g++ -c -Wall -Werror -fpic src/quadratic.cpp
	g++ quadratic.o -shared -o projektileMotion/program.dll 
	
test:
	g++ src/quadratic.cpp -o src/quadratic.exe
	./src/quadratic.exe

python:
	python projektileMotion/test.py