import http.client
import xml.dom.minidom

HOST = ""  # Host endpoint for the API
API_URL = ""

XML_FILE = ""   # Path for the XML file that is passed in the body of the POST request
CERT_FILE = ""  # Path for the cert file to be attached to the POST request
KEY_FILE = ""   # Path for the key file associated with the cert


def post_request():

    ###################################################
    # HTTPS POST request that passes an XML in the body
    ###################################################
    request = open(XML_FILE, "r").read()

    if KEY_FILE != "" and CERT_FILE != "":
        api_service = http.client.HTTPSConnection(HOST, key_file=KEY_FILE, cert_file=CERT_FILE)
    elif KEY_FILE == "" and CERT_FILE == "":
        api_service = http.client.HTTPSConnection(HOST)
    else:
        print("Please provide a valid path for a cert and key file.")

    api_service.putrequest("POST", API_URL)
    api_service.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    api_service.putheader("Content-length", "%d" % len(request))
    api_service.putheader("Host", HOST)
    api_service.putheader("User-Agent", "Python 3.7")
    api_service.endheaders()
    api_service.send(request)

    # Receive a response from the endpoint and parse it into XML format
    received_code, received_message, received_header = api_service.getresponse()
    result = api_service.getresponse().read()
    xml_result = xml.dom.minidom.parseString(result)

    print(received_code, received_message, received_header)
    print(xml_result.toprettyxml())

    with open("receivedXML.xml", "w") as xmlfile:
        xmlfile.write(xml_result.toprettyxml())


post_request()
