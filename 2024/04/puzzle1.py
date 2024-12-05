import sys

def is_XMAS(l):
    return 1 if ''.join(l) == "XMAS" else 0


def get(lines: list, i, j):
    height = len(lines)
    width = len(lines[0])

    if not(0 <= i < height) or not(0 <= j < width):
        return ''

    return lines[i][j]


def get_directions_words(lines, i, j):
    north = is_XMAS([get(lines, d, j) for d in (i, i-1, i-2, i-3)])
    east = is_XMAS([get(lines, i, d) for d in (j, j+1, j+2, j+3)])
    south = is_XMAS([get(lines, d, j) for d in (i, i+1, i+2, i+3)])
    west = is_XMAS([get(lines, i, d) for d in (j, j-1, j-2, j-3)])
    
    northeast = is_XMAS([get(lines, x, y) 
                         for x, y in ((i, j), (i-1, j+1), (i-2, j+2), (i-3,j+3))
                         ])
    
    southeast = is_XMAS([get(lines, x, y) 
                         for x, y in ((i, j), (i+1, j+1), (i+2, j+2), (i+3,j+3))
                         ])

    southwest = is_XMAS([get(lines, x, y) 
                        for x, y in ((i, j), (i+1, j-1), (i+2, j-2), (i+3,j-3))
                        ])
    
    northwest = is_XMAS([get(lines, x, y) 
                        for x, y in ((i, j), (i-1, j-1), (i-2, j-2), (i-3,j-3))
                        ])


    return north + east + south + west + northeast + southeast + southwest + northwest


def create_X_adj_graph(lines: list[str]) -> dict:
    graph = {}
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c != 'X':
                continue

            graph[(i,j)] = get_directions_words(lines, i, j)

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
