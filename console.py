#!/usr/bin/python3
"""Entry point to the command interpreter"""
import shlex
from models import storage
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The command class"""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User"]

    def emptyline(self):
        pass

    def do_quit(self, s):
        """Quit command to exit the program \n"""
        return True

    def do_EOF(self):
        """to exit the shell ctrl-c"""
        return True

    def do_create(self, obj):
        """Creates new instance of Basemodel and saves it to JSON file"""
        if obj:
            if obj in HBNBCommand.__classes:
                new_obj = BaseModel()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        params = shlex.split(arg)
        __new_dict = storage.all()

        if not params[0]:
            print("** class name missing **")
        elif params[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not params[1]:
            print("** instance id missing **")
        elif "{}.{}".format(params[0], params[1]) not in __new_dict:
            print("** no instance found **")
        else:
            print(__new_dict["{}.{}".format(params[0], params[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the specified class name
        and id and save the change to JSON file
        """
        params = shlex.split(arg)
        __new_dict = storage.all()
        if not params[0]:
            print("** class name missing **")
        elif params[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not params[1]:
            print("** instance id missing **")
        elif "{}.{}".format(params[0], params[1]) not in __new_dict:
            print("** no instance found **")
        else:
            del __new_dict["{}.{}".format(params[0], params[1])]
            storage.save()

    def do_all(self, arg):
        """prints all String representation of all instances
        based or not in the class nmae"""
        __new_dict = storage.all()
        __new_list = []
        if len(arg) > 0 and arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for i in __new_dict.values():
                if len(arg) > 0 and arg[0] == i.__class__.__name__:
                    __new_list.append(i.__str__())
                elif len(arg) == 0:
                    __new_list.append(i.__str__())
            print(__new_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
            or updating attribute and save the change to JSON file"""
        params = shlex.split(arg)
        __new_dict = storage.all()
        if len(params) < 5:
            if not params[0]:
                print("** class name missing **")
                return False
            elif len(params) > 0 and params[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return False
            elif not params[1]:
                print("** instance id missing **")
                return False
            elif "{}.{}".format(params[0], params[1]) not in __new_dict:
                print("** no instance found **")
                return False
            elif not params[2]:
                print("** attribute name missing **")
                return False
            elif len(params) == 3:
                try:
                    type(eval(params[2])) != dict
                except NameError:
                    print("** value missing **")
                    return False

            if len(params) == 4:
                obj = __new_dict["{}.{}".format(params[0], params[1])]
                if params[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[params[2]])
                    obj.__dict__[params[2]] = valtype(params[3])
                else:
                    obj.__dict__[params[2]] = params[3]
            elif type(eval(params[2])) == dict:
                obj = __new_dict["{}.{}".format(params[0], params[1])]
                for k, v in eval(params[2]).items():
                    if k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]
                    ) in {str, int, float}:
                        valtype = type(obj.__class__.__dict__[k])
                        obj.__dict__[k] = valtype(v)
                    else:
                        obj.__dict__[k] = v
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
