

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


