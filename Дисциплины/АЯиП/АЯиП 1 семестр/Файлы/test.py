x0 = float(input())
hx = float(input())
xn = float(input())


def square(a, b):
    ans = 1
    for i in range(1, b+1):
        ans *= a
    return ans


x = x0
while x <= xn:
    s = 0
    if x <= 0.5:
        for i in range(1, 9):
            s += (i*x) / (i*x*x+1)
    else:
        p = 1
        for j in range(0, 9):
            p = p*x
            s = p / (j + 1)
    x += hx
print(s)
