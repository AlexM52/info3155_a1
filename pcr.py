#import os    #Useful if going to be doing anything with directories, some file manipulation, etc

#import sys, getopt    #for command line options, args
import crypt
import sys
import time



def main():
  if len(sys.argv)!=2:
    print "Usage: pcr.py <filename>"
    sys.exit()
  else:
    print "execute pcr on file '", sys.argv[1], "'."
    t_then = time.time()
    hfile = open(sys.argv[1])          #open file
    #string = hfile.read()
    #print string
    lines = hfile.readlines()          #read in lines from file
    print str(lines)                    #print out resulting lines, to check
    i=0
    # for line in lines:                  #iterate through..
    #   line = line.strip('\n')            #stripping any newline chars..
    #   line = line.split(':')          #split lines
    #   #print line                          #print line to represent processing
    #   i = i+1
    #   psl("Processed " + str(i) + " lines.")
    for x in range(len(lines)):                  #iterate through..
      lines[x] = lines[x].strip('\n')            #stripping any newline chars..
      lines[x] = lines[x].split(':')          #split lines
      #print line                          #print line to represent processing
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
        #lines.remove(lines[x])
        solved.append(lines[x])
      psl("Tested: "+str(x+1)+"/"+str(len(lines))+". Hits: "+str(len(results))+".")
    print ""
    #clr_solved()
    print "Clearing solved lines..."
    for x in range(len(solved)):
      lines.remove(solved[x])
    solved = []
    print ""
    if len(lines)>0:
      #move on to dictionary/rainbow...pull from file (rnbo maybe can filter down on salt)
      print "Testing X"
      r, lines = test_dict(lines)
      results.extend(r)
      print len(r), "hits, ", len(lines), " unsolved."
    print ""
    # if len(lines)>0:
    #   #next stage...
    #   print "Testing Y"
      
    
    print results
    # print lines
    # print solved
    
    t_now = time.time()
    print "Execution time: ",(t_now-t_then)," s.\n"
    #print "END PROGRAM."
    
    
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
  
  #needs expanding to cover many permutations etc--fairly done, maybe just add 2-digit loops...
  #also need to try and collapse this down somehow
  return 0
  
def test_dict(line_list):
  lines = line_list
  results = []
  # solved = []
  dict_file = open('password-list.lst', 'r')
  word_list = dict_file.readlines()
  dict_file.close()
  print "Testing dictionary ("+str(len(word_list))+" words)."
  for i in range(len(word_list)):
    # if len(lines)==len(solved):
    if len(lines)<1:
      break
    elif word_list[i][0:2]=='!#':
      continue
    else:
      # for l in range(len(lines)):
      l=0
      while l<len(lines):
        un=lines[l][0]
        h=lines[l][1]
        word = word_list[i].strip("\n")
        if crypt.crypt(word, h)==h:
          results.append((un, word, h))#add salt to tuple, check last func as well
          # solved.append(lines[l])#...consider using while loop, so can dynamically remove solved items
          # #ok, do removal of solveds
          lines.remove(lines[l])
        else:
          l = l+1
          
          #some processing here to remove solved lines from list..etc
  return results, lines       #list of solved tuples, list of unsolved lines

# def clr_solved():
#   print "Clearing solved lines..."
#   global solved
#   global lines
#   for x in range(len(solved)):
#     lines.remove(solved[x])
#   solved = []

def psl(message):
  #print_status_line : Overwrites line..
  sys.stdout.write('\r%s' % message)  #Return to start of current line, write message to buffer
  sys.stdout.flush()                  #Force message to be printed
  
  
# lines = []
# results = []
# solved = []
main()    #RUN PROGRAM