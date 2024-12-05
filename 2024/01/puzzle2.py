import sys

def solution(file):
    left = []
    right = []
    for line in file:
        line = line.strip()
        l, r = line.split()

        left.append(int(l))
        right.append(int(r))

    similarity = 0

    for l in left:
        occurrences = 0
        for r in right:
            if l == r:
                occurrences += 1
        
        similarity += l * occurrences

    return similarity


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