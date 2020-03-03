#!/usr/bin/python3

from src.rsa import *
from src.utils import *
from colored import colored

# Enigma simulator: https://cryptii.com/pipes/enigma-machine

data = ""
user_input = []

def main():
    global user_input
    global data

    rsa = RSA()
    utils = Utils()

    commands = [
        ("d", unimplemented,                "| d            print data"),
        ("u", unimplemented,                "| u            update data"),
        ("l", unimplemented,                "| l <data>     load data from argument"),
        ("lf", load_file,                   "| lf <file>    load data from file"),

        ("ri", rsa.public_info,             "| ri           RSA print key information"),
        ("ru", rsa.uncipher,                "| ru           RSA uncipher"),

        ("rot13", unimplemented,            "| rot13        rot13 cipher"),
        ("xor", unimplemented,              "| xor          xor cipher"),
        ("shift", unimplemented,            "| shift        shift cipher"),
        ("bubblebabble", unimplemented,     "| bubblebabble bubblebabble cipher"),
        ("baconian", unimplemented,         "| baconian     baconian cipher"),

        ("q",  utils.quit,                  "| q            quit")
    ]

    while True:
        rsa.data = data
        utils.data = data

        print(" >> ", end="")
        user_input = input().split(" ")
        found = False

        with open("temp.txt", "w") as f:
            f.write(data)

        for command, function, info in commands:
            if command == user_input[0]:
                found = True
                rsa.command = user_input
                utils.command = user_input
                function() 

        if "?" in user_input[0]:
            found = True
            for command, function, info in commands:
                is_subset = True
                for i in range(0, len(user_input[0]) - 1):
                    if command[i] != user_input[0][i]:
                        is_subset = False
                if is_subset:
                    print(info)
        if not found:
            print("Command not found")

        os.system("rm temp.txt")

def unimplemented():
    print("Unimplemented")

def load_file():
    global data
    global user_input

    print("Loading data from file")
    data = "<empty>"
    with open(user_input[1], "r") as f:
        data = f.read()
    print("Data now is:")
    print(data)

main()
