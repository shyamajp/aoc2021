def binary_list_to_decimal_int(binary_list):
    size = len(binary_list)
    decimal = 0
    for binary in binary_list:
        size -= 1
        decimal += binary * 2 ** size
    return decimal

# Read data
data = open('03.txt', 'r')
lines = data.readlines()

### FIRST PART

# Get ganna rate abd epsilon rate for power consumption
size = len(lines[0]) - 1
count = 0
gamma_counts = [0] * size

for line in lines:
    for index, number in enumerate(line):
        if number != '\n':
            gamma_counts[index] += int(number)
    count += 1

gamma_rate = [1 if bit > count / 2 else 0 for bit in gamma_counts]
gamma_rate_dec = binary_list_to_decimal_int(gamma_rate)

epsilon_rate = [1 if bit == 0 else 0 for bit in gamma_rate]
epsilon_rate_dec = binary_list_to_decimal_int(epsilon_rate)

power_consumption = gamma_rate_dec * epsilon_rate_dec
print("FIRST:\tPower consumption\t" + str(power_consumption))

### SECOND PART

# Get oxygen generator rating
remainings = lines
count = 0
while True:
    zeros = list()
    ones = list()
    for line in remainings:
        if int(line[count]) == 0:
            zeros.append(line)
        else:
            ones.append(line)

    remainings = zeros if len(zeros) > len(ones) else ones
    count += 1
    if len(remainings) == 1 or count == size:
        break

oxygen_generator_rating = [int(number) for number in list(remainings[0].strip())]
oxygen_generator_rating_dec = binary_list_to_decimal_int(oxygen_generator_rating)

# Get CO2 scrubber rating
remainings = lines
count = 0
while True:
    zeros = list()
    ones = list()
    for line in remainings:
        if int(line[count]) == 0:
            zeros.append(line)
        else:
            ones.append(line)

    remainings = zeros if len(zeros) <= len(ones) else ones
    count += 1
    if len(remainings) == 1 or count == size:
        break

CO2_scrubber_rating = [int(number) for number in list(remainings[0].strip())]
CO2_scrubber_rating_dec = binary_list_to_decimal_int(CO2_scrubber_rating)

life_support_rating = oxygen_generator_rating_dec * CO2_scrubber_rating_dec
print("SECOND:\tLife support rating\t" + str(life_support_rating))