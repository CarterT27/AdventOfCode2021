def part_1():
    increased = 0
    with open("day1input.txt", "r") as f:
        lines = f.readlines()
        lines = [int(x) for x in lines]
        previous_n = lines[0]
        for i in range(len(lines)):
            if lines[i] > previous_n:
                increased += 1
            previous_n = lines[i]

    return increased

def part_2():
    increased = 0
    with open("day1input.txt", "r") as f:
        lines = f.readlines()
        lines = [int(x) for x in lines]
        for i in range(1, len(lines) - 2):
            increased += sum(lines[i:i+3]) > sum(lines[i-1:i+2])
    return increased

def main():
    print(f"There were {part_1()} increases")
    print(f"There were {part_2()} sum increases")

if __name__ == "__main__":
    main()