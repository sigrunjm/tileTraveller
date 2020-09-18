"""""
movePlayer tekur við núverandi staðsetningu og átt sem leikmaður ætlar.
ef þú mátt fara í þessa átt frá staðsetningunni sem þú ert á uppfærir það position (new_pos)
annars verður new_pos óbreytt.
Þá förum við í if lykkju í enda kóðans: Ef position breyttist ekkert mátti ekki fara í þessa átt og
notandi er beðinn aftur um átt.

Hverjir geta farið í hvaða átt?
Norður : 1, 2, 3, 4, 6
Suður : 4, 5, 6, 7, 9
Vestur : 5, 8, 9
Austur : 4, 7, 8
"""

def movePlayer(pos,direction):
    if direction == 'n' and  (pos == 1 or pos == 2 or pos == 4 or pos == 6):
        new_pos = pos + 3
        return new_pos
    elif direction == 'n':
        new_pos = pos
        return new_pos
    elif direction == 's' and (pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 9):
        new_pos = pos - 3
        return new_pos
    elif direction == 's':
        new_pos = pos
        return new_pos
    elif direction == 'e' and (pos == 4 or pos == 7 or pos == 8):
        new_pos = pos + 1
        return new_pos
    elif direction == 'e':
        new_pos = pos
        return new_pos
    elif direction == 'w' and (pos == 5 or pos == 8 or pos == 9):
        new_pos = pos - 1
        return new_pos
    elif direction == 'w':
        new_pos = pos
        return new_pos
    else:
        new_pos = pos
        return new_pos

pos = 1
while pos != 3:
    if pos == 1:
        print('You can travel: (N)orth')
    if pos == 2:
        print('You can travel: (N)orth')
    if pos == 4:
        print('You can travel: (N)orth or (E)ast or (S)outh')
    if pos == 5:
        print('You can travel: (W)est or (S)outh')
    if pos == 6:
        print('You can travel: (N)orth or (S)outh')
    if pos == 7:
        print('You can travel: (S)outh or (E)ast')
    if pos == 8:
        print('You can travel: (W)est or (E)ast')
    if pos == 9:
        print('You can travel: (W)est or (S)outh')

    direct = input('Direction: ')
    direct = direct.lower()
    new_position = movePlayer(pos,direct)
    if new_position == pos:
        print("Not a valid direction!")
    else:
        pos = new_position
print('Victory!')