'''
List siblings in families by decreasing age, i.e. oldest siblings first
'''
import sys
from datetime import datetime, timedelta
sys.path.insert(0, '../../')
sys.path.insert(0, '../sprint1')
sys.path.insert(0, '../sprint2')
import main_parser
from prettytable import PrettyTable

def print_siblings(dict,print_table):
    t = PrettyTable()
    t.field_names = ["Family ID", "Name", "Age"]
    for indiv_id in dict:
        t.add_row(dict[indiv_id])
    if print_table: print(t)
    return t.get_string()

def age(birth_date, death_date='NA'):
    ymd = birth_date.split('-')
    dob = datetime(*[int(x) for x in ymd])
    ymd = death_date.split('-')
    dod = datetime.today() if death_date == 'NA' else datetime(*[int(x) for x in ymd])
    day1 = dob.day
    day2 = dod.day
    mon1 = dob.month
    mon2 = dod.month
    year1 = dob.year
    year2 = dod.year
    if (day2 < day1):      
        # borrow days from february
        if (mon2 == 3):
            #  check whether year is a leap year
            if (year2 % 4 == 0):
                day2 += 29
            else:
                day2 += 28                        
        
        # borrow days from April or June or September or November
        elif (mon2 == 5 or mon2 == 7 or mon2 == 10 or mon2 == 12):
           day2 += 30                
        # borrow days from Jan or Mar or May or July or Aug or Oct or Dec
        else:
           day2 += 31
        mon2 = mon2 - 1
    
    if (mon2 < mon1):
        mon2 += 12
        year2 -= 1
    
    day_diff = day2 - day1
    mon_diff = mon2 - mon1
    year_diff = year2 - year1
    return [year_diff,"{}-{}-{}".format(year_diff,mon_diff,day_diff)]

def sort_people(birthdates):
    for i in range(1,len(birthdates)):
        current = birthdates[i]
        k = i - 1
        while (k >= 0 and birthdates[k][3] < current[3]):
            birthdates[k+1]=birthdates[k]
            k -= 1
        birthdates[k+1] = current

def list_siblings(indivs, families, print_table):
    sibling_order = []
    for fam_id in families:
        birthdates = []
        children = sorted(list(families[fam_id][7]))
        for child in families[fam_id][7]:
            birth_date = indivs[child][3]
            death_date = indivs[child][6]
            age_diff = age(birth_date,death_date)
            birthdates += [[fam_id] + [indivs[child][1]] + age_diff]
        # Uncomment this line for descending order of siblings in EACH family
        sort_people(birthdates)
        sibling_order += birthdates
    # Uncomment this line for descending order of siblings in ALL family
    # sort_people(sibling_order)
    sibling = {}
    for i in range(len(sibling_order)):
        sibling[i] = sibling_order[i][:3] 
    return print_siblings(sibling,print_table)


        
