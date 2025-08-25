first = input().split()
second = input().split()

total = float(first[1])*float(first[2]) + float(second[1])*float(second[2])

print(f"VALOR A PAGAR: R$ {total:.2f}")