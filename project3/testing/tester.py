# This module runs automated tests for a selected user story

# Filename formats: source files = usXX.py; tests = usXX_test.py; ged files = usXX.ged

import sys
from prettytable import PrettyTable
import glob
sys.path.insert(0, '../')
import gedcom

def test(testfile):
    # run tests found in test file
    pass

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
            test(us + '_test.py')
        elif us == 'quit':
            break
        else:
            print("Error: Unknown user story")

prompt_for_test()
