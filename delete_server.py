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

print "Deleting server"

r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/server/" + serverid + "?delete", auth=(username,password))
soup = BeautifulSoup(r.text).html.body

if r.status_code != 200:
    print "error: " + str(r.status_code)
    print "reason: " + soup.find("ns8:resultdetail").text
    sys.exit()

print "Successfully deleted server"
