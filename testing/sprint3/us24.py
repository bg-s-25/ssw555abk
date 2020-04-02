# US24: Unique families by spouses

import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser

'''
    Given the dictionary of families, ensure that there is no more than one family with the same spouses by name & anniversary date
'''
def verify_unique_families(fams):
    errors = []
    ids = [fams[fam_id][0] for fam_id in fams]
    annivdates_names = [fams[fam_id][1] + ' ' + fams[fam_id][4] + ' ' + fams[fam_id][6] for fam_id in fams]
    
    for i in range(len(annivdates_names)):
        if annivdates_names.count(annivdates_names[i]) > 1:
            errors += ["ERROR: FAMILY: US24: {}: More than one family with the same anniversary date and spouse names ({})".format(ids[i], annivdates_names[i])]

    return errors
