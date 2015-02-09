import sys

if len(sys.argv)!=3:
  print 'Usage: python vscan <IP address> <"list, of, port, numbers">'
  sys.exit()
else:
  ipaddr = sys.argv[1]
  ports = sys.argv[2].split(',')
  i=0
  while i<len(ports):
    ports[i] = int(ports[i])
    i = i+1
  del i
  print "IP Address: ", ipaddr
  print "Port list: ", ports