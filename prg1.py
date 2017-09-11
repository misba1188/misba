#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
    roll=input("press r to roll the dice:")
    if roll=="r":
       r=random.randint(1,6)
       count=count+r
       print("your random num is",r)
       print("you are on count",count)
       if count==8:
          count=37
       print("wow....up the ladder")
    elif count==11:
         count= 2
         print("omg...down the ladder")
    elif count==13:
         count=34
         print ("yess..pu the ladder")
    elif count==25:
         count=4
         print ("shit not again...down the ladderfrom random import randint
    elif count==38
         print("dam...down the ladder",count)
    elif count==40:
    	 count=68
    	 print("yuppe...up the ladder",count)
    elif count==52:
    	 count=81
    	 print("finally...up the ladder",count)
    elif count==65:
    	 count=46
    	 print("noo...down the ladder",count)
    elif count==76:
    	 count=97
    	 print("wow..up the ladder",count)
    elif count==89:
         count=70
         print("sadd...down the ladder",count)
    elif count==93:
         count=64
         print(":(...down the ladder",count)	 















