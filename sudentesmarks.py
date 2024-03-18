phy = int(input("Enter marks of Physics subject: "))
bio = int(input("Enter marks of Biology subject: "))
chr = int(input("Enter marks of Chemistry subject: "))
cop = int(input("Enter marks of Computer subject: "))
mth = int(input("Enter marks of Math subject: "))
lenguge =int(input("Enter marks of lenguge subject:"))

percentage = (phy + bio + chr + mth + cop) / 5.0
print("\nPercentage: {:.2f}".format(percentage))
total= (phy + bio + chr + cop + mth + lenguge)
print(" \ntotal mark :",total) 
if phy > 100 or bio > 100 or chr > 100 or cop > 100 or mth > 100 or lenguge > 100:
    print("Invalid marks assigned")
else:
    percentage = (phy + bio + chr + mth + cop) / 5.0
    print("\nPercentage: {:.2f}".format(percentage))

    if percentage >= 90:
        print("A Grade")
    elif percentage >= 80:
        print("B Grade")
    elif percentage >= 70:
        print("C Grade")
    elif percentage >= 60:
        print("D Grade")
    elif percentage >= 40:
        print("E Grade")
    else:
        print("F Grade")
  
