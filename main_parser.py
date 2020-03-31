import sys
import datetime
from prettytable import PrettyTable
sys.path.append('./testing/sprint1')
sys.path.append('./testing/sprint2')
import us02
import us03
import us06
import us21
import us22
import us27
import us29
import us30
import us31
import us33
import us35
import us36
import us38
import us39

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
    for indi_id in sorted(col):
        t.add_row(col[indi_id])
    print(t)

'''
    Print the table of families
'''
def print_fam_collection(col):
    t = PrettyTable()
    t.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for fam_id in sorted(col):
        t.add_row(col[fam_id])
    print(t)

'''
    Tester function for gedcom file
'''
def tester(file):
    return process_lines(get_valid(open_file(file)))

'''
    Collect errors using individuals and families dictionaries/lists
'''
def get_errors(indivs, fams, indivsLst, famsLst):
    errors = []
    errors += us02.bbm(indivs, fams)
    errors += us03.bbd(indivs)
    errors += us21.verify_correct_roles(indivs, fams)
    errors += us22.verify_unique_ids(indivsLst, famsLst)
    errors += us06.divorce_before_death(indivs, fams)
    return errors

'''
    Read valid lines, add information to individuals/families collections
'''
def process_lines(valid_lines):
    individuals = {}
    families = {}
    cur_type, cur_id, prev_tag = [''] * 3
    indiv_ids, fam_ids = [], []

    for line in valid_lines:
        lvl, tag, args = line
        if lvl == 0 and tag == 'INDI':
            # new individual
            cur_type = 'INDI'
            cur_id = args[0].strip('@')
            individuals[cur_id] = [''] * 9
            individuals[cur_id][0] = cur_id
            indiv_ids += [cur_id.upper()]

        elif lvl == 0 and tag == 'FAM':
            # new family
            cur_type = 'FAM'
            cur_id = args[0].strip('@')
            families[cur_id] = [''] * 8
            families[cur_id][0] = cur_id
            fam_ids += [cur_id.upper()]

        elif cur_type == 'INDI':
            # continue processing individual
            if tag == 'NAME':
                individuals[cur_id][1] = ' '.join(args)
            elif tag == 'SEX':
                individuals[cur_id][2] = args[0]
            elif tag == 'BIRT' or tag == 'DEAT':
                prev_tag = tag
            elif tag == 'DATE' and prev_tag == 'BIRT':
                individuals[cur_id][3] = str(datetime.datetime.strptime(' '.join(args), '%d %b %Y').date())
                prev_tag = ''
            elif tag == 'DATE' and prev_tag == 'DEAT':
                individuals[cur_id][5] = False
                individuals[cur_id][6] = str(datetime.datetime.strptime(' '.join(args), '%d %b %Y').date())
                prev_tag = ''
            elif tag == 'FAMC':
                if individuals[cur_id][7] == '': individuals[cur_id][7] = set()
                individuals[cur_id][7].add(args[0].strip('@'))
            elif tag == 'FAMS':
                if individuals[cur_id][8] == '': individuals[cur_id][8] = set()
                individuals[cur_id][8].add(args[0].strip('@'))

        elif cur_type == 'FAM':
            # continue processing family
            if tag == 'HUSB':
                families[cur_id][3] = args[0].strip('@')
                families[cur_id][4] = individuals[args[0].strip('@')][1]
            elif tag == 'WIFE':
                families[cur_id][5] = args[0].strip('@')
                families[cur_id][6] = individuals[args[0].strip('@')][1]
            elif tag == 'CHIL':
                if families[cur_id][7] == '': families[cur_id][7] = set()
                families[cur_id][7].add(args[0].strip('@'))
            elif tag == 'MARR' or tag == 'DIV':
                prev_tag = tag
            elif tag == 'DATE' and prev_tag == 'MARR':
                families[cur_id][1] = str(datetime.datetime.strptime(' '.join(args), '%d %b %Y').date())
                prev_tag = ''
            elif tag == 'DATE' and prev_tag == 'DIV':
                families[cur_id][2] = str(datetime.datetime.strptime(' '.join(args), '%d %b %Y').date())
                prev_tag = ''
    
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

    # finalize families
    for fam in families:
        # set NA if not divorced
        if families[fam][2] == '':
            families[fam][2] = 'NA'
        # set NA if no children
        if not isinstance(individuals[indi][7], set):
            individuals[indi][7] = 'NA'

    return (individuals, families, indiv_ids, fam_ids)

'''
    Check validity of lines and return a list of valid lines
'''
def get_valid(lines):
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
        try:
            if valid and not tag in tags[lvl]: valid = False
        except KeyError:
            continue

        # if line is valid, add it to valid lines to be processed
        if valid: valid_lines += [[lvl, tag, args]]

    return valid_lines

def open_file(filename):
    buffer = []
    # read input file and strip newlines
    try:
        with open(filename, 'r') as f:
            buffer = f.readlines()
        for i in range(len(buffer)):
            buffer[i] = buffer[i].rstrip()
    except FileNotFoundError:
        print("Error: Cannot find input file")
        raise SystemExit
    return buffer

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: gedcom.py <file>")
    else:
        buffer = open_file(sys.argv[1])
        
        # check validity & process lines
        collections = process_lines(get_valid(buffer))

        # collect errors
        errors = list(set(get_errors(*collections)))

        # print tables
        print('Individuals')
        print_indiv_collection(collections[0])
        print('Families')
        print_fam_collection(collections[1])

        # print errors
        print("")
        for err in errors: print(err)

        # List features (US29, US30, US31, US33, US38, US39)
        indivs, fams, indivsLst, famsLst = collections
        print('US27: Include individual ages when listing:')
        print(us27.indiv_prettytable(indivs))
        print('US29: List of deceased individuals:')
        us29.listdeceased(indivs)
        print('US30: List of living married individuals:')
        us30.listmarried(indivs, fams)
        print('US31: List of living single individuals:')
        us31.listsingle(indivs)
        print('US33: List of orphaned children:')
        us33.listorphaned(indivs, fams)
        print('US38: List of upcoming birthdays:')
        us38.list_upcoming_bdays(indivs, print_table=True, custom_date='2020-05-01')
        print('US39: List of upcoming anniversaries:')
        us39.list_upcoming_annivs(fams, print_table=True, custom_date='2020-05-01')
