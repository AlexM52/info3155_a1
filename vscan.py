import sys, getopt, socket
#from socket import *

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
  #RETRIEVE CMD LINE OPTIONS, ARGS
  try:
    opts, args = getopt.getopt(argv, "htli:p:")
  except getopt.GetoptError:
    print 'Usage: python vscan.py [-t <scan type>] [-l <timeout (s)>] -i <target IP address> -p <"list, of, port, numbers">'
    print "Type 'python vscan.py -h' for help."
    sys.exit(2)
  #PROCESS OPTS, ARGS
  ipaddr = ""
  ports = []
  tm_out = 0.0
  scan_type = []
  for opt, arg in opts:
    if opt == '-h':
      print 'Usage: python vscan.py [-t <scan type>] [-l <timeout (s)>] -i <target IP address> -p <"list, of, port, numbers">'
      print ('COMMAND LINE OPTIONS:'+
            '\n\tRequired:'+
            '\n\t-i: TARGET IP ADDRESS: \tIP address of host to scan.'+
            '\n\t-p: PORTS: \t\tQuoted string listing which ports to scan.'+
            '\n\tOptional:'+
            '\n\t-h: HELP: \t\tDisplays this help screen.'+
            '\n\t-t: SCAN TYPE: \t\tQuoted string listing which scan types to try.'+
            '\n\t\t\t\tE.g.: "-t "vanilla, xmas".'+
            '\n\t-l: TIMEOUT: \t\tNumber of seconds vscan should wait for a '+
            '\n\t\t\t\tresponse. Float value.')
      sys.exit()
    elif opt == '-t':
      scan_type = arg
    elif opt == '-l':
      tm_out = float(arg)
    elif opt == '-i':
      ipaddr = arg
    elif opt == '-p':
      ports = arg.split(',')
  # ipaddr = sys.argv[1]
  # ports = sys.argv[2].split(',')
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
          print "[OPEN - TCP] Port "+str(ports[i])+": "+response
        except socket.timeout:
            #print "Socket: connection timed out - no response (Port "+str(ports[i])+")."
            try:
                sock.send("GET index.html\r\n")
                response = sock.recv(4096)
                print "[OPEN - TCP] Port "+str(ports[i])+": "+response
            except socket.timeout:
                print "Socket: connection timed out - no response (Port "+str(ports[i])+")."
        except socket.error:
    ##      print "Error: could not connect"+str(error)
            print "[CLOSED] Port "+str(ports[i])+": "+str(socket.error)
    ##    finally:
    ##      socket.close()
  # try:
  #   socket = socket(AF_INET, SOCK_STREAM)
  #   socket.connect((ipaddr, ports[0]))
  #   socket.send("hello\r\n")
  #   response = socket.recv(100)
  #   print "[OPEN - TCP] Port "+str(ports[0])+": "+response
  # except:
  #   print "Error: could not connect"
  # finally:
  #   socket.close()
    
    
if __name__ == '__main__':
  main(sys.argv[1:])