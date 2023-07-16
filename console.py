#!/usr/bin/python3
"""
This module defines a cmd subclass that is an entry point to the commandline.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command processor class."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
