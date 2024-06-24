# https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

#!/bin/python3
if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    directions = [[-1, -1], [-1, 0], [-1, 1], [0, 0], [1, -1], [1, 0], [1, 1]]

    max_sum = -float("inf")

    for i in range(1, 5):
        for j in range(1, 5):
            sn = 0
            for dx, dy in directions:
                x, y = i + dx, j + dy
                sn += arr[x][y]
            max_sum = max(max_sum, sn)

    print(max_sum)
