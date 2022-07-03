#!/usr/bin/python3
"""Class HBNBComand"""


import cmd
import json



class HBNBCommand(cmd.Cmd):
    """Simple command processor"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """end of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
