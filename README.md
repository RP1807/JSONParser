# JSONParser
Build your own JSONParser Challenge
See - https://codingchallenges.fyi/challenges/challenge-json-parser

## Requirements
Python 3.10+

## Usage
```commandline
python main.py -h
usage: main.py [-h] file

Command line tool to parse JSON files

positional arguments:
  file        Provide JSON file to read

options:
  -h, --help  show this help message and exit
```

### Example input JSON in test.json
```json
{"JSON Test Pattern pass3": {"The outermost value": "must be an object or array.", "In this test": "It is an object."}}
```
### Steps to run parser
```commandline
python main.py test.json
```

### Example output (Python dict)
```
{'JSON Test Pattern pass3': {'The outermost value': 'must be an object or array.', 'In this test': 'It is an object.'}}
```

## Unit Tests
```commandline
python -m unittest -v tests.py
```
### Results
````text
test_invalid_step_1 (tests.TestJSONParser.test_invalid_step_1) ... ok
test_invalid_step_2 (tests.TestJSONParser.test_invalid_step_2) ... ok
test_invalid_step_2_1 (tests.TestJSONParser.test_invalid_step_2_1) ... ok
test_invalid_step_3 (tests.TestJSONParser.test_invalid_step_3) ... ok
test_invalid_step_4 (tests.TestJSONParser.test_invalid_step_4) ... ok
test_valid_step_1 (tests.TestJSONParser.test_valid_step_1) ... ok
test_valid_step_2 (tests.TestJSONParser.test_valid_step_2) ... ok
test_valid_step_2_1 (tests.TestJSONParser.test_valid_step_2_1) ... ok
test_valid_step_3 (tests.TestJSONParser.test_valid_step_3) ... ok
test_valid_step_4 (tests.TestJSONParser.test_valid_step_4) ... ok
test_valid_step_4_1 (tests.TestJSONParser.test_valid_step_4_1) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.008s

OK
````