quadratic2: quadratic1
	rm blah.o
quadratic1: blah.o
	gcc blah.o -o blah
blah.o: blah.c
	gcc -c quadratic.c -o blah.o
blah.c:
	echo "pass"