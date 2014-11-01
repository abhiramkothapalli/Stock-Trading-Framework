STOCK TRADING FRAMEWORK

Author: Abhiram Kothapalli
Date Created: October 2013
Copyright (c) Abhiram Kothapalli (a.kothapalli97@gmail.com)

Summary:

The stock trading framework is developed with python is intended to algorithmically trade US stocks using live data powered by finviz and yahoo finance. This is intended to be a simulator and can easily be set up with live trading with the appropriate API's

A handful of demo strategies are provided to test various classes

Requirements:

Python 2.7+

Setup:

RUNME offers a quick run of the framework on an UNIX system. For non-UNIX systems run main.py in the src directory.

src/variables.py contains important environment variables such as strategy name, starting balance, email notification setup, and debug settings

Usage:

strategies are found under src/strategies/

Every strategy contains the methods buyStock and sellStock which define the rules of when to buy and when to sell stocks using methods found in data.py. Every strategy also contains a strategy url which reaches out to Finviz to screen the initial stocks to test for buy/sell signals.

Use sample.py or skeleton.py to get started

A strategy is assigned in the variables file and is called in stockprocess.py, which loops the system to download a set of candidate stocks (using Finviz) and to calls the buyStock to verify the candidates and sellStock

Happy trading!



