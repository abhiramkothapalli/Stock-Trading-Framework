#class and methods of a single stock

import data
import datetime
import time
import variables
import sendMail

import sys
sys.dont_write_bytecode = True

class stock:
	def __init__(self, ticker):
		self.ticker = ticker
		self.buyPrice = 0
		self.numShares = int(0)
	def printQuote(self):
		print("Ticker: %s" % (self.ticker))
		print("price: %s" % (data.get_last_trade_price(self.ticker)))
		print("numShares: %s " % (self.numShares))
		print ""
	def emailQuote(self):
		msg = '''
		Ticker: %s
		price: %s
		numShares: %s
		
		BALANCE: %s
		''' % (self.ticker, data.get_last_trade_price(self.ticker), self.numShares, variables.balance)
		sendMail.sendMail(msg)		
	def inFolio(self):
		for order in variables.portfolio:
                	if self.ticker == order.ticker:
				return True
		return False
	def inList(self, localList):
		for row in range(1, len(localList) - 1):
			if self.ticker == localList[row][1]:
				return True
		return False
	def order(self, numShares):
		
		#averages out buyPrice
		if numShares > 0:
			self.buyPrice = (self.buyPrice * self.numShares + float(data.get_last_trade_price(self.ticker)) * numShares) / (self.numShares + numShares)
		
		if self.numShares + numShares < 0:
			numShares = -self.numShares
			
		
		variables.balance = variables.balance - numShares * float(data.get_last_trade_price(self.ticker)) - variables.tradePrice
			 
		self.numShares  = self.numShares + numShares
		
		if self.numShares == 0 and self.inFolio() == True:
			variables.portfolio.remove(self)
			
		if self.numShares > 0 and self.inFolio() == False:
			variables.portfolio.append(self)
		
		if numShares > 0:	
			print("BUYSTOCK %s %s:") % (variables.day, time.strftime("%H:%M"))
		elif numShares < 0:
			print("SELLSTOCK %s %s:") % (variables.day, time.strftime("%H:%M"))
		self.printQuote()
		
		if variables.SENDMAIL:
			self.emailQuote()