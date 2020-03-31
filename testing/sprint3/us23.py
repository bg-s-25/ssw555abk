# US23: Unique name and birth date

import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser

'''
    Given the dictionary of individuals, ensure that there is no more than one individual with the same name and birth date
'''
def verify_unique_namesbdate(indivs):
    errors = []
    ids = [indivs[indiv_id][0] for indiv_id in indivs]
    names_bdates = [indivs[indiv_id][1] + ' ' + indivs[indiv_id][3] for indiv_id in indivs]
    
    for i in range(len(names_bdates)):
        if names_bdates.count(names_bdates[i]) > 1:
            errors += ["ERROR: INDIVIDUAL: US23: {}: More than one individual with the same name and birth date ({})".format(ids[i], names_bdates[i])]

    return errors
