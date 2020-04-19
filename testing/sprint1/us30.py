# US30: Printing a list of living married family members

import sys
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all living married individuals
'''

def print_married(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["Family ID", "Wife", "Husband", "Marriage Date"]
    for married_id in sorted(col):
        t.add_row(col[married_id])
    if print_table: print(t)
    return t.get_string()

def listmarried(indivs, fams, print_table):
    married = {}
    for fam_id in fams:
        if (fams[fam_id][1] != "NA") and (fams[fam_id][2] == "NA"): #married(1) and not divorced(2)
            husb_id = fams[fam_id][3]     #gets wife indivs id 
            wife_id = fams[fam_id][5]      #gets husb indivs id
            if (indivs[wife_id][6] == 'NA' and indivs[husb_id][6] == 'NA'): #makes sure both husband and wife are alive
                married[fam_id] = [''] * 4
                married[fam_id][0] = fam_id #famid 
                married[fam_id][1] = fams[fam_id][6] #wife name
                married[fam_id][2] = fams[fam_id][4] #husb name
                married[fam_id][3] = fams[fam_id][1] #marriage date
    return print_married(married, print_table)