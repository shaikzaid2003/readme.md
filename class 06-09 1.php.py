num=int(input("enter the number"))
x=num
reverse=0
rem=0
while num>0:
    rem=num%10
    num=num//10
    reverse=reverse*10+rem
print("reverse+rem",reverse)    
