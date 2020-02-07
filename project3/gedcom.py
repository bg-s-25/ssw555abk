'''
    Title  : SSW 555 A - Project 03
'''

import sys

tags = {0: ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'],
        1: ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
        2: ['DATE']}

def process(block):
    individuals = {}
    families = {}

# print each line and separate the level, tag, arguments and tell if it is valid
def check_valid(lines):
    cur_block = []
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

        # if new individual/family, process the current block; otherwise, append to the current block
        if valid and lvl == 0:
            process(cur_block)
            cur_block += [lvl, tag, args]
        elif valid:
            cur_block += [lvl, tag, args]
        
        # print result
        # print('<-- ' + str(lvl) + '|' + tag + '|' + (lambda val: 'Y' if val else 'N')(valid) + '|' + args)

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
