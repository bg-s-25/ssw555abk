'''
    Title  : SSW 555 A - Project 03
'''

import sys
from prettytable import PrettyTable

tags = {0: ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'],
        1: ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
        2: ['DATE']}

def print_collection(col):
    x = PrettyTable()
    x.field_names = ["Id", "Name", "Sex", "c", "d", "e", "f", "g", "h"]
    for indi_id in col:
        x.add_row([indi_id, col[indi_id][1], col[indi_id][2], '', '', '', '', '', ''])
    print(x)

def print_family_collection(col):
    x = PrettyTable()
    x.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for indi_id in col:
        x.add_row([indi_id, col[indi_id][1], col[indi_id][2], '', '', '', '', '', ''])
    print(x)


def process(valid_lines):
    individuals = {}
    families = {}
    current = ('', '') # current type of collection & current id, e.g. ('INDI', 'I22')

    for line in valid_lines:
        lvl, tag, args = line
        if lvl == 0 and tag == 'INDI':
            # new individual
            current = ('INDI', args[0].strip('@'))
            individuals[current[1]] = [''] * 9
            individuals[current[1]][0] = current[1]

        elif lvl == 0 and tag == 'FAM':
            # new family
            current = ('FAM', args[0].strip('@'))
            families[current[1]] = [''] * 8
            families[current[1]][0] = current[1]
            pass

        elif current[0] == 'INDI':
            # continue processing individual
            if tag == 'NAME':
                individuals[current[1]][1] = ' '.join(args)
            elif tag == 'SEX':
                individuals[current[1]][2] = args[0]

        elif current[0] == 'FAM':
            # continue processing family
            pass
            
    print_collection(individuals)

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
        print("no file")
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
