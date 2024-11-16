msg = input().split()
flag=0
if len(msg[0])==3 and msg[0][0]=='+':
    for i in msg[1]:
        if(i.isdigit()):
            flag=1
            continue
        else : 
            flag=0
if flag==0:
    print("Incorrect")
else : 
    print("Correct")
