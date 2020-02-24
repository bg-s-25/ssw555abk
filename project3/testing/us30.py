# US30: Printing a list of deceased family members

import sys
sys.path.insert(0, '../')
import gedcom

'''
    Given all the individuals in the family, list all married individuals
'''

def listmarried(indivs, fams):
   married = {}
   for fam_id in fams: 
        if (fams[fam_id][1] != "NA") and (fams[fam_id][2] == "NA"): #married(1) and not divorced(2)
            married[cur_id] = [''] * 4
            married[cur_id][0] = fam_id #famid 
            married[cur_id][1] = fams[fam_id][6] #wife name
            married[cur_id][2] = fams[fam_id][4] #husb name
            married[cur_id][3] = fams[fam_id][2] #marriage date
    print_deceased(married)

def print_married(col):
    t = PrettyTable()
    t.field_names = ["Family ID", "Wife", "Husband", "Marriage Date"]
    for married_id in sorted(col):
        t.add_row(col[married_id])
    print(t)