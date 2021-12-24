# Read data
data = open('01.txt', 'r')
lines = data.readlines()

### FIRST PART
previous = 0
count = 0
for line in lines:
    num = int(line)
    if num > previous:
        count += 1
    previous = num

print("FIRST:\tCount\t" + str(count))

### SECOND PART

count = 0
for index, line in enumerate(lines):
    if index+3 >= len(lines):
        break
    # Only compare a unique number of the three
    previous_n = int(line)
    next_n = int(lines[index+3])
    if next_n > previous_n:
        count += 1

print("SECOND:\tCount\t" + str(count))
