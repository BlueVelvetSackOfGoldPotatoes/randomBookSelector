#!/usr/bin/env python
"""
SYNOPSIS

    TODO random book gen [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    Picks a random book out of a list of books.

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    TODO: Hora de Carvalho <goncalo.horadecarvalho@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $Id$
"""

import sys, os, traceback, optparse
import time
import re
GOOD_TERMINALS = ["xterm"]


def set_title():
     # Tell the terminal to change the current title.
     msg = "###############  Magic Library  ###############"
     if os.getenv("TERM") in GOOD_TERMINALS:
         print("\x1B]0;%s\x07" % msg)
#from pexpect import run, spawn

# generates a random number from 1 to s
def randomSelector(s):
    from random import randint
    return randint(1, s)

# checks if book file exists, if not creates it
def checkFile():
    try:      
        # returns absolute path of file
        path = os.path.abspath("randomBookSelector/randomBookSelector/bookList.txt")
        # reads, line by line, strings in file and saves them to list 'lines'
        with open(path) as f:
            lines = f.read().splitlines()
        return lines
    except:
        return -1

def fillLibrary():
    f= open("bookList.txt","w+")
    amountBooks = int(input("How many books do you wish to add to the magical random library?\n"))
    for i in range(0, amountBooks):
        f.write(input("Book:\n"))

def main (argv):

    # Try to change the title of the terminal to 'magic library'
    funcs = set_title, main

    for func in funcs:
        try:
            func()
        except Exception:
            pass  # or you could use 'continue'

    # try to open file it exist, if not create file and fill it
    lines = checkFile()
    
    if lines == -1 :
        fillLibrary()
    
    lines = checkFile()    

    key = int(input("pressing (0) will quit \npressing (1) will list the books in the library \npressing (2) will generate a book:\n"))
    if key == 0 :
        sys.exit(0)
    if key == 1 :
        print(*lines, sep='\n')
    if key == 2 :
        n = randomSelector(len(lines))
        print(lines[n])
'''
# came with the skeleton - unsure what it does
if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()
        main()
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
        '''

if __name__ == "__main__":
    main(sys.argv)