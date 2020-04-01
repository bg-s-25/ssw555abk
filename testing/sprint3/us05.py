# US05: Marriage should occur before death of either spouse

import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser

'''
    Given individuals, ensure that the individual has married before death
'''

def marriage_before_death(individuals,families):
    errors = []
    for indiv in individuals: #parse through all the individuals
        if (indiv[6] != 'NA' and indiv[8] != 'NA'): #person has died and person has married
            death = indiv[6] #string date of death
            spouses = indiv[8] #list of spouses
            for spouse in spouses: #parse each spouse of the individuals
                if families[spouse][1] >= death: #person has married after or on the day of the death
                    errors += ['ERROR: FAMILY: US05: {} Married after '] # add the entry to errors
    return errors