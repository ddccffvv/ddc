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
serverid = args[3]

print "Forcefully shutting down server..."

r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/server/" + serverid + "?poweroff", auth=(username,password))

soup = BeautifulSoup(r.text).html.body
if not (r.status_code == 200 or r.status_code == 400):
    print "error: " + str(r.status_code)
    print r.text
    sys.exit()

if r.status_code == 400:
    print soup.find("ns8:resultdetail").text
else:
    print "Server successfully powered off"
