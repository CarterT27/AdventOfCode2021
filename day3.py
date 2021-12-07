from statistics import mode
import copy

def part_1(data):
    digit_length = len(data[0]) - 1
    gamma_rate = ''
    epsilon_rate = ''

    for digit_index in range(digit_length):
        digit_list = []
        for number in data:
            digit_list.append(int(number[digit_index]))
        most_common = mode(digit_list)
        if most_common == 1:
            gamma_rate += '1'
            epsilon_rate += '0'
        elif most_common == 0:
            gamma_rate += '0'
            epsilon_rate += '1'
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate

def part_2(data):
    digit_length = len(data[0]) - 1
    oxygen_generator_rating = ''
    CO2_scrubber_rating = ''
    oxygen_data = copy.deepcopy(data)
    co2_data = copy.deepcopy(data)

    for digit_index in range(digit_length):
        digit_sum = 0
        most_common = 1
        for number in oxygen_data:
            digit_sum += int(number[digit_index])
        if digit_sum / len(oxygen_data) < 0.5:
            most_common = 0
        i = 0
        while i < len(oxygen_data):
            if len(oxygen_data) == 1:
                break
            if int(oxygen_data[i][digit_index]) != most_common:
                oxygen_data.pop(i)
            else:
                i += 1
    for digit_index in range(digit_length):
        digit_sum = 0
        least_common = 0
        for number in co2_data:
            digit_sum += int(number[digit_index])
        if digit_sum / len(co2_data) < 0.5:
            least_common = 1
        i = 0
        while i < len(co2_data):
            if len(co2_data) == 1:
                break
            if int(co2_data[i][digit_index]) != least_common:
                co2_data.pop(i)
            else:
                i += 1
    print(oxygen_data)
    print(co2_data)
    oxygen_generator_rating = oxygen_data[0].replace("\n", "")
    print(oxygen_generator_rating)
    CO2_scrubber_rating = co2_data[0].replace("\n", "")
    print(CO2_scrubber_rating)
    oxygen_generator_rating = int(oxygen_generator_rating, 2)
    CO2_scrubber_rating = int(CO2_scrubber_rating, 2)
    return oxygen_generator_rating * CO2_scrubber_rating

def main():
    test_data = [
        '0110',
        '0000',
        '0100'
    ]
    with open("day3input.txt", "r") as f:
        data = f.readlines()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

if __name__ == "__main__":
    main()