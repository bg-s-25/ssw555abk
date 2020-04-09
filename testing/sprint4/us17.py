# US17: No marriages to children

import sys
sys.path.insert(0, '../../')
# sys.path.insert(0, '../sprint1')
# sys.path.insert(0, '../sprint2')
# sys.path.insert(0, '../sprint3')
import main_parser

'''
    Find individuals that are married to their children
'''
def check_marr_child(indivs, fams):
    errors = []
    for indiv_id in indivs:
        children = set()

        # collect individual's children
        if indivs[indiv_id][8] == 'NA': continue
        for fam_id in indivs[indiv_id][8]:
            # for each family in which the indiv is a spouse
            children = children.union(fams[fam_id][7])

        # check if one of the individual's children is one of the spouses
        for fam_id in indivs[indiv_id][8]:
            husb_wife_ids = fams[fam_id][3] + fams[fam_id][5]
            for child_id in children:
                if child_id in husb_wife_ids and child_id != indiv_id:
                    errors += ["ERROR: FAMILY: US17: {}: {} is married to its child {}".format(fam_id, indiv_id, child_id)]
    
    return errors
