# This module runs the tests and reports test results

# Filename formats: source files = usXX.py; tests = usXX_test.py; ged files = usXX_XX.ged

import sys
import glob
import unittest
from prettytable import PrettyTable
sys.path.insert(0, '../')
import gedcom
import us02_test
import us03_test
import us21_test
import us22_test
from us02_test import Tests as us02tests
from us03_test import Tests as us03tests
from us21_test import Tests as us21tests
from us22_test import Tests as us22tests

'''
    Print the errors produced by tests
'''
def report_test_results(results):
    errs = [x for sublst in results for x in sublst]
    errs = sorted(list(set(errs)))
    for err in errs:
        print(err)

'''
    Run tests for each user story and aggregate error messages
'''
def get_all_test_results():
    results = []

    us02_test.unittest.main(exit=False)
    results += us02_test.test_results()

    us03_test.unittest.main(exit=False)
    results += us03_test.test_results()

    us21_test.unittest.main(exit=False)
    results += us21_test.test_results()

    us22_test.unittest.main(exit=False)
    results += us22_test.test_results()

    return results

def prompt_for_test():
    testfiles = glob.glob('us*_test.py')
    t = PrettyTable()
    t.field_names = ["User Story", "Test File"]
    stories = []
    for testfile in testfiles:
        story = testfile.rstrip('_test.py')
        stories += [story]
        t.add_row([story, testfile])
    print("Available tests:")
    print(t)

    while True:
        us = input("\nTest which user story? ('all' to do all, quit' to quit) -> ")
        if us in stories:
            print("For now, only testing 'all' works")
        elif us == 'all':
            report_test_results(get_all_test_results())
        elif us == 'quit':
            break
        else:
            print("Error: Unknown user story")

prompt_for_test()
