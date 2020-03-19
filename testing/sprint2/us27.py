# US 27: Include person's current age when listing individuals

import sys
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
import main_parser
from prettytable import PrettyTable

#this converts the dictionary of individuals into pretty table form
#the age is found in main_parser.age()

def indiv_prettytable(col):
    t = PrettyTable()
    t.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for indi_id in sorted(col):
        t.add_row(col[indi_id])
    return t.get_string()
