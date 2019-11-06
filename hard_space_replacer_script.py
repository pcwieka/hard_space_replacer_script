#!/usr/bin/python
#-*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime
import sys
import re

wordlength = sys.argv[1]
wordpattern = re.compile("[A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż0-9]+")

inputfilenumber = 2

while inputfilenumber <= len(sys.argv) - 1:
    
    inputfilefullpath= sys.argv[inputfilenumber]

    inputfilename = Path(inputfilefullpath).stem
    inputfileparentpath = Path(inputfilefullpath).parent
    inputfileextension = Path(inputfilefullpath).suffix
    
    print('\n@@ Processing file: ' + str(inputfilename) + '\n')

    processingdatetime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

    with open(inputfilefullpath) as infile:
    
       linenumber = 0
    
       for line in infile:

   	       linenumber += 1
   	       print('     @@ Processing line nr: ' + str(linenumber))

   	       for word in set(line.split()):
    
   	   	       if len(word) <= int(wordlength) and wordpattern.match(word):
   	   	           print('         @@ Processing word: ' + word)
   	   	           line = re.sub(r'\b'+ word + ' ', word + '\u00A0', line)
    
   	       with open(str(inputfileparentpath) + '/' + inputfilename + '_out_' + \
   	       	processingdatetime + str(inputfileextension), 'a') as outfile:
   	           outfile.write(line)


    outfile.close()
    infile.close()
    inputfilenumber+=1

print('\n@@ Processing of ' + str(inputfilenumber - 2) + ' files finished successfully! Enjoy your day!\n')
