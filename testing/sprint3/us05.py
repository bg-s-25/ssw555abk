# US05: Marriage should occur before death of either spouse

import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser

'''
    Given individuals, ensure that the individual has married before death (married < death)
'''

def marriage_before_death(individuals,families):
    errors = []
    for family in families.values():
        if (family[1] != 'NA'): #check to see if the family has been married
            #first check if husband married before death
            if (family[3] != 'NA'): #check to see if family has a husband
                husband_id = family[3]
                death = individuals[husband_id][6]
                if (death != 'NA' and death  <= family[1]):
                    errors += ["ERROR: FAMILY: US05: {}: Married {} after husband's ({}) death on {}".format(family[0],family[1],husband_id,death)]
            #second check if wife married before death
            if (family[5] != 'NA'): #check to see if family has a wife
                wife_id = family[5]
                death = individuals[wife_id][6]
                if (death != 'NA' and death  <= family[1]):
                    errors += ["ERROR: FAMILY: US05: {}: Married {} after wife's ({}) death on {}".format(family[0],family[1],wife_id,death)]
    return errors