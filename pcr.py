#import os    #Useful if going to be doing anything with directories, some file manipulation, etc

#import sys, getopt    #for command line options, args
import sys

#print "Number of args: ", len(sys.argv)
#print "Argument list: ", str(sys.argv)
# def main(argv):
#   #if len(sys.argv)!=2:
#   if len(argv)!=1:
#     print "Usage: pcr.py <filename>"
#     sys.exit()
#   else:
#     #print "execute pcr on file '",sys.argv[1],"'."
#     print "execute pcr on file '", argv[0],"'."
    
# if __name__ == "__main__":
#   main(sys.argv[1:])

if len(sys.argv)!=2:
  print "Usage: pcr.py <filename>"
  sys.exit()
else:
  print "execute pcr on file '", sys.argv[1], "'."
  hfile = open(sys.argv[1])          #open file
  #string = hfile.read()
  #print string
  lines = hfile.readlines()          #read in lines from file
  print str(lines)                    #print out resulting lines, to check
  for line in lines:                  #iterate through..
    line = line.strip('\n')            #stripping any newline chars..
    print line                          #print line to represent processing
  hfile.close()                      #close file after done
  print "File closed."              #output for verification
  