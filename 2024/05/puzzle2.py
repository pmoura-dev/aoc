import sys
from functools import cmp_to_key

def check_update(rules: dict, pages: list[str]) -> int:
    size = len(pages)
    middle_i = size // 2

    for i, pivot in enumerate(pages):
        if i == size - 1:
            continue
        for p in pages[i+1:]:
            if p in rules and pivot in rules[p]:
                return 0

    return int(pages[middle_i])


def compare(rules, x, y):
    if x in rules and y in rules[x]:
        return -1

    if y in rules and x in rules[y]:
        return 1

    return 0


def sort_update(rules: dict, pages: list[str]) -> int:
    size = len(pages)
    middle_i = size // 2

    s = sorted(pages, key=cmp_to_key(lambda x, y: compare(rules, x, y)))

    return int(s[middle_i])





def solution(file):
    rules = {}

    is_rule = True

    total = 0

    for line in file:
        line = line.strip()
        if line == "":
            is_rule = False
            continue

        if is_rule:
            x, y = line.split("|")
            if x in rules:
                rules[x].add(y)
            else:
                rules[x] = set([y])
            continue

        result = check_update(rules, line.split(","))
        if result != 0:
            continue

        total += sort_update(rules, line.split(","))

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
