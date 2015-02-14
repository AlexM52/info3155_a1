# SCANNER.PY
# Group 1 (INFO3155)
# 
# Student ID's:
# 620025838
# 620025254
# 620066080
# 620052765
# 620034264

import sys, socket#,getopt


def main(argv):
   if len(argv)!=2:
     print 'Usage: python scanner.py <IP address> <"list, of, port, numbers">'
     sys.exit()
   else:
      tm_out = 5.0
      #scan_type = []
      
      ipaddr = argv[0]
      ports = argv[1].split(',')
      #CONVERT PORT NUMBERS
      i=0
      while i<len(ports):
        ports[i] = int(ports[i])
        i = i+1
      del i
      #MAIN PROCESSING
      print "IP Address: ", ipaddr
      print "Port list: ", ports
      for i in range(len(ports)):
            try:
              sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              sock.settimeout(tm_out)
              sock.connect((ipaddr, ports[i]))
              #sock.send("ping\r\n")
              response = sock.recv(4096)
              print "OPEN TCP Port "+str(ports[i])+": "+response
            except socket.timeout:
                #print "Socket: connection timed out - no response (Port "+str(ports[i])+")."
                try:
                    sock.send("hello\r\n")
                    response = sock.recv(4096)
                    print "OPEN TCP Port "+str(ports[i])+": "+response
                except socket.timeout:
                    print "Socket: connection timed out - no response (Port "+str(ports[i])+")."
            except socket.error:
        ##      print "Error: could not connect"+str(error)
                print "CLOSED Port "+str(ports[i])+": "+str(socket.error)
        ##    finally:
        ##      socket.close()
    
    
if __name__ == '__main__':
  main(sys.argv[1:])
