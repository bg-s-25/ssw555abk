'''
List all multiple births in a GEDCOM file 
(when someone delivers more than one baby at a single time)
'''

import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser
from prettytable import PrettyTable

def print_siblings(dict,print_table):
    t = PrettyTable()
    t.field_names = ["Family ID", "Name", "Birthday"]
    for indiv_id in dict:
        t.add_row(dict[indiv_id])
    if print_table: print(t)
    return t.get_string()

def list_multiple_births(indivs, families, print_table):
    multiple_births = {}
    for fam_id in families:
        # you need to make it into a sorted list to get a single correct solution every time
        children = sorted(list(families[fam_id][7])) 
        i = 0
        while (len(children) > 0 and i < len(children)):
            flag = False
            birth_date_i = indivs[children[i]][3]
            j = 0
            while (len(children) > 0 and j < len(children)):
                birth_date_j = indivs[children[j]][3]
                # finds another sibling with the same birthday
                if (i != j and birth_date_i == birth_date_j): 
                    flag = True
                    multiple_births[children[j]] = [''] * 3
                    multiple_births[children[j]][0] = fam_id #family_id
                    multiple_births[children[j]][1] = indivs[children[j]][1] #name
                    multiple_births[children[j]][2] = birth_date_j
                    del children[j]
                j += 1
            # found another sibling with the same birthday
            if (flag):
                multiple_births[children[i]] = [''] * 3
                multiple_births[children[i]][0] = fam_id #family_id
                multiple_births[children[i]][1] = indivs[children[i]][1] #name
                multiple_births[children[i]][2] = birth_date_i
                del children[i]
            # did not find another sibling with the same birthday
            else:
                i += 1
    return print_siblings(multiple_births,print_table)
