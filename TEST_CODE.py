##### Global color variables #####
from colorama import Fore
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN
Y = Fore.YELLOW

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''

from set_class import Set
##################################

def result(flag):
  if flag:
    return f"{G}PASSED{W}"
  
  return f"{R}FAILED{W}"


def TEST_initialize(s):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Initialize a Set{W}\n")

    test = type(s) == Set
    print(f"New Set is correct data type: {result(test)}")

    test = type(s.set) == list and len(s.set) == 0
    print(f"Set.set is a list containing no elements: {result(test)}")

    test = type(s.size) == int and s.size == 0
    print(f"Set.size is initialized to zero: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_add_elements(s):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Adding Elements{W}\n")

    print(f"Current set contains no elements: {B}{s}{W}\n")

    out = s.add(1)
    print(f"An element was added to the set: {B}{s}{W}\n")

    test = s.set == [1] and 1 in s.set
    print(f"1 was added to the set: {result(test)}")

    test = out == None
    print(f"Add method does not return anything: {result(test)}")

    test = s.size == 1 and len(s) == 1
    print(f"Size of the set was increased properly: {result(test)}")

    test = True
    for num in [2,3,4,5]:
      s.add(num)
      if len(s) != num or s.size != num: test = False

    print(f"\nFour more items were added to the set: {B}{s}{W}")
    print(f"Size of the set was increased properly: {result(test)}")

    s.add(1)
    print(f"\nA duplicate element was added to the set: {B}{s}{W}")

    test = s.set == [1,2,3,4,5]
    print(f"Set was not affected by a duplicate: {result(test)}")

    test = s.size == 5 and len(s) == 5
    print(f"Size of the set was not affected by a duplicate: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_iterate(s):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Iteration{W}\n")

    print(f"Current state of the Set: {B}{s}{W}\n")

    test = True
    for i, ele in enumerate(s):
      print(f"{B}Iteration {i}:{W} {ele}")
      if i+1 != ele:
        test = False
    print(f"\n__iter__ produces the correct loop sequence: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_delete_elements(s):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Deleting Elements{W}\n")

    print(f"\n{P}~~~ .discard() ~~~{W}\n")
    print(f"Current state of the Set: {B}{s}{W}\n")

    out = s.discard(3)
    print(f"3 was discarded from the Set: {B}{s}{W}")

    test = s.set == [1,2,4,5]
    print(f"Correct element was discarded: {result(test)}")

    test = s.size == 4 and len(s) == 4
    print(f"Size of Set decreased to 4: {result(test)}")

    test = out == None
    print(f"Discard method does not return anything: {result(test)}")

    out = s.discard(9)
    print(f"\n9 was discarded from the Set: {B}{s}{W}")

    test = s.set == [1,2,4,5]
    print(f"Set was not impacted by discard: {result(test)}")

    test = s.size == 4 and len(s) == 4
    print(f"Size of was not affected by discard: {result(test)}")

    print(f"\n{P}~~~ .remove() ~~~{W}\n")
    print(f"Current state of the Set: {B}{s}{W}\n")

    out = s.remove(5)
    print(f"5 was removed from the Set: {B}{s}{W}")

    test = s.set == [1,2,4]
    print(f"Correct element was removed: {result(test)}")

    test = s.size == 3 and len(s) == 3
    print(f"Size of Set decreased to 3: {result(test)}")

    test = out == None
    print(f"Remove method does not return anything: {result(test)}")

    try:
      s.remove(9)
      print(f"\nAttempting to remove non-existent element raises exception: {result(False)}")
    
    except:
      print(f"\nAttempting to remove non-existent element raises exception: {result(True)}")

      test = s.size == 3 and len(s) == 3
      print(f"Size of Set unaffected by failed remove: {result(test)}")

    print(f"\n{P}~~~ .clear() ~~~{W}\n")
    print(f"Current state of the Set: {B}{s}{W}\n")

    temp = s.set
    out = s.clear()
    print(f"The Set was emptied: {B}{s}{W}")

    test = s.set == []
    print(f"Set contains no elements: {result(test)}")

    test = s.set is temp
    print(f"Set elements were removed with a loop: {result(test)}")
    
    test = s.size == 0 and len(s) == 0
    print(f"Set size is zero: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_element_in_set(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Check if element in set{W}\n")

    X = Set()
    Y = Set()

    for i in range(10):
      X.add(i)
      if i % 2 == 0: Y.add(i)

    print(f"Two sets were created:\n\t{B}X = {X}\n\tY = {Y}{W}\n")

    print(f"\n{P}~~~ .has_element() ~~~{W}")

    print(f"\n{P}~~ MASS TEST X ~~{W}")
    print(f"{B}X = {X}{W}")
    for i in range(10):
      test = X.has_element(i)
      print(f"{i} ∈ X: {result(test)}")

    print(f"\n{P}~~ MASS TEST Y ~~{W}")
    print(f"{B}Y = {Y}{W}")
    for i in range(10):
      test = Y.has_element(i)
      if i % 2 == 0:
        print(f"{i} ∈ Y: {result(test)}")
      else:
        print(f"{i} !∈ Y: {result(not(test))}")

    print(f"\n\n{P}~~~ in (__contains__) ~~~{W}")

    print(f"\n{P}~~ MASS TEST X ~~{W}")
    print(f"{B}X = {X}{W}")
    for i in range(10):
      test = i in X
      print(f"{i} in X: {result(test)}")

    print(f"\n{P}~~ MASS TEST Y ~~{W}")
    print(f"{B}Y = {Y}{W}")
    for i in range(10):
      test = i in Y
      if i % 2 == 0:
        print(f"{i} in Y: {result(test)}")
      else:
        print(f"{i} not in Y: {result(not(test))}")

    del X
    del Y
    print("~" * 50, "\n\n")

