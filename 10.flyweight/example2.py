import json
from typing import Dict


class Flyweight:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print('Flyweight: Displaying shared (%s) and unique (%s) state.')


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}
    