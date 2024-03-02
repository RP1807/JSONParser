"""
Build your own JSON Parser.
See - https://codingchallenges.fyi/challenges/challenge-json-parser
"""
import argparse
import sys
import traceback
from argparse import ArgumentParser
from lib.JSONParser import JSONParser
from lib.jexception import JSONException


def main():
    parser = ArgumentParser(description="Command line tool to parse JSON files")
    parser.add_argument('file', type=argparse.FileType(), help="Provide JSON file to read")

    # Parse command line inputs
    args = parser.parse_args()
    file = args.file

    # Read file
    contents = file.read()

    try:
        result = JSONParser().parse(contents)
        print(result)
        # print(type(result))
    except JSONException as ex:
        print(ex)
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)


if __name__ == '__main__':
    main()


