from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Builder(ABC):
    @abstractmethod
    def set_car_type(self, car_type: CarType) -> None:
        pass

    @abstractmethod
    def set_seats(self, seats: int) -> None:
        pass

    @abstractmethod
    def set_engine(self, engine: Engine) -> None:
        pass

    @abstractmethod
    def set_transmission(self, transmission: Transmission) -> None:
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        pass

    @abstractmethod
    def set_gps_navigator(self, gps_navigator: GPSNavigator) -> None:
        pass


class CarBuilder(Builder):

    def __init__(self) -> None:
        self._car_type: Optional[CarType] = None
        self._seats: Optional[int] = None
        self._engine: Optional[Engine] = None
        self._transmission: Optional[Transmission] = None
        self._trip_computer: Optional[TripComputer] = None
        self._gps_navigator: Optional[GPSNavigator] = None

    def set_car_type(self, car_type: CarType) -> None:
        self._car_type = car_type

    def set_seats(self, seats: int) -> None:
        self._seats = seats

    def set_engine(self, engine: Engine) -> None:
        self._engine = engine

    def set_transmission(self, transmission: Transmission) -> None:
        self._transmission = transmission

    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        self._trip_computer = trip_computer

    def set_gps_navigator(self, gps_navigator: GPSNavigator) -> None:
        self._gps_navigator = gps_navigator

    def get_result(self) -> Car:
        return Car(

        )


class CarType:
    pass


class Engine:
    pass


class Transmission:
    pass


class TripComputer:
    pass


class GPSNavigator:
    pass


class Car:
    pass
