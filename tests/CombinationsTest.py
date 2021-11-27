import unittest
import math
from src.combinations import combinations

def _combinationsNumber (n, k) :
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

class CombinationsTest(unittest.TestCase) :

    def test_numberOfCombinations (self): 
        list = [2,7,9,3,5,6,8,4,1]
        n = len(list)
        k = 3
        combs = combinations.find_combinations(list, k)
        self.assertEqual(len(combs), _combinationsNumber(n, k))
        k = 0
        combs = combinations.find_combinations(list, k)
        self.assertEqual(len(combs), 1)
        k = n
        combs = combinations.find_combinations(list, k)
        self.assertEqual(len(combs), 1)

    def test_combinationsLength (self) :
        list = [2,7,9,3,5,6,8,4,1]
        n = len(list)
        k = 3
        combs = combinations.find_combinations(list, k)
        for comb in combs :
            self.assertEqual(len(comb), k)
    
    def test_raisingErrors (self) :
        with self.assertRaises(ValueError) :
            combinations.find_combinations([], -1)
        with self.assertRaises(ValueError) :
            combinations.find_combinations([1,2,3], 4)
        


if __name__ == '__main__':
    unittest.main()