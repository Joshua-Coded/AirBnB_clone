#!/usr/bin/python3
"""This module is for the command Interpreter"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def _split(line):
    return line.split()


classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']


class HBNBCommand(cmd.Cmd):
    """The console class for the interpreter"""
    prompt = '(hbnb) '

    def default(self, line):
        """behavour for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        t = re.split(r"[.()]", line)
        if len(t) < 4:
            print("** Command doesn't exist **")
            return False
        t.remove('')
        try:
            t.remove('')
        except ValueError:
            pass
        try:
            x = t[2].replace("\"", "")
            y = x.replace(",", "")
            t[2] = y
        except IndexError:
            pass
        print(t)
        _class = t[0]
        _method = t[1]
        if len(t) == 3:
            _line = t[2]
        else:
            _line = ''
        if _class in classes:
            if _method in argdict.keys():
                argdict[_method]("{} {}".format(_class, _line))
            else:
                print("** method doesn't exist **")
        else:
            print("** class doesn't exist **")

        return False

    def emptyline(self):
        """Makes the interpreter not to execute anything if the line
            is empty or if ENTER is typed only
        """
        pass

    def do_EOF(self, line):
        """EOF signals end of file and quits the command interpreter
        Returns:
            True
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        Returns:
            True
        """
        return True

    def do_create(self, line):
        """Creates an instance of the class inputed"""
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                print(eval(g[0])().id)
                storage.save()

    def do_show(self, line):
        """prints the string rep. if an instance based on the class name
            and id
        """
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(g) == 1:
                    print("** instance id missing **")
                elif len(g) > 1:
                    object_dict = storage.all()
                    if "{}.{}".format(g[0], g[1]) not in object_dict:
                        print("** no instance found **")
                    else:
                        print(object_dict["{}.{}".format(g[0], g[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(g) == 1:
                    print("** instance id missing **")
                elif len(g) > 1:
                    object_dict = storage.all()
                    if "{}.{}".format(g[0], g[1]) not in object_dict:
                        print("** no instance found **")
                    else:
                        del object_dict["{}.{}".format(g[0], g[1])]
                        storage.save()

    def do_all(self, line):
        """prints all string representation of all instances based or
            not on the class name
        """
        object_dict = storage.all()
        if line == '':
            ulist = [str(h) for h in object_dict.values()]
            print(ulist)
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                ulist = [str(h) for h in object_dict.values()]
                dlist = []
                for i in ulist:
                    if g[0] in i:
                        dlist.append(i)
                print(dlist)

    def do_count(self, line):
        """Retrieve the number of instances of a given class."""
        g = _split(line)
        count = 0
        for obj in storage.all().values():
            if g[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
            updating an attribute
        """
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
                return False

            if len(g) == 1:
                print("** instance id missing **")
                return False

            object_dict = storage.all()
            if "{}.{}".format(g[0], g[1]) not in object_dict:
                print("** no instance found **")
                return False
            if len(g) == 2:
                print("** attribute name missing **")
                return False

            if len(g) == 3:
                print("** value missing **")
                return False

            if len(g) >= 4:
                obj = object_dict["{}.{}".format(g[0], g[1])]
                if g[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[g[2]])
                    obj.__dict__[g[2]] = valtype(g[3])
                else:
                    obj.__dict__[g[2]] = g[3]
            elif type(eval(g[2])) == dict:
                obj = object_dict["{}.{}".format(g[0], g[1])]
                for k, v in eval(g[2]).items():
                    if (k in obj.__class__.__dict__.keys() and
                       type(obj.__class__.__dict__[k]) in {str, int, float}):
                        valtype = type(obj.__class__.__dict__[k])
                        obj.__dict__[k] = valtype(v)
                    else:
                        obj.__dict__[k] = v
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
