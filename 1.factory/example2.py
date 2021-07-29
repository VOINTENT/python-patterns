from __future__ import annotations
from abc import ABC, abstractmethod


class CreatorInterface(ABC):
    @abstractmethod
    def factory_method(self) -> ProductInterface:
        pass

    def some_operation(self) -> str:
        product: ProductInterface = self.factory_method()
        result = f'Creator: The result of create is {product.operation()}'
        return result


class ConcreteCreator1(CreatorInterface):

    def factory_method(self) -> ProductInterface:
        return ConcreteProduct1()


class ConcreteCreator2(CreatorInterface):

    def factory_method(self) -> ProductInterface:
        return ConcreteProduct2()


class ProductInterface(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(ProductInterface):

    def operation(self) -> str:
        return '{Result of the ConcreteProduct1}'


class ConcreteProduct2(ProductInterface):

    def operation(self) -> str:
        return '{Result of the ConcreteProduct2}'


def client_code(creator: CreatorInterface) -> None:
    print('Client: I run the CreatorInterface...\n' f'{creator.some_operation()}')


if __name__ == '__main__':
    print('App: Launched with the ConcreteCreator1')
    client_code(ConcreteCreator1())
    print()

    print('App: Launched with the ConcreteCreator2')
    client_code(ConcreteCreator2())
    print()
