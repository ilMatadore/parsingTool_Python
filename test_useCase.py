import unittest
import useCase


class TestParseUtil(unittest.TestCase):

    def test_parse_file(self):
        test_param1 = 'test_config_1.txt'
        result = useCase.parse_file(test_param1)
        returned_string1 = 'Starting server for host test2.com:8000. Debugging in port 8001'
        returned_string2 = 'Verbose logging enabled'
        self.assertMultiLineEqual(result, returned_string1 + ' ' + returned_string2)

    def test_parse_file2(self):
        test_param1 = 'test_config_2.txt'
        result = useCase.parse_file(test_param1)
        returned_string1 = None
        self.assertEqual(result, returned_string1)


if __name__ == '__main__':
    unittest.main()