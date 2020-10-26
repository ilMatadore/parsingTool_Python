from functools import reduce


def parse_configuration(lines):
    # List comprehension
    list1 = [clean_line(line) for line in lines]  # removes comment lines, comments and whitespace
    list2 = [parse_line(line) for line in list1 if valid_line(line)]  # parse each line as string, int, boolean or
    # float and creates a key value pair from each = sign
    # Reduce
    obj = reduce(concatenate_objects, list2, {})
    return obj


def valid_line(line):
    return len(line) > 1 and line.find('=') > 0


def concatenate_objects(obj1, obj2):
    merged = dict()
    merged.update(obj1)
    merged.update(obj2)
    return merged


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
        else:
            return False
    except AttributeError:
        return False


def is_false(val):
    # checks if value is either 'false','off' or 'no', if so returns True otherwise False
    # if value.lower() is not equal to any of the options it returns None which is False.
    try:
        if val.lower() == 'false' or val.lower() == 'off' or val.lower() == 'no':
            return True
        else:
            return False
    except AttributeError:
        return False


def parse_line(line):
    obj = {}
    line_split = line.split('=')
    key = line_split[0].strip()
    value = line_split[1].strip()
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


def clean_line(s):
    # if line starts with # returns an empty string
    if s.find('#') == 0:
        return ''
    # if line contains a #, keep string (with no whitespace) on the left of the # assuming
    # what is on the right of it is a comment
    elif '#' in s:
        line_split = s.split('#')[0]
        return line_split.strip()
    # if the line does not have a # return the line with no whitespace
    else:
        return s.strip()
