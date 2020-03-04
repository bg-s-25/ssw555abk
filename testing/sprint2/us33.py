# US31: Printing a list of all orphaned children (both parents dead and child < 18 years old)

import sys
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all orphaned children(under 18)
'''

def print_orphaned(col):
    t = PrettyTable()
    t.field_names = ["Individual ID", "Name", "Age"]
    for child_id in sorted(col):
        t.add_row(col[child_id])
        
    #creates a file of the output
    table_txt = t.get_string()
    with open('output.txt','w') as file:
        file.write(table_txt)
    print(t)
    file.close()
    return 'output.txt'

def compare(file1, file2):
    errors = []
    file1 = open(file1,'r')
    file2 = open(file2,'r')
    if (file1.read() != file2.read()):
        errors += ["ERROR: INDIVIDUAL: US30: Did not properly list all living orphaned individuals"]
    file1.close()
    file2.close()
    return errors

def listorphaned(indivs, fams):
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
    file = print_orphaned(orphaned)
    return file
