import re

from lexer import Lexer
from test_queries import QUERIES

RULES = [
    (
        r'\bAND\b',
        'AND'
    ),
    (
        r'\bOR\b',
        'OR'
    ),
    (
        r'\bNOT\b',
        'NOT'
    ),
    (
        r'\(',
        'LP'
    ),
    (
        r'\)',
        'RP'
    ),
    (
        r'\[[^ \)\(\[\]]+\]',
        'SEARCH_IN'
    ),
    (
        r'[^ \)\(\[\]]+',
        'TERM'
    ),
]

def normalize_quotes(query):
    normalized = re.sub(r'[＂"“”‟〝〞]+', '"', query)
    normalized = re.sub(r'[‘’]', "'", normalized)
    if normalized.count('"') == 1:
        normalized = normalized.replace('"', '')
    return normalized

def clear_newlines(query):
    return query.replace("\n", " ")

def parse_strategy(search_strategy):
    lexer_instance = Lexer(RULES, skip_whitespace=True)
    normalized_strategy = clear_newlines(normalize_quotes(search_strategy))
    lexer_instance.input(normalized_strategy)
    stack = []
    try:
        for tok in lexer_instance.tokens():
            stack.append((tok.val, tok.type))
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
    return stack

def main():
    for sector, query_list in QUERIES.items():
        print("SECTOR: %s" % sector)
        for query in query_list:
            parse_query = parse_strategy(query)
            print("ORIGINAL_QUERY:\n\t%s" % query)
            print()
            print("PARSED_QUERY:\n\t%s" % parse_query)
            print()

if __name__ == '__main__':
    main()
