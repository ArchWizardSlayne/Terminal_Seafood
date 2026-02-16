import time

#############################
###name and price varibles###
#############################

name = input("Please Enter Your Name:\n")
price = 15.99

print("\n")

################
###print name###
################

print(name)
print("\n")

if name == "Wendell" or name == "wendell": 
    print("Hello " + name + " How are you doing sir?\n")
elif name == "Ethan" or name == "ethan": 
    print("Get out " + name + " You're not welcome here!!!\n")
    time.sleep(2)
    exit()
else:
    print("Welcome\n")

###############################
###Serve menu and take order###
###############################

order_and_menu = input("What would like to order?\nWe have (Shrimp, Crab, Catfish, Flounder, Lobster)?\n")
print("\n")

print("Good Choice " + name + ", the cost is " + str(price))  

quantity = input("How many would you like?\n")

while int(quantity) > 10:
    print("We have a 10 item limit, sorry for the inconvinence")
    quantity = input("How many would you like instead?\n")
print("\n")

print("Your " + quantity + " " + order_and_menu + " will be ready soon!")
input("Press ENTER to continue.\n")

#################
###Serve Order###
#################

total = price * int(quantity)
print("Thank you for choosing terminal seafood! Your Total cost is " + str(total))
input("Press ENTER to continue.")



