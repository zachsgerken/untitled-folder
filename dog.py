class Dog:

    def __init__(self, name, age, breed='mutt'):
        self.__name = name
        self.__age = age
        self.__breed = breed

    def get_name(self):
        return self.__name

    def set_name(self, name):
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
            self.__breed = breed

    def bark(self):
        return f'{self.__name} is barking... Woof Woof!!'

    def run(self):
        return f'{self.__name} is running!!'

    def __str__(self):
        return f'This is a {self.__age} year old {self.__breed} named {self.__name}'