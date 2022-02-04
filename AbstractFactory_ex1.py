from __future__ import annotations
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def vocalize(self):
        raise NotImplementedError

    @abstractmethod
    def texture(self):
        raise NotImplementedError

class Dog(Animal):
    def vocalize(self):
        return 'guau'

    @abstractmethod
    def texture(self):
        raise NotImplementedError

class Cat(Animal):
    def vocalize(self):
        return 'miau'

    @abstractmethod
    def texture(self):
        raise NotImplementedError

class AnimalFactory(ABC):
    """fabrica abstracta"""

    @abstractmethod
    def create_dog(self) -> Dog:
        raise NotImplementedError

    @abstractmethod
    def create_cat(self) -> Cat:
        raise NotImplementedError

class StrippedAnimalFactory(AnimalFactory):
    """fabrica concreta1"""

    def create_dog(self) -> StripedDog:
        return StripedDog()

    def create_cat(self) -> StripedCat:
        return StripedCat()

class DottedAnimalFactory(AnimalFactory):
    """fabrica concreta2"""

    def create_dog(self) ->DottedDog:
        return DottedDog()

    def create_cat(self) -> DottedCat:
        return DottedCat()

class PlainAnimalFactory(AnimalFactory):
    def create_dog(self) -> PlainDog:
        return  PlainDog()

    def create_cat(self) -> PlainCat:
        return PlainCat()

class StripedDog(Dog):
    """producto concreto1"""

    def texture(self) -> str:
        return 'Dog with stripes'

class DottedDog(Dog):
    """producto1 concreto2"""

    def texture(self) -> str:
        return 'Dog with dots'

class PlainDog(Dog):
    """producto1 concreto3"""

    def texture(self) -> str:
        return 'Dog with plain color'

class StripedCat(Cat):
    """producto2 concreto1"""

    def texture(self) -> str:
        return 'Cat with stripes'

class DottedCat(Cat):
    """producto2 concreto2"""

    def texture(self) -> str:
        return 'Cat with dots'

class PlainCat(Cat):
    """producto2 concreto3"""

    def texture(self) -> str:
        return 'Cat with plain color'


class Application:
    def __init__(self, animal_factory: AnimalFactory) -> None:
        self.factory = animal_factory

    def run(self) -> None:
        a_dog = self.factory.create_dog()
        a_cat = self.factory.create_cat()

        print(a_dog.vocalize(), a_dog.texture())
        print(a_cat.vocalize(), a_cat.texture())


style = input('Choose a style: plain, striped, dotted: ')

factory = {
    'plain': PlainAnimalFactory,
    'striped': StrippedAnimalFactory,
    'dotted': DottedAnimalFactory
}.get(style, PlainAnimalFactory)

app = Application(factory())

app.run()
