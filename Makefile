CC:=g++
STD:=c++17
SHELL=bash


.PHONY: quick heap bst rbbst hash test_quick test_heap test_bst test_rbbst test_hash tests clean

quick: cpp/src/quick_sort.cpp cpp/includes/input.h
	@${CC} -std=${STD} -I cpp/includes cpp/src/quick_sort.cpp -o cpp/bin/quick

heap: cpp/src/heap_sort.cpp cpp/includes/input.h
	@${CC} -std=${STD} -I cpp/includes cpp/src/heap_sort.cpp -o cpp/bin/heap

bst: cpp/src/binary_tree.cpp cpp/includes/input.h
	@${CC} -std=${STD} -I cpp/includes cpp/src/binary_tree.cpp -o cpp/bin/bst

rbbst: cpp/src/balanced_tree.cpp
	@${CC} -std=${STD} cpp/src/balanced_tree.cpp -o cpp/bin/rbbst

hash: cpp/src/hash.cpp
	@${CC} -std=${STD} cpp/src/hash.cpp -o cpp/bin/hash

test_quick: quick
	@pipenv run pytest -x tests/test_cpp/test_sort.py::test_quick_sort

test_heap: heap
	@pipenv run pytest -x tests/test_cpp/test_sort.py::test_heap_sort

test_bst: bst
	@pipenv run pytest -x tests/test_cpp/test_search.py::test_bst

tests: test_quick test_heap test_bst
	@pipenv run pytest -x tests/test_cpp/

clean:
	@rm bin/* 2> /dev/null
