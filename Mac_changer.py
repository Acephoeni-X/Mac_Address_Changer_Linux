import subprocess
import time
from termcolor import colored
import random
import re
import threading
from time import sleep

string_inter = "00:00:00:00:00:00"

def one_time(interface):

    text = colored("\n\n  Mac Address Changed: ", 'green', attrs=["reverse", "blink"])
    print (text)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    #time.sleep(3)
    mylist = ["a", "b", "c"]
    new = ""
    for i in string_inter:
        if i!=":":
            new += str(random.randrange(0,9,2))
        # elif i == 1:
        #      new += str(random.choice(mylist))
        else:
            new += ":"

    # old_mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", oldmac)
    subprocess.call("ifconfig " + interface + " hw" + " ether " + new, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell = True)
    # subprocess.call("ifconfig " + interface, shell = True)
    new_mac = colored(new, "green")
    print ("\n\nNew Mac-Address is: " + new_mac + "\n\n")

def many_time(interface, time):
    #threading.Timer(time, many_time(interface, time)).start()
    #time = 30
    subprocess.call("ifconfig "+ interface+ " down", shell=True)
    new= ""
    for i in string_inter:
        if i!=":":
            new += str(random.randrange(0, 9, 2))
        else:
            new += ":"
    new_mac = colored(new, 'green', attrs= ["bold", "bold"])
    subprocess.call("ifconfig "+ interface+ " hw ether "+ new, shell=True)
    subprocess.call("ifconfig "+ interface+ " up", shell=True)
    print("\nNew Mac: "+ new_mac + "  (Ctrl+ C to stop)")
    sleep(int(time))
    many_time(interface, time)

    


def second_func(interface):
    subprocess.call("clear", shell = True)
    text = colored("----------MAC ADDRESS CHANGER--------", 'red', attrs=["reverse", "bold"])
    for i in range(0,1):
        print("\n")
    print(text)
    for i in range(0, 1):
        print("\n")

    print("Do you want to change mac for :")
    print("1. Only One Time")
    print("2. After some specific time")
    # oldmac = subprocess.check_output("ifconfig "+ interface,shell = True )
    decision = input("\nEnter the choice (1 or 2): ")

    if(int(decision) == 1):
        one_time(interface)

    if(int(decision) == 2):
        print("\n\nBy Default Time is 30 sec")
        print ("\nSelect the time (in seconds): ", end=" ")
        time = input()
        color_time = colored(time, "green", attrs=["reverse","bold"])
        print("\nYou will be disconnected after every "+ str(color_time)+ " second, for very short period of time.\n Are You sure: ", end=" ")
        decision2 = input()
        if(decision2 == 'Y' or decision2 == 'y'):
            many_time(interface,time)


def function_main():
    subprocess.call("clear", shell = True)
    text = colored("------------MAC ADDRESS CHANGER-----------", 'red', attrs = ["reverse", "bold"])
    for i in range(0,1):
        print("\n")
    print(text)
    for i in range(0,2):
        print("\n")

    interface = input("Enter the name of the interface: ")
    second_func(interface)
    # if(interface == "eth0"):
    #     second_func(interface)
    # elif(interface!="eth0"):
    #     Error = colored("\n\n\n  The Interface You Have Entered Is Wrong  ", 'red', attrs=["reverse", "blink"] )
    #     print(Error+"\n\n")

function_main()