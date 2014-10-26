#STRATEGY FILE
#make sure to change the config file to point to this strategy

#these are the two imports you will always need
#look at the methods in data and the variables in variables
import variables
import data

#Buy strategy for initial finviz search
#Make sure to always have this field variable
buyStrategy = "http://finviz.com/export.ashx?f=sh_curvol_o100,ta_perf_d10u,ta_sma50_pcb&ft=4"

#buyStock is the strategy required to buy a stock besides initial finviz search
def buyStock(order):
	
	#conditions for buying a stock from the initial finviz criteria	

	#total amt of balance you are willing to invest in one stock
	maxMargin = float(0.10)
	
	#cap on no. of investments in your portfolio
	portfolioCap = int(10)
	
	#cap on volume
	volumeCap = int(500000)
	
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
	lossMargin = float(0.10)
	
	#selling conditions
	if  (
		variables.forceSell or
		float(data.get_last_trade_price(order.ticker)) > float(data.get_200_sma(order.ticker))
		):
		#print(data.get_last_trade_price(order.ticker))
		#print(data.get_200_sma(order.ticker))
		
		order.order(-order.numShares)