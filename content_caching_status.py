#!/usr/bin/python


import subprocess
import json

#!/usr/bin/env python

# Script:		content_caching_status.py
# Author:		Christopher Collins
# Last Change:	2018-01-14
###########################################
# Description: Get the status of the local caching server service
###########################################


def get_os_version():
    cmd = ["/usr/bin/sw_vers", "-productVersion"]
    os_vers = subprocess.check_output(cmd).split(".")[1]
    return os_vers


def get_caching_status():
    cmd = ["/usr/bin/AssetCacheManagerUtil", "status", "--json"]
    status = json.loads(subprocess.check_output(cmd))
    return status["result"]["Active"]


def main():
    os_vers = get_os_version()
    if os_vers >= 13:
        if get_caching_status():
            print("<result>Active</result>")
        else:
            print("<result>Not Active</result>")
    else:
        print("<result>NA</result>")


if __name__ == "__main__":
    main()
