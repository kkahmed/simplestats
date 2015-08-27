"""
Statistics class for SWC workshop

@author: Kazi
"""

def mean(vals):
    '''*******************************************************************
    Returns the mean value of a given array
    Arguments:
        vals - A list of numbers
    *******************************************************************'''
    total = sum(vals)
    length = len(vals)
    return float(total)/length

def std(vals):
    '''*******************************************************************
    Returns the standar deviation of a given array
    Arguments:
        vals - A list of numbers
    *******************************************************************'''
    
    # Default if empty
    if len(vals) == 0:
        return 0.0
    
    # Some variables for standard deviation
    meanv = mean(vals)
    sumsq = 0
    
    # Calculate and return
    for i in vals:
        sumsq = sumsq + i*i
    return (float(sumsq)/len(vals)-float(meanv)**2)**(0.5)
