# -*- coding: utf-8 -*-

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

            parse_query_joined = []
            new_terms = []
            for term,fn in parse_query:
                if (fn == "TERM"):
                    new_terms.append(term)
                else:
                    if len(new_terms) > 0:
                        parse_query_joined.append(
                            (
                                " ".join(new_terms),
                                "TERM"
                            )
                        )
                        new_terms = []
                    parse_query_joined.append((term,fn))

            print("ORIGINAL_QUERY:\n\t%s" % query)
            print()
            print("PARSED_QUERY:\n\t%s" % parse_query_joined)
            print()

if __name__ == '__main__':
    main()
