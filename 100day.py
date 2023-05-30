#just carr y 
''''''
# print("\"umesh is a good boy\"\nand she is also a good:")
# print("neeraj is tatty gay::")
# print("just carry on bro::")
# print("neeraj",7,8,9,10,sep="_",end="234")
# print("zetty")
a="hellosingh bisht"
# for ch in a:
#     print(ch)
# for i in range (2,30,3):
#     print(i)   
# print(a[-4:-2]) 
# print(len(a))
# a=int(input("enter the age:::"))
# b=int(input("enter the age:::"))
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)
      #triple cote string method::
# ans='''umesh singh bisht
# is agood boy 
# studing in btech 2 year'''

import time
time1=time.strftime('%H:%M:%S')

time2=int(time.strftime('%H'))
if time2>=1 and time2<12:
    print("Good moring start with new things::",time1)
elif time2>=12 and time2<=16:
    print("Good afternoon sir::",time1)    
elif time2>=17 and time2<=18:
    print("Good evening:::",time1)
elif time2>18 and time2<23 :
    print("Good night Hsve a  sweet dream::",time1)
else:
    print("sweet dream sir ")    

# Match Case:;
# x=4
# match x:
#     case 0:
#          print("umesh")
#     case _:
#         print(x)     

