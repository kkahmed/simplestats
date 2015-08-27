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


