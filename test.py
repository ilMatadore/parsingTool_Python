import unittest
import parse_util


class TestParseUtil(unittest.TestCase):

    def test_is_float1(self):
        test_param = 1.0
        result = parse_util.is_float(test_param)
        self.assertTrue(result)

    def test_is_float2(self):
        test_param = 1
        result = parse_util.is_float(test_param)
        self.assertTrue(result)

    def test_is_float3(self):
        test_param = 'string'
        result = parse_util.is_float(test_param)
        self.assertFalse(result)

    def test_is_true1(self):
        test_param = 'TRUE'
        result = parse_util.is_true(test_param)
        self.assertTrue(result)

    def test_is_true2(self):
        test_param = 1234
        result = parse_util.is_true(test_param)
        self.assertFalse(result)

    def test_is_true3(self):
        test_param = 'ofF'
        result = parse_util.is_true(test_param)
        self.assertFalse(result)

    def test_is_false1(self):
        test_param = 'FALSE'
        result = parse_util.is_false(test_param)
        self.assertTrue(result)

    def test_is_false2(self):
        test_param = 1234
        result = parse_util.is_false(test_param)
        self.assertFalse(result)

    def test_is_false3(self):
        test_param = 'yEs'
        result = parse_util.is_false(test_param)
        self.assertFalse(result)

    def test_parse_line1(self):
        obj1 = {}
        obj2 = {"testKey": "testValue"}
        result = parse_util.concatenate_objects(obj1, obj2)
        self.assertEqual(result, {"testKey": "testValue"})

    def test_parse_line2(self):
        obj1 = {"a": "b"}
        obj2 = {"testKey2": 2}
        result = parse_util.concatenate_objects(obj1, obj2)
        self.assertEqual(result, {"a": "b", "testKey2": 2})

    def test_parse_line3(self):
        obj1 = {"a": "b"}
        obj2 = {"testKey2": False}
        result = parse_util.concatenate_objects(obj1, obj2)
        self.assertEqual(result, {"a": "b", "testKey2": False})

    def test_get_key_value1(self):
        test_param = "test_line = 123"
        result = parse_util.parse_line(test_param)
        self.assertEqual(result, {"test_line": 123})

    def test_get_key_value2(self):
        test_param = "test_line2="
        result = parse_util.parse_line(test_param)
        self.assertEqual(result, {"test_line2": ""})

    def test_get_key_value3(self):
        test_param = "="
        result = parse_util.parse_line(test_param)
        self.assertEqual(result, {"": ""})

    def test_concatenate_objects1(self):
        test_param1 = {}
        test_param2 = {"testKey": "testValue"}
        result = parse_util.concatenate_objects(test_param1, test_param2)
        self.assertEqual(result, {"testKey": "testValue"})

    def test_concatenate_objects2(self):
        test_param1 = {"testKey1": "testValue1"}
        test_param2 = {"testKey2": "testValue2"}
        result = parse_util.concatenate_objects(test_param1, test_param2)
        self.assertEqual(result, {"testKey1": "testValue1", "testKey2": "testValue2"})

    def test_concatenate_objects2(self):
        test_param1 = {"testKey1": "testValue1"}
        test_param2 = {}
        result = parse_util.concatenate_objects(test_param1, test_param2)
        self.assertEqual(result, {"testKey1": "testValue1"})

    def test_valid_line(self):
        test_param1 = "Test line with = sign"
        result = parse_util.valid_line(test_param1)
        self.assertTrue(result)

    def test_valid_line2(self):
        test_param1 = ""
        result = parse_util.valid_line(test_param1)
        self.assertFalse(result)

    def test_valid_line3(self):
        test_param1 = "Test line with no equal sign"
        result = parse_util.valid_line(test_param1)
        self.assertFalse(result)

    def test_parse_configuration(self):
        test_param1 = ['# This is what a comment looks like, ignore it\n', '# All these config lines are valid\n',
                       'host = test.com\n', 'server_id=55331\n', 'server_load_alarm=2.5\n', 'user= user\n',
                       '# comment can appear here as well\n', 'verbose =true\n',
                       'test_mode = on\n', 'debug_mode = off\n', 'log_file_path = /tmp/logfile.log\n',
                       'send_notifications = yes\n', 'verbose=False']
        result = parse_util.parse_configuration(test_param1)
        self.assertEqual(result, {'host': 'test.com', 'server_id': 55331, 'server_load_alarm': 2.5, 'user': 'user',
                                  'verbose': False, 'test_mode': True, 'debug_mode': False,
                                  'log_file_path': '/tmp/logfile.log', 'send_notifications': True})

    def test_parse_configuration2(self):
        test_param1 = []
        result = parse_util.parse_configuration(test_param1)
        self.assertEqual(result, {})

    def test_parse_configuration3(self):
        test_param1 = ['testKey = 123']
        result = parse_util.parse_configuration(test_param1)
        self.assertEqual(result, {'testKey': 123})


if __name__ == '__main__':
    unittest.main()