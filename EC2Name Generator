#!/usr/bin/env python3.7

#Case sensitive EC2 nAME gENERATOR
from random import randint # Import random number generator
import string
#UpperCase
Accounting ="Accounting"
FinOps="FinOps"
Department="Department"

randomNumber= 0 
def random_with_N_digits(n):
 range_start = 10**(n-1)
 range_end =(10**n)-1
 return randint(range_start, range_end)
 
 
type = input ("Please Select from the following Accounts: FinOps , Department or Accounting : ")
if not type.isalpha():
  print("Please enter only alphabetical characters to access a registered account. ")
  exit()
    
if input == Accounting:
    print("Acess Granted")
elif input == FinOps:
    print("Access Granted")
elif input == Department:
    print("Correct")
else: 
    ("Cant Verify")

instance=int(input("Type your instances : ")) #Define number of instances needed 

if instance > 0:
    print("I will make " + str(instance ) +" Instances for you")
else:
    print("You need more than to generate")

for _ in range(1, instance +1):
    ec2Name= type
    ID=ec2Name
    ec2name = type
    ID = ec2Name + "_" + str(random_with_N_digits(7))
    print("Here is your EC2 instance ID: ",ID)
        
        
        



