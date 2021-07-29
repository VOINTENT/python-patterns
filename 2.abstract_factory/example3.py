from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class Factory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()


class Factory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ProductA1(AbstractProductA):

    def useful_function_a(self) -> str:
        return 'The result of product A1'


class ProductA2(AbstractProductA):

    def useful_function_a(self) -> str:
        return 'The result of product A2'


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        pass


class ProductB1(AbstractProductB):

    def useful_function_b(self) -> str:
        return 'The result of product B1'

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f'The result of collaborating with the ({result})'


class ProductB2(AbstractProductB):

    def useful_function_b(self) -> str:
        return 'The result of product B2'

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f'The result of the B1 collaborating with the ({result})'


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f'{product_b.useful_function_b()}')
    print(f'{product_b.another_useful_function_b(product_a)}')


if __name__ == '__main__':
    print('Client: Testing the same client code with the first 1.factory type:')
    client_code(Factory1())

    print()

    print('Client: Testing the same client code with second 1.factory type:')
    client_code(Factory2())
