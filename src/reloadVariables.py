#cleans the variables as needed

import variables

def reloadVariables():
	balanceTemp = variables.balance
	portfolioTemp = variables.portfolio

	reload(variables)

	variables.balance = balanceTemp
	variables.portfolio = portfolioTemp 