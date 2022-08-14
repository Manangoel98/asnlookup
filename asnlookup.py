import sys
import json
import argparse
import requests
import os


def parse_args():
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + ' -o twitter')
	org = parser.add_argument('-o', '--org', help='Organization to look up.', required=True)
	return parser.parse_args()

headers = {
    'X-RapidAPI-Key': 'aa913ad958msh1df3f3d897ef721p165a87jsnb681342e973e',
    'X-RapidAPI-Host': 'asn-lookup.p.rapidapi.com'
  }

def get_ip_space(Organization):
	url = "https://asn-lookup.p.rapidapi.com/api?orgname=" + str(org)
	print(url)
	r = requests.get(url ,headers=headers, timeout=10)
	json_object = json.loads(r.text)
	json_formatted_str = json.dumps(json_object, indent=2)
	print(json_formatted_str)


if __name__ == '__main__':
    org = parse_args().org
    get_ip_space(org)
