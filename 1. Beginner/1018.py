m = int(input())
print(f"{m}")

nums = [100, 50, 20, 10, 5, 2, 1]

for n in nums:
    c = 0
    while m-n >= 0:
        m -= n
        c += 1
    print(f"{c} nota(s) de R$ {n},00")
