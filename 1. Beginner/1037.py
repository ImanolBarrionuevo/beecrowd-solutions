# Read a decimal number from input
num = float(input())

# Determine which interval the number falls into and print the corresponding label
if num >= 0 and num <= 25:
    print("Intervalo [0,25]")
elif num > 25 and num <= 50:
    print("Intervalo (25,50]")
elif num > 50 and num <= 75:
    print("Intervalo (50,75]")
elif num > 75 and num <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")