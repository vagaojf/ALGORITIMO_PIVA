L1 = []
L2 = []
for i in range(5):
    x = int(input(f"digite o {i+1}o valor!"))
    L1.append(x)
print("L1 = ",L1)
for i in range(5):
    x = int(input(f"digite o {i+1}o valor!"))
    L2.append(x)
print("L2 = ",L2)
c1 = set(L1)
c2 = set(L2)
print("c1 = ", c1)
print("c2 = ", c2)
c = c1.union(c2).union(c3)
print(c)
