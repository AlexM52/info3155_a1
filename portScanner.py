#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


# 620025838
# 620025254
# 620066080
# 620052765
# 620034264
__author__ = "tks"
__date__ = "$Feb 13, 2015 10:52:17 AM$"


import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tarhost,tarport):
    try:
        connskt =Socket(AF_INET, SOCK_STREAM)
        connskt.connect((tarhost,tarport))
        connskt.send("Hello\r\n")
        verify=True
        
        results= connskt.recv(100)
        screenLock.acquire()
        print "[+] " + str(tarport) + "/tcp open"
    except:
        screenLock.acquire()
        print "[+] " + str(tarport) + "/tcp closed"
        verify=False
    finally:
        screenLock.release()
        if(verify):
            connskt.close()
        
def portScan(tarhost, tarports):
    try:
        tarip = gethostbyname(tarhost)
    except:
        print "[+] Cannot resolve " + tarhost + ": unknown host"
        return
    
    try:
        tarname = gethostbyaddr(tarip)
        print "\n[+] Scan results for: "+ tarname[0]
    except:
        print "\n[+] Scan results for: "+ tarip
        
    setdefaulttimeout(1)
    for tarport in tarports:
        t = Thread(target=connScan, args=(tarhost, int(tarport)))
        t.start()
        
        
def Main():
    parser = optparse.OptionParser("usage %prog -H <target host= -p <target port>")
    parser.add_option('-H', dest='tarhost',type='string', help='specify target host')
    parser.add_option('-p',dest='tarport', type='string',help='specify target port[s] separated by a coma')
    (options,args) = parser.parse_args()
    if(options.tarhost== None) | (options.tarhost==None):
        print parser.usage
        exit(0)
    else:
        tarhost= options.tarhost
        tarports = str(options.tarport).split(',')
        
    portScan(tarhost,tarports)
    
if __name__ == "__main__":
    Main()
