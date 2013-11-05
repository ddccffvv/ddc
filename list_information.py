import requests, sys
from optparse import OptionParser
from bs4 import BeautifulSoup

usage = "usage: %prog username password"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()

if len(args) < 2:
    print "Not enough arguments: "
    print usage
    sys.exit()

username = args[0]
password = args[1]


r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/myaccount", auth=(username,password))

if r.status_code != 200:
    print "error: " + str(r.status_code)
    print r.text
    sys.exit()

soup = BeautifulSoup(r.text).html.body
print "Personal infromation:"
print "Username: " + soup.find("ns2:username").text
print "Email: " + soup.find("ns2:emailaddress").text
orgid = soup.find("ns2:orgid").text
print "Organisation id: " + orgid
print "roles:"
for role in soup.find_all("ns2:role"):
    print "\t" + role.find("ns2:name").text

# data center information
r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/datacenterWithDiskSpeed", auth=(username,password))

if r.status_code != 200:
    print "error: " + str(r.status_code)
    print r.text
    sys.exit()

soup = BeautifulSoup(r.text).html.body
print "---------------------------"
print "Servers in: "
location = soup.find("ns7:datacenter")["ns7:location"]
print soup.find("ns7:displayname").text + " (" + location + ")"

r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/base/image/deployedWithSoftwareLabels/" + location, auth=(username,password))

if r.status_code != 200:
    print "error: " + str(r.status_code)
    print r.text
    sys.exit()

print "---------------------------"
print "Available os images: "
soup = BeautifulSoup(r.text).html.body
for entry in  soup.find_all("deployedimagewithsoftwarelabels"):
    print entry.find("description").text + " (" + entry.find("id").text + ")"

r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/networkWithLocation", auth=(username,password))

if r.status_code != 200:
    print "error: " + str(r.status_code)
    print r.text
    sys.exit()

print "---------------------------"
print "Network details: "
soup = BeautifulSoup(r.text).html.body
for network in soup.find_all("ns4:network"):
    print network.find("ns4:name").text + " (" + network.find("ns4:id").text + ")"
