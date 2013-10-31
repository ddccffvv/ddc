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

#r = requests.get("https://api-eu.dimensiondata.com/oec/0.9/" + orgid + "/serverWithState", params=payload, auth=(username,password))

#if r.status_code != 200:
    #print "error: " + str(r.status_code)
    #sys.exit()

response_body = """
<ServersWithState
        xmlns="http://oec.api.opsource.net/schemas/server"
        totalCount="320"
        pageCount="250"
        pageNumber="1"
        pageSize="250">
    <!--Zero or more repetitions:-->
    <serverWithState id="c325fe04-7711-4968-962e-c88784eb2" location="NA1">
        <name>Production LAMP Server</name>
        <!--Optional:-->
        <description>Main web application server.</description>
        <operatingSystem id="REDHAT564" displayName="REDHAT5/64" type="UNIX"/>
        <cpuCount>2</cpuCount>
        <memoryMb>4096</memoryMb>
        <!-- one or more repetitions:-->
        <disk id="x445fe05-7113-4988-9d2e-cbjt78eb2" scsiId="0" sizeGb="50"
speed="STANDARD" state="NORMAL"/>
        <disk id="ef49974c-87d0-400f-aa32-ee43559fdb1b" scsiId="1" sizeGb="150"
speed="STANDARD" state="NORMAL"/>
        <!--Zero or more repetitions:-->
        <softwareLabel>REDHAT5ES64</softwareLabel>
        <!--Optional:-->
        <sourceImageId>5a18d6f0-eaca-11e1-8340-d93da27669ab</sourceImageId>
        <networkId>xb632974c-87d0-400faa32-hb43559flk765</networkId>
        <machineName>10-157-3-125</machineName>
        <privateIp>10.157.3.125</privateIp>
        <!--Optional:-->
        <publicIp>206.80.63.208</publicIp>
        <created>2012-07-02T10:43:31.000Z</created>
        <isStarted>false</isStarted>
        <isDeployed>true</isDeployed>
        <state>PENDING_CHANGE</state>
        <!--Zero or more repetitions:-->
        <machineStatus name="vmwareToolsRunningStatus">
            <value>RUNNING</value>
        </machineStatus>
        <!--Optional:-->
        <status>
            <action>START_SERVER</action>
            <requestTime>2012-09-26T08:36:28</requestTime>
            <userName>btaylor</userName>
            <!--Optional:-->
            <numberOfSteps>3</numberOfSteps>
            <!--Optional:-->
            <updateTime>2012-09-26T08:37:28</updateTime>
            <!--Optional:-->
            <step>
                <name>Waiting for operation</name>
                <number>3</number>
                <!--Optional:-->
                <percentComplete>3</percentComplete>
            </step>
            <!--Optional: (present only if the last operation failed and left
the server in a locked state) -->
            <failureReason>Message Value</failureReason>
        </status>
    </serverWithState>
</ServersWithState>
"""
soup = BeautifulSoup(response_body)

print soup
servers = soup.html.body.serverswithstate.find_all("serverwithstate")

for server in servers:
    print "-----------------------"
    print "server\t" + server["id"] + " in " + server["location"]
    print "\t" + server.description.text
