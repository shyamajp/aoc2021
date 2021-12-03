# Read data
data = open('02.txt', 'r')
lines = data.readlines()

### FIRST PART

# Set initial values
horizontal = 0
depth = 0

def move (direction, distance):
    global horizontal
    global depth
    if direction == "forward":
        horizontal += distance
    elif direction == "down":
        depth += distance
    elif direction == "up":
        depth -= distance

for line in lines:
    [direction, distance] = line.split()
    move(direction, int(distance))

result = horizontal * depth    
print("FIRST:\tProduct of horizontal position and depth\t" + str(result))

### SECOND PART

# Set initial values
horizontal = 0
depth = 0
aim = 0

def move_second (direction, score):
    global horizontal
    global depth
    global aim
    if direction == "forward":
        horizontal += score
        depth += aim * score
    elif direction == "down":
        aim += score
    elif direction == "up":
        aim -= score

for line in lines:
    [direction, distance] = line.split()
    move_second(direction, int(distance))

result = horizontal * depth    
print("SECOND:\tProduct of horizontal position and depth\t" + str(result))
