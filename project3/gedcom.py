'''
    Title  : SSW 555 A - Project 03
'''

import sys

tags = {
    'INDI': 0,
    'NAME': 1,
    'SEX': 1,
    'BIRT': 1,
    'DEAT': 1,
    'FAMC': 1,
    'FAMS': 1,
    'FAM': 0,
    'MARR': 1,
    'HUSB': 1,
    'WIFE': 1,
    'CHIL': 1,
    'DIV': 1,
    'DATE': 2,
    'HEAD': 0,
    'TRLR': 0,
    'NOTE': 0
}

valid = {'0': ['INDI', 'FAM', 'HEAD','TRLR','NOTE'],
             '1': ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'],
             '2':'DATE'}



def process(lvl, tag, args):

    individuals = {}

    families = {}


# print each line and separate the level, tag, arguments and tell if it is valid
def check_valid(lines):
    for line in lines:
        
        line = line.split()
        valid = True

        # # get level, tag, args, THEN valid
        tag = ''
        lvl = -1
        args = ''

        # identify the tag, level, other args
        if len(line) > 2 and (line[2] == 'INDI' or line[2] == 'FAM'):
            tag = line[2]
            lvl = int(line[0])
            args = line[1] + ' ' + ' '.join(line[3:])
        else:
            tag = line[1]
            lvl = int(line[0])
            args = ' '.join(line[2:])

            # wrongly placed INDI or FAM tag?
            if tag in ['INDI', 'FAM']:
                valid = False
            
        # valid tag?
        if valid and not tag in tags.keys():
            valid = False
        # valid level for tag?
        elif valid and not lvl == tags[tag]:
            valid = False

        if valid:
            process(lvl, tag, args)
        # print result
        #print('<-- ' + str(lvl) + '|' + tag + '|' + (lambda val: 'Y' if val else 'N')(valid) + '|' + args)

# entry point
if len(sys.argv) != 2:
    print("Usage: gedcom.py <file>")
else:
    buffer = []
    try:
        with open(sys.argv[1], 'r') as f:
            buffer = f.readlines()
        for i in range(len(buffer)):
            buffer[i] = buffer[i].rstrip()
    except FileNotFoundError:
        print("no file")
        raise SystemExit
    

    # read input file and strip newlines
    

    # print file lines and check validity
    check_lines(buffer)
