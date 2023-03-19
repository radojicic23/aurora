#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time
import signal

from time import sleep
from sys import argv
from platform import system

# TODO -> Wrap up all in function or class so you can access this script from main menu.
# TODO -> Refactor everything, bad and shit code.
# TODO -> Update GUI more with more colors and stuff.

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

defaultportscan="50";


def menu1():
        print("\n\033[1;91m[*] Your output file is in your current directory \033[1;m")
        os.system("pwd")
        print("\033[1;91m[*] Your current directory \033[1;m")
        print("\n\033[1;91m[1] ~ Back to Main Menu \n[2] ~ Exit\n \033[1;m")
        option = input("root""\033[1;91m@aurora:~$\033[1;m ")
        
        if option == "1":
            mainLogic()
            
        if option == "2":
            print("\033[1;91m[*] Exiting...\033[1;m")
            sys.exit()
        else:
            print("[*] Please enter one of the options in the menu. \n[*] Exiting to the main menu.")
            time.sleep(2)
            mainLogic()


def sigint_handler(signum, frame):
    os.system("clear")
    print("~ CTRL+C detected!")
    print("\033[1;91m[*] Exiting...\033[1;m")
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)


def menu():
    print("""
\033[1;91m[*] Default Scan Types \033[1;m
[1] ~ Default Scan
[2] ~ Host Discovery
[3] ~ Port(SYN) Scan
[4] ~ Port(TCP) Scan
[5] ~ Port(UDP) Scan
[6] ~ Null scan (-sN)
[7] ~ FIN scan (-sF)
[8] ~ OS Analysis and Version Discovery
[9] ~ Nmap Script Engineering (default)
\033[1;91m[*] Firewall Bypass \033[1;m
[10] ~ Script Bypass (--script=firewall-bypass)
[11] ~ Data Length (--data-length <number> )
[12] ~ Smash (-ff)
\033[1;91m[*] Vulnerability Scanning \033[1;m
[13] ~ Default Vuln Scan (--script vuln)
[14] ~ FTP Vuln Scan
[15] ~ SMB Vuln Scan
[16] ~ HTTP Vuln Scan
[17] ~ SQL Injection Vuln Scan
[18] ~ Stored XSS Vuln Scan
[19] ~ Dom Based XSS vuln Scan
\033[1;91m[*] Subdomain Scanning \033[1;m
[20] ~ DNS Brute-force Hostnames
[21] ~ Subdomain/hostmap-crtsh
\033[1;91m[*] Other \033[1;m
[22] ~ Whois
[0] ~ Exit
""")


