import copy
from typing import Any


class SelfReferencingEntity:

    def __init__(self) -> None:
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int: int, some_list_of_objects: list[Any], some_circular_ref: Any) -> None:
        self.some_circular_ref = some_circular_ref
        self.some_list_of_objects = some_list_of_objects
        self.some_int = some_int

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memodict={}):
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects)
        some_circular_ref = copy.deepcopy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memodict)
        return new


if __name__ == '__main__':
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)