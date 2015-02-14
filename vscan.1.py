import sys, getopt
from socket import *

# def main():
#   if len(sys.argv)!=3:
#     print 'Usage: python vscan <IP address> <"list, of, port, numbers">'
#     sys.exit()
#   else:
#     ipaddr = sys.argv[1]
#     ports = sys.argv[2].split(',')
#     i=0
#     while i<len(ports):
#       ports[i] = int(ports[i])
#       i = i+1
#     del i
#     print "IP Address: ", ipaddr
#     print "Port list: ", ports
#     try:
#       socket = socket(AF_INET, SOCK_STREAM)
#       socket.connect((ipaddr, ports[0]))
#       socket.send("hello\r\n")
#       response = socket.recv(100)
#       print "[OPEN - TCP] Port "+str(ports[0])+": "+response
#     except:
#       print "Error: could not connect"
#     finally:
#       socket.close()
    
    
# if __name__ == '__main__':
#   main()

def main(argv):
  # if len(sys.argv)!=3:
  #   print 'Usage: python vscan <IP address> <"list, of, port, numbers">'
  #   sys.exit()
  # else:
  try:
    opts, args = getopt.getopt(argv, "hti:p:")
  except getopt.GetoptError:
    print 'python vscan.py [-t <scan type>] -i <target IP address> -p <"list, of, port, numbers">'
    sys.exit(2)
    
  ipaddr = ""
  ports = []
  for opt, arg in opts:
    if opt == '-h':
      print 'python vscan.py [-t <scan type>] -i <target IP address> -p <"list, of, port, numbers">'
      sys.exit()
    elif opt == '-i':
      ipaddr = arg
    elif opt == '-p':
      ports = arg.split(',')
  # ipaddr = sys.argv[1]
  # ports = sys.argv[2].split(',')
  i=0
  while i<len(ports):
    ports[i] = int(ports[i])
    i = i+1
  del i
  print "IP Address: ", ipaddr
  print "Port list: ", ports
  try:
    socket = socket(AF_INET, SOCK_STREAM)
    socket.connect((ipaddr, ports[0]))
    socket.send("hello\r\n")
    response = socket.recv(100)
    print "[OPEN - TCP] Port "+str(ports[0])+": "+response
  except:
    print "Error: could not connect"
  finally:
    socket.close()
    
    
if __name__ == '__main__':
  main(sys.argv[1:])