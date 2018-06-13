#!/usr/bin/env python2

import argparse
import os
import sys
import json
import requests

EPILOG = '''
%(prog)s GET the results of annotation region search from T2DREAM server in JSON format

Basic Useage:

    %(prog)s --genome GRCh37 --region rs7903146
    
    rs id or chromosome location of variant (chr10:114758349-114758349) and genome version - region, genome version
'''
def region_search(genome, region):
    HEADERS = {'accept': 'application/json'}
    URL = 'https://t2depigenome-test.org/peak_metadata/region='
    response = requests.get(URL + region  + '&genome=' + genome + '/peak_metadata.json', headers=HEADERS)
    response_json_dict = response.json()
    region_search_response = json.dumps(response_json_dict, indent=4, separators=(',', ': '))
    return region_search_response
def main():
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument('--region', help="rs id or chromosome location")
    parser.add_argument('--genome', help="Genome version: GRCh37 or GRCh38")
    args = parser.parse_args()
    region = args.region
    genome = args.genome
    json_response = region_search(genome, region)
    print json_response
if __name__ == "__main__":
    main()
