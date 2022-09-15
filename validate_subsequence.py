



y = [1,3,4]
x = [1,2,3,4]

j = 0
for i, element in enumerate(x):
    if element == y[j]: j += 1
if j == len(y):
    print("Subset")
else:
    print("Not subset")