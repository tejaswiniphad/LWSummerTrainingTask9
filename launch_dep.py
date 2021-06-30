#!/usr/bin/python3

print("Content-Type:text/plain")
print()

import cgi
import subprocess
import time

form = cgi.FieldStorage()
depname = form.getvalue("dn")
imagename = form.getvalue("i")

output = subprocess.getoutput("sudo kubectl create deployment "+depname+" --image="+imagename+" --kubeconfig admin.conf")
print(output)

