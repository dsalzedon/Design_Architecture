from abc import ABC,abstractmethod

class Director:


    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_walls()
        self._builder._build_ceiling()
        self._builder._build_garage()


class Builder(ABC):

    @abstractmethod
    def _build_walls():
        raise NotImplementedError

    @abstractmethod
    def _build_ceiling(self):
        raise NotImplementedError

    @abstractmethod
    def _build_garage(self):
        raise NotImplementedError

    @abstractmethod
    def _build_pool(self):
        raise NotImplementedError


class ConcreteBuilder(Builder):
    """Consctruct an object using the builder interface"""
    def _build_walls(self):
        print('Walls made with concrete')

    def _build_ceiling(self):
        print('Ceiling made with concrete')

    def _build_garage(self):
        print('Garage Walls made with concrete')

    def _build_pool(self):
        print('Pool walls made with concrete')


class WoodBuilder(Builder):

    def _build_walls(self):
        print('Walls made with wood')

    def _build_ceiling(self):
        print('Ceiling made with wood')

    def _build_garage(self):
        print('Garage Walls made with wood')

    def _build_pool(self):
        print('Pool walls made with wood')



concrete_builder = ConcreteBuilder()
director = Director()
director.construct(concrete_builder)

print('\nUsing no director')
wood_builder = WoodBuilder()
wood_builder._build_walls()
wood_builder._build_garage()
wood_builder._build_pool()
wood_builder._build_ceiling()
