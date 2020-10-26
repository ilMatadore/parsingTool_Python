import sys
import json
from parse_util import parse_configuration


def parse_file(config_file, *args):
    try:
        file = open(config_file)
        lines = file.readlines()
        # call parse_configuration from parse_util passing config file as parameter
        # obj contains file parsed
        obj = parse_configuration(lines)
        file.close()
        # using json library, a file output.json is generated from obj
        json_file = open("output.json", "w")

        # prints obj and generates json file, filtered or not.
        if args:
            # if specific key/s are passed in cmd, response is filtered by requested keys
            filtered_obj = dict(filter(lambda item: item[0] in args[0], obj.items()))
            json_file = open("output.json", "w")
            # generates a filtered json file
            json.dump(filtered_obj, json_file, indent=2)
            # prints filtered object
            return print(filtered_obj)

        else:
            # generates a json file
            json.dump(obj, json_file, indent=2)
            json_file.close()
            # prints object
            return print(obj)
    except FileNotFoundError as err:
        print('Error occurred', err)


try:
    # display an error if a config file is not passed in cmd
    if __name__ == '__main__':
        if len(sys.argv) == 2:
            # pass file as parameter to parse_file()
            parse_file(sys.argv[1])
        elif len(sys.argv) > 2:
            # pass any additional parameter in cmd to parse_file() in order to filter by keys
            to_filter = sys.argv[2:]
            parse_file(sys.argv[1], to_filter)
        else:
            print("Please provide a config file")

except IndexError as err:
    print('Error occurred', err)

