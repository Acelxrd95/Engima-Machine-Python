# Import the necessary packages
from consolemenu import ConsoleMenu, SelectionMenu, MultiSelectMenu
from consolemenu.items import MenuItem, FunctionItem, CommandItem, SubmenuItem
from enigma import Enigma

machine = Enigma()


def validate(msg, cond):
    while True:
        var = input(msg)
        if cond == "alpha":
            if var.isalpha():
                if len(var) == 1:
                    break
                else:
                    print("Input must be only 1 letter")
            else:
                print("Input is not an alphabet")
    return var


import subprocess
import platform
import re


def clearterminal() -> None:
    if platform.system() == "Windows":
        subprocess.check_call("cls", shell=True)
    else:
        print(subprocess.check_output("clear").decode())


def exceptionHandlingMenu(message: str, num_options: int) -> int:
    print(message)
    error: bool = False
    while True:
        try:
            if error:
                print(f"Please enter a number between 1 and {num_options}", end=": ")
                error = False
            choice = input()
            if type(choice) == float:
                print("Please dont enter an integer not a float")
                continue
            choice = int(choice)
        except:
            error = True
        else:
            if choice >= 1 and choice <= num_options:
                return choice
            else:
                error = True


if __name__ == "__main__":
    clearterminal()
    mach = Enigma()
    while True:
        unc_string: str = input("Please enter text to be encrypted\decrypted: ")
        regex_str = re.findall(r"[^\w\d\.\)\(\]\[\{\},\?\^\/\\\"\'\s]", unc_string)
        if regex_str:
            print(f"The characters {regex_str} are not allowed")
        else:
            break

    start_pos = tuple(
        [
            validate(
                f"Rotor {i} starting position\nEnter a letter between A and Z: ",
                "alpha",
            )
            for i in [1, 2, 3]
        ]
    )
    rotors = []
    for key, rot in mach.rotorkeys_store.items():
        
    rotors = tuple(rotors)
