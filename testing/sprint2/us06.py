# US06: Divorce can only occur before death of both spouses

import sys
sys.path.insert(0, '../../')
import main_parser
from datetime import datetime
from prettytable import PrettyTable

'''
    Given all the divorces in the family, check that divorce occurs before the death of both spouses
'''

def divorce_before_death(indivs, fams):
    errors = []
    for fam_id in fams:
     #checks that person is divorced
        if (fams[fam_id][2] != "NA"):        
            divorce_day = datetime.strptime(fams[fam_id][2], '%Y-%m-%d').date()    #convert divorce date to date object
            husb_id = fams[fam_id][3] 
            wife_id = fams[fam_id][5]
        #check if the husb and wife are deceased
            if (indivs[husb_id][6] != 'NA' and indivs[wife_id][6] != 'NA'):         
                husb_death_date = datetime.strptime(indivs[husb_id][6], '%Y-%m-%d').date()     #convert the dates to date object
                wife_death_date = datetime.strptime(indivs[wife_id][6], '%Y-%m-%d').date()
        #check if the divorce occurs after the deaths of the couple
                if (divorce_day > wife_death_date and divorce_day > husb_death_date):
                    errors += ["ERROR: INDIVIDUAL: US06: {}: Divorce occured after the death of both spouses".format(fam_id)]
    return errors