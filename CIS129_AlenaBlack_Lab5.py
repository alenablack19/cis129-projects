# Lab 5 The Bottle Return Program
#Alena Black
#21 June 2024
#This program is used to calculate the total weekely bottles that are collected and returned

#Initalize variables
totalBottles = 0
totalPayout = 0
keepGoing = "y"

#Set conditions to determine totals for the week
while keepGoing== "y":
    totalBottles = 0  
    totalPayout = 0   

#A week of bottle Collections 
    NBR_OF_DAYS = 7
    for day in range(1, NBR_OF_DAYS + 1):
        print(f"Enter number of bottles returned for the  day #{day}:")
        todayBottles = int(input())
        totalBottles += todayBottles
    PAYOUT_PER_BOTTLE = 0.1
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE

#Information for weeks total   
    print(f"The total  number of bottles returned: {totalBottles}")
    print(f"The total paid out was: ${totalPayout:.2f}")
    
#Ask if additional data should be entered 
    print("Do you want to enter another week’s worth of data?")
    print("(Enter y or n)")
    keepGoing = input ("Do you want to enter another week’s worth of data?")

print("Information Printed Successfully.")
