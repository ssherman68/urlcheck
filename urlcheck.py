#! /usr/bin/env python

'''
Original Version: Stacy Sherman 9/12/20
Given a list of domains or URLs, look each one up and determine if it will
be blocked by Umbrella/OpenDNS or not. A block will be evidenced by seeing
'block.opendns.com' in the resulting HTML

'''


# Import any modules

import os
from urlparse import urlparse
import requests

def process_list(ulist):
    
    # Do something with each element in the list

	print "\nThere are", len(ulist), "sites to look up.\n"
	for u in ulist:
		tmp_url = urlparse(u) 			# Parse URL to see if it starts w/ http...
		if not tmp_url.scheme:			# if no scheme, add "http://"" to it
			clean_u = "http://" + u
		else:
			clean_u = u
		url = urlparse(clean_u)			# Re-parse now valid URL
		result = url.scheme + "://" + url.netloc	
		print "URL: ", result
		try:
			url_file = requests.get(result, timeout=2)
			response = url_file.text
			if response == '':
				print "  ^--- No Response\n"
			elif response.find('block.opendns.com') != -1:
				print "  ^--- BLOCKED\n"
			else:
				print "  ^--- ALLOWED\n"
		except IOError:
			print "  ^--- Not a valid domain\n" 



def main():
	filename = raw_input("\nEnter file name: ")
	with open(filename, 'r') as fin:
		print "\nAttempting to load ",filename
		ulist = fin.readlines()				# Read the file into a list of URLs
	process_list(ulist)



    



if __name__ == '__main__':
    main()