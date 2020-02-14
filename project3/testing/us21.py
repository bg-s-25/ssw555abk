# US21: Correct gender for role

import sys
sys.path.insert(0, '../')
import gedcom

'''
    Ensure that husband and wife in each family have the correct role according to gender
'''
def verify_correct_roles(indivs, fams):
    for fam_id in fams:
        husb_id = fams[fam_id][3]
        wife_id = fams[fam_id][5]
        if indivs[husb_id][2] != 'M':
            return (False, "Error: Incorrect role for husband (id={}) in family (id={})".format(husb_id, fam_id))
        if indivs[wife_id][2] != 'F':
            return (False, "Error: Incorrect role for wife (id={}) in family (id={})".format(wife_id, fam_id))
    return (True, "")
