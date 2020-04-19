# US01: Dates (birth, marriage, divorce, death) should not be after the current date
import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
sys.path.insert(0, '../sprint3')
import main_parser

'''
Given lists of individuals and families, dates of mariage, divorce, birth, and death should not be after the current date
'''

def check_date(date):
    today = datetime.today().strftime('%Y-%m-%d')
    today = datetime.strptime(today, '%Y-%m-%d').date()     #making today datetime object

    date = datetime.strptime(date, '%Y-%m-%d').date()       #making date datetime object
    
    if(today > date):       #determining if today occurs before date
        return True
    else:
        return False

def check_all_dates(indivs, fams):
    errors = []

    for indiv_id in indivs: 
        #gets birthday and checks if it is after the current date
        bday = indivs[indiv_id][3] 
        if (check_date(bday) == False):
            errors += ["ERROR: INDIVIDUAL: US01: {}: Birthday occurs before the current date".format(indiv_id)]
    
        #gets death date and checks if it is after the current date
        if indivs[indiv_id][6] != "NA":  #check if they have a death date
            death = indivs[indiv_id][6]
            if(check_date(death) == False):
                errors += ["ERROR: INDIVIDUAL: US01: {}: Death date occurs before the current date".format(indiv_id)]
             
    for fam_id in fams:
        #gets death date and checks if it is after the current date
        if (fams[fam_id][1] != "NA"):    #check if there is a marraige date
            married = fams[fam_id][1]
            if(check_date(married) == False):
                errors += ["ERROR: FAMILY: US01: {}: Marriage date occurs before the current date".format(fam_id)]
    
        #gets death date and checks if it is after the current date
        if (fams[fam_id][2] != "NA"):    #check if there is a divorced date
            divorced = fams[fam_id][2]
            if(check_date(divorced) == False):
                errors += ["ERROR: FAMILY: US01: {}: Divorce date occurs before the current date".format(fam_id)]

    return errors