#!/usr/bin/python
# -*- coding: utf-8 -*-

##                                       ##
# Author: Peter Manev                     #
# pmanev@emerginthreats.net               #
##                                       ##
# Given a directory this script will traverse it,
# look for *.rules files and enable all rules inside.
# Then it will save the all enabled rules file using the same name but
# with a "enableall-" prefix in front of the original file name.
# The rule files that have names starting with "enableall-" will
# be skipped or overwritten. 

import sys, re, os


if __name__ == "__main__":
  
  
  if len(sys.argv) != 2:
    print sys.argv
    print len(sys.argv)
    sys.stderr.write('Usage: \n \
    1. rule directory, \n \
    EXAMPLE: python enable-all-rules.py /full/path/to/rules/directory \
    \n \n ' )
    sys.exit(1)
    
  rule_dir = sys.argv[1]
  
  if not os.path.exists(rule_dir):
    print "Directory %s does not exist - exiting\n" % results_directory
    sys.exit(1)
    
  
  for rule_file in os.listdir(rule_dir):
    if not rule_file.startswith("enableall-") and rule_file.endswith(".rules"): 
      #print rule_dir+rule_file
      fin = open(rule_dir+rule_file)
      fout = open(rule_dir+"enableall-"+rule_file, "w")
      for line in fin:
	line = re.sub('^\s*#+\s*alert ', 'alert ',line , 1)
	#print line
	fout.write(line)
	
      fin.close()
      fout.close()                
    else:
        continue


  

      