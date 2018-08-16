import os
import xml.etree.ElementTree as et

acord = et.Element('ACORD')

# Create tags for fields under ACORD
signonRq = et.SubElement(acord, 'SignonRq')
insuranceSvcRq = et.SubElement(acord, "InsuranceSvcRq")

# Create tags for fields under SignonRq
signonPswd = et.SubElement(signonRq, "SignonPswd")
clientDT = et.SubElement(signonRq, "ClientDt")
custLangPref = et.SubElement(signonRq, "CustLangPref")
clientApp = et.SubElement(signonRq, "ClientApp")

# Set text for fields under SignonRq
clientDT.text = "2016-11-11"
custLangPref.text = "en-US"

# Create tags for fields under SignonPswd
custID = et.SubElement(signonPswd, "CustId")
custPswd = et.SubElement(signonPswd, "CustPswd")

# Create tags for fields under CustID
spName = et.SubElement(custID, "SPName")
custPermID = et.SubElement(custID, "CustPermId")
custLoginID = et.SubElement(custID, "CustLoginID")

# Set text for fields under CustID
spName.text = 'www.yourdomain.com'
custPermID.text = ""
custLoginID.text = "Your@SIRISLogin.com"

# Create tags for fields under CustPswd
encryptionTypeCd = et.SubElement(custPswd, "EncryptionTypeCd")
pswd = et.SubElement(custPswd, "Pswd")

# Set text for fields under CustPswd
encryptionTypeCd.text = "NONE"
pswd.text = "YourSIRISPassword"

# Create tags for fields under ClientApp
org = et.SubElement(clientApp, "Org")
name = et.SubElement(clientApp, "Name")
version = et.SubElement(clientApp, "Version")

# Set text for fields under ClientApp
org.text = "Agent Name"
name.text = "Agent Name SCOTTSDALE Upload"
version.text = "V1.9"

# Create tags for fields under InsuranceSvcRq
rqUID = et.SubElement(insuranceSvcRq, "RqUID")
transactionRequestDt = et.SubElement(insuranceSvcRq, "TransactionRequestDt")
transactionEffectiveDt = et.SubElement(insuranceSvcRq, "TransactionEffectiveDt")
curCd = et.SubElement(insuranceSvcRq, "CurCd")

# Set tags for fields under InsuranceSvcRq


# Write XML Tree to output XML file
myfile = open("items2.xml", "w")
mydata = et.tostring(acord, encoding="unicode")

myfile.write(mydata)
