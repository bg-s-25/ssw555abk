# US04: Marriage should occur before divorce of spouses, and divorce can only occur after marriage

import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser

'''
    Given individuals, ensure that marriage occurs before divorce and divorce occurs after marriage
'''

def marriage_before_divorce(families):
    errors = []
    for family in families.values(): # parse through each family
        #check to see if the family has divorced and check to see if divorce occurred before or on the day of marriage
        if (family[2] != 'NA' and family[2] <= family[1]): 
            errors += ['ERROR: FAMILY: US04: {}: Divorced {} before married {}'.format(family[0],family[2],family[1])]
    return errors