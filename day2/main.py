from pathlib import Path


def part1(lines: list) -> int:
    total_res = 0
    for line in lines:
        inc = 0
        calc = 0
        temp = list(map(int, line.split(" ")))

        for i, num in enumerate(temp[:-1]):
            if num > temp[i + 1]:
                inc -= 1
            else:
                inc += 1

        if abs(inc) == len(temp) - 1:
            for i in range(len(temp) - 1):
                if 1 <= abs(temp[i] - temp[i + 1]) <= 3:
                    calc += 1
            if calc == (len(temp) - 1):
                total_res += 1

    return total_res


def part2(lines: list) -> int:
    pass


if __name__ == "__main__":
    lines = Path("input.txt").read_text().rstrip().split("\n")

    p1_answer = part1(lines)
    print(p1_answer)
    # p2 = part2(lines)
