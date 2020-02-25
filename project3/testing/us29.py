# US29: Printing a list of deceased family members

import sys
sys.path.insert(0, '../')
import gedcom
from prettytable import PrettyTable
'''
    Given all the individuals in the family, list all deceased individuals
'''
def print_deceased(col):
    t = PrettyTable()
    t.field_names = ["ID", "Name", "Birthday", "Age", "Death"]
    for deceased_id in sorted(col):
        t.add_row(col[deceased_id])
    
    #creates a file of the output
    table_txt = t.get_string()
    with open('output.txt','w') as file:
        file.write(table_txt)
    print(t)
    file.close()
    return 'output.txt'


def listdeceased(indivs):
    deceased = {}
    for indivs_id in indivs: 
        if indivs[indivs_id][6] != "NA":     #check if they have a death date
            deceased[indivs_id] = [''] * 5
            deceased[indivs_id][0] = indivs_id #id
            deceased[indivs_id][1] = indivs[indivs_id][1] #name
            deceased[indivs_id][2] = indivs[indivs_id][3] #birthday
            deceased[indivs_id][3] = gedcom.age(indivs[indivs_id][3], indivs[indivs_id][6]) #age
            deceased[indivs_id][4] = indivs[indivs_id][6] #death
    file = print_deceased(deceased)
    return file
