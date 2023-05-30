import datetime
import time

#PROGRAM TO INCREASE INVESTMENT VALUE BY 10% EVERY 5SEC
def calc_profit(investment):
	interest = 0.1
	current_date = datetime.date.today()
	print(f"Today {current_date.ctime()[:10]}, your balance is {investment:,.2f}")
	time.sleep(86400)
	investment += (investment*interest)
	return(calc_profit(investment))

capital = float(input("Please enter investment amount: "))

while True:
	calc_profit(capital)
