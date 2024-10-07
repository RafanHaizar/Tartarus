#!/usr/bin/env python

import sys
import os

def run():
    if not check_eula_file():
        prompt_eula()
    else:
        try:
            os.system("python main.py")
        except Exception as e:
            print(f"Error running main.py: {e}")
            sys.exit(1)

def check_eula_file():
    return os.path.isfile("tartarus.agreement")

def red(text):
    return f"\033[1;91m{text}\033[0m"

def prompt_eula():
    os.system('cls' if os.name == 'nt' else 'clear')
    notice = (
        '______________________________________________________________________________\n'
        '|                 ATTENTION!!! ATTENTION!!! ATTENTION!!!                     |\n'
        '|                          Tartarus v0.0.1 Alpha                             |\n'
        '|____________________________________________________________________________|\n'
        '| This program contains live and dangerous malware files.                    |\n'
        '| This program is intended to be used only for malware analysis and research |\n'
        '| and by agreeing to the EULA you agree to use it only for legal purposes    |\n'
        '| and for studying malware.                                                  |\n'
        '| You understand that these files are dangerous and should only be run on VMs|\n'
        '| you can control and know how to handle. Running them on a live system will |\n'
        '| infect your machines with live and dangerous malware!                      |\n'
        '|____________________________________________________________________________|\n'
    )
    print(red(notice))
    
    eula_answer = input('Type YES in capital letters to accept this EULA.\n > ')
    if eula_answer.strip() == 'YES':
        with open("tartarus.agreement", 'w+') as new_file:
            new_file.write(eula_answer + '\n')
        run_main_program()
    else:
        print('You need to accept the EULA.\nExiting the program.')
        sys.exit(0)

def run_main_program():
    try:
        os.system("python main.py")
    except Exception as e:
        print(f"Error running main.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
