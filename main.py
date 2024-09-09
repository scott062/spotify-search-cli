from auth import authenticate
import os
from commands import commands_lookup, search

def main():
    try:
        authenticate()
        while True:
            cmd = input("Please type the number of the desired command:\n1. Search\n2. Pause\n3. Go Back\n4. Go Next\n")
            print(search())
            print(f"you typed: {cmd}")
            if cmd in commands_lookup:
                print("good command...")
                commands_lookup[cmd]
            else:
                print("Invalid command, try again")
    finally:
        print("deleting token before ending")
        os.remove("token.txt")
        print("done")

main()


