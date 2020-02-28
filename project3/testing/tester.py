# This module runs automated tests for a selected user story

# Filename formats: source files = usXX.py; tests = usXX_test.py; ged files = usXX_XX.ged

import sys
import glob
import unittest
from prettytable import PrettyTable
sys.path.insert(0, '../')
import gedcom
import us02_test
# import test_us03
from us02_test import Tests as us02tests
# from us03_test import Tests as us03tests
# import us21_test
# from us21_test import Tests as us21tests
# import us22_test
# from us22_test import Tests as us22tests

def report_test_results(results):
    print(results)
    # for r in results:
    #     if not r[0]: # test failed
    #         print(r[1]) # print error message

def get_all_test_results():
    results = []

    us02_test.unittest.main(exit=False)
    results += us02_test.test_results()

    # test_us03.unittest.main(exit=False)
    # results += test_us03.test_results()

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
            # run_tests(us + '_test.py')
            print("For now, only testing 'all' works")
        elif us == 'all':
            # get_all_test_results()
            report_test_results(get_all_test_results())
        elif us == 'quit':
            break
        else:
            print("Error: Unknown user story")

prompt_for_test()
