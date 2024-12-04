from pathlib import Path
import re


def part1(lines: list) -> int:
    total = 0
    with open("input.txt") as f:
        content = f.read()
        pattern = r"mul\((\d+),(\d+)\)"
        # utilisations de parantheses pour trouver les groupes
        matches = re.finditer(pattern, content)

        for match in matches:
            a = int(match.group(1))
            b = int(match.group(2))
            total += a * b

    print(total)


def part2(lines: list) -> int:
    total = 0
    with open("input.txt") as f:
        content = f.read()
        pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
        matches = re.finditer(pattern, content)

    enabled = True
    for match in matches:
        matched_text = match.group(0)
        if matched_text == "do()":
            enabled = True
        elif matched_text == "don't()":
            enabled = False
        else:
            if enabled:
                a = int(match.group(1))
                b = int(match.group(2))
                total += a * b
    print(total)


if __name__ == "__main__":
    lines = Path("input.txt").read_text().rstrip().split("\n")

    p1_answer = part1(lines)
    p2 = part2(lines)
