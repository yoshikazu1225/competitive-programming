N, S = map(int, input().split())

A = list(map(int, input().split()))
P = list(map(int, input().split()))

# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記

# 答えを格納する変数
ans = 0

# リンゴを一つずつ選ぶ
for i in range(N):
    # パイナップルを一つずつ選ぶ
    for d in range(N):
        # 合計がSだった場合、変数に1を足す
        if A[i] + P[d] == S:
            ans += 1
print(ans)