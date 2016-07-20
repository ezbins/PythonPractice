import re

line = "From dennis@caretek.com.tw Feb 26 2016 13:04:45"
email= re.findall( '(\S+@\S+)' ,line)
host = re.findall( '@(\S+)', line)
send_date = re.findall('([^@][A-Z].+)',line)
print  ("The email is " + email.pop(0))
print  ("The host is "+ host.pop(0))
print ("The send date is " + send_date.pop(0))
