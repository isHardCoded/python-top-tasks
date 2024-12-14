class Car:
    def __init__(self, brand, model, speed):
        self._brand = brand
        self._model = model
        self._speed = speed

    def get_info(self):
        return f"Brand: {self._brand}\nModel: {self._model}\n Стандартная скорость: {self._speed}"

    def move(self):
        return f"{self._brand} {self._model} едет."
    
    def stop(self):
        return f"{self._brand} {self._model} остановилась."
    
    # метод для ускорения
    def increase_speed(self, value):
        self._speed += value
        return f"Скорость увеличена на {value}. Текущая скорость машины: {self._speed}"

    # метод для замедления
    def decrease_speed(self, value):
        self._speed -= value
        return f"Скорость уменьшина на {value}. Текущая скорость машины: {self._speed}"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self._battery_capacity = battery_capacity

    def get_info(self):
        return f"{super().get_info()} с аккамулятором - {self._battery_capacity}"

    def charge_finished(self):
        return f"Зарядка завершена. Объем заряда: {self._battery_capacity}"
    
class GasolineCar(Car):
    def __init__(self, brand, model, gas_capacity):
        super().__init__(brand, model)
        self._gas_capacity = gas_capacity

    def get_info(self):
        return f"{super().get_info()} с объемом бака - {self._gas_capacity}"

    def charge_finished(self):
        return f"Заправка завершина. Объем бака: {self._gas_capacity}"

electric = ElectricCar("Tesla", "Cybertrack", 100)
print(electric.get_info())

gasoline = GasolineCar("Toyota", "Supra", 52)
print(gasoline.get_info())
