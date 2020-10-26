import sys
from parse_util import parse_configuration


def parse_file(config_file):
    try:
        file = open(config_file)
        lines = file.readlines()
        # call parse_configuration from parse_util passing config file as parameter
        # obj contains file parsed
        obj = parse_configuration(lines)
        file.close()
        # getting values from obj in code via their name, in this example
        # we get 'host', 'port' and 'verbose' values from obj keys names.
        host_address = obj['host']
        port_number = obj['port']
        # port is parsed as integer
        debug_port = port_number + 1
        string_to_print = f"Starting server for host {host_address}:{port_number}. Debugging in port {debug_port}"
        print(string_to_print)

        verbose_logging = obj['verbose']
        # verbose is parsed as boolean
        if verbose_logging:
            enabled_verbose_to_print = "Verbose logging enabled"
            print(enabled_verbose_to_print)
            return string_to_print + ' ' + enabled_verbose_to_print
        else:
            disabled_verbose_to_print = "Verbose logging disabled"
            print(disabled_verbose_to_print)
            return string_to_print + ' ' + disabled_verbose_to_print

    except FileNotFoundError as err:
        return print('Error occurred', err)
    except KeyError as err:
        return print('Requested Key does not exist in config file', err)



try:
    # display an error if a config file is not passed in cmd
    if __name__ == '__main__':
        if len(sys.argv) == 2:
            # pass file as parameter to parse_file()
            parse_file(sys.argv[1])
        else:
            print("Please provide a config file")

except IndexError as err:
    print('Error occurred', err)

