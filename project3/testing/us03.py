# US03: Birth before death

import sys
sys.path.insert(0, '../')
import gedcom


'''
    Given list of birth dates and death dates of individuals, ensure that all people are born before death
'''

# bbd = birth before death
def bbd(person):
    errors = []
    pers, births, deaths = listbirthsanddeaths(person)
    for i in range(len(pers)):
        '''
        Death can either be 'NA' for people who are alive
        or 'xxxx-xx-xx' for people who died
        Birth can either be '' for people who did not put birth
        or 'xxxx-xx-xx' for people who put in their info and are born
        Returns false if birth info is not put in or death has a 
        date before the birth date
        '''
        if (deaths[i] != 'NA' and births[i] >= deaths[i]) or births[i] == '': 
            errors += ["ERROR: FAMILY: US03: {}: Died {} before born {}".format(pers[i],deaths[i],births[i])]
    return [False] + errors if len(errors) > 0 else [True] + errors

# lists ids, births, deaths in 3 separate lists
def listbirthsanddeaths(person):
    individuals = []
    birth_list = []
    death_list = []
    for onepers in person.values():
        individuals += [onepers[0]]
        birth_list += [onepers[3]]
        death_list += [onepers[6]]
    return individuals, birth_list, death_list
