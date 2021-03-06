# This module runs the tests and reports test results

# Filename formats: source files = usXX.py; tests = usXX_test.py; ged files = usXX_XX.ged

import sys
import glob
import unittest
from prettytable import PrettyTable
sys.path.insert(0, '../')
sys.path.insert(0, './sprint1/')
sys.path.insert(0, './sprint2/')
sys.path.insert(0, './sprint3/')
sys.path.insert(0, './sprint4/')
import main_parser
import us01_test
import us02_test
import us03_test
import us04_test
import us05_test
import us06_test
import us15_test
import us17_test
import us18_test
import us21_test
import us22_test
import us23_test
import us24_test
import us27_test
import us28_test
import us29_test
import us30_test
import us31_test
import us32_test
import us33_test
import us35_test
import us36_test
import us38_test
import us39_test
from us01_test import Tests as us01tests
from us02_test import Tests as us02tests
from us03_test import Tests as us03tests
from us04_test import Tests as us04tests
from us05_test import Tests as us05tests
from us06_test import Tests as us06tests
from us15_test import Tests as us15tests
from us17_test import Tests as us17tests
from us18_test import Tests as us18tests
from us21_test import Tests as us21tests
from us22_test import Tests as us22tests
from us23_test import Tests as us23tests
from us24_test import Tests as us24tests
from us27_test import Tests as us27tests
from us28_test import Tests as us28tests
from us29_test import Tests as us29tests
from us30_test import Tests as us30tests
from us31_test import Tests as us31tests
from us32_test import Tests as us32tests
from us33_test import Tests as us33tests
from us35_test import Tests as us35tests
from us36_test import Tests as us36tests
from us38_test import Tests as us38tests
from us39_test import Tests as us39tests

'''
    Print the errors produced by tests
'''
def report_test_results(results):
    errs = list(set(results))
    for err in errs:
        print(err)

'''
    Run all tests and return errors
'''
def get_all_results():
    results = []
    results += get_sprint1_results()
    results += get_sprint2_results()
    results += get_sprint3_results()
    results += get_sprint4_results()
    return results

'''
    Run tests for each user story in Sprint 1 and collect error messages
'''
def get_sprint1_results():
    results = []

    us02_test.unittest.main(argv=[''], exit=False)
    results += us02_test.test_results()

    us03_test.unittest.main(argv=[''], exit=False)
    results += us03_test.test_results()

    us21_test.unittest.main(argv=[''], exit=False)
    results += us21_test.test_results()

    us22_test.unittest.main(argv=[''], exit=False)
    results += us22_test.test_results()

    us29_test.unittest.main(argv=[''], exit=False)
    results += us29_test.test_results()

    us30_test.unittest.main(argv=[''], exit=False)
    results += us30_test.test_results()

    return results

'''
    Run tests for each user story in Sprint 2 and collect error messages
'''
def get_sprint2_results():
    results = []
    
    us06_test.unittest.main(argv=[''], exit=False)
    results += us06_test.test_results()

    us27_test.unittest.main(argv=[''], exit=False)
    results += us27_test.test_results()

    us31_test.unittest.main(argv=[''], exit=False)
    results += us31_test.test_results()

    us33_test.unittest.main(argv=[''], exit=False)
    results += us33_test.test_results()

    us38_test.unittest.main(argv=[''], exit=False)
    results += us38_test.test_results()

    us39_test.unittest.main(argv=[''], exit=False)
    results += us39_test.test_results()

    return results

'''
    Run tests for each user story in Sprint 3 and collect error messages
'''
def get_sprint3_results():
    results = []
    
    us04_test.unittest.main(argv=[''], exit=False)
    results += us04_test.test_errors()

    us05_test.unittest.main(argv=[''], exit=False)
    results += us05_test.test_errors()

    us23_test.unittest.main(argv=[''], exit=False)
    results += us23_test.test_results()

    us24_test.unittest.main(argv=[''], exit=False)
    results += us24_test.test_results()

    us35_test.unittest.main(argv=[''], exit=False)
    results += us35_test.test_results()

    us36_test.unittest.main(argv=[''], exit=False)
    results += us36_test.test_results()

    return results

'''
    Run tests for each user story in Sprint 4 and collect error messages
'''
def get_sprint4_results():
    results = []
    
    us01_test.unittest.main(argv=[''], exit=False)
    results += us01_test.test_errors()

    us15_test.unittest.main(argv=[''], exit=False)
    results += us15_test.test_errors()

    us17_test.unittest.main(argv=[''], exit=False)
    results += us17_test.test_errors()

    us18_test.unittest.main(argv=[''], exit=False)
    results += us18_test.test_errors()

    us28_test.unittest.main(argv=[''], exit=False)
    results += us28_test.test_results()

    us32_test.unittest.main(argv=[''], exit=False)
    results += us32_test.test_results()

    return results

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: tester.py <all/sprint1/sprint2/sprint3/sprint4>")
    else:
        if sys.argv[1] == 'all':
            get_all_results()
        elif sys.argv[1] == 'sprint1':
            report_test_results(get_sprint1_results())
        elif sys.argv[1] == 'sprint2':
            report_test_results(get_sprint2_results())
        elif sys.argv[1] == 'sprint3':
            report_test_results(get_sprint3_results())
        elif sys.argv[1] == 'sprint4':
            report_test_results(get_sprint4_results())
        else:
            print("Error: Option not recognized")
