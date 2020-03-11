#compares the result_text of the user story to the result_file which is the expected output

def compare(result_text, result_file, us_num):
    errors = []
    result_file = open(result_file, 'r')
    if (result_file.read() != result_text):
        if (us_num == "US29"):
            errors += ["ERROR: INDIVIDUAL: US29: Did not properly list all dead individuals"]

        elif (us_num == "US30"):
            errors += ["ERROR: INDIVIDUAL: US30: Did not properly list all living married individuals"]

        elif (us_num == "US31"):
            errors += ["ERROR: INDIVIDUAL: US31: Did not properly list all single individuals over 30"]

        elif (us_num == "US33"):
            errors += ["ERROR: INDIVIDUAL: US33: Did not properly list all living orphaned individuals"]

        elif (us_num == "US38"):
            errors += ["ERROR: INDIVIDUAL: US38: Did not properly list all upcoming birthdays"]
    result_file.close()
    return errors