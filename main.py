import sys
import json


def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def is_true(val):
    if val.lower() == 'true' or val.lower() == 'on' or val.lower() == 'yes':
        return True


def is_false(val):
    if val.lower() == 'false' or val.lower() == 'off' or val.lower() == 'no':
        print(val, val.lower())
        return True


def parsefile(args):
    file = args

    obj = {}

    with open(file) as data:
        for line in data:
            if line[0] == '#':
                pass
            else:
                line_split = line.split('=')
                value = line_split[1][:-1].lstrip()
                key = line_split[0].strip()

                if is_true(value):
                    obj[key] = True
                elif is_false(value):
                    obj[key] = False
                elif value.isdigit():
                    obj[key] = int(value)
                elif isfloat(value):
                    obj[key] = float(value)
                else:
                    obj[key] = value

    json_file = open("output.json", "w")
    json.dump(obj, json_file, indent=2)
    json_file.close()

    return json_file


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
