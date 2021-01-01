CC:=g++
STD:=c++17
SHELL=bash


.PHONY: quick test_quick tests clean

quick: src/quick_sort.cpp includes/input.h
	@${CC} -std=${STD} -I includes src/quick_sort.cpp -o bin/quick

heap: src/heap_sort.cpp includes/input.h
	@${CC} -std=${STD} -I includes src/heap_sort.cpp -o bin/heap

test_quick: quick
	@pipenv run pytest -x tests/test_sort.py::test_quick_sort

test_heap: heap
	@pipenv run pytest -x tests/test_sort.py::test_heap_sort

tests: quick heap
	@pipenv run pytest -x tests/test_sort.py

clean:
	@rm bin/* 2> /dev/null
