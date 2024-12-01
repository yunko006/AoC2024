from pathlib import Path


def part1(lines: list) -> int:
    r: list = []
    l: list = []
    res = 0
    for line in lines:
        temp = line.split("   ")

        l.append(int(temp[0]))
        r.append(int(temp[1]))

    sorted_r = sorted(r)
    sorted_l = sorted(l)

    final = zip(sorted_l, sorted_r)

    for l_elem, r_elem in final:
        res += abs(l_elem - r_elem)

    print(res)


def part2(lines: list) -> int:
    r: list = []
    l: list = []
    res = 0
    for line in lines:
        temp = line.split("   ")

        # faire un count de la liste l dans la liste r
        l.append(int(temp[0]))
        r.append(int(temp[1]))

    for num in l:
        v = r.count(num)
        res += v * num

    print(res)


if __name__ == "__main__":
    lines = Path("input.txt").read_text().rstrip().split("\n")

    p1_answer = part1(lines)
    p2 = part2(lines)
