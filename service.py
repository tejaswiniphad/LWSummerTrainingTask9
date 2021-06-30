#!/usr/bin/python3

print("Content-Type:text/plain")
print()

import cgi
import subprocess
import time

form = cgi.FieldStorage()
depname = form.getvalue("d")
port = form.getvalue("p") 
Type = form.getvalue("t")

output = subprocess.getoutput("sudo kubectl expose deployment "+depname+" --port="+port+" --type="+Type+" --kubeconfig admin.conf")
time.sleep(2)
print(output)
