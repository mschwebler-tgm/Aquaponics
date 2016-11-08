install:
	cd hiredis && $(MAKE) && $(MAKE) install && ldconfig && cd ..

all:
	gcc example.c -o example.out -levent -levent_core -lhiredis
