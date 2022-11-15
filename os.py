import time
import os

print("""

██╗░░░░░██╗░██████╗░███╗░░░███╗░█████╗░░░░░░░░█████╗░░██████╗
██║░░░░░██║██╔════╝░████╗░████║██╔══██╗░░░░░░██╔══██╗██╔════╝
██║░░░░░██║██║░░██╗░██╔████╔██║███████║█████╗██║░░██║╚█████╗░
██║░░░░░██║██║░░╚██╗██║╚██╔╝██║██╔══██║╚════╝██║░░██║░╚═══██╗
███████╗██║╚██████╔╝██║░╚═╝░██║██║░░██║░░░░░░╚█████╔╝██████╔╝
╚══════╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░

""")

print("""
[1]Log in...
[2]Already done with setup...
[3]I haven't created an acount
""")

setup = input("[?]: ")

if setup == '1':
    name = input(str("Please Enter UserName/email: "))
    pas = input(str("Please Enter Password: "))
    os.startfile("home.py")

if setup == '2':
    os.startfile("home.py")

if setup == '3':
    os.startfile("Start.py")


    
    





