#STRATEGY FILE
#make sure to change the config file to point to this strategy

'''
skeleton

Description: use this skeleton file to create all following strategy files

author: Abhiram Kothapalli
version: March 2, 2014
updates: put your changes for future reference here

strategy: put a little detail about the strategy here
'''

#these are the two imports you will always need
#look at the methods in data and the variables in variables
import variables
import data
import sys
sys.dont_write_bytecode = True

#Buy strategy for initial finviz search (use the url)
#Make sure to always have this field variable
buyStrategy = ""

#buyStock is the strategy required to buy a stock besides initial finviz search
def buyStock(order):
	
	#conditions for buying a stock apart from the initial finviz criteria	

	
	#buying conditions
	if  (
		variables.forceBuy or
		order.inFolio() == False
		):
		
		#calculations needed to buy stock	


		#proceeds to buy after conditions and calculations
		order.order(numShares)		

#sellStock is the strategy required to sell a stock from your portfolio
def sellStock(order):

	#conditions for selling a stock
	
	#selling conditions
	if  (
		variables.forceSell
		):
		
		#calculations needed to sell stock
		
		
		#proceeds to buy after conditions and calculations
		order.order(-order.numShares)