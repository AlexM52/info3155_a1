# PASSWORDCRACKER.PY
# Group 1 (INFO3155)
# 
# Student ID's:
# 620025838
# 620025254
# 620066080
# 620052765
# 620034264

import crypt
import sys
import getopt
import time



def method1(argv):
  if len(argv)!=1:
    print "Usage: python passwordcracker.py 1 <filename>"
    sys.exit()
  else:
    print "execute pcr on file '", argv[0], "'."
    t_then = time.time()
    hfile = open(argv[0])          #open file
    lines = hfile.readlines()          #read in lines from file
    print str(lines)                    #print out resulting lines, to check
    i=0
    for x in range(len(lines)):                  #iterate through..
      lines[x] = lines[x].strip('\n')            #stripping any newline chars..
      lines[x] = lines[x].split(':')          #split lines
      i = i+1
      psl("Processed " + str(i) + " lines.")
    print ""                            #newline after loop's status line
    hfile.close()                      #close file after done
    print "File closed.\n"              #output for verification
    results = []
    solved = []
    print "Testing usernames..."
    for x in range(len(lines)):
      r = test_UNs(lines[x])
      if (r!=0):
        results.append((lines[x][0], r, lines[x][1]))
        solved.append(lines[x])
      psl("Tested: "+str(x+1)+"/"+str(len(lines))+". Hits: "+str(len(results))+".")
    print ""
    print "Clearing solved lines..."
    for x in range(len(solved)):
      lines.remove(solved[x])
    solved = []
    print ""
    if len(lines)>0:
      print "Testing X"
      r, lines = test_dict(lines)
      results.extend(r)
      print len(r), "hits, ", len(lines), " unsolved."
    print ""
    
    print results
    t_now = time.time()
    print "Execution time: ",(t_now-t_then)," s.\n"
    
    
def test_UNs(line):
  #takes line (format: ['username', 'hash',...]), tests for matches on variations of username
  un = line[0]
  h = line[1]
  if crypt.crypt(un, h)==h:                           #test all plain un variations
    return un
  for i in range(10):
    if crypt.crypt(un+str(i), h)==h:
      return un+str(i)
  if crypt.crypt(un+"_", h)==h:                       #test all un_
    return un+"_"
  for i in range(10):
    if crypt.crypt(un+"_"+str(i), h)==h:
      return un+"_"+str(i)
  if crypt.crypt(un.lower(), h)==h:                   #test all lowercase un
    return un.lower()
  for i in range(10):
    if crypt.crypt(un.lower()+str(i), h)==h:
      return un.lower()+str(i)
  if crypt.crypt(un.lower()+"_", h)==h:               #test all lowercase un_
    return un.lower()+"_"
  for i in range(10):
    if crypt.crypt(un.lower()+"_"+str(i), h)==h:
      return un.lower()+"_"+str(i)
  if crypt.crypt(un.capitalize(), h)==h:              #test all cap Un
    return un.capitalize()
  for i in range(10):
    if crypt.crypt(un.capitalize()+str(i), h)==h:
      return un.capitalize()+str(i)
  if crypt.crypt(un.capitalize()+"_", h)==h:          #test all cap Un_
    return un.capitalize()+"_"
  for i in range(10):
    if crypt.crypt(un.capitalize()+"_"+str(i), h)==h:
      return un.capitalize()+"_"+str(i)
  if crypt.crypt(un.upper(), h)==h:                   #test all upper UN
    return un.upper()
  for i in range(10):
    if crypt.crypt(un.upper()+str(i), h)==h:
      return un.upper()+str(i)
  if crypt.crypt(un.upper()+"_", h)==h:               #test all upper UN_
    return un.upper()+"_"
  for i in range(10):
    if crypt.crypt(un.upper()+"_"+str(i), h)==h:
      return un.upper()+"_"+str(i)
  return 0
  
def test_dict(line_list):
  lines = line_list
  results = []
  dict_file = open('password-list.lst', 'r')
  word_list = dict_file.readlines()
  dict_file.close()
  print "Testing dictionary ("+str(len(word_list))+" words)."
  for i in range(len(word_list)):
    if len(lines)<1:
      break
    elif word_list[i][0:2]=='!#':
      continue
    else:
      l=0
      while l<len(lines):
        un=lines[l][0]
        h=lines[l][1]
        word = word_list[i].strip("\n")
        if crypt.crypt(word, h)==h:
          results.append((un, word, h))#add salt to tuple, check last func as well
          lines.remove(lines[l])
        else:
          l = l+1
  return results, lines       #list of solved tuples, list of unsolved lines


def psl(message):
  #print_status_line : Overwrites line..
  sys.stdout.write('\r%s' % message)  #Return to start of current line, write message to buffer
  sys.stdout.flush()                  #Force message to be printed
  




def checkPass(cryptPass,dictn):
    salt = cryptPass[0:2]
    dictFile = open(dictn, "r")
    for word in dictFile.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word,salt)
        #print cryptWord
        #print cryptPass
        if(cryptWord == cryptPass):
            print "Password found: " + word + '\n'	
            return
    print "Password Not found \n"
    return

def Method2(args):
    passFile = open(args[0], "r") #copy of shadow file from unix environ
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(" ")
            print "Cracking password for: " +user + " ......"
            checkPass(cryptPass, "password-2011.lst") #file containing list of possible passwords





def Main(args):
    print args
    if args[1]=='1':
        print "Cracking with method 1..."
        method1(args[2:])
    elif args[1]=='2':
        print "Cracking with method 2..."
        Method2(args[2:])
    else:
        print "Usage: python passwordcracker.py <method (1|2)> <hashed password file>"

if __name__ == '__main__':
    Main(sys.argv)