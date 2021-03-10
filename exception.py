x=input("Enter  Number 1:")
y=input("Enter  Number 2:")
try:
   
    z=int(x)//y
# except Exception as e:
except ZeroDivisionError as e:
    print('Exception occured:',e)
    z=None
except Exception as e:
    print(e)
    z=None
print("Division is :",z)
