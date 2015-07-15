#!/usr/bin/env python

##	Script:		jamfuserid.py
##	Author:		Christopher Collins (christophercollins@livenation.com)
##	Last Change:	2014-01-14
###########################################
##Description: Get the user UID of the jamf management user.
###########################################

import subprocess

user = 'jamf'

userexists = subprocess.Popen(['id', '-u', user], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
useroutput = userexists.communicate()

if userexists.returncode == 0:
  print "<result>%s</result>" % useroutput[0].strip()
else:
  print "<result></result>"

