class Hero:
    def __init__(self, name, lvl, health, strenght):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strenght = strenght

    def greet(self):
        print(f'Меня зовут {self.name} | Мой уровень {self.lvl}!')

    def attack(self):
        self.strenght -= 1
        print(f'{self.name} наносит удар!!! '
              f'Сила героя уменьшена на 1, '
              f'сейчас она равна {self.strenght}')

    def rest(self):
        self.health += 1
        print(f'{self.name} отдыхает. '
              f'Здоровье увеличено на 1, '
              f'сейчас оно равно {self.health}')


Ilya = Hero("Ilya", 10, 50, 25)
Dobrynya = Hero("Dobrynya", 12, 48, 27)
Alesha = Hero("Alesha", 8, 39, 22)

Ilya.greet()
Ilya.attack()
Ilya.rest()

Dobrynya.greet()
Dobrynya.attack()
Dobrynya.rest()

Alesha.greet()
Alesha.attack()
Alesha.rest()