from lib.jtype import JType
from lib.jexception import JSONException


class JSONParser:

    def __init__(self):
        self.index = 0
        self.tokens = []  # list of tuple to store each token in string and its type

    def __next(self):
        if self.index >= len(self.tokens):
            raise JSONException(f"Unexpected end of JSON. Current index {self.index} "
                                f"length of contents {len(self.tokens)}")
        self.index += 1

    def __get_tokens(self, contents):
        index = 0

        while index < len(contents):
            content = contents[index]

            # Check for whitespaces
            if content.isspace():
                index += 1
                continue

            if content.isdigit() or content.startswith('-'):
                number = ""
                while contents[index] is not None and (contents[index].isdigit() or
                                                       contents[index] in ['-', '.', 'e', 'E', '+']):
                    number += str(contents[index])
                    index += 1
                self.tokens.append((number, JType.NUMBER.value))
            elif content.startswith('t') or content.startswith('f') or content.startswith('n'):
                value = ""
                while contents[index] is not None and contents[index].isalpha():
                    value += str(contents[index])
                    index += 1
                if value in ['true', 'false']:
                    self.tokens.append((value, JType.BOOLEAN.value))
                elif value in ['null']:
                    self.tokens.append((value, JType.NULL.value))
                else:
                    raise JSONException(f"Unexpected token {value} at index {index}")
            else:
                match content:
                    case JType.OPEN_BRACE.value:
                        self.tokens.append((content, JType.OPEN_BRACE.value))
                    case JType.CLOSE_BRACE.value:
                        self.tokens.append((content, JType.CLOSE_BRACE.value))
                    case JType.OPEN_BRACKET.value:
                        self.tokens.append((content, JType.OPEN_BRACKET.value))
                    case JType.CLOSE_BRACKET.value:
                        self.tokens.append((content, JType.CLOSE_BRACKET.value))
                    case '"':
                        index += 1
                        content = ""
                        while contents[index] != '"':
                            content += contents[index]
                            index += 1
                        self.tokens.append((content, JType.STRING.value))
                    case ':':
                        self.tokens.append((content, JType.COLON.value))
                    case ',':
                        self.tokens.append((content, JType.COMMA.value))
                    case _:
                        raise JSONException(f"Unexpected token '{content}' at index {index}")
                index += 1

    def parse(self, contents: str):
        contents.strip()

        if not contents.startswith(JType.OPEN_BRACE.value):
            if not contents.startswith(JType.OPEN_BRACKET.value):
                raise JSONException(f"Unexpected token at the start of index."
                                    f"Expected {JType.OPEN_BRACE.value} or {JType.OPEN_BRACKET.value} at position 0")
        # Tokenizer
        self.__get_tokens(contents)

        first_char = self.tokens[self.index][0]
        if first_char == JType.OPEN_BRACKET.value:
            final_result = self.__parse_json_array()
        else:
            final_result = self.__parse_json_object()

        # if  final_result and len(final_result) < len(self.tokens):
        #     raise JSONException(f"Unexpected token at the end at index {self.index}")
        return final_result

    def __parse_json_array(self):
        arr = []
        self.index += 1
        while self.tokens[self.index][1] != JType.CLOSE_BRACKET.value:
            value = self.__parse_value()
            arr.append(value)
        return arr

    def __parse_value(self):
        token = self.tokens[self.index][1]
        match token:
            case JType.STRING.value:
                result = self.__parse_string()
                self.index += 1
                return result
            case JType.NUMBER.value:
                result = self.__parse_number()
                self.index += 1
                return result
            case JType.BOOLEAN.value:
                result = self.tokens[self.index][0] == 'true'
                self.index += 1
                return result
            case JType.NULL.value:
                result = None
                self.index += 1
                return result
            case JType.OPEN_BRACKET.value:  # Parse JSON array
                result = self.__parse_json_array()
                self.index += 1
                return result
            case JType.OPEN_BRACE.value:  # Parse JSON object
                result = self.__parse_json_object()
                self.index += 1
                return result
            case _:
                raise JSONException(f'Unexpected token type: {self.tokens[self.index][1]}')

    def __parse_string(self):
        return str(self.tokens[self.index][0])

    def __parse_number(self):
        if '.' in self.tokens[self.index][0]:
            return float(self.tokens[self.index][0])
        else:
            return int(self.tokens[self.index][0])

    def __parse_json_object(self):
        result = dict()
        self.__next()
        while self.tokens[self.index][1] != JType.CLOSE_BRACE.value:
            key = self.__parse_key()
            self.__next()
            self.__parse_colon()
            self.__next()
            value = self.__parse_value()
            if key in result:
                raise JSONException(f"Key must be unique. {result}")
            result[key] = value
            self.__parse_comma()
        return result

    def __parse_colon(self):
        if self.tokens[self.index][1] != JType.COLON.value:
            raise Exception(f'Unexpected token {self.tokens[self.index][1]}, expected: :')

    def __parse_comma(self):
        if self.tokens[self.index][1] == JType.COMMA.value:
            self.__next()
            if self.tokens[self.index][1] == JType.CLOSE_BRACE.value:
                raise JSONException(f"Unexpected token {self.tokens[self.index-1][1]} at index {self.index} ")

    def __parse_key(self):
        if self.tokens[self.index][1] == JType.STRING.value:
            return str(self.tokens[self.index][0])
        else:
            raise Exception('Invalid key in JSON. Key must be of string type')
