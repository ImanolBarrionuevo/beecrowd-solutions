import math

a, b = map(float, input().split())
c, d = map(float, input().split())

print(f"{math.sqrt((c-a)**2+(d-b)**2):.4f}")