""" A module for finding all combinations of a list of elements.

This module contains a function to find all combinations in a set. 

Functions
---------
find_combinations(list, k)
    Returns all the possible combinations of length k of the given list.

Definitions
-----------
indexes : list
    A list of indexes. It determines the positions of the elements of 
    the list to pick to form a combination. If you ask for all combinations
    of length k, then the indexes list will be of length k.
"""


def __move(indexes, maxLength) :
    """ Determines the element to move in the indexes list and moves it.

    This function determines the element to move in the indexes list and moves 
    it. The returned new indexes list represent the indexes of the elements to 
    pick to form the next combinations
    It does this depending on tha maxLength parameter which represents the 
    length of the set we are trying to find combinations of.

    Raises
    ------
    ValueError
        If the given indexes list contains an index that is higher than 
        maxLength

    Parameters
    ----------
    indexes : list
        A list of indexes.
    maxLength : int
        The length of the set we are trying to find combinations of.
    
    Returns
    -------
    bool
        True if the indexes list has been modified, False otherwise.
        False signifies that the indexes list is in its final state :
        a list of the form [n-k-1, ..., n-2, n-1] and of length k.
    """

    # Determining the indexToMove
    length = len(indexes)
    indexToMove = -1
    for i in range (length) :
        if indexes[length - 1 -i] >= maxLength :
            raise ValueError ("Indexes must be less than maxLength")
        if indexes[length - 1 - i] != maxLength - 1 - i :
            indexToMove = length - 1 - i
            break
    if indexToMove == -1 :
        return False
    # Moving the index and the indexes after it
    indexes[indexToMove] += 1
    for i in range (indexToMove + 1, length) :
        indexes[i] = indexes[i - 1] + 1
    return True



def find_combinations (list, k) :
    """ Returns all the possible combinations of length k of the given list.

    This function returns all the possible combinations of length k of the 
    given list. It assumes that the given list if a set (the elements occur
    only once). It returns a list of lists. Each list in the returned list 
    represents a combination.
    If the given list contains elements occuring more than once, then those
    elements will be considered as many time as they occur in the list.

    Preconditions
    -------------
    list : list
        A list of elements.
    k : int
        The length of the combinations must be >= 0

    Parameters
    ----------
    list : list
        A list of elements
    k : int
        The length of the combinations to find.

    Raises
    ------
    ValueError
        If the given given k is negative or greater than the length of the set.
    
    Returns
    -------
    list
        A list of lists. Each list in the returned list represents a 
        combination.
    """

    n = len(list)
    combinations = []
    if k < 0 or k > n :
        raise ValueError ("k must be equal to 0 or positive and less than or equal to n")
    if k == 0 :
        return [[]]
    elif k == 1 :
        return [[i] for i in list]
    elif k == len (list) :
        return [list]
    else :
        indexes = [i for i in range (k)]
        combinations.append ([list[i] for i in indexes])
        while __move(indexes, n) :
            combinations.append([list[i] for i in indexes])
    return combinations