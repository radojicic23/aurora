#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.lan_scanner import lan_scan
from src.port_scanner import port_scan
from src.nmap_automation import nmap_script


print("""____
       /      \         __      _\( )/_
    \  \  ,,  /  /   | /  \ |    /(O)\  
     '-.`\()/`.-'   \_\\  //_/     _.._   _\(o)/_  
    .--_'(  )'_--.   .'/()\'.    .'    '.  /(_)\  
   / /` /`""`\ `\ \   \\  //    /   __   \    
    |  |  ><  |  |          ,  |   ><   |  ,  
    \  \      /  /         . \  \      /  / .
   _    '.__.'    _\(O)/_   \_'--`(  )'--'_/  
_\( )/_            /(_)\      .--'/()\'--.  
 /(O)\   //  \\         _     /  /` '' `\  \  
        _\\()//_     _\(_)/_    |        |  
      / //  \\  \     /(o)\      
       | \__/ |    
""")

print('-' * 52)
print("[*] ~ 1. Discover all devices on your network.")
print("[*] ~ 2. Port Scanner.")
print("[*] ~ 3. NMAP Automation tool.")
print('-' * 52)

try:
    USER_INPUT = input("[+] Enter your option: ")
    
    if USER_INPUT == '1':
        lan_scan()
    elif USER_INPUT == '2':
        port_scan()
    elif USER_INPUT == '3':
        nmap_script()
except KeyboardInterrupt:
    print("\n\n[*] Exiting...")
    