
"""
# MRO

## Алгоритм.

1. Обходим дерево в глубину слева направо.
2. Формируем список из пройденных классов.
3. Удаляем повторяющиеся классы (оставляем первое вхождение).
4. Если встречаются базовые классы, идущие после потомков, перемещаем их перед потомком.

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

1. Last, SecondLine1, FirstLine1, FOther1, [Grand], Grand1, Grand2, Main, [Grand], Grand1, Grand2, SOther1, SecondLine2, FirstLine2, Main, [Grand], Grand1, Grand2, FOther2, SOther2
2. Last, SecondLine1, FirstLine1, FOther1, Grand, [Grand1], Grand2, Main, [Grand1], Grand2, SOther1, SecondLine2, FirstLine2, Main, [Grand1], Grand2, FOther2, SOther2
3. Last, SecondLine1, FirstLine1, FOther1, Grand, Grand1, [Grand2], Main, [Grand2], SOther1, SecondLine2, FirstLine2, Main, [Grand2], FOther2, SOther2
4. Last, SecondLine1, FirstLine1, FOther1, Grand, Grand1, Grand2, [Main], SOther1, SecondLine2, FirstLine2, [Main], FOther2, SOther2
5. Last, SecondLine1, FirstLine1, FOther1, Grand, Grand1, Grand2, Main, SOther1, SecondLine2, FirstLine2, FOther2, SOther2
6. Last, SecondLine1, FirstLine1, FOther1, SecondLine2, FirstLine2, Main, Grand, Grand1, Grand2, SOther1, FOther2, SOther2

доп. материалы
- https://tirinox.ru/mro-python/

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

"""
Будет ошибка: Cannot create consistent method ordering
N = type('N', (object,), {})
M = type('M', (N,), {})
Y = type('Y', (N, M), {})
"""
