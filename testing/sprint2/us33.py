# US31: Printing a list of all orphaned children (both parents dead and child < 18 years old)

import sys
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all orphaned children(under 18)
'''

def print_orphaned(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["Individual ID", "Name", "Age"]
    for child_id in sorted(col):
        t.add_row(col[child_id])
    if print_table: print(t)
    return t.get_string()    

def listorphaned(indivs, fams, print_table):
    orphaned = {}
    for fam_id in fams:
        if (fams[fam_id][7] != "NA"):   #ensures they have children
            husb_id = fams[fam_id][3]   
            wife_id = fams[fam_id][5]  
            if (indivs[wife_id][6] != 'NA' and indivs[husb_id][6] != 'NA'): #ensures both husband and wife are deceased
                children_id = fams[fam_id][7]  #gets the children(s) id in a list
                for child_id in children_id:   #gets each child in the list 
                    age = main_parser.age(indivs[child_id][3], indivs[child_id][6])   #gets childs age
                    if (age < 18):
                        orphaned[child_id] = [''] * 3
                        orphaned[child_id][0] = child_id #id
                        orphaned[child_id][1] = indivs[child_id][1] #name
                        orphaned[child_id][2] = main_parser.age(indivs[child_id][3], indivs[child_id][6]) #age
    return print_orphaned(orphaned, print_table)