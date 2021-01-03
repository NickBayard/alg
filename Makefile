CC:=g++
STD:=c++17
SHELL=bash


.PHONY: quick test_quick tests clean

quick: cpp/src/quick_sort.cpp cpp/includes/input.h
	@${CC} -std=${STD} -I cpp/includes cpp/src/quick_sort.cpp -o cpp/bin/quick

heap: cpp/src/heap_sort.cpp cpp/includes/input.h
	@${CC} -std=${STD} -I cpp/includes cpp/src/heap_sort.cpp -o cpp/bin/heap

test_quick: quick
	@pipenv run pytest -x tests/test_cpp/test_sort.py::test_quick_sort

test_heap: heap
	@pipenv run pytest -x tests/test_cpp/test_sort.py::test_heap_sort

tests: quick heap
	@pipenv run pytest -x tests/test_cpp/test_sort.py

clean:
	@rm bin/* 2> /dev/null
