import os
import xml.etree.ElementTree as et

# Path to the XML file to be read from
base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "data\\SIRIS_HO_YTD.xml")

tree = et.parse(xml_file)

root = tree.getroot()

# Iterate through XML file pulling out data from each tag
for child in root:
    # print(child.tag, ":", child.text)
    for element in child:
        if element.tag == 'QuoteID':
            quoteID_Text = element.text
            print(element.text)
        elif element.tag == 'StatusID':
            statusID_Text = element.text
            print(element.text)
        elif element.tag == 'NamedInsured':
            namedInsured_Text = element.text
            print(element.text)
        elif element.tag == 'MailAddress1':
            mailAddress1_Text = element.text
            print(element.text)
        elif element.tag == 'MailAddress2':
            mailAddress2_Text = element.text
            print(element.text)
        elif element.tag == 'MailCity':
            mailCity_Text = element.text
            print(element.text)
        elif element.tag == 'MailState':
            mailState_Text = element.text
            print(element.text)
        elif element.tag == 'MailZip':
            mailZip_Text = element.text
            print(element.text)
        elif element.tag == 'PolicyID':
            policyID_Text = element.text
            print(element.text)
        elif element.tag == 'Description':
            description_Text = element.text
            print(element.text)
        elif element.tag == 'Address1':
            address1_Text = element.text
            print(element.text)
        elif element.tag == 'Address2':
            address2_Text = element.text
            print(element.text)
        elif element.tag == 'City':
            city_Text = element.text
            print(element.text)
        elif element.tag == 'State':
            state_Text = element.text
            print(element.text)
        elif element.tag == 'Zip':
            zip_Text = element.text
            print(element.text)
        elif element.tag == 'COUNTY':
            county_Text = element.text
            print(element.text)
        elif element.tag == 'Effective':
            effective_Text = element.text
            print(element.text)
        elif element.tag == 'Expiration':
            expiration_Text = element.text
            print(element.text)
        elif element.tag == 'SubmitTypeID':
            submitTypeID_Text = element.text
            print(element.text)
        elif element.tag == 'companyname':
            companyname_Text = element.text
            print(element.text)
        elif element.tag == 'PolicyForm':
            policyForm_Text = element.text
            print(element.text)
        elif element.tag == 'CoverageID':
            coverageID_Text = element.text
            print(element.text)
        elif element.tag == 'coveragename':
            coveragename_Text = element.text
            print(element.text)
        elif element.tag == 'marketname':
            marketname_Text = element.text
            print(element.text)
        elif element.tag == 'Premium':
            premium_Text = element.text
            print(element.text)
        else:
            print("Error: Could not match this tag to a predefined tag!")
    print()
