# US21: Correct gender for role

import sys
sys.path.insert(0, '../')
import gedcom

'''
    Given dictionaries of individuals & families, ensure that husband and wife in each family have the correct role
'''
def verify_correct_roles(indivs, fams):
    for fam_id in fams:
        husb_id = fams[fam_id][3]
        wife_id = fams[fam_id][5]
        if indivs[husb_id][2] != 'M':
            return (False, "ERROR: INDIVIDUAL: US21: X: {}: Incorrect role for husband in family {}".format(husb_id, fam_id))
        if indivs[wife_id][2] != 'F':
            return (False, "ERROR: INDIVIDUAL: US21: X: {}: Incorrect role for wife in family {}".format(wife_id, fam_id))
    return (True, "")
