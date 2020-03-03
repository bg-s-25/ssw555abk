# This module runs the tests and reports test results

# Filename formats: source files = usXX.py; tests = usXX_test.py; ged files = usXX_XX.ged

import sys
import glob
import unittest
from prettytable import PrettyTable
sys.path.insert(0, '../')
sys.path.insert(0, './sprint1/')
import main_parser
import us02_test
import us03_test
import us21_test
import us22_test
import us29_test
import us30_test
from us02_test import Tests as us02tests
from us03_test import Tests as us03tests
from us21_test import Tests as us21tests
from us22_test import Tests as us22tests
from us29_test import Tests as us29tests
from us30_test import Tests as us30tests

'''
    Print the errors produced by tests
'''
def report_test_results(results):
    errs = list(set(results))
    for err in errs:
        print(err)

'''
    Run tests for each user story in Sprint 1 and aggregate error messages
'''
def get_sprint1_results():
    results = []

    us02_test.unittest.main(exit=False)
    results += us02_test.test_results()

    us03_test.unittest.main(exit=False)
    results += us03_test.test_results()

    us21_test.unittest.main(exit=False)
    results += us21_test.test_results()

    us22_test.unittest.main(exit=False)
    results += us22_test.test_results()

    us29_test.unittest.main(exit=False)
    results += us29_test.test_results()

    us30_test.unittest.main(exit=False)
    results += us30_test.test_results()

    return results

def prompt_for_test():
    testfiles = glob.glob('sprint1/us*_test.py')
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
        us = input("\nTest which user story/sprint? (quit' to quit) -> ")
        if us in stories:
            print("For now, only testing 'all' works")
        elif us == 'sprint1':
            report_test_results(get_sprint1_results())
        elif us == 'quit':
            break
        else:
            print("Error: Unknown user story")

prompt_for_test()
