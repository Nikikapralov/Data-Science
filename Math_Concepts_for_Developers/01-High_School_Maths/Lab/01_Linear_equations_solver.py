a = float(input())
b = float(input())
x = None
if a == 0 and b != 0:
    x = 'nan'
elif a == 0 and b == 0:
    x = []
elif a != 0:
    x = -b / a
    if x == 0:
        x = abs(x)
print(x)