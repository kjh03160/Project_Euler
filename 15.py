"""
아래와 같은 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다 (거슬러 가지는 않기로 합니다).

그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
"""

def answer(n):
    matrix = [[1] for i in range(n + 1)]

    for i in range(n):
        matrix[0].append(1)
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            matrix[i].append(matrix[i - 1][k] + matrix[i][k - 1])

    return matrix[n][n]

print(answer(20000))