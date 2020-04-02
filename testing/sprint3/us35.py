# US35: Printing a list of all people in a GEDCOM file who were born in the last 30 days

import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all people who were born in the last 30 days
'''

def print_recently_born(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["Individual ID", "Name", "Birthday"]
    for indiv_id in sorted(col):
        t.add_row(col[indiv_id])
    print(t)
    return t.get_string()

def check_bday(bday):
    today = datetime.today().strftime('%Y-%m-%d')
    today = datetime.strptime(today, '%Y-%m-%d').date()     #making today datetime object

    bday = datetime.strptime(bday, '%Y-%m-%d').date()       #making bday datetime object
    
    daysago30 = today - bday       #determining how many days ago it was
    
    return daysago30

def list_recently_born(indivs):
    born_recently = {}
    for indiv_id in indivs:
        bday = indivs[indiv_id][3]
        if check_bday(bday) < timedelta(30):
            born_recently[indiv_id] = [''] * 3
            born_recently[indiv_id][0] = indiv_id #id
            born_recently[indiv_id][1] = indivs[indiv_id][1] #name
            born_recently[indiv_id][2] = indivs[indiv_id][3] #birthday
    return print_recently_born(born_recently)