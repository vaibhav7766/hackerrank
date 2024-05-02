# https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    pad = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(
            f"{str(i).rjust(pad)} "
            f"{oct(i)[2:].rjust(pad)} "
            f"{hex(i)[2:].upper().rjust(pad)} "
            f"{bin(i)[2:].rjust(pad)} "
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
