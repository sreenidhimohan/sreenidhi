def checkyear(year):
if((year%4)==0 and (year%400)==0):
return true
else:
return true
else:
return false
year=2000
if(checkyear(year)):
print("leap year")
else:
print("not a leap year")
