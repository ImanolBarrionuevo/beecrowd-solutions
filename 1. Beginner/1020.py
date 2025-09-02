n = int(input())

y = n // 365
n = n % 365

m = n // 30
d = n % 30

print(f"{y} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")