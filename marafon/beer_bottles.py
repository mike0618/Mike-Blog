def beer_bottles(N, K):
    print(N - ( -N // (K - 1)) - 1)
    amount = N
    while N >= K:
        N, rem = divmod(N, K)
        amount += N
        N += rem
    return amount


print(beer_bottles(100, 7))

for i in range(2, 101):
    print(beer_bottles(100, i))
