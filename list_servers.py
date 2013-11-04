import requests, sys
from optparse import OptionParser
from bs4 import BeautifulSoup

usage = "usage: %prog username password orgid serverid"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()

if len(args) < 3:
    print "Not enough arguments: "
    print usage
    sys.exit()

username = args[0]
password = args[1]
orgid = args[2]

if len(args) == 4:
    serverid = args[3]
else:
    serverid = None
payload = {}
if serverid:
    payload["id"] = serverid

r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/serverWithState", params=payload, auth=(username,password))

if r.status_code != 200:
    print "error: " + str(r.status_code)
    sys.exit()

soup = BeautifulSoup(r.text)

print soup
servers = soup.html.body.serverswithstate.find_all("serverwithstate")

for server in servers:
    print "-----------------------"
    print "server\t" + server["id"] + " in " + server["location"]
    print "\t" + server.description.text
