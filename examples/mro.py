
"""
# MRO

## Алгоритм.
Обходим дерево слева направо. То есть:

1. Выбираем первого левого родителя.
2. Поторяем пункт 1 пока не дойдем до вершины ромба (по умолчанию: object).
3. Находим все ветки, которые идут до данной вершины. (ищем слева направо)
3. Продолжаем идти по крайней левой ветки, пока не закончатся классы.

## Пример

   object(14)
    |        \   
Grand1(9)   Grand2(10)
    |      /
   Grand(8)
    |     \__
    |        \
    |       Main(7)
    |       __|__
FOther1(4) /     \     FOther2(12)
    |     /       \    /
FirstLine1(3)   FirstLine2(6)
    |            |
    | SOther1(11)|  SOther2(13)
    | /          | /
SecondLine1(2)  SecondLine2(5)
        \       /  # noqa
         \__ __/  # noqa
            |
          Last(1)

"""


Grand1 = type('Grand1', (object,), {})
Grand2 = type('Grand2', (object,), {})

SOther1 = type('SOther1', (object,), {})

FOther2 = type('FOther2', (object,), {})
SOther2 = type('SOther2', (object,), {})

Grand = type('Grand', (Grand1, Grand2), {})

Main = type('Main', (Grand,), {})
FOther1 = type('FOther1', (Grand,), {})

FirstLine1 = type('FirstLine1', (FOther1, Main), {})
FirstLine2 = type('FirstLine2', (Main, FOther2), {})

SecondLine1 = type('SecondLine1', (FirstLine1, SOther1), {})
SecondLine2 = type('SecondLine2', (FirstLine2, SOther2), {})


class Last(SecondLine1, SecondLine2):
    pass


print(Last.mro())
# [
#   <class '__main__.Last'>,
#   <class '__main__.SecondLine1'>,
#   <class '__main__.FirstLine1'>,
#   <class '__main__.FOther1'>,
#   <class '__main__.SecondLine2'>,
#   <class '__main__.FirstLine2'>,
#   <class '__main__.Main'>,
#   <class '__main__.Grand'>,
#   <class '__main__.Grand1'>,
#   <class '__main__.Grand2'>,
#   <class '__main__.SOther1'>,
#   <class '__main__.FOther2'>,
#   <class '__main__.SOther2'>,
#   <class 'object'>
# ]

X = type('X', (object,), {})
Z = type('Z', (object,), {})

A = type('A', (X,), {})
B = type('B', (X,), {})
C = type('C', (X,), {})

D = type('D', (A, B, Z), {})
E = type('E', (C,), {})

F = type('F', (D, E), {})

print(F.mro())
# [
#   <class '__main__.F'>,
#   <class '__main__.D'>,
#   <class '__main__.A'>,
#   <class '__main__.B'>,
#   <class '__main__.E'>,
#   <class '__main__.C'>,
#   <class '__main__.X'>,
#   <class '__main__.Z'>,
#   <class 'object'>
# ]
