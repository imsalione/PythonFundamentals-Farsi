import curses
import random
import time

food_age = 500
food_number = 10
player_char = '🏃'
food_char = '🍕'
enemy_char = '👾'

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
curses.curs_set(False)

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
    for i in range(-1, maxl+1):
        world.append([])
        for j in range(-1, maxc+1):
            world[i].append(' ' if random.random() > 0.03 else '.')
            
    for i in range(food_number):
        fl, fc = random_place()
        fa = random.randint(food_age, food_age*5)
        food.append((fl, fc, fa))
    
    for i in range(3):
        el, ec = random_place()
        enemy.append((el, ec))
    
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
    stdscr.addstr(1, 1, f"Score: {score}")      
      
    for f in food:
        fl, fc, fa = f
        stdscr.addch(fl, fc, food_char)
        
    for e in enemy:
        l, c = e
        stdscr.addch(l, c, enemy_char)
        
    stdscr.addch(player_l, player_c, player_char)
    
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
        fa -= 1
        if fl == player_l and fc == player_c:
            score += 10
            fl, nfc = random_place()
            fa = random.randint(1000, 10000)
        if fa <= 0:
              fl, fc = random_place()
              fa = random.randint(1000, 10000)
              
        food[i] = (fl, fc, fa)

def move_enemy():
    global playing
    for i in range(len(enemy)):
        l, c = enemy[i]
        if random.random() > 0.9:
            if l > player_l:
                l -= 1
        if random.random() > 0.9:
            if c > player_c:
                c -= 1
        if random.random() > 0.9:
            if l < player_l:
                l += 1
        if random.random() > 0.9:
            if c < player_c:
                c += 1
            enemy[i] = (l, c)
            l in range(l, 0, maxl)
            c in range(c, 0, maxl)
            
        if l == player_l and c == player_c:
            stdscr.addstr(maxl//2, maxc//2, "You DIED!")
            stdscr.refresh()
            time.sleep()
            playing = False

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
    check_food()
    move_enemy()
    time.sleep(0.01)
    draw()

stdscr.addnstr(maxl//2, maxc//2, "Thanks for playing")
stdscr.refresh()
time.sleep(2)
stdscr.clear()
stdscr.refresh()

