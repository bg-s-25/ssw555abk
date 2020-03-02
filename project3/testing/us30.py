# US30: Printing a list of living married family members

import sys
sys.path.insert(0, '../')
import gedcom
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all living married individuals
'''

def print_married(col):
    t = PrettyTable()
    t.field_names = ["Family ID", "Wife", "Husband", "Marriage Date"]
    for married_id in sorted(col):
        t.add_row(col[married_id])
        
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
        errors += ["ERROR: INDIVIDUAL: US30: {}: Did not properly list all living married individuals"]
    file1.close()
    file2.close()
    return errors

def listmarried(indivs, fams):
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
    file = print_married(married)
    return file
