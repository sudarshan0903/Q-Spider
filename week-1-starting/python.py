#wap to check whether the given integer is single digit or two digits or three digits or more than three digits.
n=int(input("enter number;"))
if 0<=n<=9:
    print("single digit")
elif 10<=n<=99:
    print("double digit no ")
elif 100<=n<=1000:
    print("tripple digit no ")
elif 1000<=n<=10000:
   print("qudra digit no")  
else:
 print("more than 3 digit")

# consider a character input if it is uppercase convet it into lowercase,if it is lowercase convert it into uppercase ,if it is digit print the reminder when it is divided by 3 else if it is special character print it ASCII value 

# ch=input ("enter a character?:")
# if 'A'<=ch<='Z':``
#     res =chr(ord(ch)+32 )
#     print (res)                                  # ascii value means upper case madhun lower case madhye convert kartan use kartat
# elif 'a'<=ch<='z':
#     res =chr(ord(ch)-32)
#     print (res)
# elif '0'<=ch<='9':
#      rem = int(ch)%3
#      print(rem)
# else:
#     print(ord(ch))  
