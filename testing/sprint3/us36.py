# US31: Printing a list of all people in a GEDCOM file who died in the last 30 days

import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
import main_parser
from prettytable import PrettyTable

'''
    Given all the individuals in the family, list all people who died in the last 30 days
'''
def print_recently_deceased(col, print_table=True):
    t = PrettyTable()
    t.field_names = ["Individual ID", "Name", "Birthday"]
    for indiv_id in sorted(col):
        t.add_row(col[indiv_id])
    print(t)
    return t.get_string()

def list_recently_deceased(indivs, print_table=True, custom_date=None):
    died_recently = {}

    return print_recently_deceased(died_recently)
