# Implementation & testing of the Set data structure

# Import file
from TEST_CODE import *
from set_class import Set
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    s = Set()

    # TEST 1 - Test Set initialization
    # BEFORE TESTING: implement __init__, __len__
    TEST_initialize(s)

    # TEST 2 - Test adding elements
    # BEFORE TESTING: implement add
    TEST_add_elements(s)

    # TEST 3 - Test iteration
    # BEFORE TESTING: implement __iter__
    TEST_iterate(s)

    # TEST 4 - Test removing elements
    # BEFORE TESTING: implement remove, discard, clear
    TEST_delete_elements(s)

    # TEST 5 - Test if an element is in a set
    # BEFORE TESTING: implement is_element, __contains__ 
    TEST_element_in_set(Set)

    # TEST 6 - Test if two sets are disjointed
    # BEFORE TESTING: implement is_disjoint
    TEST_disjoint(Set)

    # TEST 7 - Test if a set is a subset of another
    # BEFORE TESTING: implement is_subset, __lt__, __gt__, __le__, __ge__, __eq__. __ne__
    TEST_subset(Set)

    # TEST 8 - Test set operators
    # BEFORE TESTING: implement union, intersection, difference
    TEST_operators(Set)

    # TEST 9 - Test cartesian product
    # BEFORE TESTING: implement cartesian_product
    TEST_cartesian(Set)

    # TEST 10 - Test power set
    # BEFORE TESTING: implement power_set
    TEST_power(Set)

    # TEST 11 - Docstrings
    # BEFORE TESTING: implement docstrings for all methods
    TEST_docs(Set)

    

if __name__ == "__main__":
    os.system("clear")
    main()