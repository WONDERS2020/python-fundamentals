#!/usr/bin/python3
import cmd
import os


class Filemanager(cmd.Cmd):
    prompt = "(fm) "
    intro = "Welcome to the file manager CLI. Type help or ? to list command.\n" 
    
    def emptyline (self):
        """ A methode that handle empty line passing"""
        return super().emptyline()
    
    def do_exit(self, arg):
        """ Exit the file mnager CLI"""
        print("Existing filemanager. Goodbye")
        return True
    
    def do_quit(self, line):
        """ Quit the filemanager"""
        return True
    
    def do_EOF(self, line):
        """ Handle EOF (ctrl + D) to exit the CLI """
        print("Existing filemanager. Goodbye")
        return True
    

if __name__ == "__main__":
    Filemanager().cmdloop()