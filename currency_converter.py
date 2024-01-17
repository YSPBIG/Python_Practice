#Covert the euro and pound currency
euro = 0.9
pound = 1.12

print("Currency converter, Euro / Pound")
choice = input("Would you like to convert Pound or Euro [P or E] ?")

amount = float(input("Please enter the amount of currency"))

if choice in ["P","p","pound","Pound"]:
    print(amount, "converted to Euro is ", amount * euro)
elif choice in ["E","e","Euro","euro"]:
    print(amount, "converted to Pound is", amount * pound)
else:
    print("Choice not found")

print("End of program")