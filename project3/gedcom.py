'''
    Title : SSW 555 A - Project 03
    Date  : 02-10-2020
'''

import sys
import datetime
from prettytable import PrettyTable

tags = {0: ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'],
        1: ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
        2: ['DATE']}

'''
    Return the age given a birthdate in YYYY-MM-DD format
'''
def age(birth_date, death_date='NA'):
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

'''
    Print the table of individuals
'''
def print_indiv_collection(col):
    t = PrettyTable()
    t.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for indi_id in col:
        t.add_row(col[indi_id])
    print(t)

'''
    Print the table of families
'''
def print_fam_collection(col):
    # 
    t = PrettyTable()
    t.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for fam_id in col:
        t.add_row(col[fam_id])
    print(t)

def process(valid_lines):
    individuals = {}
    families = {}
    cur_type, cur_id, prev_tag = [''] * 3

    for line in valid_lines:
        lvl, tag, args = line
        if lvl == 0 and tag == 'INDI':
            # new individual
            cur_type = 'INDI'
            cur_id = args[0].strip('@')
            individuals[cur_id] = [''] * 9
            individuals[cur_id][0] = cur_id

        elif lvl == 0 and tag == 'FAM':
            # new family
            cur_type = 'FAM'
            cur_id = args[0].strip('@')
            families[cur_id] = [''] * 8
            families[cur_id][0] = cur_id

        elif cur_type == 'INDI':
            # continue processing individual
            if tag == 'NAME':
                individuals[cur_id][1] = ' '.join(args)
            elif tag == 'SEX':
                individuals[cur_id][2] = args[0]
            elif tag == 'BIRT':
                prev_tag = 'BIRT'
            elif tag == 'DEAT':
                prev_tag = 'DEAT'
            elif tag == 'DATE' and prev_tag == 'BIRT':
                individuals[cur_id][3] = str(datetime.datetime.strptime(' '.join(args), '%d %b %Y').date())
                prev_tag = ''
            elif tag == 'DATE' and prev_tag == 'DEAT':
                individuals[cur_id][5] = False
                individuals[cur_id][6] = str(datetime.datetime.strptime(' '.join(args), '%d %b %Y').date())
            elif tag == 'FAMC':
                if individuals[cur_id][7] == '': individuals[cur_id][7] = set()
                individuals[cur_id][7].add(args[0].strip('@'))
            elif tag == 'FAMS':
                if individuals[cur_id][8] == '': individuals[cur_id][8] = set()
                individuals[cur_id][8].add(args[0].strip('@'))

        elif cur_type == 'FAM':
            # continue processing family
            pass
    
    # finalize individuals
    for indi in individuals:
        # set alive
        if individuals[indi][5] != False:
            # if not dead, then alive!
            individuals[indi][5] = True
            individuals[indi][6] = 'NA'
        # set ages
        individuals[indi][4] = age(individuals[indi][3], individuals[indi][6])
        # set NA if not a child or spouse
        if not isinstance(individuals[indi][7], set):
            individuals[indi][7] = 'NA'
        if not isinstance(individuals[indi][8], set):
            individuals[indi][8] = 'NA'

    print_indiv_collection(individuals)

# print each line and separate the level, tag, arguments and tell if it is valid
def check_valid(lines):
    valid_lines = []
    for line in lines:
        line = line.split()
        valid = True

        # get level, tag, args, THEN valid
        tag, lvl, args = '', -1, []

        # identify the tag, level, other args
        if len(line) > 2 and (line[2] == 'INDI' or line[2] == 'FAM'):
            lvl = int(line[0])
            tag = line[2]
            args = [line[1]] + line[3:]
        else:
            lvl = int(line[0])
            tag = line[1]
            args = line[2:]

            # wrongly placed INDI or FAM tag?
            if tag in ['INDI', 'FAM']:
                valid = False
        
        # valid tag/level?
        if valid and not tag in tags[lvl]: valid = False

        # if line is valid, add it to valid lines to be processed
        if valid: valid_lines += [[lvl, tag, args]]
        
        # print result
        # print('<-- ' + str(lvl) + '|' + tag + '|' + (lambda val: 'Y' if val else 'N')(valid) + '|' + args)
    
    # finally, pass the valid lines to be processed
    process(valid_lines)

# entry point
if len(sys.argv) != 2:
    print("Usage: gedcom.py <file>")
else:
    buffer = []
    # read input file and strip newlines
    try:
        with open(sys.argv[1], 'r') as f:
            buffer = f.readlines()
        for i in range(len(buffer)):
            buffer[i] = buffer[i].rstrip()
    except FileNotFoundError:
        print("Error: Cannot find input file")
        raise SystemExit

    # check validity & process lines
    check_valid(buffer)

    '''
    def familes(famId, block):
    x.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    prevtag = " "
    for line in block:
        if tag = "HUSB":
            #remove @ and store id
            husbID = "id"
        elif tag = "WIFE":
            #remove @ and store id
            husbID = "id"
        elif tag = "CHIL":
            #remove @ and store id
            husbID = "id"

        #if prevTag is set
        elif tag = "DATE" and prevtag = "MARR":
            marrDate = line[2:]
        elif if tag = "DATE" and prevtag = "DIV":
            divDate = line[2:]

        # knowing a date will follow, set the prevTag
        elif tag = "MARR": prevtag = "MARR"
        elif tag = "DIV": prevtag = "DIV"

        
    x.add_row([famId, marrDate, divDate, husbID, husbName, wifeID, wifeName, Child])

    '''
