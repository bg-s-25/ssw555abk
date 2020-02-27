# US02: Birth before marriage

import sys
sys.path.insert(0, '../')
import gedcom

'''
    Given list of birth dates and marriage dates of individuals, ensure that all people are born before marriage
    Assumptions:
    Every marriage has a husband and a wife.
    Every person has a birthday listed in this format 'xxxx-xx-xx'
'''

# bbm = birth before marriage
def bbm(pers, fam):
    # errors will be a list of all the inconsistent entries
    # Every marriage has a husband and a wife
    errors = []
    for key in fam:
        hus_id = fam[key][3]
        wife_id = fam[key][5]
        if (pers[hus_id][3] >= fam[key][1]):
            errors += ["ERROR: FAMILY: US02: {}: Husband's birth date {} after marriage date {}".format(hus_id,pers[hus_id][3],value[1])]
        if (pers[wife_id][3] >= fam[key][1]):
            errors += ["ERROR: FAMILY: US02: {}: Wife's birth date {} following marriage date {}".format(hus_id,pers[wife_id][3],value[1])]
    return [False] + errors if len(errors) > 0 else [True] + errors

