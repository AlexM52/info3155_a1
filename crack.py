import crypt

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


def Main():
    passFile = open("test", "r") #copy of shadow file from unix environ
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(" ")
            print "Cracking password for: " +user + " ......"
            checkPass(cryptPass, "password-2011.lst") #file containing list of possible passwords


if __name__ == '__main__':
    Main()
            