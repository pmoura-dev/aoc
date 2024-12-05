import sys

def dampener(line):
    if safe(line):
        return True

    for i in range(len(line)):
        copy = line[:]
        del copy[i]

        if safe(copy):
            return True
        
    return False
            


def safe(line):
     # check 1
    sorted_line = list(sorted(line))
    if sorted_line != line and sorted_line != list(reversed(line)):
        return False

    # check 2
    for i in range(len(line) - 1):
        if not (1 <= abs(line[i] - line[i+1]) <= 3):
            return False
    
    return True


def solution(file):
    count = 0
    for line in file:
        line = [int(x) for x in line.strip().split()]

        if dampener(line):
            count += 1
        
    return count


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