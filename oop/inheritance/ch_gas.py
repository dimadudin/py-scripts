class Vehicle:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, fuel_price):
        return (distance / self.efficiency) * fuel_price

    def get_cargo_volume(self):
        pass


class Truck(Vehicle):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.__load_weight = load_weight
        self.__bed_area = bed_area

    def get_trip_cost(self, distance, fuel_price):
        return super().get_trip_cost(distance, fuel_price) + (self.__load_weight * 0.01)

    def get_cargo_volume(self):
        return 2 * self.__bed_area 


class Car(Vehicle):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.__cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.__cargo_volume

