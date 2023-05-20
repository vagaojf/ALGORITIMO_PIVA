t = ()
for i in range(5):
    x = int(input(f"digite o {i+1}o. número: "))
    t = t + (x,)

print(t[::-1])