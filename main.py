# from turtle import Turtle
# from random import random
#
# import radius
#
# t = Turtle()
# t.screen.screensize(1024,768)
# for i in range(100):
#     if i < 30:
#         width = random() * 15
#         t.width(width)
#     else:
#         width = random() * 3
#         t.width(width)
#     steps = int(random() * 50)
#     angle = int(random() * 180)
#     if angle >= 40:
#         t.left(angle)
#     else:
#         t.right(angle)
#     t.fd(steps)
#     t.circle((steps/20*angle), extent=None, steps=None)
#     t.screen.colormode(255)
#     t.pencolor(int(random()*255), int(random()*255), int(random()*255))
#     t.screen.title('you are gay')
# t.screen.mainloop()

import numbers
import telebot

class Cat:
    def __init__(self, breed='none', age=0, color='unnamed'):
        self._breed = breed
        self._age = age
        self._color = color

    @staticmethod
    def make_meow():
        print('Meow, dear sir`s')

    @staticmethod
    def make_purr():
        print('MUUUUUUUR NAHUYYYYYY')

    @property
    def breed(self):
        return self._breed

    @property
    def color(self):
        return self._color

    @property
    def age(self):
        return self._age

    def print_cat(self):
        print(f'This cat breed is {self._breed}, also age is {self._age} and the color is {self._color} ')

    @age.setter
    def age(self, value):
        self._age = value

    @breed.setter
    def breed(self, value):
        self._breed = value

    @color.setter
    def color(self, value):
        self._color = value


class HomelessCat(Cat):
    def __init__(self, breed = 'huy', age = 0, color = 'unnamed', prevhome = '2 floors painthouse', wheretosleep = 'pomoyka'):
        super().__init__(breed, age, color)
        self._prevhome = prevhome
        self._where = wheretosleep

    @property
    def prevhome(self):
        return self._prevhome

    @property
    def where(self):
        return self._where

    @where.setter
    def where(self, value):
        self._where = value

    @prevhome.setter
    def prevhome(self, value):
        self._prevhome = value

    @staticmethod
    def call_for_eat():
        print('дай еда по братски а')

    @staticmethod
    def print_cat(self):
        super().print_cat()
        print(f'also prev home is {self._prevhome} and the sleep place is {self._where}')

    @staticmethod
    def make_meow(self):
        super().make_meow()
        print(' \tsaid sadcat')


def cheatmeal(*args):
    if len(args) == 1 and isinstance(args[0], str):
        return "Строка: " + args[0]
    elif len(args) == 2 and all(isinstance(arg, float) for arg in args):
        return "Сумма: " + str(sum(args))

print(cheatmeal("cheaps"))  # Вывод: Строка: тест
print(cheatmeal(100.0111, 100.901))

print('\n\n')
cat = Cat()
cat.make_meow()
print(cat.age)

cat.age = 10
cat.breed = 'Bessinskaya'
cat.color = 'orange'
cat.print_cat()
print('\n')

sadcat = HomelessCat('siberian', 5, 'semi-dark', 'russian usad`ba', 'still pomoyka')
sadcat.print_cat(sadcat)
print('\n')
sadcat.call_for_eat()
print('\n')
sadcat.make_meow(sadcat)
sadcat.prevhome = 'ebanaya pomoyka'
sadcat.where = 'he`s smiling right now, he`s living in big flat with coca cola and so much viskas'
sadcat.print_cat(sadcat)
print()
