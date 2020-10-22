import unittest
import main


class TestMain(unittest.TestCase):
    def test_is_float(self):
        test_param = 1.0
        result = main.is_float(test_param)
        self.assertEqual(result, True)

    def test_is_float2(self):
        test_param = 1
        result = main.is_float(test_param)
        self.assertEqual(result, True)

    def test_is_float3(self):
        test_param = 'string'
        result = main.is_float(test_param)
        self.assertEqual(result, False)

    def test_is_true(self):
        test_param = 'TRUE'
        result = main.is_true(test_param)
        self.assertEqual(result, True)

    def test_is_true2(self):
        test_param = 1234
        result = main.is_true(test_param)
        self.assertEqual(result, False)

    def test_is_true3(self):
        test_param = 'ofF'
        result = main.is_true(test_param)
        self.assertEqual(result, None)

    def test_is_false(self):
        test_param = 'FALSE'
        result = main.is_false(test_param)
        self.assertEqual(result, True)

    def test_is_false2(self):
        test_param = 1234
        result = main.is_false(test_param)
        self.assertEqual(result, False)

    def test_is_false3(self):
        test_param = 'yEs'
        result = main.is_false(test_param)
        self.assertEqual(result, None)

    def test_parse_line(self):
        test_param1 = {}
        test_param2 = "testKey"
        test_param3 = "testValue"
        result = main.parse_line(test_param1, test_param2, test_param3)
        self.assertEqual(result, {"testKey": "testValue"})

    def test_parse_line2(self):
        test_param1 = {"a": "b"}
        test_param2 = "testKey2"
        test_param3 = '2'
        result = main.parse_line(test_param1, test_param2, test_param3)
        self.assertEqual(result, {"a": "b", "testKey2": 2})

    def test_parse_line3(self):
        test_param1 = {"a": "b"}
        test_param2 = "testKey2"
        test_param3 = 'false'
        result = main.parse_line(test_param1, test_param2, test_param3)
        self.assertEqual(result, {"a": "b", "testKey2": False})

    # def test_parsefile(self):


unittest.main()

