from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
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
            car_type=self._car_type,
            seats=self._seats,
            engine=self._engine,
            transmission=self._transmission,
            trip_computer=self._trip_computer,
            gps_navigator=self._gps_navigator
        )


class CarManualBuilder(Builder):

    def __init__(self, car_type: CarType, seats: int, engine: Engine, transmission: Transmission,
                 trip_computer: TripComputer, gps_navigator: GPSNavigator) -> None:
        self._gps_navigator = gps_navigator
        self._trip_computer = trip_computer
        self._transmission = transmission
        self._engine = engine
        self._seats = seats
        self._car_type = car_type

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


class Car:

    def __init__(self, car_type: CarType, seats: int, engine: Engine, transmission: Transmission,
                 trip_computer: TripComputer, gps_navigator: GPSNavigator) -> None:
        self._car_type = car_type
        self._seats = seats
        self._engine = engine
        self._transmission = transmission
        self._trip_computer = trip_computer
        if trip_computer is not None:
            self._trip_computer.set_car(self)
        self._gps_navigator = gps_navigator
        self._fuel: float = 0

    @property
    def car_type(self):
        return self._car_type

    @property
    def seats(self):
        return self._seats

    @property
    def engine(self):
        return self._engine

    @property
    def transmission(self):
        return self.transmission

    @property
    def trip_computer(self):
        return self._trip_computer

    @property
    def gps_navigator(self):
        return self._gps_navigator

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value: float):
        self._fuel = value


class Manual:
    def __init__(self, car_type: CarType, seats: int, engine: Engine, transmission: Transmission,
                 trip_computer: TripComputer, gps_navigator: GPSNavigator) -> None:
        self._gps_navigator = gps_navigator
        self._trip_computer = trip_computer
        self._transmission = transmission
        self._engine = engine
        self._seats = seats
        self._car_type = car_type

    def print(self) -> str:
        info = ''
        info += 'Type of car: %s\n' % self._car_type
        info += 'Count of seats: %s\n' % self._seats
        info += 'Engine volume - %s; mileage - %s\n' % self._engine.get_volume(), self._engine.get_mileage()
        info += 'Transmission: %s\n'
        if self._trip_computer is not None:
            info += 'Trip computer: Functional\n'
        else:
            info += 'Trip computer: N/A\n'

        if self._gps_navigator is not None:
            info += 'GPS Navigator: Functional'
        else:
            info += 'GPS Navigator: N/A\n'
        return info


class CarType(str, Enum):
    CITY_CAR = 'city-car'
    SPORTS_CAR = 'sports-car'
    SUV = 'suv'


class Engine:
    def __init__(self, volume: float, mileage: float) -> None:
        self._started: Optional[bool] = None
        self._mileage = mileage
        self._volume = volume

    def on(self) -> None:
        self._started = True

    def off(self) -> None:
        self._started = False

    def go(self, mileage: float) -> None:
        if self._started:
            self._mileage += mileage
        else:
            raise TypeError('Can\'t go(), you must start engine first!')

    @property
    def started(self):
        return self._started

    @property
    def mileage(self):
        return self._mileage

    @property
    def volume(self):
        return self._volume


class GPSNavigator:
    def __init__(self, manual_route: Optional[str] = None) -> None:
        if manual_route:
            self._manual_route = manual_route
        else:
            self._manual_route = '221b, Baker Street, London  to Scotland Yard, 8-10 Broadway, London'

    @property
    def manual_route(self):
        return self._manual_route


class Transmission(str, Enum):
    SINGLE_SPEED = 'single-speed'
    MANUAL = 'manual'
    AUTOMATIC = 'AUTOMATIC'
    SEMI_AUTOMATIC = 'SEMI_AUTOMATIC'


class TripComputer:
    def __init__(self) -> None:
        self._car: Optional[Car] = None

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        self._car = value

    def show_fuel_level(self) -> None:
        print('Fuel level: %s' % self._car.fuel)

    def show_status(self) -> None:
        if self._car.engine.started:
            print('Car is started!')
        else:
            print('Car isn\'t started!')


class Director:
    def construct_sports_car(self, builder: Builder) -> None:
        builder.set_car_type(CarType.SPORTS_CAR)
        builder.set_seats(2)
        builder.set_engine(Engine(3.0, 0))
        builder.set_transmission(Transmission.SEMI_AUTOMATIC)
        builder.set_trip_computer(TripComputer())
        builder.set_gps_navigator(GPSNavigator())
