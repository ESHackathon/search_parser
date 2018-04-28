# -*- coding: utf-8 -*-
import re

from lexer import Lexer, LexerError
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

def merge_terms(parse_query):
    parse_query_joined = []
    new_terms = []
    for term, type_ in parse_query:
        if type_ == "TERM":
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
            parse_query_joined.append((term, type_))
    if len(new_terms) > 0:
        parse_query_joined.append(
            (
                " ".join(new_terms),
                "TERM"
            )
        )
    return parse_query_joined

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
    return merge_terms(stack)

def get_terms(search_strategy):
    return [part[0] for part in parse_strategy(search_strategy) if part[1] == "TERM"]
