#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
	"""Defines the HBNB command interpreter."""
	prompt="(hbnb)"
	def emptyline(self):
		"""Do nothing when receiving an empty line."""
		pass
	def do_quit(self,line):
		"""Quit command to exit the program."""
		return True
	def do_EOF(self,line):
		"""EOF signal to exit the program"""
		print("")
		return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
