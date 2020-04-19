# US15: There should be fewer than 15 siblings in a family
import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
sys.path.insert(0, '../sprint3')
import main_parser

'''
Given a family, there should be fewer than 15 siblings in a family 
'''
def number_siblings(fams):
    errors = []
    for fam_id in fams:
        if (fams[fam_id][7] != "NA"):  #children list
            num_siblings = len(fams[fam_id][7])
            if (num_siblings >= 15):
                errors += ["ERROR: FAMILY: US15: {}: Number of siblings in family exceeds 15".format(fam_id)]
    
    return errors    