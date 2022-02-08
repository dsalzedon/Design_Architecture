# OCP = Open for extension, Closed for modification
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        # added after class done
        # Breaking OCP
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        # added after class done
        # Breaking OCP
        for p in products:
            if p.color == color and p.size == size: yield p


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, specs):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
            ))

def breaking_ocp(product_list):

    product_filter = ProductFilter()
    print('Green Products (old):')
    for p in product_filter.filter_by_color(product_list, Color.GREEN):
        print(f' - {p.name} is green')


def following_ocp(product_list):
    better_filter = BetterFilter()

    print('Green products(new): ')
    green = ColorSpecification(Color.GREEN)
    for p in better_filter.filter(product_list, green):
        print(f' - {p.name} is green')

    print('Large blue Items:')
    # large = SizeSpecification(Size.LARGE)
    # blue = ColorSpecification(Color.BLUE)
    # large_and_blue = AndSpecification(large, blue)
    large_and_blue = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)
    for p in better_filter.filter(product_list, large_and_blue):
        print(f' - {p.name} is blue and large')


def main():
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    breaking_ocp(products)
    following_ocp(products)


if __name__ == '__main__':
    main()
