!/usr/bin/env python3
amount = float(input("Enter the amount: ")) #get amount of money 
inrate = float(input("Enter the interest rate: ")) # get the interest rate 
period = int(input("Enter the time period: "))     #get the period of saving 

#check and calculate 
value = 0          
year = 1           
while year <= period:                            
    value = amount + (inrate * amount)           
    print("year {} Rs. {:.2f}”.format(year,value))
    amount = value 
    year = year + 1
