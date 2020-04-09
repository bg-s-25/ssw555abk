# US29: Printing a list of deceased family members

import sys
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all deceased individuals
'''
def print_deceased(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["ID", "Name", "Birthday", "Age", "Death"]
    for deceased_id in sorted(col):
        t.add_row(col[deceased_id])
    if print_table: print(t)
    return t.get_string()
 
def listdeceased(indivs, print_table):
    deceased = {}
    for indivs_id in indivs: 
        if indivs[indivs_id][6] != "NA":     #check if they have a death date
            deceased[indivs_id] = [''] * 5
            deceased[indivs_id][0] = indivs_id #id
            deceased[indivs_id][1] = indivs[indivs_id][1] #name
            deceased[indivs_id][2] = indivs[indivs_id][3] #birthday
            deceased[indivs_id][3] = main_parser.age(indivs[indivs_id][3], indivs[indivs_id][6]) #age
            deceased[indivs_id][4] = indivs[indivs_id][6] #death
    return print_deceased(deceased, print_table)
