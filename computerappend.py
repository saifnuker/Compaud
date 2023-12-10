#computerappend.py <~ Use it to add to your text file
import compaud
import os
import re
from argparse import ArgumentTypeError
from argparse import ArgumentParser

def parse_arguments():
    pr = ArgumentParser(description='Computers auditing & filing', prefix_chars='--')

    pr.add_argument("--name",
                    metavar="desktop-01",
                    help='Host name of the computer device (required)',
                    required=True,
                    type=str
                    )
    
    def validate_ip(ip):
        if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
            raise ArgumentTypeError("Unacceptable IP address format")
        return ip
    
    pr.add_argument("--ip",
                    metavar="xxx.xxx.xxx.xxx",
                    help="IP address of the device (required)",
                    required=True,
                    type=validate_ip
                    )
    pr.add_argument("--location",
                    metavar="'Reception desk'",
                    help="Where the device is located on premises (required)",
                    required=True,
                    type=str
                    )
    pr.add_argument("--os",
                    metavar="Win7",
                    choices=['Win8', 'Win8.1', 'Win10', 'Win11', 'WinServer'],
                    help="The type of windows, Available options are: Win8, Win8.1, Win10, Win11, WinServer (required)",
                    required=True,
                    type=str
                    )
    pr.add_argument("--ver",
                    metavar="Version",
                    help="Windows version can be found by going to [Settings ~> System ~> About ~> version] (required)",
                    required=True,
                    type=str
                    )
    return pr.parse_args()

def main():
    computers = parse_arguments()
    filing = os.getcwd() + '\\computer_audit.txt'
    compaud.write_computer(computers, filing)
    with open(filing, 'r') as files:
        print(files.read())

if __name__ == "__main__":
    main()
