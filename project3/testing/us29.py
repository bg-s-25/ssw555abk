# US29: Printing a list of deceased family members

import sys
sys.path.insert(0, '../')
import gedcom

'''
    Given all the individuals in the family, list all deceased individuals
'''

def listdeceased(indivs):
   deceased = {}
   for indivs_id in indivs:
        #check if they have a death date
        if (indivis[individs_id][6] != "NA"):
            deceased[cur_id] = [''] * 5
            deceased[cur_id][0] = individs_id #id
            deceased[cur_id][1] = individuals[individs_id][1] #name
            deceased[cur_id][2] = individuals[individs_id][3] #birthday
            deceased[cur_id][3] = age(individuals[individs_id][3], individuals[individs_id][6]) #age #***********
            deceased[cur_id][4] = individuals[individs_id][6] #death
    print_deceased(deceased)

def print_deceased(col):
    t = PrettyTable()
    t.field_names = ["ID", "Name", "Birthday", "Age", "Death"]
    for deceased_id in sorted(col):
        t.add_row(col[deceased_id])
    print(t)

def age(birth_date, death_date='NA'): #repeated from original doc.. edit this later
    ymd = birth_date.split('-')
    dob = datetime.datetime(*[int(x) for x in ymd])
    ymd = death_date.split('-')
    doc = datetime.datetime.today() if death_date == 'NA' else datetime.datetime(*[int(x) for x in ymd])
    yrs = doc.year - dob.year
    if dob.month > doc.month:
        yrs -= 1
    elif dob.month == doc.month and dob.day > doc.day:
        yrs -= 1
    return yrs















