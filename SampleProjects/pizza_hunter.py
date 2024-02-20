import curses
import random
import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)

maxl = curses.LINES - 1
maxc = curses.COLS - 1


world = []
player_l = player_c = 0
food = []
enemy = []
score = 0

def random_place():
    a = random.randint(0, maxl)
    b = random.randint(0, maxc)
    while world[a][b] != ' ':
        a = random.randint(0, maxl)
        b = random.randint(0, maxc)
    return a, b

def init():
    global player_c, player_l
    for i in range(-1, maxl + 1):
        world.append([])
        for j in range(-1, maxc + 1):
            world[i].append(' ' if random.random() > 0.03 else '.')
            
        for i in range(10):
            fl, fc = random_place()
            fa = random.randint(1000, 10000)
            food.append((fl, fc, fa))
    
    player_l, player_c = random_place()

def in_range(a, min, max):
    if a > max:
        return max
    if a < min:
        return min
    return a

def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    stdscr.addstr(1, 1, f'Score: {score}')      
      
    for f in food:
        fl, fc, fa = f
        stdscr.addch(fl, fc, '*')
        
    stdscr.addch(player_l, player_c, 'x')
    
    stdscr.refresh()
    
def move(c):
    global player_l, player_c
    if c == 'w' and world[player_l - 1][player_c] != '.':
        player_l -= 1
    elif c == 's' and world[player_l + 1][player_c] != '.':
        player_l += 1
    elif c == 'a' and world[player_l][player_c - 1] != '.':
        player_c -= 1
    elif c == 'd' and world[player_l][player_c + 1] != '.':
        player_c += 1
        
    player_l = in_range(player_l, 0, maxl - 1)
    player_c = in_range(player_c, 0, maxc - 1)

def check_food():
    global score
    for i in range(len(food)):
        fl, fc, fa = food[i]
        if fl == player_l and fc == player_c:
            score += 10
            nfl, nfc = random_place()
            nfa = random.randint(1000, 10000)
            food[i] = (nfl, nfc, nfa)

init()

playing = True
while playing:
    try:
        c = stdscr.getkey()
    except:
        c = ''
    if c in 'asdw':
        move(c)
    elif c == 'q':
        playing = False
    draw()

stdscr.clear()
stdscr.refresh()