def TEST_disjoint(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Check if two sets are disjointed{W}\n")

    X = Set()
    Y = Set()
    Z = Set()

    for i in range(10):
      X.add(i)
      if i % 2 == 0: Y.add(i)
      else: Z.add(i)

    print(f"Three sets were created:\n\t{B}X = {X}\n\tY = {Y}\n\tZ = {Z}{W}\n")

    test = not(X.is_disjoint(Y) and Y.is_disjoint(X))
    print(f"Sets X and Y are not disjointed: {result(test)}")

    test = not(X.is_disjoint(Z) and Z.is_disjoint(X))
    print(f"Sets X and Z are not disjointed: {result(test)}")

    test = Z.is_disjoint(Y) and Y.is_disjoint(Z)
    print(f"Sets Y and Z are disjointed: {result(test)}")

    del X
    del Y
    del Z
    print("~" * 50, "\n\n")


def TEST_subset(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Subsets & Inequalities{W}\n")

    w = Set()
    X = Set()
    Y = Set()
    Z = Set()

    for i in range(10):
      w.add(i)
      X.add(i)
      if i % 2 == 0: Y.add(i)
      else: Z.add(i)

    print(f"Four sets were created:\n\t{B}W = {w}\n\tX = {X}\n\tY = {Y}\n\tZ = {Z}{W}\n")

    print(f"\n{P}~~~ == (__eq__) ~~~{W}")

    test = w == X
    print(f"Sets W and X are equal: {result(test)}")

    test = not(w == Y)
    print(f"Sets W and Y are not equal: {result(test)}")

    test = not(w == Z)
    print(f"Sets W and Z are not equal: {result(test)}")

    print(f"\n{P}~~~ != (__ne__) ~~~{W}")

    test = not(w != X)
    print(f"Sets W and X are not not equal: {result(test)}")

    test = w != Y
    print(f"Sets W and Y are not equal: {result(test)}")

    test = w != Z
    print(f"Sets W and Z are not equal: {result(test)}")

    print(f"\n{P}~~~ .is_subset() ~~~{W}")

    test = not(w.is_subset(Y))
    print(f"A large set cannot be a subset of a small set: {result(test)}")

    test = w.is_subset(X)
    print(f"Sets of equal sizes can be assessed with ==: {result(test)}")

    test = Y.is_subset(X) and Y.is_subset(w) and Z.is_subset(X) and Z.is_subset(w)
    print(f"Subsets are correctly identified: {result(test)}")

    print(f"\n{P}~~~ <= (__le__) ~~~{W}")

    test = Y <= X and Y <= w and Z <= X and Z <= w and not(w <= Y) and w <= X
    print(f"Subsets are correctly identified: {result(test)}")

    print(f"\n{P}~~~ >= (__ge__) ~~~{W}")
    
    test = X >= Y and w >= Y and X >= Z and w >= Z and not(Y >= w) and X >= w
    print(f"Subsets are correctly identified: {result(test)}")

    print(f"\n{P}~~~ < (__lt__) ~~~{W}")
    
    test = Y < X and Y < w and Z < X and Z < w
    print(f"Subsets are correctly identified: {result(test)}")

    test = not(X < w) and not(w < X)
    print(f"Equal sets do not pass: {result(test)}")

    print(f"\n{P}~~~ > (__gt__) ~~~{W}")
    
    test = X > Y and w > Y and X > Z and w > Z
    print(f"Subsets are correctly identified: {result(test)}")

    test = not(X > w) and not(w > X)
    print(f"Equal sets do not pass: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_operators(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Set Operators{W}\n")

    w = Set()
    X = Set()
    Y = Set()
    Z = Set()

    for i in range(10):
      w.add(i)
      X.add(i)
      if i % 2 == 0: Y.add(i)
      else: Z.add(i)

    print(f"Four sets were created:\n\t{B}W = {w}\n\tX = {X}\n\tY = {Y}\n\tZ = {Z}{W}\n")

    print(f"\n{P}~~~ .union() ~~~{W}")
    new = Y.union(Z)
    print(f"The union of sets Y and Z: {B}Y U Z = {new}{W}\n")

    test = type(new) == Set
    print(f"Union produces a new Set object: {result(test)}")

    test = len(new) == 10
    print(f"Union contains correct number of elements: {result(test)}")

    test = Y.is_subset(new) and Z.is_subset(new)
    print(f"Union contains all elements from both sets: {result(test)}")

    new2 = Z.union(Y)
    test = new == new2
    print(f"Union operation is unordered: {result(test)}")

    new = X.union(Y)
    print(f"\nThe union of sets X and Y: {B}X U Y = {new}{W}\n")

    test = new == X and len (new) == 10
    print(f"New set does not contain duplicate elements: {result(test)}")

    test = X.is_subset(new) and Y.is_subset(new)
    print(f"Union contains all elements from both sets: {result(test)}")

    print(f"\n{P}~~~ .intersection() ~~~{W}")
    new = X.intersection(Z)
    print(f"The intersection of sets X and Z: {B}X ∩ Z = {new}{W}\n")

    test = type(new) == Set
    print(f"Intersection produces a new Set object: {result(test)}")

    test = len(new) == 5
    print(f"Intersection contains correct number of elements: {result(test)}")

    test = new.is_subset(X) and new.is_subset(Z)
    print(f"Intersection is a subset of both parent sets: {result(test)}")

    new2 = Z.intersection(X)
    test = new == new2
    print(f"Intersection operation is unordered: {result(test)}")

    new = Y.intersection(Z)
    print(f"\nThe intersection of sets Y and Z: {B}Y ∩ Z = {new}{W}\n")

    test = len(new) == 0 and str(new) == '{}' and type(new) == Set
    print(f"Intersection of disjointed sets is an empty set: {result(test)}")

    print(f"\n{P}~~~ .difference() ~~~{W}")
    new = w.difference(Z)
    print(f"The difference of sets W and Z: {B}W - Z = {new}{W}\n")

    test = type(new) == Set
    print(f"Difference produces a new Set object: {result(test)}")

    test = len(new) == 5 and new == Y
    print(f"Difference contains correct elements: {result(test)}")

    test = new.is_subset(w) and not(new.is_subset(Z))
    print(f"Result is a subset of left-hand starting set: {result(test)}")

    new2 = Z.difference(w)
    print(f"\nThe difference of sets Z and W: {B}Z - W = {new2}{W}\n")

    test = str(new2) == '{}' and len(new2) == 0
    print(f"New set contains correct elements: {result(test)}")

    test = new != new2
    print(f"Difference operation is ordered: {result(test)}")

    test = new.is_disjoint(new2)
    print(f"W - Z and Z - W sets are disjointed: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_cartesian(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Cartesian Product{W}\n")

    X = Set()
    Y = Set()

    for i in range(3): X.add(i)
    for i in "abcd": Y.add(i)

    print(f"Two sets were created:\n\t{B}X = {X}\n\tY = {Y}{W}\n")

    cp1 = X.cartesian_product(Y)
    cp2 = Y.cartesian_product(X)

    print(f"X x Y = {B}{cp1}{W}\n")

    test = True
    for el in cp1:
      if type(el) != tuple or len(el) != 2:
        test = False
    print(f"CP result contains ordered pairs (tuples): {result(test)}")

    test = len(cp1) == len(X) * len(Y)
    print(f"CP result contains correct number of tuples: {result(test)}")

    compare = [(0,'a'),(0,'b'),(0,'c'),(0,'d'),(1,'a'),(1,'b'),(1,'c'),(1,'d'),(2,'a'),(2,'b'),(2,'c'),(2,'d')]

    test = True
    for ele in compare:
      if not(ele in cp1): test = False
    print(f"CP elements are correct: {result(test)}")

    test = cp1 != cp2
    print(f"CP is an ordered operation: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_power(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Power set{W}\n")

    A = Set()
    for el in range(4): A.add(el)
    print(f"A set was created:\n\t{B}A = {A}{W}\n")

    new = A.power_set()
    print(f"P(A) = {B}{new}{W}\n")

    test = len(new) == 2**len(A)
    print(f"P(A) contains the correct number of elements: {result(test)}")

    expected = ["{}","{3}","{2}","{2,3}","{1}","{1,3}","{1,2}","{1,2,3}","{0}","{0,3}","{0,2}","{0,2,3}","{0,1}","{0,1,3}","{0,1,2}","{0,1,2,3}"]
    test = True
    for el in new:
      if str(el) not in expected:
        print(f"{R}EXTRA FOUND: {el}{W}")
        test = False
      else:
        expected.remove(str(el))
    if len(expected) != 0:
      test = False
      print(f"{R}MISSING: {', '.join(expected)}{W}")

    print(f"P(A) contains the correct elements: {result(test)}")

    print("~" * 50, "\n\n")

def TEST_docs(Set):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = Set.__len__.__doc__
    if doc != None:
        print(f"{B}Len Documentation:{W} {doc}\n")
    else:
        print(f"{R}Len Documentation Missing{W}\n")

    doc = Set.__str__.__doc__
    if doc != None:
        print(f"{B}To-string Documentation:{W} {doc}\n")
    else:
        print(f"{R}To-string Documentation Missing{W}\n")
    
    doc = Set.add.__doc__
    if doc != None:
        print(f"{B}Add Documentation:{W} {doc}\n")
    else:
        print(f"{R}Add Documentation Missing{W}\n")

    doc = Set.discard.__doc__
    if doc != None:
        print(f"{B}Discard Documentation:{W} {doc}\n")
    else:
        print(f"{R}Discard Documentation Missing{W}\n")

    doc = Set.remove.__doc__
    if doc != None:
        print(f"{B}Remove Documentation:{W} {doc}\n")
    else:
        print(f"{R}Remove Documentation Missing{W}\n")

    doc = Set.clear.__doc__
    if doc != None:
        print(f"{B}Clear Documentation:{W} {doc}\n")
    else:
        print(f"{R}Clear Documentation Missing{W}\n")

    doc = Set.has_element.__doc__
    if doc != None:
        print(f"{B}Has_element Documentation:{W} {doc}\n")
    else:
        print(f"{R}Has_element Documentation Missing{W}\n")

    doc = Set.__contains__.__doc__
    if doc != None:
        print(f"{B}Contains Documentation:{W} {doc}\n")
    else:
        print(f"{R}Contains Documentation Missing{W}\n")

    doc = Set.is_disjoint.__doc__
    if doc != None:
        print(f"{B}Is_disjoint Documentation:{W} {doc}\n")
    else:
        print(f"{R}Is_disjoint Documentation Missing{W}\n")

    doc = Set.is_subset.__doc__
    if doc != None:
        print(f"{B}Is_subset Documentation:{W} {doc}\n")
    else:
        print(f"{R}Is_subset Documentation Missing{W}\n")

    doc = Set.union.__doc__
    if doc != None:
        print(f"{B}Union Documentation:{W} {doc}\n")
    else:
        print(f"{R}Union Documentation Missing{W}\n")

    doc = Set.intersection.__doc__
    if doc != None:
        print(f"{B}Intersection Documentation:{W} {doc}\n")
    else:
        print(f"{R}Intersection Documentation Missing{W}\n")

    doc = Set.difference.__doc__
    if doc != None:
        print(f"{B}Difference Documentation:{W} {doc}\n")
    else:
        print(f"{R}Difference Documentation Missing{W}\n")

    doc = Set.power_set.__doc__
    if doc != None:
        print(f"{B}Power_set Documentation:{W} {doc}\n")
    else:
        print(f"{R}Power_set Documentation Missing{W}\n")

    doc = Set.cartesian_product.__doc__
    if doc != None:
        print(f"{B}Cartesian_product Documentation:{W} {doc}\n")
    else:
        print(f"{R}Cartesian_product Documentation Missing{W}\n")

    doc = Set.__eq__.__doc__
    if doc != None:
        print(f"{B}eq Documentation:{W} {doc}\n")
    else:
        print(f"{R}eq Documentation Missing{W}\n")

    doc = Set.__ne__.__doc__
    if doc != None:
        print(f"{B}ne Documentation:{W} {doc}\n")
    else:
        print(f"{R}ne Documentation Missing{W}\n")

    doc = Set.__lt__.__doc__
    if doc != None:
        print(f"{B}lt Documentation:{W} {doc}\n")
    else:
        print(f"{R}lt Documentation Missing{W}\n")

    doc = Set.__gt__.__doc__
    if doc != None:
        print(f"{B}gt Documentation:{W} {doc}\n")
    else:
        print(f"{R}gt Documentation Missing{W}\n")

    doc = Set.__le__.__doc__
    if doc != None:
        print(f"{B}le Documentation:{W} {doc}\n")
    else:
        print(f"{R}le Documentation Missing{W}\n")

    doc = Set.__ge__.__doc__
    if doc != None:
        print(f"{B}ge Documentation:{W} {doc}\n")
    else:
        print(f"{R}ge Documentation Missing{W}\n")

    doc = Set.__iter__.__doc__
    if doc != None:
        print(f"{B}iter Documentation:{W} {doc}\n")
    else:
        print(f"{R}iter Documentation Missing{W}\n")


    print("~" * 50, "\n\n")