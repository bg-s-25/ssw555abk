# US38: List upcoming anniversaries (in the next 30 days)

import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

def print_annivs(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["Family ID", "Husband Name", "Wife Name", "Anniversary"]
    for fam_id in sorted(col):
        t.add_row(col[fam_id])
    if print_table: print(t)
    return t.get_string()

'''
    Given the date string in YYYY-MM-DD format, tell if the anniversary is in the next 30 days
'''
def is_upcoming_anniv(anniv, date_now=datetime.date(datetime.now())):
    # if a custom date is provided, convert it to a date object
    if isinstance(date_now, str):
        date_now = datetime.strptime(date_now, '%Y-%m-%d').date()

    # anniv manipulation
    anniv = datetime.strptime(anniv, '%Y-%m-%d').date()
    anniv = anniv.replace(year=date_now.year) # convert anniv to have the same year, for comparison purposes

    # anniv should be between now and 30 days from now
    annivlessthan = date_now + timedelta(days=30)
    upcoming = anniv > date_now and anniv <= annivlessthan
    return upcoming

def list_upcoming_annivs(fams, print_table=True, custom_date=None):
    upcoming_annivs = {}
    for fam_id in fams:
        if fams[fam_id][2] != 'NA': continue # do not display anniversary of divorced couple
        if is_upcoming_anniv(fams[fam_id][1], custom_date if custom_date is not None else datetime.date(datetime.now())):
            upcoming_annivs[fam_id] = [''] * 4
            upcoming_annivs[fam_id][0] = fam_id # id
            upcoming_annivs[fam_id][1] = fams[fam_id][4] # husband name
            upcoming_annivs[fam_id][1] = fams[fam_id][6] # wife name
            upcoming_annivs[fam_id][2] = fams[fam_id][1] # anniversary
    return print_annivs(upcoming_annivs, print_table)
