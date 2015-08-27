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

# Run tests for the mean function
testMean()
testFloatMean()