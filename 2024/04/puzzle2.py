import sys


def is_MAS(l):
    return 1 if ''.join(l) in ['MAS', 'SAM'] else 0

def get(lines: list, i, j):
    height = len(lines)
    width = len(lines[0])

    if not(0 <= i < height) or not(0 <= j < width):
        return ''

    return lines[i][j]


def get_X(lines, i, j):
    d1 = [get(lines, x, y) for x, y in ((i-1, j-1), (i, j), (i+1, j+1))]
    d2 = [get(lines, x, y) for x, y in ((i+1, j-1), (i, j), (i-1, j+1))]

    return is_MAS(d1) * is_MAS(d2)

def create_X_adj_graph(lines: list[str]) -> dict:
    graph = {}
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c != 'A':
                continue

            graph[(i,j)] = get_X(lines, i, j)

    return graph


def solution(file):
    lines = []

    for line in file:
        lines.append(line.strip())

    g = create_X_adj_graph(lines)
    return sum(g.values())

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
