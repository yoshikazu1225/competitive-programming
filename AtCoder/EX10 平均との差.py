N = int(input())
# ここにプログラムを追記

A = list(map(int, input().split()))

# 合計点
total = 0

# 全体の合計点を計算
for i in range (N):
    total += A[i]

# 平均点を計算
ave = total // N

# 平均点と何点離れているかを計算
for i in range(N):
    if A[i] > ave:
        print(A[i] - ave)

    else:
        print(ave - A[i])