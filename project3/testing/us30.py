# US30: Printing a list of deceased family members

import sys
sys.path.insert(0, '../')
import gedcom
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all married individuals
'''

def print_married(col):
    t = PrettyTable()
    t.field_names = ["Family ID", "Wife", "Husband", "Marriage Date"]
    for married_id in sorted(col):
        t.add_row(col[married_id])
    print(t)

def listmarried(fams):
    married = {}
    for fam_id in fams: #make sure not dead
        if (fams[fam_id][1] != "NA") and (fams[fam_id][2] == "NA"): #married(1) and not divorced(2)
            married[fam_id] = [''] * 4
            married[fam_id][0] = fam_id #famid 
            married[fam_id][1] = fams[fam_id][6] #wife name
            married[fam_id][2] = fams[fam_id][4] #husb name
            married[fam_id][3] = fams[fam_id][1] #marriage date
    print_married(married)
    return True