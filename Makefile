all:test main link
test:
	@./sub.py test.c > testc.c
	gcc -c testc.c -g -o test.o
main:
	gcc -c main.c -g -o main.o
link:
	gcc main.o test.o -o test

.PHONY:clean
clean:
	@rm -rf *.o test
	
