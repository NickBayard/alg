CC:=g++
STD:=c++17
SHELL=bash


.PHONY: quick test_quick tests clean

quick: src/quick_sort.cpp includes/input.h
	@${CC} -std=${STD} -I includes src/quick_sort.cpp -o bin/quick

test_quick: quick
	@pipenv run pytest -s tests/test_quick_sort.py

tests: test_quick

clean:
	@rm bin/* 2> /dev/null
