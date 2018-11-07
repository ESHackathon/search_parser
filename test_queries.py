# -*- coding: utf-8 -*-

from parser_util import get_terms, parse_strategy
from queries import QUERIES

def main():
    for sector, query_list in QUERIES.items():
        print("SECTOR: %s" % sector)

        for query in query_list:
            parsed_strategy = parse_strategy(query)
            parsed_terms = get_terms(query)

            print("ORIGINAL QUERY:\n\t%s" % query)
            print()
            print("PARSED STRATEGY:\n\t%s" % parsed_strategy)
            print()
            print("PARSED TERMS:\n\t%s" % parsed_terms)
            print()

if __name__ == '__main__':
    main()
