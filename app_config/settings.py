import yaml
from functools import reduce
import operator
from pathlib import Path


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Settings(metaclass=SingletonMeta):

    def __init__(self, *args, **kwargs):
        print("Here", parent_dir + 'app_config/config.yaml')

        with open('config.yaml', "r") as stream:
            try:
                self.settings = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
    def get(self, element):
        return reduce(operator.getitem, element.split('.'), self.settings)


# setting = Settings()

# if __name__ == "__main__":
#     # The client code.
#
#     s1 = Settings()
#     s2 = Settings()
#     print(s1.get('databases.mongo.ENGINE'))
#     if id(s1) == id(s2):
#         print("Singleton works, both variables contain the same instance.")
#     else:
#         print("Singleton failed, variables contain different instances.")