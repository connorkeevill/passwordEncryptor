#CK

# | Note:
# |-----------------------------------------------------------
# | This file will 'command' the running of the program. It
# | creates the command line and will ensure that the file
# | and all other dependencies are acquired before being
# | ran. The CommandLine() class makes this file more
# | clean, to make it just what initiates the rest.
# |--------------------------------------------

from objects.CommandLine import CommandLine
from objects.FileHandler import FileHandler

file = FileHandler('../data/accounts.txt')
console = CommandLine(file)
