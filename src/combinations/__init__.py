""" Combinations generator

This module is used to generate all possible combinations of a 
given set, as a list. It assumes that the elements of the list 
are unique. If there is an element occuring more than once, it 
will still be considered as a unique element. That is, if you 
want to generate combinations of length 2 of the list [1, 1], 
you will get [[1, 1]].



Modules include:
    :mod:`combinations.combinations`
        A module that contains the :func:`find_combinations` function.
-------
combinations
    Combinations generator

This module contains the following functions : 
    * find_combinations - returns a list of all possible combinations of 
        a given list, as a list.
"""