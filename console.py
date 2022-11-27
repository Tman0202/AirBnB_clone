#!/usr/bin/python3
"""Entry point to the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_quit(self):
        """Exits from this shell and back to the original bash shell"""
        pass
    def do_EOF(self):
        """to exit the shell ctrl-c"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()