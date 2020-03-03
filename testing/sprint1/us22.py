# US21: Unique ids

import sys
sys.path.insert(0, '../../')
import main_parser

'''
    Given lists of read ids, ensure that all individuals and families have unique ids
'''
def verify_unique_ids(indivsLst, famsLst):
    errors = []
    for indiv_id in indivsLst:
        if indivsLst.count(indiv_id) > 1:
            errors += ["ERROR: INDIVIDUAL: US22: {}: Multiple occurrences of individual's id".format(indiv_id)]
    for fam_id in famsLst:
        if famsLst.count(fam_id) > 1:
            errors += ["ERROR: FAMILY: US22: {}: Multiple occurrences of family's id".format(fam_id)]
    return errors
