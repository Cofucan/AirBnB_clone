#!/usr/bin/python3
"""
This module defines a cmd subclass that is an entry point to the commandline.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A simple commandline interpreter for HBNB."""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Enables exiting the program with Crtl-D
        """
        return True

    def do_quit(self, line) -> bool:
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
