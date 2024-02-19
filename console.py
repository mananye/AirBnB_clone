#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parse the arguments into class name, method, and dictionary."""
    class_method_dict = re.search(r"([a-zA-Z_]+)\.(\w+)\((.*)\)", arg)
    if class_method_dict:
        class_name = class_method_dict.group(1)
        method = class_method_dict.group(2)
        dict_str = class_method_dict.group(3)
        try:
            dictionary = eval(dict_str)
        except Exception:
            return None, None, None
        return class_name, method, dictionary
    return None, None, None


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        class_name, method, dictionary = parse(arg)
        if class_name and method:
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            if method == "update":
                if dictionary:
                    return self.do_update("{} {} {}".format(class_name, dictionary.get("id", ""), dictionary))
                else:
                    print("** invalid syntax. Usage: <class name>.update(<id>, <dictionary representation>) **")
                    return
            else:
                print("** invalid syntax. **")
                return
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.get(args[0], args[1])
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.get(args[0], args[1])
        if obj is None:
            print("** no instance found **")
        else:
            storage.delete(obj)
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = arg.split()
        if args and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        objects = []
        for obj in storage.all().values():
            if not args or obj.__class__.__name__ == args[0]:
                objects.append(str(obj))
        print(objects)

    def do_count(self, arg):
        """Usage: count <class>
        Retrieve the number of instances of a given class."""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.get(args[0], args[1])
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except Exception:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

