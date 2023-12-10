# compaud.py 


class compaud:
    def __init__(self, name, ip, location, os, ver):
        self.name = name
        self.ip = ip
        self.location = location
        self.os = os
        self.ver = ver


def write_computer(computer, path):
    file = open(path, 'a+')
    file.write(f'{computer.name}\n{computer.ip}\n{computer.location}\n{computer.os}\n{computer.ver}\n————————————————\n')
    file.close()
