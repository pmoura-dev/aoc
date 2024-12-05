import sys
import re

def solution(file):
    r = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0

    for line in file:
        line = line.strip()

        matches = re.findall(r, line)
        for m in matches:
            x, y = (int(m[0]), int(m[1]))
            total += x * y

    return total

def main():
    if len(sys.argv) == 1:
        print("no input passed")
        exit()
    
    input_file = sys.argv[1]

    with open(input_file) as f:
        result = solution(f)
        print(result)


if __name__ == "__main__":
    main()
