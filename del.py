#!/usr/bin/python3

print("Content-Type:text/plain")
print()

import cgi
import subprocess
import time

form = cgi.FieldStorage()
name = form.getvalue("n")
Type = form.getvalue("t")

output = subprocess.getoutput("sudo kubectl delete deployment "+name+" --kubeconfig admin.conf")
#time.sleep(2)
print(output)

