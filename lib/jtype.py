import enum


class JType(enum.Enum):
    STRING = 'string'
    NUMBER = 'number'
    BOOLEAN = 'boolean'
    NULL = 'null'
    OPEN_BRACE = '{'
    CLOSE_BRACE = '}'
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'
    COLON = ':'
    COMMA = ','

