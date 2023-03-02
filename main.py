from lan_scanner import lan_scan
from port_scanner import port_scan


print(" _______  _______ _________ _______  _______\n"
      "(  ___  )(  ____ \\__   __/(  ____ )(  ___  )\n"
      "| (   ) || (    \/   ) (   | (    )|| (   ) |\n"
      "| (___) || (_____    | |   | (____)|| (___) |\n"
      "|  ___  |(_____  )   | |   |     __)|  ___  |\n"
      "| (   ) |      ) |   | |   | (\ (   | (   ) |\n"
      "| )   ( |/\____) |   | |   | ) \ \__| )   ( |\n"
      "|/     \|\_______)   )_(   |/   \__/|/     \|\n\n")

print(""" """)

print('-' * 52)
print("[*] ~ 1. Discover all devices on your network.")
print("[*] ~ 2. Port Scanner.")
print('-' * 52)

try:
    USER_INPUT = input("Enter your option: ")
    
    if USER_INPUT == '1':
        lan_scan()
    elif USER_INPUT == '2':
        port_scan()
except KeyboardInterrupt:
    print("\n\n[*] Exiting...")
    