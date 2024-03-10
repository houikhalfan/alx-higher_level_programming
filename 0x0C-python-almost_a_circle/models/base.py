#!/usr/bin/python3
"""base class"""

import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.
        If the id parameter is provided, it sets the id attribute
        of the instance to the given value.
        Otherwise, it increments the __nb_objects
        class attribute and assigns the resulting value to the id attribute of
         the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.
        If the input is None or an empty list, it returns the string "[]".
        Otherwise, it uses the json.dumps()
        function to convert the list of dictionaries to a JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.
        It first checks if list_objs is None
        and assigns an empty list if it is.
        Then, it creates a filename based on the
        class name and opens a file with that name in write mode.
        It creates a list comprehension to generate
        a list of dictionaries using the to_dictionary()
        method of each object in list_objs.
        Finally, it calls the to_json_string() method
        on the class cls (which is Base in this case)
        and writes the resul
        ting JSON string to the file.
        """
        if list_objs is None:
            list_objs = []
        f_name = "{}.json".format(cls.__name__)
        with open(f_name, "w") as f:
            dict = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.
        If the input is None or an empty string, it returns an empty list.
        Otherwise, it uses the json.loads() function to convert the JSON string
        to a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class.
        If the class name is 'Rectangle', it creates a Rectangle instance.
        Otherwise, it creates an instance using the default constructor.
        Then, it updates the attributes of the instance
        using the values from the dictionary.
        Finally, it returns the created instance.
        """
        if cls.__name__ == "Rectangle":
            abdelilah = cls(1, 1)
        else:
            abdelilah = cls(1)
        abdelilah.update(**dictionary)
        return abdelilah

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.
        The filename is based on the class name (e.g., Rectangle.json).
        If the file doesn't exist, it returns an empty list.
        Otherwise, it reads the JSON string from the file,
        converts it to a list of dictionaries
        using the from_json_string method,
        and creates instances using the create method.
        Finally, it returns the list of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        lis = cls.from_json_string(json_string)
        instance = [cls.create(**ins) for ins in lis]
        return instance
