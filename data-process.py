import sys



def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")


"""
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
./variables.py
export FRUIT=Pineapple
./variables.py

"""


##commande line Arguments and Exits status  
#command line arguments are the arguments passed to a program when it is invoked from the command line. In Python, you can access these arguments using the sys module. The sys.argv list contains the command line arguments, with sys.argv[0] being the name of the script and subsequent elements being the additional arguments.
#Example:
#l'importation du module sys en top

print("Listes des arguments de la ligne de commande :", sys.argv,sep="\n")

# Exit status is a way for a program to communicate its success or failure to the operating system or calling process. In Python, you can use the sys.exit() function to exit a program and provide an exit status code. By convention, an exit status of 0 indicates success, while any non-zero value indicates an error or failure.

#Example:
if len(sys.argv) < 2:
    print("Usage: python script.py <arg1> <arg2> ...")
    sys.exit(1)  # Exit with a non-zero status code to indicate an error
    
    
