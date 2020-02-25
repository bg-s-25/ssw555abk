# US02: Birth before marriage

import sys
sys.path.insert(0, '../')
import gedcom

'''
    Given list of birth dates and marriage dates of individuals, ensure that all people are born before marriage
'''

# bbm = birth before marriage
def bbm(births, marriages):
    for b, m in zip(births, marriages):
        if b >= m: 
            return (False, "ERROR: FAMILY: US02")