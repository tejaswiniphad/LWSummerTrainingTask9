#!/usr/bin/python3

print("Context-Type:text/plain")
print()

import cgi 
import subprocess
import time

form = cgi.FieldStorage()
depname = form.getvalue("a")
rep = form.getvalue("b")
output = subprocess.getoutput("sudo kubectl scale deployment "+depname+" --replicas="+rep+" --kubeconfig admin.conf")
print(output)
