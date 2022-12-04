'''n = int(input("enter the number"))
for i in range(2, n):
    if(n%i==0):
        flag=False
        break
    else:
        flag=True
if(flag==True):
    print("prime")
else:
    print("prime")'''


'''n = int(input("enter the number"))
for i in range(2, n):
    if(n%i==0):
        flag=True
        break
    else:
        flag=False
if(flag==False):
    print("is prime")
if(flag==True):
    if(n%2==0):
       print("is even")
  else:
      print("is odd")'''


a = input()
for ch in a:
    if ch=='':
        continue
    else:
        print(ch,'')
