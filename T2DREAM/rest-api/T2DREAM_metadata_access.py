#!/usr/bin/env python2

import argparse
import os
import sys
import json
import requests

EPILOG = '''
%(prog)s GET the results of a search from an T2DREAM server metadata in JSON or TSV format

Basic Useage:

    %(prog)s --type experiment --accession TSTSR112545
    
    A accession and metadata type - experiment, file, annotation
'''
def metadata_search(accession, type):
    HEADERS = {'accept': 'application/json'}
    URL = 'http://www.t2dream-demo.org/'
    response = requests.get(URL + type  + '/' + accession, headers=HEADERS)
    response_json_dict = response.json()
    metadata_search_response = json.dumps(response_json_dict, indent=4, separators=(',', ': '))
    return metadata_search_response
def main():
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument('--accession', help="accession id")
    parser.add_argument('--type', help="Data type: experiment, annotation or file")
    args = parser.parse_args()
    accession= args.accession
    type = args.type
    metadata_result = metadata_search(accession,type)
    print metadata_result
if __name__ == "__main__":
    main()