def mainLogic():
    
    menu()
    print("[+] Enter one of the options.\n")
    user_input = input("root""\033[1;91m@aurora:~$\033[1;m ")
    
    if user_input == "1":
        print("\n[*] Starting Default Scan...\n")
        time.sleep(2)
        os.system("clear")
        print("[+] Enter your IP address or example.com.")
        option1 = input("[+] Enter here: ")
        
        if not option1:
            print("\n[*] Please enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(3)
            os.system("clear")
            mainLogic()
        else:
            topport1=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            print("\n")
            
            if not topport1:
                os.system("nmap -vv --top-ports=" + defaultportscan + " " + option1 + " -oN " + option1)
            else:
                os.system("nmap -vv --top-ports=" + topport1 + " " + option1 + " -oN " + option1)
           
    menu1()
    
    if user_input =="2":
        print("\n[*] Starting Host Discovery...\n")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        option2 = input("[+] Enter here: ")

        if not option2:
            print("\n[*] Please enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport2=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport2:
                os.system("nmap -vv -Pn --top-ports=" + defaultportscan + " " + option2 + " -oN HostD-" + option2 + "-output")
            else:
                os.system("nmap -vv -Pn --top-ports=" + topport2 + " " + option2 + " -oN HostD-" + option2 + "-output")
           
    menu1()
   
    if user_input== "3":
        print("\n[*] Starting Port(SYN) Scan...\n")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        option3 = input("[+] Enter here: ")
        
        if not option3:
            print("\n[*] Please enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport3=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport3:
                os.system("nmap -vv -sS --top-ports=" + defaultportscan + " " + option3 + " -oN " + option3 + "-output")
            else:
                os.system("nmap -vv -sS --top-ports=" + topport3 + " " + option3 + " -oN " + option3 + "-output")
    
    menu1()
   
    if user_input== "4":
        print("\n[*] Starting Port(TCP) Scan...\n")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option4 = input("[+] Enter here: ")
        
        if not option4:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport4=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport4:
                os.system("nmap -vv –sT --top-ports=" + defaultportscan + " " + option4 + " -oN TcpScan-" + option4 + "-output")
            else:
                os.system("nmap -vv –sT --top-ports=" + topport4 + " " + option4 + " -oN TcpScan-" + option4 + "-output")
    
    menu1()
   
    if user_input== "5":
        print("[*] Starting Port(UDP) Scan...")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option5 = input("[+] Enter Here: ")
        
        if not option5:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport5=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport5:
                os.system("nmap -vv –sU --top-ports=" + defaultportscan + " " + option5 + " -oN UdpScan-" + option5 + "-output")
            else:
                os.system("nmap -vv –sU --top-ports=" + topport5 + " " + option5 + " -oN UdpScan-" + option5 + "-output")
           
    menu1()
    
    if user_input=="6":
        print("[*] Null scan (-sN)")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option6 = input("[+] Enter Here: ")
        if not option6:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport6=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport6:
                os.system("nmap -vv -sN --top-ports=" + defaultportscan + " " + option6 + " -oN NullScan-" + option6 + "-output")
            else:
                os.system("nmap -vv -sN --top-ports=" + topport6 + " " + option6 + " -oN NullScan-" + option6 + "-output")
                
    menu1()
    
    if user_input=="7":
        print("[*] FIN scan (-sF)")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option7 = input("[+] Enter Here: ")
        
        if not option7:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport7=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport7:
                os.system("nmap -vv -sF --top-ports=" + defaultportscan + " " + option7 + " -oN FinScan-" + option7 + "-output")
            else:
                os.system("nmap -vv -sF --top-ports=" + topport7 + " " + option7 + " -oN FinScan-" + option7 + "-output")
                
    menu1()
    
    if user_input=="8":
        print("[*] Starting OS Analysis and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option8 = input("[+] Enter Here: ")
        
        if not option8:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport8=input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport8:
                os.system("nmap –sS -sV -O --top-ports=" + defaultportscan + " " + option8 + " -oN Os-Version-" + option8 + "output")
            else:
                os.system("nmap –sS -sV -O --top-ports=" + topport8 + " " + option8 + " -oN Os-Version-" + option8 + "output")
       
    menu1()
    
    if user_input=="9":
        print("[*] Starting Nmap Script Engineering...")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option9 = input("[+] Enter Here: ")
        
        if not option9:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport9= input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport9:
                os.system("nmap -vv --script=default --top-ports=" + defaultportscan + " " + option9 + " -oN ScScan-" + option9 + "-output")
            else:
                os.system("nmap -vv --script=default --top-ports=" + topport9 + " " + option9 + " -oN ScScan-" + option9 + "-output")
           
    menu1()

    if user_input=="10":
        print("[*] Starting Nmap Scripting Firewall Bypass...")
        time.sleep(1)
        os.system("clear")
        print("[+] Enter your IP address or example.com")
        print("")
        option10 = input("[+] Enter Here: ")
        
        if not option10:
            print("[*] Please Enter IP Address!")
            print("\033[1;91m[*] You are grounded! Exiting to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport10= input("[+] Top Port? Example: 10 or 50, Default 50:  ")
            if not topport10:
                os.system("nmap -vv --script=firewall-bypass --top-ports=" + defaultportscan + " " + option10 + " -oN "+"firewallbaypass-" + option10 + "-output")
            else :
                os.system("nmap -vv --script=firewall-bypass --top-ports=" + topport10 + " " + option10 + " -oN "+"firewallbaypass-" + option10 + "-output")
    
    menu1()
    # TODO -> NEXT
    if user_input=="11":
        print("[*] Starting Data Length...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option11 = input(" Enter Your Destination: ")
        if not option11:
            print(" Please Enter IP Address!")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport11= input("[+] Top Port? Example 10 or 50, Default 50:  ")
            print("Append random data to sent packets")
            datalength=input("Number:")
            if not topport11:
                os.system("nmap --data-string "+datalength+" --top-ports="+defaultportscan+" "+option11+" -oN datalength-"+option11+"-output")
            else:
                os.system("nmap ---data-string +"+datalength+" --top-ports="+topport11+" "+option11+" -oN datalength-"+option11+"output")
           
    menu1()
    
    if user_input=="12":
        print("[*] Starting Smash (-ff)...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option12 = input(" Enter Your Destination: ")
        if not option12:
            print(" Please Enter IP Address!")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport12= input("[+] Top Port? Example 10 or 50, Default 50:  ")
            if not topport12:
                os.system("nmap -vv -ff --top-ports="+defaultportscan+" " +option12+" -oN "+"ff-"+option12+"-output" )
            else:
                os.system("nmap -vv -ff --top-ports="+topport12+" " +option12+" -oN "+"ff-"+option12+"-output" )

    menu1()
    
    if user_input=="13":
        print("[*] Starting Default Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option13 = input(" Enter Your Destination: ")
        if not option13:
            print(" Please Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport13=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport13:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script vuln " +option13+" -oN "+"VulnScanDef-"+option13+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport13+" --script vuln " +option13+" -oN "+"VulnScanDef-"+option13+"-output" )
       
    menu1()
    
    if user_input=="14":
        print("[*] Starting FTP Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option14 = input(" Enter Your Destination: ")
        if not option14:
            print(" Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport14=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport14:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script ftp* " +option14+" -oN "+"FTPvuln-"+option14+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport14+" --script ftp* " +option14+" -oN "+"FTPvuln-"+option14+"-output" )
       
    menu1()
    
    if user_input=="15":
        print("[*] Starting SMB Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option15=input(" Enter Your Destination: ")
        if not option15:
            print(" Please Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport15=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport15:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script smb* " +option15+" -oN "+"SMBvuln-"+option15+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport15+" --script smb* " +option15+" -oN "+"SMBvuln-"+option15+"-output" )
       
    menu1()
    
    if user_input=="16":
        print("[*] Starting HTTP Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option16=input("     Enter Your Destination: ")
        if not option16:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport16=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport16:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script smb* " +option16+" -oN "+"HTTPvuln-"+option16+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport16+" --script smb* " +option16+" -oN "+"HTTPvuln-"+option16+"-output" )
       
    menu1()  
    
    if user_input=="17":
        print("[*] Starting SQL Injection Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print("   Enter your IP address or example.com")
        print("")
        option17 = input("     Enter Your Destination: ")
        if not option17:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport17=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport17:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script=http-sql-injection " +option17+" -oN "+"SQLvuln-"+option17+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport17+" --script=http-sql-injection " +option17+" -oN "+"SQLvuln-"+option17+"-output" )
       
    menu1()
    
    if user_input=="18":
        print("[*] Starting Stored XSS Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option18 = input("     Enter Your Destination: ")
        if not option18:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport18=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport18:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script=http-stored-xss.nse " +option18+" -oN "+"StoredXSSvuln-"+option18+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport18+" --script=http-stored-xss.nse " +option18+" -oN "+"StoredXSSvuln-"+option18+"-output" )
       
    menu1()
    
    if user_input=="19":
        print("[*] Starting DOM Based XSS Vuln Scan...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option19=input("     Enter Your Destination: ")
        if not option19:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport19=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport19:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script=http-dombased-xss.nse " +option19+" -oN "+"DomBasedXSSvuln-"+option19+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport19+" --script=http-dombased-xss.nse " +option19+" -oN "+"DomBasedXSSvuln-"+option19+"-output" )
       
    menu1()
   
    if user_input=="20":
        print("[*] Starting DNS Brute-force Hostnames...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option20 = input("     Enter Your Destination: ")
        if not option20:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport20=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport20:
                os.system("nmap --top-ports="+defaultportscan+" --script dns-brute " +option20+" -oN "+"subdomain_DnsBruteForce-"+option20+"-output" )
            else:
                os.system("nmap --top-ports="+topport20+" --script dns-brute " +option20+" -oN "+"subdomain_DnsBruteForce-"+option20+"-output" )
                   
    menu1()
    
    if user_input=="21":
        print("[*] Starting Subdomain/hostmap-crtsh...")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option21= input("     Enter Your Destination: ")
        if not option21:
            print("Pls Enter Target ")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport21=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport21:
                os.system("nmap --top-ports="+defaultportscan+" --script hostmap-crtsh " +option21+" -oN "+"Subdomain_crtsh-"+option21+"-output" )
            else:
                os.system("nmap --top-ports="+topport21+" --script hostmap-crtsh " +option21+" -oN "+"Subdomain_crtsh-"+option21+"-output" )
                
    menu1()
    
    if user_input=="22":
        print("Whois ")
        time.sleep(1)
        os.system("clear")
        print(" Enter your IP address or example.com")
        print("")
        option22 = input("     Enter Your Destination: ")
        if not option22:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            mainLogic()
        else:
            topport22=input("[+] Top Port? Example 10 or 50, Default 50: ")
            if not topport22:
                os.system("nmap --top-ports="+defaultportscan+" --script whois-domain.nse " +option22+" -oN "+"whois-"+option22+"-output" )
            else:
                os.system("nmap --top-ports="+topport22+" --script whois-domain.nse " +option22+" -oN "+"whois-"+option22+"-output" )
                
    menu1()
    
    if user_input=="0":
        print("\n\033[1;91m[*] Exiting...\033[1;m") 
        sys.exit()
    else:
        print("\n\033[1;91m[*] Please enter one of the options.\033[1;m")
        time.sleep(2)
        mainLogic()
        
        
def root_control():
    if os.geteuid()==0:
        mainLogic()
    else:
        print("[*] Please run it with root access.")
        sys.exit()
        
root_control()
