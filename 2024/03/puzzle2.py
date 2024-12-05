import sys
import re

def solution(file):
    mul_r = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_r = r'do\(\)'
    dont_r = r"don't\(\)"

    r = rf'{mul_r}|({do_r})|({dont_r})'

    total = 0
    enabled = True

    for line in file:
        line = line.strip()

        matches = re.findall(r, line)
        for m in matches:
            if m[2] != '':
                enabled = True
                continue

            if m[3] != '':
                enabled = False
                continue
            
            if not enabled:
                continue
            
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
