"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра."""


class Stationery:
    title = "\n -[Канцелярская принадлежность]-"

    def draw(self):
        print("Отрисовка")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()
