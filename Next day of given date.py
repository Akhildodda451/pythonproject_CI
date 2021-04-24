day=int(input("Enter The Day:"))
month=int(input("Enter The Month:"))
year=int(input("Enter The Year:"))

if year%400==0 or (year%4==0 and year%100!=0):
   if month==2:
       no_of_days=29
   elif month in [4,6,9,11]:
       no_of_days=30
   else:
       no_of_days=31
else:
   if month==2:
       no_of_days=28
   elif month in [4,6,9,11]:
       no_of_days=30
   else:
       no_of_days=31
if day<no_of_days:
   print(day+1,"-",month,"-",year)
else:
   if month==12:
       print(1,"-",1,"-",year+1)
   else:
       print(1,"-",month+1,"-",year)