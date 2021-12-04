def part_1(data):
    h_pos = 0
    depth = 0
    for line in data:
        line_parts = line.split()
        line_parts[1] = int(line_parts[1])
        if line_parts[0] == "forward":
            h_pos += line_parts[1]
        elif line_parts[0] == "down":
            depth += line_parts[1]
        elif line_parts[0] == "up":
            depth -= line_parts[1]
    return h_pos * depth

def part_2(data):
    h_pos = 0
    depth = 0
    aim = 0
    for line in data:
        line_parts = line.split()
        line_parts[1] = int(line_parts[1])
        if line_parts[0] == "forward":
            h_pos += line_parts[1]
            depth += line_parts[1] * aim
        elif line_parts[0] == "down":
            aim += line_parts[1]
        elif line_parts[0] == "up":
            aim -= line_parts[1]
    return h_pos * depth

def main():
    with open("day2input.txt", "r") as f:
        data = f.readlines()
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

if __name__ == "__main__":
    main()