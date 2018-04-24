# -*- coding: utf-8 -*-

from parser_util import get_terms
from test_queries import QUERIES

def main():
    for sector, query_list in QUERIES.items():
        print("SECTOR: %s" % sector)

        for query in query_list:
            parsed_terms = get_terms(query)

            print("ORIGINAL_QUERY:\n\t%s" % query)
            print()
            print("PARSED_QUERY:\n\t%s" % parsed_terms)
            print()

if __name__ == '__main__':
    main()
