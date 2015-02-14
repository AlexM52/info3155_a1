README
-------
This file is has been packaged along with a password cracker (passwordcracker.py)
and a portscanner(scanner.py) for Group 1's first assignment submission for course INFO3155
at UWI MONA. 

Student ID's:
-------------
620025838
620025254
620066080
620052765
620034264

passwordcracker.py
------------------
The password cracker has 2 methods for cracking passwords. A command line argument
is used to determine which is used at runtime:

    'python passwordcracker.py 1 <filename>' for method 1, and
    'python passwordcracker.py 2 <filename>' for method 2

where <filename> is the name of a file in the same directory as passwordcracker.py,
containing username:hashedpassword rows.

We used the file 'test' as an example file for testing the password cracker.
The password cracker also makes use of a dictionary file, 'password-list.lst',
based on password-2011.lst from http://www.openwall.com/passwords/wordlists/password-2011.lst
These files have also been included.


scanner.py
----------
scanner.py accepts 2 command line arguments:

    'python vscan <IP address> <"list, of, port, numbers">'

where <IP address> is the address of the target host and <"list, of, port, numbers">
is a comma-separated list of port numbers to be scanned. Entering this list within quotes
ensures the list is read as a single argument.