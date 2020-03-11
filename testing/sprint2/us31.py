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
    print(t)
    return t.get_string()

def listsingle(indivs):
    single = {}
    for indiv_id in indivs:
        age = main_parser.age(indivs[indiv_id][3], indivs[indiv_id][6])
        if(age > 30 and indivs[indiv_id][8] == 'NA'):     #ensures over 30 and has never had spouse
            single[indiv_id] = [''] * 3
            single[indiv_id][0] = indiv_id #id
            single[indiv_id][1] = indivs[indiv_id][1] #name
            single[indiv_id][2] = age #age

    return print_single(single)