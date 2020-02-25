# US03: Birth before death

import sys
sys.path.insert(0, '../')
import gedcom


'''
    Given list of birth dates and death dates of individuals, ensure that all people are born before death
'''

# bbd = birth before death
def bbd(pers, fam, pers_id, fam_id):
    for b, m in zip(pers, fam):
        if b >= m: 
            return (False, "ERROR: FAMILY: US02")