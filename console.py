#!/usr/bin/python3
"""AirBnB command interpreter Module"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB Console Class"""

    prompt = "(hbnb) "
    list_class = ["BaseModel"]

    def do_EOF(self, line):
        """EOF comand exit console"""
        return True

    def do_quit(self, line):
        """quit command to exit console"""
        return True

    def do_create(self, line):
        """create new instance of BaseModel"""
        comands = line.split()
        if comands:
            if comands[0] in self.list_class:
                new_model = globals()[comands[0]]()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        comands = line.split()
        if comands:
            if comands[0] in self.list_class:
                if len(comands) < 2:
                    print("** instance id missing **")
                else:
                    inst = comands[0] + "." + comands[1]
                    storage.reload()
                    objects = storage.all()
                    if inst in objects:
                        obj = globals()[comands[0]](**objects[inst])
                        print(obj)
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        comands = line.split()
        if comands:
            if comands[0] in self.list_class:
                if len(comands) < 2:
                    print("** instance id missing **")
                else:
                    inst = comands[0] + "." + comands[1]
                    storage.reload()
                    objects = storage.all()
                    if inst in objects:
                        del objects[inst]
                        json_dict = json.dumps(objects)
                        with open("file.json", mode='w') as json_file:
                            json_file.write(json_dict)
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        storage.reload()
        objects = storage.all()
        list_obj = []
        comands = line.split()
        if comands:
            if comands[0] in self.list_class:
                for key in objects:
                    if key.split('.')[0] == comands[0]:
                        new_obj = globals()[comands[0]](**objects[key])
                        list_obj.append(str(new_obj))
                print(list_obj)
            else:
                print("** class doesn't exist **")
        else:
            for key in objects:
                new_obj = globals()[key.split('.')[0]](**objects[key])
                list_obj.append(str(new_obj))
            print(list_obj)

    def do_update(self, line):
        """ Updates an instance based on the class name and id"""
        comands = line.split()
        if comands:
            if comands[0] in self.list_class:
                if len(comands) > 1:
                    storage.reload()
                    objects = storage.all()
                    obj = comands[0] + "." + comands[1]
                    if obj in objects:
                        if len(comands) > 2:
                            if len(comands) > 3:
                                new_obj = globals()[comands[0]](**objects[obj])
                                setattr(new_obj, comands[2], comands[3])
                                new_obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()