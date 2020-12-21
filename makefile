# SOURCES := $(shell find -name '*.cpp')
shared:
	g++ -c -Wall -Werror -fpic src/projectile.cpp -o projectile.o
	g++ projectile.o -shared -o projektileMotion/program.dll 
	rm projectile.o
	
test:
	g++ src/quadratic.cpp -o src/quadratic.exe
	./src/quadratic.exe

python:
	python projektileMotion/test.py

pull:
	git pull

push: test
	git commit -a
	git push