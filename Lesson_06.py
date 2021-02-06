# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __light_color = ['Красный', 'Жёлтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Цвет светофора \n '
                  f'{TrafficLight.__light_color[i]}')
            # Уменьшил показатели задержек относительно задания, чтобы не было так мучительно долго отлаживать.
            if i == 0:
                sleep(2)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(2)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class WeightCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


total_mass = WeightCount(5, 10000, 230)
print(f'Масса асфальта равна {total_mass.mass()}')

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_info = Position('Иван', 'Пупкин', 'Трудовик', 25000, 3000)
print(f'Имя работника: {worker_info.get_full_name()}')
print(f'Должность работника: {worker_info.position}')
print(f'Зарплата работника: {worker_info.get_total_income()}')

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал движение.'

    def stop(self):
        return f'{self.name} остановился.'

    def turn_right(self):
        return f'{self.name} повернул направо.'

    def turn_left(self):
        return f'{self.name} повернул налево.'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed}.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной для городского автомобиля.'
        else:
            return f'Скорость {self.name} в пределах разрешенной для городского автомобиля.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость слежубной машины {self.name} равна {self.speed}.')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для служебной машины.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - не полицейская машина'


ferrari = SportCar(120, 'Красная', 'Феррари', False)
lada = TownCar(30, 'Серая', 'Лада', False)
niva = WorkCar(80, 'Коричневая', 'Нива', True)
dodge = PoliceCar(130, 'Черный',  'Додж', True)
print(niva.turn_left())
print(f'{ferrari.name} - полицеская машина? {ferrari.is_police}')
print(f'{niva.name} - полицеская машина? {niva.is_police}')
print(f'{lada.go()}, {ferrari.stop()}')
print(f'{niva.go()} со скоростью {niva.show_speed()}')
print(f'{niva.name} имеет {niva.color} цвет.')

print(ferrari.show_speed())
print(lada.show_speed())
print(dodge.police())
print(dodge.show_speed())

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки, используем {self.title}.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки, используем {self.title}.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки, используем {self.title}.'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
