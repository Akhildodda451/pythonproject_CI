n=int(input())
price=123
if(n%2==0):
    price=123-3
    total=price*n
    print(total)
elif(n%2!=0):
    print(price*n)
else:
    print("Enter a valid input")