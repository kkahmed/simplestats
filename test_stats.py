from stats import mean, std
from nose.tools import assert_equal, assert_almost_equal

def testMean():
    '''*******************************************************************
    Checks the mean function using integers with integer result expected
    *******************************************************************'''
    assert_equal(mean([2,4]),3)

def testFloatMean():
    '''*******************************************************************
    Checks the mean function using integers with float result expected
    *******************************************************************'''
    assert_equal(mean([0.5,2.5]),1.5)

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
    
def testInfMean():
    '''*******************************************************************
    Checks the mean function to 3 places for a infinitely-repeating result
    *******************************************************************'''
    assert_almost_equal(mean([2,3,5]),3.333,places=3)

def testStd1():
    obs = std([0.0,2.0])
    exp = 1.0
    assert_equal(obs,exp)

def testStd2():
    obs = std([ ])
    exp = 0.0
    assert_equal(obs,exp)
    
def testStd3():
    obs = std([0.0,4.0])
    exp = 2.0
    assert_equal(obs,exp)  

def testStd4():
    obs = std([1.0,3.0])
    exp = 1.0
    assert_equal(obs,exp) 
    
def testStd5():
    obs = std([1.0,1.0,1.0])
    exp = 0.0
    assert_equal(obs,exp)   

''' # Run tests for the mean function
testMean()
testFloatMean()
testNegMean()
testVaryMean() '''