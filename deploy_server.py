import requests, sys
from optparse import OptionParser
from bs4 import BeautifulSoup

usage = "usage: %prog username password orgid netid imageid name password"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()

if len(args) < 7:
    print "Not enough arguments: "
    print usage
    sys.exit()

username = args[0]
password = args[1]
orgid = args[2]
netid = args[3]
imageid = args[4]
name = args[5]
password = args[6]



payload = """<Server xmlns='http://oec.api.opsource.net/schemas/server'>
    <name>""" + name + """</name>
    <description>test description</description>
    <vlanResourcePath>/oec/""" + orgid + """/network/""" + netid + """</vlanResourcePath>
    <imageResourcePath>/oec/base/image/""" + imageid + """</imageResourcePath>
    <administratorPassword>""" + password + """</administratorPassword>
    <isStarted>true</isStarted>
</Server>"""



r = requests.post("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/server", params=payload, auth=(username,password))

if r.status_code != 200:
    print "error: " + str(r.status_code)
    print r.text
    sys.exit()

soup = BeautifulSoup(r.text).html.body
print r.text

