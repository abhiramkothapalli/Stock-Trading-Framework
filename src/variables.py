import os
import sys
#environment variables of the entire process. Set this up first


sys.dont_write_bytecode = True

#FIELD VARIABLES

path = os.path.dirname(os.path.realpath(__file__))
hourMin = int(0)
day = ""
portfolio = []


#TESTING METRICS

#forces a cycle of buy and sell
forceCycle = False

#forces to buy all of list
forceBuy = False

#forces to sell all of portfolio
forceSell = False

#turns on/off log
log = False

#STRATEGY METRICS

#name of the strategy(s)
strategy = ["trueDrop"]

#starting bank balance
balance = float(100000)

#assumed price of transaction
tradePrice = float(10)

#start time given in numeric format
startTime = int(930)

#end time given in numeric format
endTime = int(1600)

#amount of time between each cycle (seconds)
sleepTime = 900

#SMTP METRICS(FOR SENDMAIL)

#decides to send mail or not
SENDMAIL = False

#your email username
USER = ""

#your email password
PASS = ""

#email you want to send it to
TO = ""

#Server that your email is hosted on
SERVER = "smtp.gmail.com"