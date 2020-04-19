# US18: Siblings should not marry

import sys
sys.path.insert(0, '../../')
import main_parser

'''
    Find individuals that are married to their sibling
'''
def check_marr_sib(indivs, fams):
    errors = []

    for indiv_id in indivs:
        siblings = set()

        # collect individual's siblings
        if indivs[indiv_id][7] == 'NA' or indivs[indiv_id][8] == 'NA': continue
        for fam_id in indivs[indiv_id][7]:
            # for each family in which the indiv is a child
            siblings = siblings.union(fams[fam_id][7])
        siblings.discard(indiv_id)

        # check if one of the individual's siblings is one of the spouses
        for fam_id in indivs[indiv_id][8]:
            husb_wife_ids = fams[fam_id][3] + fams[fam_id][5]
            for sib_id in siblings:
                if sib_id in husb_wife_ids:
                    errors += ["ERROR: FAMILY: US18: {}: {} is married to its sibling {}".format(fam_id, indiv_id, sib_id)]
    
    return errors
