from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List


class Component(ABC):

    def __init__(self) -> None:
        self._parent: Optional[Component] = None

    @property
    def parent(self) -> Optional[Component]:
        return self._parent

    @parent.setter
    def parent(self, parent: Component) -> None:
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):

    def operation(self) -> str:
        return 'Leaf'


class Composite(Component):

    def __init__(self) -> None:
        super().__init__()
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f'Branch(%s)' % '+'.join(results)


def client_code(component: Component) -> None:
    print(f'RESULT: %s' % component.operation())


def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print('RESULT: %s' % component1.operation())


if __name__ == '__main__':
    simple = Leaf()
    print('Client: I\'ve got a simple component:')
    client_code(simple)
    print()

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print('Client: Now I have got a composite tree:')
    client_code(tree)
    client_code2(tree, simple)
