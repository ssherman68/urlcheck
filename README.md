urlcheck.py

Original Version: Stacy Sherman 9/12/20

Given a list of domains or URLs, look each one up and determine if it will
be blocked by Umbrella/OpenDNS or not. A block will be evidenced by seeing
'block.opendns.com' in the resulting HTML

Requires the urlparse and requests libraries

The script must be run on a machine that is actively using Umbrella/OpenDNS
and only evaluates based on the Umbrella policy that applies to the machine
running it. 