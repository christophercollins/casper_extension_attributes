#!/usr/bin/python

##	Script:		get_chrome_extensions.py
##	Author:		Christopher Collins (christophercollins@livenation.com)
##	Last Change:	2015-07-14
###########################################
##Description: This script searches the last logged in user's installed extensions and submits it to Casper during an inventory report.
###########################################

import os
import json
from Foundation import CFPreferencesCopyAppValue

#Get name of last logged in user so the extension attribute will report information for the user even if they aren't logged in"
lastloggedinuser = CFPreferencesCopyAppValue('lastUserName', 'com.apple.loginwindow')
userchromepath = '/Users/' + lastloggedinuser + '/Library/Application Support/Google/Chrome/'

#List of extension names that can be ignored and not reported. Can be edited if needed
ignored_extensions = ['__MSG_CHROME_EXT_SHORT_NAME__', '__MSG_APP_NAME__', "__MSG_appName__"]
installed_extensions = []

for (dirpath, dirnames, filenames) in os.walk(userchromepath):
    for file in filenames:
        if ("Extensions" in dirpath  and "manifest.json" in file):
            manifest = json.load(open(os.path.join(dirpath, file)))
            extension_name = manifest.get('name')
            if extension_name not in ignored_extensions:
                installed_extensions.append(extension_name)

print "<result>{}</result>".format(', '.join(installed_extensions))