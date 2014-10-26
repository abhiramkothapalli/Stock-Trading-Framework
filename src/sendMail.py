#sends updates to selected email found in variables.py

import sys
sys.dont_write_bytecode = True

import smtplib
import variables

def sendMail(MSG):
 
	smtpserver = smtplib.SMTP(variables.SERVER,587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(variables.USER, variables.PASS)
	header = 'To:' + variables.TO + '\n' + 'From: ' + variables.USER + '\n' + 'Subject:Stock trader update \n'
	msg = header + MSG
	smtpserver.sendmail(variables.USER, variables.TO, MSG)
	smtpserver.close() 
	
	

