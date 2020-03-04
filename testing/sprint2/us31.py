# US31: Printing a list all living people over 30 who have never been married

import sys
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all living people over 30 who have never been married
'''

def print_single(col):
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
        errors += ["ERROR: INDIVIDUAL: US31: Did not properly list all single individuals over 30"]
    file1.close()
    file2.close()
    return errors

def listsingle(indivs):
    single = {}
    for indiv_id in indivs:
        age = main_parser.age(indivs[indiv_id][3], indivs[indiv_id][6])
        if(age > 30 and indivs[indiv_id][8] == 'NA'):     #ensures over 30 and has never had spouse
            single[indiv_id] = [''] * 3
            single[indiv_id][0] = indiv_id #id
            single[indiv_id][1] = indivs[indiv_id][1] #name
            single[indiv_id][2] = age #age

    file = print_single(single)
    return file