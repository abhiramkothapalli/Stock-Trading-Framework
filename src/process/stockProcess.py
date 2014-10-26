#  Runs the main process and invokes buyStock and sellStock of the chosen strategy

import sys
sys.dont_write_bytecode = True

import csvReader
import data
import datetime
import importlib
import reloadVariables
import stock
import strategies
import subprocess
import time
import variables

strategy = None

def stockProcess():

	global strategy

	print ""
	print ("DIGITAL STOCK TRADER")
	print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////BALANCE: %s" % variables.balance)
	print ""

	sleep = '''
        sleep %s;
        ''' % (variables.sleepTime)

	while variables.balance >= 0:
		variables.hourMin = int(time.strftime("%H%M"))
		variables.day = datetime.datetime.now().strftime("%A")
		
		if variables.forceCycle or (variables.hourMin > variables.startTime) and (variables.hourMin < variables.endTime) and variables.day != "Saturday" and variables.day != "Sunday":
			
			for strategyName in variables.strategy:
			
				strategy = getattr(__import__("strategies", fromlist=[strategyName]), strategyName)
						
				temp = variables.balance
			
				#BUYSTOCK: Buys the stock once certain criteria are met. Finviz provides the initial batch			

				buyList = csvReader.csvReader(strategy.buyStrategy)
			
				for row in buyList:
						order = stock.stock(row[1])
						buyStock(order)			
			
				#SELLSTOCK: Sells stock in portfolio once certian criteria are met	
			
				for order in reversed(variables.portfolio):
					sellStock(order)

				if temp != variables.balance:
					print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////BALANCE: %s" % variables.balance)
					print ""
        	
		subprocess.call(['sh','-c',sleep])
		reloadVariables.reloadVariables()
		#strategy = getattr(__import__("strategies", fromlist=[variables.strategy]), variables.strategy)


def buyStock(order):
	strategy.buyStock(order)	
	
def sellStock(order):
	strategy.sellStock(order)
				
#stockProcess()