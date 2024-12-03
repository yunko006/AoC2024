from pathlib import Path


def part1(lines: list) -> int:
    total_res = 0
    for line in lines:
        temp = list(map(int, line.split(" ")))

        check = all(1 <= temp[i + 1] - temp[i] <= 3 for i in range(len(temp) - 1)) or (
            all(1 <= temp[i] - temp[i + 1] <= 3 for i in range(len(temp) - 1))
        )
        if check:
            total_res += 1

    return total_res


def part2(lines: list) -> int:
    total_res = 0
    for line in lines:
        temp = list(map(int, line.split(" ")))

        sub_sequences = [temp[:i] + temp[i + 1 :] for i in range(len(temp))]

        for sub in sub_sequences:
            check = all(
                1 <= sub[i + 1] - sub[i] <= 3 for i in range(len(sub) - 1)
            ) or all(1 <= sub[i] - sub[i + 1] <= 3 for i in range(len(sub) - 1))
            if check:
                total_res += 1
                break

    return total_res


if __name__ == "__main__":
    lines = Path("input.txt").read_text().rstrip().split("\n")

    p1_answer = part1(lines)
    print(p1_answer)
    p2 = part2(lines)
    print(p2)
