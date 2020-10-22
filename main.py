import sys
import json


def parsefile(args):

    obj = {}

    with open(args) as data:
        for line in data:
            try:
                if line.find('#') == 0:

                    # if line starts with '#' ignore
                    pass

                elif '#' in line:

                    # if line contains a comment remove it from line
                    line_split = line.split('#')
                    key = line_split[0].split('=')[0].strip()
                    value = line_split[0].split('=')[1].strip()

                    # call parse_line with line without comment
                    parse_line(obj, key, value)

                else:
                    # any other line
                    line_split = line.split('=')
                    key = line_split[0].strip()
                    value = line_split[1].strip()

                    # call parse_line with each line
                    parse_line(obj, key, value)

            except IndexError:

                # ignore empty lines in txt file
                pass

    json_file = open("output.json", "w")
    json.dump(obj, json_file, indent=2)
    json_file.close()

    return json_file


def is_float(val):
    # checks if value is a float, if so returns True otherwise False.
    try:
        float(val)
        return True
    except ValueError:
        return False


def is_true(val):
    # checks if value is either 'true','on' or 'yes', if so returns True otherwise False
    # if value.lower() is not equal to any of the options it returns None which is False.
    try:
        if val.lower() == 'true' or val.lower() == 'on' or val.lower() == 'yes':
            return True
    except AttributeError:
        return False


def is_false(val):
    # checks if value is either 'false','off' or 'no', if so returns True otherwise False
    # if value.lower() is not equal to any of the options it returns None which is False.
    try:
        if val.lower() == 'false' or val.lower() == 'off' or val.lower() == 'no':
            return True
    except AttributeError:
        return False


def parse_line(obj, key, value):
    if is_true(value):
        obj[key] = True
    elif is_false(value):
        obj[key] = False
    elif value.isdigit():
        obj[key] = int(value)
    elif is_float(value):
        obj[key] = float(value)
    else:
        obj[key] = value
    return obj


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
