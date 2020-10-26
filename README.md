# parsingTool_Python

Create a parsing tool that takes a config file and turns it into a usable object in the language of your choice (hash, JSON object, associative array, class, etc).

1. Do not use existing "complete" configuration parsing libraries/functions, we want to see how you would write the code to do this.

2. Use of core and stdlib functions/objects such as string manipulation, regular expressions, etc is ok.

3. We should be able to get the values of the config parameters in code, via their name. How this is done specifically is up to you.

4. Boolean-like config values (on/off, yes/no, true/false) should return real booleans: true/false.

5. Numeric config values should return real numerics: integers, doubles, etc

6. Ignore or error out on invalid config lines, your choice.

7. Please include a short example usage of your code so we can see how you call it/etc.

8. Push your work to a public git repository (github, bitbucket, etc) and send us the link.

# Assumptions

1. Config file is txt

2. Comments start with # either at the beggining of a line or in a line

3. Valid config lines have an equal sign (=)

# How to run

From the command line, run main.py file with a configuration file as parameter
```
python main.py config.txt
```
An object will be printed and a output.json file will be generated
```
{'host': 'test.com', 'server_id': 55331, 'server_load_alarm': 2.5, 'user': 'user', 'port': 8080, 'verbose': True, 'test_mode': True, 'debug_mode': False, 'log_file_path': '/tmp/logfile.log', 'send_notifications': True}
```
Specific keys can be requested as additional parameters:
```
python main.py config.txt host user verbose
```
An object with the requested keys and values will be printed and a output.json file will be generated.
```
{'host': 'test.com', 'user': 'user', 'verbose': True}
```

# Use Case

A server is starting based on configuration file, once file is parsed, specific keys are called by name and their values are printed in a string
```
python useCase.py config.txt
```
Keys 'host', 'port' and 'verbose' are called by name and the following strings are printed:
```
Starting server for host test.com:8080. Debugging in port 8081
Verbose logging enabled
```

# Unit Tests

Each function in parse_util.py has been tested with three different scenarios.

```
> python test.py -v

test_concatenate_objects1 (__main__.TestParseUtil) ... ok
test_concatenate_objects2 (__main__.TestParseUtil) ... ok
test_get_key_value1 (__main__.TestParseUtil) ... ok
test_get_key_value2 (__main__.TestParseUtil) ... ok
test_get_key_value3 (__main__.TestParseUtil) ... ok
test_is_false1 (__main__.TestParseUtil) ... ok
test_is_false2 (__main__.TestParseUtil) ... ok
test_is_false3 (__main__.TestParseUtil) ... ok
test_is_float1 (__main__.TestParseUtil) ... ok
test_is_float2 (__main__.TestParseUtil) ... ok
test_is_float3 (__main__.TestParseUtil) ... ok
test_is_true1 (__main__.TestParseUtil) ... ok
test_is_true2 (__main__.TestParseUtil) ... ok
test_is_true3 (__main__.TestParseUtil) ... ok
test_parse_configuration (__main__.TestParseUtil) ... ok
test_parse_configuration2 (__main__.TestParseUtil) ... ok
test_parse_configuration3 (__main__.TestParseUtil) ... ok
test_parse_line1 (__main__.TestParseUtil) ... ok
test_parse_line2 (__main__.TestParseUtil) ... ok
test_parse_line3 (__main__.TestParseUtil) ... ok
test_valid_line (__main__.TestParseUtil) ... ok
test_valid_line2 (__main__.TestParseUtil) ... ok
test_valid_line3 (__main__.TestParseUtil) ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.004s

OK
```
