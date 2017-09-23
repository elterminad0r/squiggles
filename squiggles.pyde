from random import randrange

BLOCK_SIZE = 40
CHPS = 1

def shufflepop(l):
    ind = randrange(len(l))
    l[ind], l[-1] = l[-1], l[ind]
    return l.pop()

def setup():
    global states, pool
    size(1280, 720)
    states = [[0 for _ in xrange(height // BLOCK_SIZE)] for _ in xrange(width // BLOCK_SIZE)]
    pool = [(x, y) for x in xrange(width // BLOCK_SIZE) for y in xrange(height // BLOCK_SIZE)]
    noFill()
    stroke(255)

def draw():
    global pool
    background(0)
    for _ in xrange(CHPS):
        try:
            nx, ny = shufflepop(pool)
            states[nx][ny] = not states[nx][ny]
        except ValueError:
            pool = [(x, y) for x in xrange(width // BLOCK_SIZE) for y in xrange(height // BLOCK_SIZE)]
    for x in xrange(width // BLOCK_SIZE):
        for y in xrange(height // BLOCK_SIZE):
            if states[x][y]:
                arc(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, 0, HALF_PI)
                arc((x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, PI, PI + HALF_PI)
            else:
                arc((x + 1) * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, HALF_PI, PI)
                arc(x * BLOCK_SIZE, (y + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, PI + HALF_PI, TWO_PI)
                