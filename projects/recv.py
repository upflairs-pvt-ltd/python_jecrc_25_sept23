import  socket 
import  time 
import os
import notepad 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
my_ip="0.0.0.0" 
# whenever  ip is 0.0.0.0  mean default wifi /lan ip will be used by RECEIVER 
my_port=9999
my_address=(my_ip,my_port)
# let me start above defined address 
s.bind(my_address)
while 3 > 2 :
    data=s.recvfrom(100)
    # only filetring message 
    new_data=data[0]
    final_msg=new_data.decode('ascii')
    print("original data : ",data)
    print(final_msg)
    time.sleep(2)
    # handling message 
    msg_search=final_msg.lower()
    # search for notepad open operation 
    if 'notepad' in msg_search and 'open' in msg_search:
        # calling open function
        notepad.open_notepad()
    elif 'notepad' in msg_search and 'close' in msg_search:
        # calling function 
        notepad.close_notepad() 
    else :
    # implement file handing print 
        time.sleep(2)
        print(final_msg," ...FROM user  ",data[1][0])
        # selecting file name 
        file_name=data[1][0] 
        # creating chat user file to store data
        print("_________________")
        print("Saving user data in a file ....")
        with open('chat_users/'+file_name,'a+')  as f:
            f.write(final_msg+'\n')  

        # reply to user
        okmsg="cool" 
        s.sendto(okmsg.encode('ascii'),data[1])
