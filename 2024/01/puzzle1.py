import sys

def solution(file):
    left = []
    right = []
    for line in file:
        line = line.strip()
        l, r = line.split()

        left.append(int(l))
        right.append(int(r))

    distance = 0

    while left != [] or right != []:        
        min_l = min(left)
        min_r = min(right)

        distance += abs(min_l - min_r)

        left.remove(min_l)
        right.remove(min_r)

    return distance


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