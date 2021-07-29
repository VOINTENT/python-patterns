from abc import abstractmethod, ABC


class ChairInterface(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def is_on(self):
        pass


class TableInterface(ABC):
    pass


class SofaInterface(ABC):
    pass


class VictorianChair(ChairInterface):
    def has_legs(self):
        pass

    def is_on(self):
        pass


class ModernChair(ChairInterface):
    def has_legs(self):
        pass

    def is_on(self):
        pass


class VictorianTable(TableInterface):
    pass


class ModernTable(TableInterface):
    pass


class VictorianSofa(SofaInterface):
    pass


class ModernSofa(SofaInterface):
    pass


class FurnitureFactoryInterface(ABC):
    @abstractmethod
    def create_chair(self) -> ChairInterface:
        pass

    @abstractmethod
    def create_table(self) -> TableInterface:
        pass

    @abstractmethod
    def create_sofa(self) -> SofaInterface:
        pass


class VictorianFurnitureFactoryInterface(FurnitureFactoryInterface):
    def create_chair(self) -> ChairInterface:
        pass

    def create_table(self) -> TableInterface:
        pass

    def create_sofa(self) -> SofaInterface:
        pass
