def emp(name, age):#positional Arguments
    print("NAme=", Name, "AGe=", age)
emp("harry")
#keyword Arugment: An alternative to positional arguments


def emp(Name, Age):
    print("Name=", NAme, "Age=",Age)
emp(Age=25, NAme="harry")


#parameter with default values:
def emp(name, msg="Welcome"):
    print("Hello",name,msg)
emp("harry")    
    
