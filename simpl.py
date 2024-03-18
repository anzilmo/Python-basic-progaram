principal = 10000
ayis = 1000000
rate = 10
tenure = 15
intrest = (principal * rate * tenure) / 100
print("Principal * rate * tenure / 100 =", intrest)

reteb = 5
tenureb = 6
intrestb = (ayis * reteb * tenureb) / 100
print("simple interest:", intrestb)

principal = (rate * tenure * intrest) / 100
print("principal:", principal)

ayis = (principal * tenure * rate) / 100
print("ayis:", ayis)

originalvalue = ayis
decimalPlaces = 2
originalvalue2 = intrest
originalvalue3 = tenure

print("ROUNDED value:", round(originalvalue, decimalPlaces))
print("total interest:", round(originalvalue2, decimalPlaces))
print("total closing years:", round(originalvalue3))
