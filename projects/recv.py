import  socket 
import  time 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
my_ip="127.0.0.1"
# -- 52.2.116.225 -- jecrc.delvex.io 
my_port=9999
my_address=(my_ip,my_port)
# let me start above defined address 
s.bind(my_address)
#  socket --  IP:PORT  --  52.2.116.225:9999 
#   facebook ---          www.facebook.com:443 
# --                       157.240.239.35:443 
# port -- 0-65535
# lets recv text data
while 3 > 2 :
    data=s.recvfrom(100)
    # only filetring message 
    new_data=data[0]
    final_msg=new_data.decode('ascii')
    print(final_msg)
    # implement file handing print 
    time.sleep(2)
    # let me store data persistently 
    with open('')
