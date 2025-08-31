a, b, c = map(int, input().split())

MaiorAB = (a + b + abs(a - b)) // 2
Maior = (MaiorAB + c + abs(MaiorAB - c)) // 2

print(f"{Maior} eh o maior")