'''
Maria L Marinez
CS 4320 - Spring '15
Assignment 2: hw2_testh1.py
Test Cases for Hw1 functions
''' 

import unittest
from hw1 import *

# BEGIN tests for Compare function
class CompareTests(unittest.TestCase):
    # test that returns negative value
    def test_compare_negative(self):
        self.assertLess(compare('buy', 'hold'), 0)

    # test that returns positive value
    def test_compare_positive(self):
        self.assertGreater(compare('sell', 'hold'), 0)
        
    # test that returns 0
    def test_compare_zero(self):
        self.assertEquals(0, compare('hold', 'hold'))


# BEGIN tests for Changes function
class ChangesTests(unittest.TestCase):
    # test without enough opinions to indicate changes
    def test_changes_missing_opinions(self):
        self.assertEquals([], changes(['sell']))

    # test with an upgrade
    def test_changes_upgrate(self):
        op = ['sell', 'buy']
        self.assertEquals(['upgrade'], changes(op))

    # test with a downgrade
    def test_changes_downgrade(self):
        op = ['buy', 'hold']
        self.assertEquals(['downgrade'], changes(op))

    # test with no change between opinions
    def test_changes_same(self):
        op = ['hold', 'hold']
        self.assertEquals(['same'], changes(op))


# BEGIN tests for CurrentOpinions function
class CurrentOpinionsTest(unittest.TestCase):
    # test with non empty list
    def test_changes_same(self):
        op = [['hold','sell','strong sell'],['sell', 'sell']]
        self.assertEquals(['strong sell', 'sell'], currentOpinions(op))


# BEGIN tests for RemoveEmpties function
class RemoveEmptiesTest(unittest.TestCase):
    # test with empty lists
    def test_remove_empties(self):
        seq = [[1,2],[],['a'],[],[],[],['a','b']]
        self.assertEquals([[1, 2], ['a'], ['a', 'b']], removeEmpties(seq))


# BEGIN tests for AverageRating functionrs
class AverageRatingTests(unittest.TestCase):
    # test with empty parameter
    def test_average_rating_empty(self):
        self.assertEquals(0, averageRating([]))

    # test with opinions
    def test_average_rating_opinions(self):
        self.assertAlmostEqual(4.5, averageRating(['strong sell', 'sell']), 7)
        

# run tests
if __name__ == '__main__':
    unittest.main()