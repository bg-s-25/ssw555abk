#compares the result_text of the user story to the result_file which is the expected output

def compare(result_text, result_file, us_num):
    errors = []
    result_file = open(result_file, 'r')
    if (result_file.read() != result_text):
        if (us_num == "US27"):
            errors += ["ERROR: INDIVIDUAL: US27: Did not properly list the age of all individuals"]

        elif (us_num == "US28"):
            errors += ["ERROR: FAMILY: US28: Did not properly list siblings in decreasing order"]
        
        elif (us_num == "US29"):
            errors += ["ERROR: INDIVIDUAL: US29: Did not properly list all dead individuals"]

        elif (us_num == "US30"):
            errors += ["ERROR: INDIVIDUAL: US30: Did not properly list all living married individuals"]

        elif (us_num == "US31"):
            errors += ["ERROR: INDIVIDUAL: US31: Did not properly list all single individuals over 30"]

        elif (us_num == "US32"):
            errors += ["ERROR: FAMILY: US32: Did not properly list all multiple births"]

        elif (us_num == "US33"):
            errors += ["ERROR: INDIVIDUAL: US33: Did not properly list all living orphaned individuals"]

        elif (us_num == "US35"):
            errors += ["ERROR: INDIVIDUAL: US35: Did not properly list all individuals born in the last 30 days"]

        elif (us_num == "US36"):
            errors += ["ERROR: INDIVIDUAL: US36: Did not properly list all individuals who died in the last 30 days"]

        elif (us_num == "US38"):
            errors += ["ERROR: INDIVIDUAL: US38: Did not properly list all upcoming birthdays"]

        elif (us_num == "US39"):
            errors += ["ERROR: INDIVIDUAL: US38: Did not properly list all upcoming anniversaries"]
    result_file.close()
    return errors