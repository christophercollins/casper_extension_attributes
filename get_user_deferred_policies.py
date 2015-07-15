#!/usr/bin/python

##	Script:		get_user_deferred_policies.py
##	Author:		Christopher Collins (christophercollins@livenation.com)
##	Last Change:	2015-05-15
###########################################
##Description: This extension attribute checks the .userdelay.plist file for any deferred policies
##where a user has opted out for more time to run the policy in the future.
###########################################

import sys
import os
import plistlib

#Check to see if .userdelay.plist exists. If it doesn't, exit out of the script
if not os.path.exists('/Library/Application Support/JAMF/.userdelay.plist'):
    print '<result>there is no .userdelay.plist file</result>'
    sys.exit()
    
#Use plistlib to read in the .plist for user delayed policies
pref_file = plistlib.readPlist('/Library/Application Support/JAMF/.userdelay.plist')

#If the user delay plist is not empty then iterate through each policy number to get its delayed till time
#and then print the results (seperated by a comma and space if there are multiples)
if pref_file:
    policies=[]
    for policy in pref_file:
        policies.append(policy + ' ' + str(pref_file[policy]))
    print '<result>' + (', ').join(policies) + '</result>'
    
else:
    print '<result>.userdelay.plist empty</result>'
        

