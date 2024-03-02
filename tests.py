import json
import os
import unittest
from lib.JSONParser import JSONParser
from lib.jexception import JSONException

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TESTS_DIR = os.path.join(BASE_DIR, "tests/")
STEP_1_TESTS_DIR = os.path.join(TESTS_DIR, "step1/")
STEP_2_TESTS_DIR = os.path.join(TESTS_DIR, "step2/")
STEP_3_TESTS_DIR = os.path.join(TESTS_DIR, "step3/")
STEP_4_TESTS_DIR = os.path.join(TESTS_DIR, "step4/")
STEP_5_TESTS_DIR = os.path.join(TESTS_DIR, "step5/")


class TestJSONParser(unittest.TestCase):

    @classmethod
    def setUp(cls):
        parser = JSONParser()
        cls.parser = parser

    def test_valid_step_1(self):
        file_path = os.path.join(STEP_1_TESTS_DIR, "valid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            result = self.parser.parse(contents=contents)
            self.assertEqual(result, dict(), f"FAILED: Expected: {dict()} found {result}")

    def test_invalid_step_1(self):
        file_path = os.path.join(STEP_1_TESTS_DIR, "invalid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            with self.assertRaises(expected_exception=JSONException):
                self.parser.parse(contents=contents)

    def test_valid_step_2(self):
        file_path = os.path.join(STEP_2_TESTS_DIR, "valid.json")
        expected_json = {"key": "value"}
        with open(file_path, 'r') as f:
            contents = f.read()
            result = self.parser.parse(contents=contents)
            self.assertEqual(result, expected_json, f"FAILED: Expected: {expected_json} found {result}")

    def test_valid_step_2_1(self):
        file_path = os.path.join(STEP_2_TESTS_DIR, "valid2.json")
        expected_json = {
            "key": "value",
            "key2": "value"
        }
        with open(file_path, 'r') as f:
            contents = f.read()
            result = self.parser.parse(contents=contents)
            self.assertEqual(result, expected_json, f"FAILED: Expected: {expected_json} found {result}")

    def test_invalid_step_2(self):
        file_path = os.path.join(STEP_2_TESTS_DIR, "invalid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            with self.assertRaises(expected_exception=JSONException):
                self.parser.parse(contents=contents)

    def test_invalid_step_2_1(self):
        file_path = os.path.join(STEP_2_TESTS_DIR, "invalid2.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            with self.assertRaises(expected_exception=JSONException):
                self.parser.parse(contents=contents)

    def test_valid_step_3(self):
        file_path = os.path.join(STEP_3_TESTS_DIR, "valid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            result = self.parser.parse(contents=contents)
            expected_result = {
                "key1": True,
                "key2": False,
                "key3": None,
                "key4": "value",
                "key5": 101
            }
            self.assertEqual(expected_result, result)

    def test_invalid_step_3(self):
        file_path = os.path.join(STEP_3_TESTS_DIR, "invalid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            with self.assertRaises(expected_exception=JSONException):
                self.parser.parse(contents=contents)

    def test_valid_step_4(self):
        file_path = os.path.join(STEP_4_TESTS_DIR, "valid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            result = self.parser.parse(contents=contents)
            expected_result = {
                "key": "value",
                "key-n": 101,
                "key-o": {},
                "key-l": []
            }
            self.assertEqual(result, expected_result, f"FAILED: Expected {expected_result} found {result}")

    def test_valid_step_4_1(self):
        file_path = os.path.join(STEP_4_TESTS_DIR, "valid2.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            result = self.parser.parse(contents=contents)
            expected_result = {
                "key": "value",
                "key-n": 101,
                "key-o": {
                    "inner key": "inner value"
                },
                "key-l": ["list value"]
            }
            self.assertEqual(result, expected_result, f"FAILED: Expected {expected_result} found {result}")

    def test_invalid_step_4(self):
        file_path = os.path.join(STEP_4_TESTS_DIR, "invalid.json")
        with open(file_path, 'r') as f:
            contents = f.read()
            with self.assertRaises(expected_exception=JSONException):
                self.parser.parse(contents=contents)

    # def test_valid_step_5(self):
    #     file_path = os.path.join(STEP_5_TESTS_DIR, "pass1.json")
    #     with open(file_path, 'r') as f:
    #         contents = f.read()
    #         expected_json = json.loads(contents)
    #         result = self.parser.parse(contents=contents)
    #         self.assertEqual(result, expected_json, f"FAILED: Expected {expected_json} found {result}")
