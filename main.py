
#write a python program for currency convertor

# Read a currencyData.txt file line by line .
with open("currencyData.txt", "r") as f:
    lines = f.readlines()
    f.close()
    
# empty Dictionary
currencydict = {}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]] = parsed[1]

# input a amount and enter name of currency inwhich you want
amount = int(input("Enter amount:\n"))
print("Enter the name of currency you want to convert this amount?\n available options:\n")
[print(item) for item in currencydict.keys()]
currency = input("\nPlease enter one of these values:\n")
print(f"\n{amount} INR  = {amount*float(currencydict[currency])} {currency}\n")