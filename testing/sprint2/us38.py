# US38: List upcoming birthdays (in the next 30 days)

import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

compare_files = []

def print_bdays(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["ID", "Name", "Birthday"]
    for indiv_id in sorted(col):
        t.add_row(col[indiv_id])
    # with open('output.txt', 'w') as f:
    #     f.write(t.get_string())
    if print_table: print(t)
    return t.get_string()

'''
    Given a date string in YYYY-MM-DD format, tell if the birthday is in the next 30 days
'''
def is_upcoming_bday(bday, date_now=datetime.date(datetime.now())):
    # if a custom date is provided, convert it to a date object
    if isinstance(date_now, str):
        date_now = datetime.strptime(date_now, '%Y-%m-%d').date()

    # bday manipulation
    bday = datetime.strptime(bday, '%Y-%m-%d').date()
    bday = bday.replace(year=date_now.year) # convert bday to have the same year, for comparison purposes

    # bday should be between now and 30 days from now
    bdaylessthan = date_now + timedelta(days=30)
    upcoming = bday > date_now and bday <= bdaylessthan
    return upcoming

def compare(result_text, file):
    errors = []
    file = open(file, 'r')
    if (file.read() != result_text):
        errors += ["ERROR: INDIVIDUAL: US38: Did not properly list all upcoming birthdays"]
    file.close()
    return errors

def list_upcoming_bdays(indivs, print_table=True, custom_date=None):
    upcoming_bdays = {}
    for indiv_id in indivs:
        if is_upcoming_bday(indivs[indiv_id][3], custom_date if custom_date is not None else datetime.date(datetime.now())):
            upcoming_bdays[indiv_id] = [''] * 3
            upcoming_bdays[indiv_id][0] = indiv_id # id
            upcoming_bdays[indiv_id][1] = indivs[indiv_id][1] # name
            upcoming_bdays[indiv_id][2] = indivs[indiv_id][3] # birthday
    return print_bdays(upcoming_bdays, print_table)
