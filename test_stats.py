from stats import mean

def testMean():
    '''*******************************************************************
    Checks the mean function using integers with integer result expected
    *******************************************************************'''
    assert(mean([2,4]) == 3)

def testFloatMean():
    '''*******************************************************************
    Checks the mean function using integers with float result expected
    *******************************************************************'''
    assert(mean([1,2]) == 1.5)

def testNegMean():
    '''*******************************************************************
    Checks the mean function using integers with negative result expected
    *******************************************************************'''
    assert(mean([-4,2]) == -2)

def testVaryMean():
    '''*******************************************************************
    Checks the mean function using integer lists of varying length
    *******************************************************************'''
    assert(mean([2,4,6,8]) == mean([1,3,7,9]))

# Run tests for the mean function
testMean()
testFloatMean()
testNegMean()
testVaryMean()