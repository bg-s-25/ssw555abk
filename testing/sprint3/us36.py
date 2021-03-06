# US31: Printing a list of all people in a GEDCOM file who died in the last 30 days

import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
sys.path.insert(0, '../sprint4')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all people who died in the last 30 days
'''
def print_recently_deceased(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["Individual ID", "Name", "Death Date"]
    for indiv_id in sorted(col):
        t.add_row(col[indiv_id])
    if print_table: print(t)
    return t.get_string()

def check_dday(bday, custom_date=None):
    if custom_date is not None:
        today = datetime.strptime(custom_date, '%Y-%m-%d').date()
    else:
        today = datetime.today().strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d').date()     #making today datetime object

    dday = datetime.strptime(bday, '%Y-%m-%d').date()       #making dday datetime object
    
    daysago30 = today - dday       #determining how many days ago it was
    
    return daysago30

def list_recently_deceased(indivs, print_table, custom_date=None):
    died_recently = {}
    for indiv_id in indivs: 
        if indivs[indiv_id][6] != "NA":
            deathday = indivs[indiv_id][6]
            if check_dday(deathday, custom_date) < timedelta(30):
                died_recently[indiv_id] = [''] * 3
                died_recently[indiv_id][0] = indiv_id #id
                died_recently[indiv_id][1] = indivs[indiv_id][1] #name
                died_recently[indiv_id][2] = indivs[indiv_id][6] #deathday

    return print_recently_deceased(died_recently, print_table)