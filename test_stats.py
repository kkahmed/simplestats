from stats import mean
from nose.tools import assert_equal

def testMean():
    '''*******************************************************************
    Checks the mean function using integers with integer result expected
    *******************************************************************'''
    assert_equal(mean([2,4]),3)

def testFloatMean():
    '''*******************************************************************
    Checks the mean function using integers with float result expected
    *******************************************************************'''
    assert_equal(mean([1,2]),1.5)

def testNegMean():
    '''*******************************************************************
    Checks the mean function using integers with negative result expected
    *******************************************************************'''
    assert_equal(mean([-4,2]),-1)

def testVaryMean():
    '''*******************************************************************
    Checks the mean function using integer lists of varying length
    *******************************************************************'''
    assert_equal(mean([2,4,6,8]),mean([1,3,7,9]))

''' # Run tests for the mean function
testMean()
testFloatMean()
testNegMean()
testVaryMean() '''