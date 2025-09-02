n = int(input())

h = n // 3600
n = n % 3600

m = n // 60
s = n % 60

print(f"{h}:{m}:{s}")