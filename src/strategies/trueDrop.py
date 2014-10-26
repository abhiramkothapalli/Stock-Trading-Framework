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

#Buy strategy for initial finviz search (use the url)
#Make sure to always have this field variable
buyStrategy = "http://finviz.com/export.ashx?v=111&s=ta_toplosers&f=sh_price_o3,ta_changeopen_u2,ta_gap_d5&ft=4&o=change"

#buyStock is the strategy required to buy a stock besides initial finviz search
def buyStock(order):
	
	#conditions for buying a stock apart from the initial finviz criteria	

	#total amt of balance you are willing to invest in one stock
	maxMargin = float(0.10)
	
	#cap on no. of investments in your portfolio
	portfolioCap = int(10)
	
	#buying conditions
	if  (
		variables.forceBuy or
		order.inFolio() == False and
		len(variables.portfolio) < portfolioCap
		):
		
		#calculations needed to buy stock
		maxPay = float(variables.balance * maxMargin)
		numShares = int(maxPay / float(data.get_last_trade_price(order.ticker)))
		if numShares > int(data.get_volume(order.ticker)):
			numShares = int(data.get_volume(order.ticker))	

		#proceeds to buy after conditions and calculations
		order.order(numShares)		

#sellStock is the strategy required to sell a stock from your portfolio
def sellStock(order):

	#conditions for selling a stock
	
	#total margin you are willing to lose on an investment
	lossMargin = float(0.05)
	
	#selling conditions
	if  (
		variables.forceSell or
		float(data.get_last_trade_price(order.ticker)) > float(data.get_50_sma(order.ticker)) or
		float(data.get_last_trade_price(order.ticker)) < float(order.buyPrice) * float(1 - lossMargin)
		):
		
		#calculations needed to sell stock
		
		
		#proceeds to buy after conditions and calculations
		order.order(-order.numShares)