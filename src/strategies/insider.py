#STRATEGY FILE
#make sure to change the config file to point to this strategy

'''
insider

Description: insider trading strategy

author: Abhiram Kothapalli
version: March 2, 2014
updates: none

strategy: buy or sell based on insider flags
'''

#these are the two imports you will always need
#look at the methods in data and the variables in variables
import variables
import data

#Buy strategy for initial finviz search (use the url)
#Make sure to always have this field variable
buyStrategy = "http://finviz.com/export.ashx?s=n_earningsafter&f=sh_avgvol_100to1000"

#buyStock is the strategy required to buy a stock besides initial finviz search
def buyStock(order):
	
	#conditions for buying a stock from the initial finviz criteria	

	#total amt of balance you are willing to invest in one stock
	maxMargin = float(0.10)
	
	#cap on no. of investments in your portfolio
	portfolioCap = int(10)
	
	#insider trading flag
	insiderStrategy = "http://finviz.com/export.ashx?s=it_latestbuys"
	
	insiderList = csvReader(insiderStrategy)
	
	#buying conditions
	if  (
		forceBuy or
		order.inFolio() == False and
		len(portfolio) < portfolioCap and
		order.inList(insiderList) == True
		):
		
		#calculations needed to buy stock	
		maxPay = float(balance * maxMargin)
		numShares = int(maxPay / float(data.get_price(order.ticker)))
		if numShares > int(data.get_volume(order.ticker)):
			numShares = int(data.get_volume(order.ticker))

		#proceeds to buy after conditions and calculations
		order.order(numShares)		

#sellStock is the strategy required to sell a stock from your portfolio
def sellStock(order):

	#conditions for selling a stock
	
	#total margin you are willing to lose on an investment
	lossMargin = float(0.10)
	
	#day after flag
	dayAfterStrategy = "http://finviz.com/export.ashx?s=n_earningsbefore"
	
	#selling conditions
	if  (
		forceSell or
		order.inList(dayAfterStrategy)
		):
		order.order(-order.numShares)