# This module runs automated tests for a selected user story

# Filename formats: source files = usXX.py; tests = usXX_test.py; ged files = usXX_XX.ged

import sys
import glob
from prettytable import PrettyTable
sys.path.insert(0, '../')
import gedcom

def run_tests(testfile):
    # run tests found in test file
    mod = __import__('us21_test')
    func = getattr(mod, 'tester')
    func() # runs 0 tests, run tests via us21_test

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
        us = input("\nTest which user story? ('quit' to quit) -> ")
        if us in stories:
            run_tests(us + '_test.py')
        elif us == 'quit':
            break
        else:
            print("Error: Unknown user story")

prompt_for_test()
